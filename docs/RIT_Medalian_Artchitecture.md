---
layout: page
title: Real Time Intelligence
subtitle: Medallion Architecture
menubar: docs_menu
show_sidebar: false
toc: true
---

# Microsoft Fabric Real-Time Intelligence

Microsoft Fabric Real-Time Intelligence is built to continously flowing data, big data analytics, and high-granularity analytics. The components that make up this area are:

- **Data Ingestion** The primary way to ingest data into Fabric Real-Time Intelligence is via [Eventstream](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/overview?tabs=enhancedcapabilities). Eventstream can connect to Azure Eventhubs or expose a enpoint (Eventhub or Kafka) that can be written directly to. It also has built-in transformation abilities via the [Event Processor](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/process-events-using-event-processor-editor?pivots=enhanced-capabilities).
- **Data Analytics** Analytics on near real-time data or high granular analytic at an almost limitless scale (think billions of rows) is provided via [Eventhouse](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/eventhous)
- **React** The ability to take action on data is provided via [Data Activator](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/data-activator/activator-introduction)

## Common Use Cases

Telemetry data is the fasted growing dataset and spans across all verticles. Below are some of the most common implementations of Fabric Real-Time Intelligence for each verticle.

**Automotive**
- Connected fleet application
-- **Vehicle/device messaging**: The foundational layer for connected fleets, enabling the secure and private curated relaying of telemetry, other activity data, and instructions or updates to vehicles.
-- **Fleet integration, data models & harmonization**: Transformation and routing of inbound telemetry to persistent data stores, enabling advanced analytics and inferencing, as well as business systems integration.
-- **Data and analytics for vehicle and business data on Microsoft Fabric**: Microsoft Fabric helps in making the following details available over the entire scope of the vehicle and related data: extensive facilities for self-service data discovery, prescribed analytics and reports, advanced data mining, and the power of AI and ML.
-- **Business integration of vehicle telemetry data, alerts, and notification**: Data flowing from vehicles can trigger events in near real-time and enable contextual functionality and automation that drives better decision-making and actions to improve operations. 
- Autonomous Driving
- Manufacturing + R&D

**Manufacturing**
- Enterprise Historian
Centralize historian data across your manufacturing plants Bringing data from historians such as OSISoft PI, Schneider Electric ClearSCADA, AspenTech IP.21, and OPC-UA to Eventhouse for an centralized view across plants.
- Predictive Maintenance
- Inventory Prediction

**Logistics**
- Delivery Tracking and Routing
- Warehouse Management
- Supply and Demand Operations

**Finance and Insurance**
- Finance Automation
- Fraud Detection
- Operational Efficiency

**Energy and Utilities**
- Station Monitoring
- Equipment Maintenance and Monitoring
- Failure Monitoring

**Retail**
- Inventory Tracking
- Promotions and Buying Experiences
- Supply Chain Management

## Architecture
Across all of these scenarios there is a common approach on how to ingest data, transform the data, enrich the data, and visualize the data. The medallion architecture guarantees the Atomicity, Consistency, Isolation, and Durability (ACID) set of properties as data progresses through the layers. Starting with raw data, a series of validations and transformations prepares data that's optimized for efficient analytics. There are three medallion stages: bronze (raw), silver (validated), and gold (enriched). 

For more information, see [What is the medallion lakehouse architecture?](/azure/databricks/lakehouse/medallion).  

Microsoft Fabric Real-Time Intelligence possess truly unique features that make the Medallion Architecture easy to build and does not require additional infrastructure as other Data Analytics platforms.

The unique features that make this possible are:  

**Update Policies**
 - As data enters the Bronze Layer, you can use ingestion policies to transform and enrich it, adding business value.
 - These policies facilitate the processing of a continuous stream of data, by simplifying complex streaming concepts like incremental processing, checkpointing, and watermarks.
 - This abstraction allows you to build streaming applications and pipelines without the need for extra tools.
 - Microsoft Fabric Real-Time Intelligence's capability to ingest and transform live streaming data enables data engineers and data scientists to handle real-time data from various sources.
 - For more details, you can refer to [Update Policy](https://learn.microsoft.com/en-us/kusto/management/update-policy?view=microsoft-fabric)

**Materialized views**
 - Materialized views remove duplicate values as they arrive. Making deduplicated records immediately available to query.
 - Materialized views compute aggregate views as data arrives, ensuring performance enhancement, data freshness, and cost reduction.
 - Removes the need for extra tools to perform data aggregation.
 - By exposing an aggregation query over a source table or another materialized view, they always provide up-to-date results.
 - Querying a materialized view is more efficient than running the aggregation directly over the source table, leading to performance improvements.
 - Additionally, materialized views consume fewer resources, which can lead to cost savings.
 - For more details, you can refer to [Materialized View](https://learn.microsoft.com/en-us/kusto/management/materialized-views/materialized-view-overview?view=microsoft-fabric)

## Real-Time Intelligence Medallion Architecture

Real-Time Intelligence allows you to build a meallion lakehouse architecture by processing the data as it arrives. This enables you to build your Bronze, Silver, and Gold layer while mainting the real-time aspect of your data.

![Real-Time Intelligence Medallion Architecture]({{ site.baseurl }}/assets/images/rtiarch.png)

[🔍 Click to zoom in](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/architecture-medallion/architecture-medallion.png#lightbox)

For an overview of the Fabric RTI Medallion Architecture go [here]().

In order to be sucessful with a Fabric RTI archetecture you need to understand each layer. 
- Data Sources
- Bronze Layer
- Silver Layer
- Gold Layer
- Visualization and Act
  
**Bronze Layer** 
- Contains the raw records that can land in either Eventstream or a table in Eventhouse.
- Mirrors the structure of the source system and can be utilized for Change Data Captu
 
**Silver Layer** 
- As data lands in the Bronze Layer it is transformed and enriched to add business value, including deduplication of records
- Data in Eventstream uses the [Event Processing](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/process-events-using-event-processor-editor?pivots=enhanced-capabilities) capabilities, inserting the results into a table in Eventhouse
- Data in an Eventhouse table is processed immediately using an [Update Policy](https://learn.microsoft.com/en-us/kusto/management/update-policy?view=microsoft-fabric), inserting the results into a table in Eventhouse
- Deduplication occures via a [Materialized View](https://learn.microsoft.com/en-us/kusto/management/materialized-views/materialized-view-overview?view=microsoft-fabric) in Eventhouse, maintining the real-time aspect of the solution by processing duplicate records as they arrive.

**Gold Layer** 
- Data in the gold layer is optimized for visualization needs while still maintaining the real-time aspect of your data
- Aggregate views are computed as data arrives via a [Materialized View](https://learn.microsoft.com/en-us/kusto/management/materialized-views/materialized-view-overview?view=microsoft-fabric)
- Latest value views are also common via a [Materialized View](https://learn.microsoft.com/en-us/kusto/management/materialized-views/materialized-view-overview?view=microsoft-fabric) allow quick acces to the latest received value based on your dataset

**Visualize and Act**
- Data can be visualized using many components such as Power BI, RTI Dashboards, or KQL Querysets
- The performnce capabilities of RTI allow these visuals to pull from both the Gold Layer for aggregated views and unlock high granularity analytics by pulling from the Silver Layer
- DataActivator unlocks the ability to act on data at any layer
  - As data arrives in Eventstream
  - High-Granular data in the Silver Layer
  - Aggregated Data from the Gold Layer

## Key Benefits of Medallion Lakehouse Architecture in Real-Time Intelligence

**Purposely Build**
Real-Time Intelligence in Microsoft Fabric was built to handle continuously flowing data along with high granularity data. The entire flow from Bronze to Gold is built into the product and with no scheduling is able to process the data from Bronze to Silver to Gold immediately as it arrives.

This is made possible by:
- [Event Processing](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/process-events-using-event-processor-editor?pivots=enhanced-capabilities)
- [Update Policy](https://learn.microsoft.com/en-us/kusto/management/update-policy?view=microsoft-fabric)
- [Materialized View](https://learn.microsoft.com/en-us/kusto/management/materialized-views/materialized-view-overview?view=microsoft-fabric)

**Flexibility**
In a typical medallion lakehouse architecture, data is consumed only from the Gold Layer, loosing the individual records and preventing high-granular analytics. With Eventhouse you are able to consume data from both the Gold Layer or the Silver Layer, unlocking high-granularity analytics.

**Built-In Data Management**
Data at each layer has different requirements for retention and querying. This process is easily implemented via built-in capabilities.
- **Bronze Layer**
You may want to keep this data for Change Capture purposes and the ability to replay the data. If your Bronze Layer is utilizing Eventstream then you can output the data to OneLake before any transformations or enhancements are performed by the event processing. If your Bronze Layer is utilizing an Eventhouse table you can [mirror](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-house-onelake-availability) the data to OneLake.

- **Silver Layer**
Typically, at this layer you will have two tables. One for the transfromation and enhancements along wih a materialized-view for deduplications. On the first table you can set the [retention policy](https://learn.microsoft.com/en-us/kusto/management/retention-policy?view=microsoft-fabric) to 0 days meaning the data never shows up in the table but is stilled deduped by the materialized-view. The dedup materialized-view is used for high granular analytics, so setting both the [retention policy](https://learn.microsoft.com/en-us/kusto/management/retention-policy?view=microsoft-fabric) for how long you want to keep the data and the [caching policy](https://learn.microsoft.com/en-us/kusto/management/cache-policy?view=microsoft-fabric) based on your query patterns allows you to optimize your cost. Many time the silver layer is not needed for the length of time the Gold Layer is.

- **Gold Layer**
This layer is optimized for visualization with your aggregate materialized-view and latest value materialized-view. In most scenarios this down-sampled data is kept and queried for a longer period of time than your Silver Layer. By utilizing [retention policy](https://learn.microsoft.com/en-us/kusto/management/retention-policy?view=microsoft-fabric) for how long you want to keep the data and the [caching policy](https://learn.microsoft.com/en-us/kusto/management/cache-policy?view=microsoft-fabric) based on your query patterns, this process is handle nativly.

**Native Visualization Layer**
With a single click I can pin any query from the Gold or Silver layer into a new or existing Power BI Report or RTI Dashboard.

**OneLake Availability**
Taking your data from the Silver Layer and expose it as delta parquet in OneLake via [Eventhouse OneLake Availability](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-house-onelake-availability). RTI wil maintain the data based on your retention policy and you are only charged for a single copy of the data.

## Related content

For more information about implementing a Fabric lakehouse, see the following resources.

- [Microsoft Fabric decision guide: choose a data store](../get-started/decision-guide-data-store.md)
- Questions? Try asking the [Fabric community](https://community.fabric.microsoft.com/).
- Suggestions? [Contribute ideas to improve Fabric](https://ideas.fabric.microsoft.com/).
