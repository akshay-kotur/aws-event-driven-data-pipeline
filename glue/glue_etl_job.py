from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import col

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Read raw JSON data from S3
df = spark.read.option("multiline", "true").json(
    "s3://bison-de-project/raw/data_20260504174400.json"
)

# Filter purchase events
purchase_df = df.filter(col("event") == "purchase")

# Select required fields
final_df = purchase_df.select(
    "user_id",
    "event",
    "product_id",
    "timestamp"
)

# Write transformed output to curated layer
final_df.write.mode("overwrite").parquet(
    "s3://bison-de-project/curated/"
)

print("Transformation completed successfully")
