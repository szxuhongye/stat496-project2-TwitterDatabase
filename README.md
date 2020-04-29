# stat496-project2-TwitterDatabase
This project provides twitter data collection, storage, cache and search application using MongoDB and MySQL.

1. Data Collection
Use TwitterListener.py to get raw data through tweepy api

2. Data Wrangling
MongoAtlasSetup.ipynb preprocess the raw data and select 45,000 samples from it.

3. MongoDB
Store the samples into MongoDB.

4. MySQL
Store the samples into MySQL.

5. LRU
We use LRU to cache part of the data.

6. Search Application
GUI_LRUCaching.ipynb is a rough application to help us realize search actions. 
