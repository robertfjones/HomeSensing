#!/usr/bin/env python3
from datetime import datetime
from pymongo import MongoClient
import pandas as pd


def query_between(start = "2020-01-01T00:00:00Z",end = "2029-01-01T00:00:00Z", limit_records = 14400, asc = True):
    if asc:
        sort_data = 1
    else:
        sort_data = -1
    
    data = collection.find({"time":{"$gte":datetime.strptime(start,"%Y-%m-%dT%H:%M:%SZ"),
                                    "$lte":datetime.strptime(end,"%Y-%m-%dT%H:%M:%SZ")}}).sort("time",sort_data).limit(limit_records)
    return pd.DataFrame([x for x in data]).drop("_id", axis = 1)


# Set up client for MongoDB
mongoClient=MongoClient()
db=mongoClient.local
collection=db.sensors

df = query_between(start = "2020-12-02T07:00:00Z",end = "2029-01-01T00:00:00Z")
df['time_10m'] = df['time'].dt.floor('10min')
df = df[["time_10m","topic","value"]].pivot("time_10m","topic","value")
print(df.columns)
print(df['Home/MasterNode/ExtTemp'])
df.to_csv("test.csv")