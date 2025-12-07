import pandas as pd
from sqlalchemy import create_engine
import pymysql
import json

# ----------------------------
# Step 1: Load the cleaned CSV
# ----------------------------
csv_path = "data/completely_cleaned_jobs_data.csv"  # change to your CSV path
df = pd.read_csv(csv_path)

# ----------------------------
# Step 2: Convert clean_skills to JSON string
# ----------------------------
# SQLAlchemy / MySQL needs JSON as a string
# df['clean_skills'] = df['clean_skills'].apply(lambda x: json.dumps(eval(x)) if pd.notnull(x) else '[]')

# ----------------------------
# Step 3: Connect to MySQL
# ----------------------------
# Replace user, password, host, port, db_name as per your setup
user = "root"
password = "LetsDatabase_3"
host = "localhost"
port = 3306
db_name = "jobs_data"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}", echo=False)

# ----------------------------
# Step 4: Create / Replace table and load data
# ----------------------------
# if_exists options: 'fail', 'replace', 'append'
# 'replace' will drop table if exists and create a new one
df.to_sql("jobs", con=engine, if_exists="replace", index=False, chunksize=500)

print("✅ Table populated successfully!")
