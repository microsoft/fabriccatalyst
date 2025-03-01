---
layout: page
title: Real Time Intelligence
subtitle: Medallion Architecture - Silver Layer
menubar: docs_menu
show_sidebar: false
toc: true
---

## Silver Layer
The Silver Layer is about getting your data into an easily queriable format. This typically includes transformation, normalization, and connecting to reference data to provide additonal context for the telemetry data.

In a typical RTI Medalian Architecture the Silver Layer is made up of two table:
- Transformed Table: Using either Eventstream Event Procesor or Update Policies in KQL DB this table contains your transformed, normalized, and refernce data
- Dedup Materialized View: This layer isn't always needed but is typical for any telemetry workload. This layer will dedup the records fromt he transformed table as the records arrive.

## Transform Table
As records arrive in the Bronze layer they are processed and inserted into this transform table in a KQL DB. 
  
### Event Processor
Eventstream has a built in processor to allow you to transform and enhance data and output the results to a KQL DB table. The current list of supported operations are:

| Transformation |	Description |
| ------- | ------- |
| Filter	| Use the Filter transformation to filter events based on the value of a field in the input. Depending on the data type (number or text), the transformation keeps the values that match the selected condition, such as is null or is not null.
| Manage fields |	The Manage fields transformation allows you to add, remove, change data type, or rename fields coming in from an input or another transformation.
| Aggregate |	Use the Aggregate transformation to calculate an aggregation (Sum, Minimum, Maximum, or Average) every time a new event occurs over a period of time. This operation also allows for the renaming of these calculated columns, and filtering or slicing the aggregation based on other dimensions in your data. You can have one or more aggregations in the same transformation.
|Group by |	Use the Group by transformation to calculate aggregations across all events within a certain time window. You can group by the values in one or more fields. It's like the Aggregate transformation allows for the renaming of columns, but provides more options for aggregation and includes more complex options for time windows. Like Aggregate, you can add more than one aggregation per transformation.
| Union |	Use the Union transformation to connect two or more nodes and add events with shared fields (with the same name and data type) into one table. Fields that don't match are dropped and not included in the output.
| Expand |	Use the Expand array transformation to create a new row for each value within an array.
| Join |	Use the Join transformation to combine data from two streams based on a matching condition between them.

### KQL Update Policy
In a KQL DB you can define an [Update Policy](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/table-update-policy) on the destination table. Part of the update policy defines the source table. Once this is defined as soon as data is ingested into the source table a KQL query will be run to transform the data and the results will be inserted into the destination table. 

This gives you the ability to process the data however you like as long as you can create a KQL Query to do the procesing. 

### How to Choose
- First look is the transformation possible in both.
  - Typically time window function are easier in event processor
  - More advanced transformations typically lean towards KQL Update Policies
- Comfort Level
  - If the transformation can be done in both then lean towards the tool your most comfortable with
  - Event Processor is low-code/no-code experience
  - KQL DB Update Policy is driven by KQL Queries
- Cost
  - Event Procesor consumes capacity units according to how many transformations you are doing

{: .no_toc }
#### Next: [Gold Layer]({{ site.baseurl }}/docs/GoldLayer/)