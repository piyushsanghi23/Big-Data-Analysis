# Cloud-Project-2

This project will have you perform data analysis and processing using
Hadoop MapReduce or Apache Spark. The project will use the weather dataset from
<https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/>. This project will
use only 19 years of data (2000-2019) for all the stations starting with "US"
and the elements TMAX and TMIN. 

## Creation of datasets

For the Global Historical Climatology Network (GHCN) [weather data][ghcn]:

```bash
# change into the directory where this repo was cloned
cd /dir/where/you/cloned/this/repo

mkdir data  # if it doesn't exist
cd data

for i in `seq 2000 2019`; do
    wget https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/${i}.csv.gz
    gzip -cd ${i}.csv.gz  | grep -e TMIN -e TMAX | grep ^US > ${i}.csv
done
```

The project is done in hadoop eecs cluster in mapreduce processing in python.

The mapper.py and reducer.py are mapper and reducer files respectively.

To run the MapReduce on hadoop cluster using Hadoop jar streaming, use the below command

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file /home/sanghiph/mapper.py -mapper /home/sanghiph/mapper.py -file /home/sanghiph/reducer.py -reducer /home/sanghiph/reducer.py -input /user/tatavag/weather -output /tmp/piyush_project/output_1

To check the results of the output file, use the below command

 hadoop fs -cat /tmp/piyush_project/output_1*
