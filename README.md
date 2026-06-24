# Logistics-Job-Market-Analysis
# Logistics Job Market Analysis & Web Scraping

## Overview

This project focuses on collecting and analyzing logistics and supply chain job postings from Naukri.com using Python and Selenium. The objective is to build a clean dataset of logistics-related job opportunities across major Indian cities and analyze the skills currently demanded in the industry.

## Features

* Automated job data collection using Selenium.
* Multi-city job search across:

  * Mumbai
  * Delhi
  * Chennai
  * Pune
  * Bengaluru
  * Ahmedabad
* Collection of logistics and supply chain job postings for multiple roles.
* Extraction of:

  * Job Title
  * Company Name
  * Location
  * Required Skills
  * Posted Date
  * Job URL
* Data cleaning and preprocessing using Pandas.
* Duplicate removal and city name standardization.
* Comparative analysis of skill requirements between Naukri and LinkedIn job postings.

## Technologies Used

* Python
* Selenium
* Pandas
* Chrome WebDriver

## Project Structure

```text
Logistics-Job-Market-Analysis/
│
├── naukri_scraper_200.py
├── clean_jobs_200.xlsx
├── clean_jobs_200.csv
├── requirements.txt
└── README.md
```

## Dataset Details

The final dataset contains:

* 200+ unique logistics job postings
* 6 major Indian cities
* Multiple logistics and supply chain job roles
* Cleaned and standardized data for analysis

## Job Roles Covered

* Fleet Supervisor
* Dispatch Executive
* Warehouse Coordinator
* Logistics Trainer
* Last Mile Delivery Manager
* Supply Chain Executive
* Fleet Manager

## Key Outcomes

* Developed a scalable web scraping solution for job market research.
* Built a structured logistics recruitment dataset.
* Identified common technical, operational, and managerial skills required in logistics roles.
* Compared hiring trends across multiple recruitment platforms.

## Future Improvements

* Multi-page scraping support.
* Automated LinkedIn job analysis.
* Interactive dashboard using Power BI or Streamlit.
* Job trend visualization and reporting.

## Author

Raghul Baskaran
