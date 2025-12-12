import pandas as pd
import re

# Load dataset
df = pd.read_csv("data/jobs.csv")

# print(df.head())
# print(df.info())
# print(df.isnull().sum())
# print(df.describe())
# df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# df.drop_duplicates(subset = 'job_id', inplace=True)

# # Handle missing values
# df['experience'] = df['experience'].fillna("Not Provided")
# df['qualifications'] = df['qualifications'].fillna("Not Specified")
# df['salary_range'] = df['salary_range'].fillna("Not Provided")
# df['location'] = df['location'].fillna("Unknown")
# df['country'] = df['country'].fillna("Unknown")
# df['latitude'] = df['latitude'].fillna("None")
# df['longitude'] = df['longitude'].fillna("None")
# df['work_type'] = df['work_type'].fillna("Unknown")
# df['company_size'] = df['company_size'].fillna("Unknown")
# df['job_posting_date'] = pd.to_datetime(df['job_posting_date'], errors='coerce')
# df['preference'] = df['preference'].fillna("None")
# df['contact_person'] = df['contact_person'].fillna("Not Provided")
# df['contact'] = df['contact'].fillna("Not Provided")
# df['job_title'] = df['job_title'].fillna("Unknown")
# df['role'] = df['role'].fillna("Unknown")
# df['job_portal'] = df['job_portal'].fillna("Unknown")
# df['job_description'] = df['job_description'].fillna("")
# df['benefits'] = df['benefits'].fillna("")
# df['skills'] = df['skills'].fillna("")
# df['responsibilities'] = df['responsibilities'].fillna("")
# df['company'] = df['company'].fillna("Unknown")
# df['company_profile'] = df['company_profile'].fillna("")

# # Parsing Salary Range into salry_min & salary_max cols! (also removing the $ and K symbols from the values)
# def parse_salary_usd(salary_str):
#     if pd.isnull(salary_str):
#         return None, None
    
#     # Remove $ and spaces
#     s = salary_str.replace("$", "").replace(" ", "")
    
#     # Split range
#     parts = s.split("-")
    
#     def convert(part):
#         # Handle K for thousand
#         if "K" in part.upper():
#             return int(float(part.upper().replace("K","")) * 1000)
#         else:
#             return int(part)
    
#     if len(parts) == 2:
#         salary_min = convert(parts[0])
#         salary_max = convert(parts[1])
#     elif len(parts) == 1:
#         salary_min = salary_max = convert(parts[0])
#     else:
#         salary_min = salary_max = None
    
#     return salary_min, salary_max

# # calling the salary parsing function and creating two new columns salary_min and salary_max
# df[['salary_min', 'salary_max']] = df['salary_range'].apply(lambda x: pd.Series(parse_salary_usd(x)))

# def clean_skills(skills_str):
#     if pd.isnull(skills_str):
#         return []
    
#     skills_list = re.split(r',|;', skills_str)
#     skills_list = [s.strip().lower() for s in skills_list if s.strip()]
#     return skills_list

# df['clean_skills'] = df['skills'].apply(clean_skills)

# def clean_text(text):
#     if pd.isnull(text):
#         return ""
    
#     text = re.sub(r'<[^>]+>', ' ', text) # this will find and replace '<[^>]+>' with ' ' (whitespace) from the 'text'
#     text = re.sub(r'\s+', ' ', text)
#     return text.strip().lower()

# columns_to_clean = ['job_description', 'benefits', 'responsibilities', 'company_profile']

# for col in columns_to_clean:
#     if col in df.columns:
#         df[col + '_clean'] = df[col].apply(clean_text)


# # Normalizing the dataset
# # ----- Text categorical columns -----
# df['work_type'] = df['work_type'].fillna("Unknown").str.title().str.strip()
# df['location'] = df['location'].fillna('unknown')


# # again checking for null values after cleaning
# print(df.isnull().sum())

# # Dropping rows with critical missing values
# df = df.dropna(subset = ['job_id', 'job_title'])

# # saving the cleaned dataset to a new csv file
# df.to_csv('data/cleaned_data.csv', index=False)




# Removing 'company_profile', 'responsibilities', 'benefits', 'job_description', 'skills', 'salary_range' cols from the 
# cleaned_jobs file and keeping just their cleaned versions along with remaining cols

# df2 = pd.read_csv('data/cleaned_data.csv')
# print("Before dropping columns:")
# print(df2.columns)

# columns_to_drop = ['company_profile', 'responsibilities', 'benefits', 'job_description', 'skills', 'salary_range']
# df2.drop(columns = columns_to_drop, inplace = True)

# print("\n\n\nAfter dropping columns:")
# print(df2.columns)

# # renaming cleaned columns
# df2.rename(columns={
#     'company_profile_clean': 'company_profile',
#     'responsibilities_clean': 'responsibilities',
#     'benefits_clean': 'benefits',
#     'job_description_clean': 'job_description',
#     'clean_skills': 'skills'
# }, inplace=True)

# print("\n\n\nAfter renaming cleaned columns:")
# print(df2.columns)

# def parse_company_profile(profile):
#     try:
#         profile = profile.replace("'", "\"")  # replace single quotes with double quotes for valid JSON
#         profile_dict = ast.literal_eval(profile)
#         # Return as separate columns instead of keeping a dict
#         # company_name = profile_dict.get('company', '')
#         sector = profile_dict.get('sector', '')
#         industry = profile_dict.get('industry', '')
#         city = profile_dict.get('city', '')
#         state = profile_dict.get('state', '')
#         zip_code = profile_dict.get('zip', '')
#         website = profile_dict.get('website', '')
#         ticker = profile_dict.get('ticker', '')
#         ceo = profile_dict.get('ceo', '')
#         return pd.Series([sector, industry, city, state, zip_code, website, ticker, ceo])
#     except:
#         return pd.Series(['']*8)  # empty columns if parsing fails

# # Apply function
# company_cols = ['sector','industry','city','state','zip','website','ticker','ceo']
# company_df = df2['company_profile'].apply(parse_company_profile)
# company_df.columns = company_cols
# df2 = pd.concat([df2, company_df], axis=1)


# df2 = df2.rename(columns = {'company' : 'company_name'})

# df2.to_csv('data/completely_cleaned_jobs_data.csv', index=False) # this is the final dataset

df3 = pd.read_csv('data/completely_cleaned_jobs_data.csv')
df4 = pd.read_csv('csv_files_creation/companies.csv')

merged = df3.merge(df4, on = 'company_name', how = 'left')

merged = merged.drop(columns = ['company_profile'])

merged.to_csv('data/final_jobs_companies_data.csv', index=False)