# SimpleSearch
This repository contains a simple direct match based search system. The entire implemetation is in python. 
Requirement:
Python > 3.5
No extra packages needed to be installed
Installation instructions:
1. Clone this git repo or download it as zip
2. Unzip the folder if downloaded as zip
3. cd SimpleSearch
4. python SearchInterface.py
This will start a commandline promt and you can start interacting with the system.

Future improvements:
  1. The current implementation loads al the data to memory to perform search. Setting up a solr based search system would be an ideal solution to this problem. ElasticSearch has been a very successful Solr based system in market today. Indexing the data in ElasticSearch will enable us to search partial terms, range queries on datetime columns and also lets us use sql type complex queries. But this system is not efficient when joining different indices but support parent child relationship in documents.
  2. We could create sql tables based on the data available and perform any kind of search operation on fields. This storage option will be useful and faster to perform simple joins and also supports date range queries. But it can be very slow for partial queries on search values
