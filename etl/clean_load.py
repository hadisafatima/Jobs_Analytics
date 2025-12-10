# import os
# import mysql.connector
# import pandas as pd

# # Read DB credentials from environment
# db_host = os.environ.get("DB_HOST", "localhost")
# db_user = os.environ.get("DB_USER", "user")
# db_pass = os.environ.get("DB_PASSWORD", "")
# db_name = os.environ.get("DB_NAME", "job_market")

# conn = mysql.connector.connect(
#     host=db_host,
#     user=db_user,
#     password=db_pass,
#     database=db_name
# )

# df = pd.read_csv("data/jobs.csv")
# df.to_sql('jobs', con=conn, if_exists='replace', index=False)
# print("Data loaded successfully!")







# # import os
# # import pandas as pd
# # import mysql.connector

# # # Connect to MySQL
# # conn = mysql.connector.connect(
# #     host=os.environ['DB_HOST'],
# #     user=os.environ['DB_USER'],
# #     password=os.environ['DB_PASSWORD'],
# #     database=os.environ['DB_NAME']
# # )
# # cursor = conn.cursor()

# # # Load cleaned CSV
# # df = pd.read_csv("data/cleaned_jobs.csv")

# # # Insert companies first
# # companies = df['company'].drop_duplicates()
# # for comp in companies:
# #     cursor.execute("INSERT IGNORE INTO companies (name) VALUES (%s)", (comp,))

# # conn.commit()

# # # Map company names to IDs
# # cursor.execute("SELECT id, name FROM companies")
# # company_map = {name: id for id, name in cursor.fetchall()}

# # # Insert jobs
# # for _, row in df.iterrows():
# #     cursor.execute("""
# #         INSERT INTO jobs (title, company_id, city, province, posted_date, description, salary_raw)
# #         VALUES (%s,%s,%s,%s,%s,%s,%s)
# #     """, (
# #         row['title'],
# #         company_map[row['company']],
# #         row['city'],
# #         row.get('province', None),
# #         row.get('posted_date', None),
# #         row['description'],
# #         row['salary_raw']
# #     ))

# # conn.commit()
# # conn.close()
# # print("Data loaded successfully!")

