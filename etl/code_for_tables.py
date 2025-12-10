import pandas as pd
import ast

# Load CSV
df = pd.read_csv("data/completely_cleaned_jobs_data.csv")

# --- Convert job_id to integer ---
df['job_id'] = df['job_id'].round(0).astype('Int64')

# --- 1. Extract and clean company profile ---
def parse_company_profile(profile):
    try:
        profile_dict = ast.literal_eval(profile)
        return {
            'sector': profile_dict.get('sector', ''),
            'industry': profile_dict.get('industry', ''),
            'city': profile_dict.get('city', ''),
            'state': profile_dict.get('state', ''),
            'zip': profile_dict.get('zip', ''),
            'website': profile_dict.get('website', ''),
            'ticker': profile_dict.get('ticker', ''),
            'ceo': profile_dict.get('ceo', '')
        }
    except:
        return dict(sector='', industry='', city='', state='', zip='', website='', ticker='', ceo='')

company_info = df['company_profile'].apply(parse_company_profile)
company_df = pd.concat([df[['company']].rename(columns={'company':'company_name'}), company_info], axis=1)
company_df = company_df.drop_duplicates(subset=['company_name']).reset_index(drop=True)

# --- 2. Locations ---
locations_df = df[['location', 'country', 'latitude', 'longitude']].drop_duplicates()
locations_df = locations_df.rename(columns={'location':'city'})

# --- 3. Jobs ---
# company_df['company_id'] = company_df.index + 1
# locations_df['location_id'] = locations_df.index + 1

df = df.merge(company_df[['company_name', 'company_id']], left_on='company', right_on='company_name')
df = df.merge(locations_df[['city', 'country', 'location_id']], left_on=['location','country'], right_on=['city','country'])

jobs_df = df[['job_id','job_title','role','job_portal','location_id','company_id',
              'work_type','company_size','job_posting_date','preference',
              'contact_person','contact','salary_min','salary_max','job_description','benefits','responsibilities']]

# --- 4. Skills ---
skills_set = set()
job_skill_map = []

for _, row in df.iterrows():
    try:
        skills_list = ast.literal_eval(row['skills'])
        for skill_item in skills_list:
            for skill in skill_item.split(','):
                skill_clean = skill.strip()
                if skill_clean:
                    skills_set.add(skill_clean)
                    job_skill_map.append({'job_id': row['job_id'], 'skill_name': skill_clean})
    except:
        continue

skills_df = pd.DataFrame(list(skills_set), columns=['skill_name'])
skills_df['skill_id'] = skills_df.index + 1

job_skill_map_df = pd.DataFrame(job_skill_map)
job_skill_map_df['job_id'] = job_skill_map_df['job_id'].astype('Int64')
job_skill_map_df = job_skill_map_df.merge(skills_df, on='skill_name')[['job_id','skill_id']]

# --- 5. Save CSVs for SQL import ---
company_df.to_csv('final/companies.csv', index=False)
locations_df.to_csv('final/locations.csv', index=False)
jobs_df.to_csv('final/jobs.csv', index=False)
skills_df.to_csv('final/skills.csv', index=False)
job_skill_map_df.to_csv('final/job_skill_map.csv', index=False)
