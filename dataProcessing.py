from pyspark.sql import SparkSession

# Initialize Spark Session with Cassandra connector
spark = SparkSession.builder \
    .appName("Jabodetabek House Price Processing") \
    .config("spark.cassandra.connection.host", "127.0.0.1") \
    .config("spark.cassandra.connection.port", "9042") \
    .config("spark.jars.packages", "com.datastax.spark:spark-cassandra-connector_2.12:3.1.0") \
    .getOrCreate()

def process_data():
    # Read the data from Cassandra table into a DataFrame
    df = spark.read \
        .format("org.apache.spark.sql.cassandra") \
        .options(table="homeprice_table", keyspace="homeprice_db") \
        .load()

    # Select the required columns
    selected_columns = [
        "price_in_rp", "address", "district", "city", "lat", "long",
        "property_type", "land_size_m2", "building_size_m2", "certificate", "electricity",
        "floors", "building_age", "year_built", "property_condition"
    ]
    df_selected = df.select(*selected_columns)

    # Clean the data by removing rows with null values in any of the selected columns
    df_cleaned = df_selected.dropna()

    df_cleaned.show(df_cleaned.count(), False)
    df_cleaned.printSchema()

    return df_cleaned

process_data()
