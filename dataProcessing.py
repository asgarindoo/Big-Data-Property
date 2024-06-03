from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("Jabodetabek House Price Processing").getOrCreate()

def process_data():
        # Read the CSV file into a DataFrame
        df = spark.read.csv("E:/jabodetabek_house_price.csv", header=True, inferSchema=True)

        # Select the required columns
        selected_columns = [
            "price_in_rp", "address", "district", "city", "lat", "long",
            "property_type", "land_size_m2", "building_size_m2", "certificate", "electricity",
            "floors", "building_age", "year_built", "property_condition"
        ]
        df_selected = df.select(*selected_columns)

        # Clean the data by removing rows with null values in any of the selected columns

        df_selected.show(df_selected.count(), False)

        df_selected.printSchema()


        return df_selected

process_data()
