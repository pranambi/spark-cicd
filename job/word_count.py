from pyspark.sql import SparkSession


def count_words(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def run_spark_job(input_text):
    spark = SparkSession.builder.appName("WordCount").getOrCreate()
    data = [input_text]
    rdd = spark.sparkContext.parallelize(data)
    result = rdd.flatMap(lambda line: line.lower().split()) \
                .map(lambda word: (word, 1)) \
                .reduceByKey(lambda a, b: a + b) \
                .collect()
    spark.stop()
    return dict(result)


if __name__ == "__main__":
    sample_text = "the quick brown fox jumps over the lazy dog the fox"
    print(run_spark_job(sample_text))
