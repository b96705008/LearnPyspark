# Let's learning PySpark!

## Setup the enviroment
1. Setup the Scala 2.11.8: 
 * download from https://www.scala-lang.org/download/2.11.8.html
 * move folder to /usr/local/share/scala
 * vim ~/.bashrc or vim ~/.bash_profile
 ```
 export SCALA_HOME=/usr/local/scala
 export PATH=$PATH:$SCALA_HOME/bin
 ```

2. Setup Spark 2.1.0
 * download from http://spark.apache.org/downloads.html (hadoop version can be 2.6)
 * vim ~/.bashrc or vim ~/.bash_profile
 ```
 export SPARK_HOME=$RES_PATH/spark/spark-2.1.0-bin-hadoop2.6
 export PATH=$PATH:$SPARK_HOME/bin
 export PYTHONPATH=$SPARK_HOME/python/lib/pyspark.zip:$PYTHONPATH
 export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH
 export PYSPARK_DRIVER_PYTHON=ipython
 ```
 
3. Start with pyspark and jupyter
 * pyspark shell
 ```
 pyspark
 ```
 
 * jupyter (check the notebook.sh)
 ```
 export PYSPARK_DRIVER_PYTHON=jupyter
 export PYSPARK_DRIVER_PYTHON_OPTS="notebook" 
 pyspark
 ```
 
## Course syllabus
* Week 1 - introduce the Spark and RDD (Roger)
* Week 2 - Spark Dataframe, SQL and interact with Hive (冠穎、采襄)
* Week 3 - Spark configuration with partitions, yarn mode and so on. (Miles)
* Week 4~ - Case study (hackathon, digital, hive table, text or work with Kafka)
