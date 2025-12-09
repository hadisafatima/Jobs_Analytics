# Data Cleaning:
- Understanding the dataset

- strandradized the col names (all lowercase)

- Removing the duplicate jobs on the basis its job_id (if its repeating means job is entered twice or more in the dataset)

- Handling missing values:
    - Job Id -> Drop rows if missing, keep unique IDs
    - Experience -> Fill missing with "Not Provided"; normalize to "X-Y years" format later
    - Qualifications -> Fill missing with "Not Specified"
    - Salary Range -> Fill missing with "Not Provided"; later parse min/max
    - Location -> Fill missing with "Unknown"
    - Country -> Fill missing with "Pakistan"
    - latitude & longitude -> Fill missing with None (optional: geocode later)
    - Work Type -> Fill missing with "Unknown"; normalize values (Full-Time, Part-Time, Contract)
    - Company Size -> Fill missing with "Unknown"; normalize ranges
    - Job Posting Date -> Convert to datetime; fill missing with NaT
    - Preference -> Fill missing with "None"
    - Contact Person & Contact -> Fill missing with "Not Provided"
    - Job Title -> Drop rows if missing
    - Role -> Fill missing with "Unknown"; normalize categories later
    - Job Portal -> Fill missing with "Unknown"
    - Job Description -> Fill missing with empty string ""
    - Benefits -> Fill missing with empty string ""
    - skills -> Fill missing with empty string ""
    - Responsibilities -> Fill missing with empty string ""
    - Company -> Drop rows if missing; normalize names later
    - Company Profile -> Fill missing with empty string ""

- Parsing the salary range values into pure integers, creating 2 new columns, salary_min & salary_max, and removing $ and K symbols from the salary range!

- converting skills from strings to lists for following reasons:
    - lists can be used to count skills
    - measure skill demand
    - generate recommendations
    - analyze most-needed skills per job role
    - run NLP models
    - useful for creating skill analytics table
    - Running NLP would be easier, it will help to remove duplicates, detect important skills in job descriptions, cluster similar skills
    - helpful for advances ML Tasks such as, Job matching, Recommendation engine, Skill gap detection, Similarity search ("find similar jobs")
    - Dashboarding specific to skills becomes easier

- Removing HTML tags symbols, coverting text to lowercase after stripping them (for multiple columns, such as: job_description, benefits, responsibilities). Because, these columns usually contain bullet points, new lines and long paragraphs.

- Renamed the changed/cleaned cols with the names of original cols and removed the uncleaned cols.
- saved the cleaned dataset into a separate .csv file.


# Data Population in DB
- Populated the cleaned and final version of data in DB.

- Creating 2 new tables from the initial DB load.
- A table from a separate csv file (job_contacts, because was facing a timeout issue when creating that).
- Three tables from a different csv file for creating skills and jobs related tables, i.e: skills, job_details,