#!/usr/bin/env python3
"""
Microsoft Fabric Deployment Pipeline Script
Converts PowerShell deployment script to Python using Fabric API
"""

import os
import sys
import time
import json
import requests
from typing import Optional, Dict, Any

class FabricDeployment:
    def __init__(self, tenant_id: str, app_id: str, client_secret: str):
        self.tenant_id = tenant_id
        self.app_id = app_id
        self.client_secret = client_secret
        self.access_token = None
        self.base_url = "https://api.fabric.microsoft.com/v1"
        
    def get_access_token(self) -> bool:
        """
        Get OAuth2 access token using client credentials flow for Fabric API
        """
        token_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        
        token_data = {
            'grant_type': 'client_credentials',
            'client_id': self.app_id,
            'client_secret': self.client_secret,
            'scope': 'https://api.fabric.microsoft.com/.default'
        }
        
        try:
            response = requests.post(token_url, data=token_data)
            response.raise_for_status()
            
            token_response = response.json()
            self.access_token = token_response.get('access_token')
            
            if self.access_token:
                print("Successfully authenticated with Microsoft Fabric service")
                return True
            else:
                print("Failed to obtain access token")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"Error during authentication: {e}")
            return False
    
    def get_headers(self) -> Dict[str, str]:
        """
        Get HTTP headers with authorization token
        """
        return {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
    
    def get_deployment_pipelines(self) -> Optional[list]:
        """
        Get all deployment pipelines using Fabric API
        """
        url = f"{self.base_url}/deploymentPipelines"
        
        try:
            response = requests.get(url, headers=self.get_headers())
            response.raise_for_status()
            
            pipelines_data = response.json()
            return pipelines_data.get('value', [])
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching deployment pipelines: {e}")
            return None
    
    def get_pipeline_stages(self, pipeline_id: str) -> Optional[list]:
        """
        Get deployment pipeline stages using Fabric API
        """
        url = f"{self.base_url}/deploymentPipelines/{pipeline_id}/stages"
        
        try:
            response = requests.get(url, headers=self.get_headers())
            response.raise_for_status()
            
            stages_data = response.json()
            return stages_data.get('value', [])
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching pipeline stages: {e}")
            return None
        """
        Get all deployment pipelines using Fabric API
        """
        url = f"{self.base_url}/deploymentPipelines"
        
        try:
            response = requests.get(url, headers=self.get_headers())
            response.raise_for_status()
            
            pipelines_data = response.json()
            return pipelines_data.get('value', [])
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching deployment pipelines: {e}")
            return None
    
    def find_pipeline_by_name(self, pipeline_name: str) -> Optional[Dict[str, Any]]:
        """
        Find a deployment pipeline by its display name
        """
        pipelines = self.get_deployment_pipelines()
        
        if pipelines is None:
            return None
            
        for pipeline in pipelines:
            if pipeline.get('displayName') == pipeline_name:
                return pipeline
                
        return None
    
    def deploy_stage_content(self, pipeline_id: str, source_stage_order: int) -> bool:
        """
        Deploy content from source stage to target stage using Fabric API
        The Fabric API uses 'deploy' endpoint instead of 'deployAll'
        """
        # Get pipeline stages to determine source and target stage IDs
        stages = self.get_pipeline_stages(pipeline_id)
        if not stages:
            print("Failed to retrieve pipeline stages")
            return False
        
        # Sort stages by order to find source and target
        sorted_stages = sorted(stages, key=lambda x: x.get('order', 0))
        
        if source_stage_order >= len(sorted_stages) - 1:
            print(f"Invalid source stage order: {source_stage_order}. Cannot deploy from the last stage.")
            return False
        
        source_stage = sorted_stages[source_stage_order]
        target_stage = sorted_stages[source_stage_order + 1]
        
        source_stage_id = source_stage.get('id')
        target_stage_id = target_stage.get('id')
        
        print(f"Deploying from stage '{source_stage.get('displayName')}' to '{target_stage.get('displayName')}'")
        
        url = f"{self.base_url}/deploymentPipelines/{pipeline_id}/deploy"
        
        deploy_body = {
            "sourceStageId": source_stage_id,
            "targetStageId": target_stage_id,
            "note": f"Automated deployment from stage {source_stage_order}",
            "options": {
                "allowCreateArtifact": True,
                "allowOverwriteArtifact": True
            }
        }
        
        try:
            response = requests.post(
                url, 
                headers=self.get_headers(), 
                json=deploy_body
            )
            response.raise_for_status()
            
            # For Fabric API, the response may include operation details directly
            # or we need to check the response headers for operation location
            if response.status_code == 202:
                # Long running operation
                operation_location = response.headers.get('Location')
                if operation_location:
                    # Extract operation ID from location header
                    operation_id = operation_location.split('/')[-1]
                    print(f"Operation ID: {operation_id}")
                    return self.wait_for_operation(pipeline_id, operation_id)
                else:
                    print("Deployment started but no operation ID found")
                    return True
            else:
                # Immediate response
                deploy_result = response.json()
                print(f"Deployment completed: {deploy_result}")
                return True
                
        except requests.exceptions.RequestException as e:
            print(f"Error during deployment: {e}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_detail = e.response.json()
                    print(f"Error details: {json.dumps(error_detail, indent=2)}")
                except:
                    print(f"Error response: {e.response.text}")
            return False
    
    def wait_for_operation(self, pipeline_id: str, operation_id: str) -> bool:
        """
        Wait for the deployment operation to complete using Fabric API
        """
        url = f"{self.base_url}/operations/{operation_id}"
        
        max_attempts = 240  # Maximum 20 minutes (240 * 5 seconds)
        attempts = 0
        
        while attempts < max_attempts:
            try:
                response = requests.get(url, headers=self.get_headers())
                response.raise_for_status()
                
                operation = response.json()
                status = operation.get('status', 'Unknown')
                
                print(f"Operation Status: {status}")
                
                if status in ['NotStarted', 'Executing', 'Running']:
                    print("Waiting for operation to complete...")
                    time.sleep(5)
                    attempts += 1
                    continue
                elif status in ['Succeeded', 'Completed']:
                    print("Deployment completed successfully!")
                    return True
                else:
                    print(f"Deployment failed with status: {status}")
                    # Print additional error details if available
                    if 'error' in operation:
                        print(f"Error details: {json.dumps(operation['error'], indent=2)}")
                    return False
                    
            except requests.exceptions.RequestException as e:
                print(f"Error checking operation status: {e}")
                return False
        
        print("Operation timed out")
        return False

def main():
    """
    Main function to execute the deployment
    """
    # Get parameters from environment variables or command line arguments
    tenant_id = os.getenv('TENANT_ID')
    app_id = os.getenv('APP_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    pipeline_name = os.getenv('PIPELINE_NAME')
    stage_order = int(os.getenv('STAGE_ORDER', '0'))
    
    # If not in environment variables, try command line arguments
    if not all([tenant_id, app_id, client_secret, pipeline_name]):
        if len(sys.argv) >= 5:
            tenant_id = sys.argv[1]
            app_id = sys.argv[2]
            client_secret = sys.argv[3]
            pipeline_name = sys.argv[4]
            stage_order = int(sys.argv[5]) if len(sys.argv) > 5 else 0
        else:
            print("Error: Missing required parameters")
            print("Usage: python deploy_all.py [tenant_id] [app_id] [client_secret] [pipeline_name] [stage_order]")
            print("Or set environment variables: TENANT_ID, APP_ID, CLIENT_SECRET, PIPELINE_NAME, STAGE_ORDER")
            sys.exit(1)
    
    # Validate pipeline name is provided
    if not pipeline_name:
        print("Error: Pipeline name is required")
        print("Set PIPELINE_NAME environment variable or provide as command line argument")
        sys.exit(1)
    
    # Pipeline configuration - now from environment variable
    print(f"Starting deployment for pipeline: {pipeline_name}")
    print(f"Source stage order: {stage_order}")
    
    # Initialize Fabric deployment client
    deployment = FabricDeployment(tenant_id, app_id, client_secret)
    
    # Authenticate
    if not deployment.get_access_token():
        print("Authentication failed")
        sys.exit(1)
    
    # Find the pipeline
    pipeline = deployment.find_pipeline_by_name(pipeline_name)
    
    if not pipeline:
        print(f"Pipeline with name '{pipeline_name}' was not found")
        sys.exit(1)
    
    pipeline_id = pipeline.get('id')
    print(f"Found pipeline with ID: {pipeline_id}")
    
    # Execute deployment
    success = deployment.deploy_stage_content(pipeline_id, stage_order)
    
    if success:
        print("Deployment completed successfully!")
        sys.exit(0)
    else:
        print("Deployment failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
