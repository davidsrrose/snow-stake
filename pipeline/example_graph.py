import duckdb

# Create a DuckDB in-memory connection
conn = duckdb.connect(":memory:")

# Path to your CSV file
csv_file_path = "sources/snowfall_data/daily_snowfall_data.csv"

# Load the CSV into a DuckDB table
conn.execute(f"""
    CREATE TABLE snowfall_data AS 
    SELECT * 
    FROM read_csv_auto('{csv_file_path}');
""")
print("CSV data loaded into DuckDB.")

# Corrected SQL query
query = """
WITH daily_data AS (
    SELECT 
        CAST(strftime('%Y', Date) AS INTEGER) AS year,
        CAST(strftime('%m', Date) AS INTEGER) AS month,
        SUM("Snowfall") AS total_snowfall
    FROM snowfall_data
    GROUP BY year, month
),
year_over_year AS (
    SELECT
        year,
        month,
        total_snowfall,
        LAG(total_snowfall) OVER (PARTITION BY month ORDER BY year) AS last_year_snowfall,
        (total_snowfall - LAG(total_snowfall) OVER (PARTITION BY month ORDER BY year)) AS yoy_difference
    FROM daily_data
)
SELECT * FROM year_over_year
ORDER BY year, month;
"""

# Execute the query
result = conn.execute(query).fetchall()

# Print the results
print("Year-over-Year Snowfall Data:")
for row in result:
    print(row)

# Save results to a new CSV
output_csv = "sources/snowfall_data/year_over_year_snowfall.csv"
conn.execute(f"""
    COPY (
        {query.strip().rstrip(';')}  -- Remove the trailing semicolon
    ) TO '{output_csv}' (HEADER, DELIMITER ',');
""")
print(f"Results saved to {output_csv}.")

