from __future__ import print_function
from pyspark import SparkContext, SparkConf

# how to run: spark-submit intro-rdd.py

if __name__ == '__main__':

	# spark context
	conf = SparkConf().setAppName("FirstSpark").setMaster("local[*]")
	sc = SparkContext(conf=conf)

	# log off
	logger = sc._jvm.org.apache.log4j
	logger.LogManager.getLogger("org").setLevel(logger.Level.OFF)
	logger.LogManager.getLogger("akka").setLevel(logger.Level.OFF)

	# process text
	lines = sc.textFile('../dataset/news.txt')
	print(lines.count())

	# save text
	lines.filter(lambda line: 'Google' in line) \
		.saveAsTextFile("../outputs/news2")

	sc.stop()
