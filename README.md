# Cloud-Project-2


The project is done in hadoop eecs cluster in mapreduce processing in python.

The map.py and red.py are mapper and reducer files respectively.

To run the MapReduce on hadoop cluster using Hadoop jar streaming, use the below command

hadoop jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.3.0-235.jar -file map.py -mapper map.py -file red.py -reducer red.py -input /data/nyc/nyc-traffic.csv -output result4.csv

To check the results of the output file, use the below command

 hadoop fs -cat /user/madhyasa/result4.csv/*
