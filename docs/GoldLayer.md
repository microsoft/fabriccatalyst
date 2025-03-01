---
layout: page
title: Real Time Intelligence
subtitle: Gold Layer
menubar: docs_menu
show_sidebar: false
toc: true
---
# Gold Layer
The Gold Layer typically needed but not always required. In you're traditional medallion architecture this layer would be the only layer available for analytics. In a RTI Medallion architecture both the Silver Layer and Gold Layer are available for analytics.

## Why do I need a Gold Layer
There are several reason that will drive you to utilze a Gold Layer

### Time Series Analytics over long Periods
As your query grows in time period the need for individual records becomes unecessary. For instance, if I want to look at the temperature of my IoT devices over the last year I'll want an aggregate view, hourly/daily/etc.., the individual records are not helpful in this case. With a materialized view in a KQL Database you can pre-aggregate this aggregate and improve query performance.

### Down Sampling
The Eventhouse will be sized based on the amount of cache you are storing. In most situations the raw telemetry can be kept for a shorter time and the aggregate data for the longer period. Reducing the total amount of hot cache used by the Eventhouse. For example, I may keep 30 days of the Silver Table and 1 Year of an hourly aggregate.

### Latest Value
If you have a dashboard that displays tiles that show the latest value for each device. It can be useful to create a MV that just shows the latest value. This allows the tile to refresh instantly, which is typically the expectation for this type of visual.

## What not to do at the Gold Layer
There are a few common mistakes that you want to avoid at this layer:

### View for Every Aggregate Required
Just because the customer commonly creates a 5 min, 30 min, 1 hour, and daily aggregates doesn't mean that you need to create a materialized view for each.

For example, in the above scenario you can approach the solution in this manner
- Create a function that bins the Silver table in 5 min aggregates
- Create a function that bins the Silver table in 30 min aggregates
- Create a materialized view that pre-aggregates the Silver table into 1 hour aggregates
- Create a function that bins the 1 hour materialized view into daily aggregates

So now I've made it easy to pull the most common aggregates but only created a single materialized view.

### A lot of late arriving data past the Cache Period
One of the most powerful features of a materialized view is it's ability to handle late arriving data. But if you have a lot of late arriving data remember that it needs to join that with the existing MV to recalculate the aggregates. This is typically not an issue but if you have a lot of data coming in that is past the caching period for the Materialized View then it can lead to a backlog. You can handle this by
- Increasing the caching period on the MV to accomidate the data
- Setting the look back period on the MV so data past a certain age will not be materialized

## Example Aggregate MV
We'll continue the example of the IoT Data where we have a true dedup MV called ExampleDedupMV. Now we want to create a MV that does hourly aggregates and backfills the data to June 2024

```
.create async materialized-view with(backfill, effectiveDateTime=datetime(2024-06-01)) IoT_Hourly_MV on materialized-view IoTSilverDedupMV { 
IoTSilverDedupMV 
| summarize avg_Battery_Level=avg(BatteryLevel),avg_Temp=avg(Temp), avg_Humidity=avg(Humidity) by DeviceId,Model,SerialNumber, bin(EnqueuedTimeUTC,1h) 
} 
```
Once this is finished you'll have an aggregate materialized view that aggregates data as it arrives and handles late arriving data.

### Options if Silver is Arg_Max or Arg_Min Materialized View
As mentioned in the Silver Layer if you create your "dedup" materialized view using something like arg max of the ingestion time then you cannot create an aggregate MV on top of this data. In that case there are two common options you can take:

Option 1: Aggregate the data at query time instead of pre-aggregation

Option 2: Utilize a scheduled job (for example Fabric Notebook) to aggregate the data
- This will not handle late arriving data. So you need to decide when is it acceptable to aggregate the data and ignore late arriving data. For example, I may aggregate everything over 14 days to hourly aggregates and then create a function that does the following:
  - Aggregate everything less that 14 days fromt he arg max MV
  - Union that with the preaggregated data over 14 days

## Example Latest Value MV
Here is an example command to create a latest value view with backfill.

```
.create async materialized-view with(backfill, effectiveDateTime=datetime(2024-06-01)) IoT_Hourly_MV on materialized-view IoTSilverDedupMV { 
IoTSilverDedupMV 
| summarize arg_max(EnqueuedTimeUTC, *) by DeviceId
} 
```

## Summary
At this stage you have a queriable Silver Layer along with an aggregated Gold Layer. This allow you to run ad-hoc queries and build visuals that can span long periods of time along with drilling down to specific records.

{: .no_toc }
#### Next: [Visualization]({{ site.baseurl }}/docs/Visualization/)
