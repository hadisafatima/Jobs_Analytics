import pandas as pd
import re

# Load dataset
df = pd.read_csv("data/jobs.csv")

# print(df.head())
# print(df.info())
# print(df.isnull().sum())
# print(df.describe())
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# df.drop_duplicates(subset = 'job_id', inplace=True)

# Handle missing values
df['experience'] = df['experience'].fillna("Not Provided")
df['qualifications'] = df['qualifications'].fillna("Not Specified")
df['salary_range'] = df['salary_range'].fillna("Not Provided")
df['location'] = df['location'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['latitude'] = df['latitude'].fillna("None")
df['longitude'] = df['longitude'].fillna("None")
df['work_type'] = df['work_type'].fillna("Unknown")
df['company_size'] = df['company_size'].fillna("Unknown")
df['job_posting_date'] = pd.to_datetime(df['job_posting_date'], errors='coerce')
df['preference'] = df['preference'].fillna("None")
df['contact_person'] = df['contact_person'].fillna("Not Provided")
df['contact'] = df['contact'].fillna("Not Provided")
df['job_title'] = df['job_title'].fillna("Unknown")
df['role'] = df['role'].fillna("Unknown")
df['job_portal'] = df['job_portal'].fillna("Unknown")
df['job_description'] = df['job_description'].fillna("")
df['benefits'] = df['benefits'].fillna("")
df['skills'] = df['skills'].fillna("")
df['responsibilities'] = df['responsibilities'].fillna("")
df['company'] = df['company'].fillna("Unknown")
df['company_profile'] = df['company_profile'].fillna("")

# Parsing Salary Range into salry_min & salary_max cols! (also removing the $ and K symbols from the values)
def parse_salary_usd(salary_str):
    if pd.isnull(salary_str):
        return None, None
    
    # Remove $ and spaces
    s = salary_str.replace("$", "").replace(" ", "")
    
    # Split range
    parts = s.split("-")
    
    def convert(part):
        # Handle K for thousand
        if "K" in part.upper():
            return int(float(part.upper().replace("K","")) * 1000)
        else:
            return int(part)
    
    if len(parts) == 2:
        salary_min = convert(parts[0])
        salary_max = convert(parts[1])
    elif len(parts) == 1:
        salary_min = salary_max = convert(parts[0])
    else:
        salary_min = salary_max = None
    
    return salary_min, salary_max

# calling the salary parsing function and creating two new columns salary_min and salary_max
df[['salary_min', 'salary_max']] = df['salary_range'].apply(lambda x: pd.Series(parse_salary_usd(x)))



# continue form step 5 of chat "Data Analysis project ideas"