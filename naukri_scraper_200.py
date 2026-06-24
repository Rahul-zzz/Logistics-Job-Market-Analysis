from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Job Titles
job_titles = [
    "fleet supervisor",
    "dispatch executive",
    "warehouse coordinator",
    "logistics trainer",
    "last mile delivery manager",
    "supply chain executive",
    "fleet manager India"
]

# Cities
cities = [
    "Mumbai",
    "Delhi",
    "Chennai",
    "Pune",
    "Bengaluru",
    "Ahmedabad"
]

# Store job data
jobs_data = []

# Browser setup
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# Search jobs city-wise
for city in cities:

    for job in job_titles:

        try:
            url_part = job.replace(" ", "-")
            city_part = city.lower()

            url = f"https://www.naukri.com/{url_part}-jobs-in-{city_part}"

            print("\n" + "=" * 50)
            print("City:", city)
            print("Job:", job)
            print("URL:", url)

            driver.get(url)

            time.sleep(8)

            job_cards = driver.find_elements(
                By.CLASS_NAME,
                "cust-job-tuple"
            )

            print("Jobs Found:", len(job_cards))

            for card in job_cards:

                try:
                    title = card.find_element(
                        By.CSS_SELECTOR,
                        "a.title"
                    ).text

                    job_url = card.find_element(
                        By.CSS_SELECTOR,
                        "a.title"
                    ).get_attribute("href")

                    company = card.find_element(
                        By.CSS_SELECTOR,
                        "a.comp-name"
                    ).text

                    location = card.find_element(
                        By.CSS_SELECTOR,
                        "span.locWdth"
                    ).text

                    posted_date = card.find_element(
                        By.CSS_SELECTOR,
                        "span.job-post-day"
                    ).text

                    skills_elements = card.find_elements(
                        By.CSS_SELECTOR,
                        "li.tag-li"
                    )

                    skills = " | ".join(
                        [skill.text for skill in skills_elements]
                    )

                    jobs_data.append({
                        "Search City": city,
                        "Job Title": title,
                        "Company": company,
                        "Location": location,
                        "Required Skills": skills,
                        "Posted Date": posted_date,
                        "Job URL": job_url
                    })

                except:
                    continue

        except:
            continue

driver.quit()

# Create DataFrame
df = pd.DataFrame(jobs_data)

# Remove exact duplicates
df.drop_duplicates(inplace=True)

# Standardize city names
df["Location"] = (
    df["Location"]
    .str.replace("Bangalore", "Bengaluru", regex=False)
)

# Clean skills column
df["Required Skills"] = (
    df["Required Skills"]
    .fillna("")
    .str.replace("\n", " ")
    .str.strip()
)

# Keep only first 200 records
df = df.head(200)

# Save CSV
df.to_csv(
    "clean_jobs_200.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n" + "=" * 50)
print("Completed Successfully")
print("Total Records:", len(df))
print("Output File: clean_jobs_200.csv")