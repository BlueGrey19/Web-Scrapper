import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

write_file = open("jobs.txt", "w")
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    write_file.write(
        f"{title_element.text.strip()}, {company_element.text.strip()}, {location_element.text.strip()}\n")

soft_jobs = open("software_jobs.txt", "w")

if "Developer" in title_element:
    soft_jobs.write(
        f"{title_element.text.strip()}, {company_element.text.strip()}, {location_element.text.strip()}\n")
elif "Engineer" in title_element:
    soft_jobs.write(
        f"{title_element.text.strip()}, {company_element.text.strip()}, {location_element.text.strip()}\n")

soft_jobs.close()
write_file.close()
