---
layout: page
title: Real Time Intelligence
subtitle: Medallion Architecture - Data Sources
menubar: docs_menu
show_sidebar: false
toc: true
---

## Data Sources  
Data coming into Fabric Real-Time Intelligence can come from anywhere. Anything that emits telemetry can be a data source for Fabric Real-Time Intelligence. But there are proven patterns that you can follow that should drive how you get data from you're data source to Fabric Real-Time Intelligence.

### Option 1: Output to Eventstream
The best pattern for data coming into Fabric RTI is to ingest via Evenstream. If any of these options are available you can output data from your Data Source to Evenstreams
- Can it write to an Azure Eventhub endpoint
If the data source has built-in capabilities to write to Azure Eventhub then it can write to Fabric Eventstream via the [Custom Endpoint](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-custom-app?pivots=enhanced-capabilities#event-hub)
- Can it write to a Kafka Endpoint
  If the data source has built-in capabilities to write to a Kafka endpoint then it can write to Fabric Evenstream via the [Custom Endpoint](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-custom-app?pivots=enhanced-capabilities#kafka)
- Can it write to a AMQP Endpoint
If the data source has built-in capabilities to write to a Kafka endpoint then it can write to Fabric Evenstream via the [Custom Endpoint](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-custom-app?pivots=enhanced-capabilities#advanced-message-queuing-protocol-amqp)
- Utilize CDC on Database Platform
Eventstream supports CDS feeds from
-- [Azure SQL Database](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-azure-sql-database-change-data-capture)
-- [PostgresSQL Database](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-postgresql-database-change-data-capture)
-- [MySQL Database](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-mysql-database-change-data-capture)
-- [Azure Cosmos DB](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-azure-cosmos-db-change-data-capture)
-- [SQL Server on VM](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-sql-server-change-data-capture)
-- [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-azure-sql-managed-instance-change-data-capture)
- Also Supported
-- [Google Cloud Pub/Sub](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-google-cloud-pub-sub)
-- [Amazon Kinesis Data Streams](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-amazon-kinesis-data-streams)
-- [Confluent Cloud Kafka](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-confluent-kafka)
-- [Apache Kafka](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-apache-kafka)
-- [Amazon Managed Streaming for Apache Kafka](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-amazon-managed-streaming-for-apache-kafka)
-- [Fabric Workspace Item Events](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-fabric-workspace)
-- [Fabric OneLake Events](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-fabric-onelake)
-- [Fabric Job Events](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-fabric-job)
-- [Azure Blob Storage Events](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-azure-blob-storage)
- Is it already landing in Azure Event Hub, Azure Service Bus, or Azure IoT Hub?
If data is already landing in any of these product in Azure then Eventstream can bring that data in by connect directly to the exising data.

### Option 2: Output to Storage (Fabric OneLake or Azure Blob Storage)
We are introducing continous ingestion from both Azure Storage and also from Fabric OneLake in the coming months. Currently the approach to do continous ingestion is to utilize Data Pipeline in fabric and the trigger for storag.

[Fabric Data Pipeline Storage Trigger](https://learn.microsoft.com/en-us/fabric/data-factory/pipeline-storage-event-triggers)
[Data Pipeline Eventhouse Connector](https://learn.microsoft.com/en-us/fabric/data-factory/connector-kql-database-overview)

### Option 3: Connectors/Agents
We've worked with many of the most popular agents to support an output to kusto. Any of these agents that can output to ADX in Azure can also output to Eventhouse in Fabric. The most popular agents are Logstash, Fluent Bit, Cribl, Telegraf, and Apache Flink. But for a full list and documentation go [here](https://learn.microsoft.com/en-us/azure/data-explorer/integrate-data-overview?tabs=connectors).

### Option 4: KQL API/SDKs  
Eventhouse has a full set of APIs and SDKs that allow you to write data directly to a KQL DB on an Eventhouse. This allows you to write directly to the platform from code and adds flexibility.

We have SDKs for [.NET](https://learn.microsoft.com/en-us/azure/data-explorer/net-sdk-ingest-data), [Python](https://learn.microsoft.com/en-us/azure/data-explorer/python-ingest-data), [Node](https://learn.microsoft.com/en-us/azure/data-explorer/node-ingest-data), [Go](https://learn.microsoft.com/en-us/azure/data-explorer/go-ingest-data), and [Java](https://learn.microsoft.com/en-us/azure/data-explorer/java-ingest-data). You can also utiize the [Rest API](https://learn.microsoft.com/en-us/rest/api/azurerekusto/)

### Option 5: Amazon S3 Bucket  
Eventhouse has the capability of ingesting data from S3 Buckets. Combining AWS Lambda functions with our native capabilities allows you to continously ingest from S3. More details and implementation guide can be found [here](https://techcommunity.microsoft.com/blog/azuredataexplorer/azure-data-explorer-supports-native-ingestion-from-amazon-s3/3606746)