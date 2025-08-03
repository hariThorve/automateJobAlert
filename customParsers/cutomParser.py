import pandas as pd
from bs4 import BeautifulSoup
import requests
#since we  are working on only Moody's therefore extracting only moody's data

data = pd.read_excel("../data/data.xlsx")
baseUrl = "https://careers.moodys.com"

moodyData = {
    'co-ordinator': data["Name"][0],
    "Mobile Number": str(data["Mobile Number"][0]),
    "Comapany Name": data["Company Name"][0],
    "currentRoles":[],
    "jobUrl": "https://careers.moodys.com/jobs?sort_by=update_date"
}

# Database Structure

# #currentRoles: [{
#   "role": fetch data,
#   "roleApplyUrl": fetch,
#   "Posted": fetch,
#   "Location": fetch,
#   "JobCategory": fetch,
#   "ExperienceLevel": fetch,
# }]



#experienced level cannot be fetched because it contains same class as the datePosted tag with no unique id, hence whenever it is to be fetched date gets printed



def getJobsList(url):
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data , 'lxml')
    jobLists = soup.find_all('li' , 'results-list__item')
    return jobLists

def getJobsDetailsFromJobsList(moodyData, jobLists):
    for li in jobLists:
        role = li.find('a','results-list__item-title--link').text
        roleApplyUrl = li.find('a', 'results-list__item-title--link')['href']
        html_data = requests.get(baseUrl+roleApplyUrl).text
        soup = BeautifulSoup(html_data , 'lxml')
        jobDescription = soup.find('ul', 'text-[1rem] font-normal leading-[1.5] job-details-brief__description-list md:basis-1/3')
        postedDate = jobDescription.find('span', id='posted').get_text(strip=True)
        locationUl = jobDescription.find('ul', 'job-description__locations-list')
        location = locationUl.find('li', 'attr-value').text
        jobCategoryUl = jobDescription.find('ul', 'job-description__categories-list')
        jobCategory = jobCategoryUl.find('li', 'attr-value').text
        jobCategoryUl = jobDescription.find('ul', 'job-description__categories-list')
        jobCategory = jobCategoryUl.find('li', 'attr-value').text
        # experienceUl = jobDescription.find('li', 'job-details-brief__description-list--item')
        # experience = experienceUl.find('span', 'attr-value').text
        moodyData["currentRoles"].append({
            "role": role,
            "roleApplyUrl": baseUrl+roleApplyUrl,
            "Posted": postedDate,
            "Location": location,
            "JobCategory": jobCategory,
            # "ExperienceLevel": experience,
        })

    return moodyData

jobList = getJobsList(moodyData["jobUrl"])
moodyData = getJobsDetailsFromJobsList(moodyData, jobList)


print("Following roles found\n")
for roles in moodyData['currentRoles']:
    print(roles)
    print("\n")