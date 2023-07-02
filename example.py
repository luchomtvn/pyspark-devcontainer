from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName(SparkByExamples.com).getOrCreate()

print(spark)

rdd = sparl.sparkContext.parallelize([1,2,3,4,56])
print("RDD count" + rdd.count())

