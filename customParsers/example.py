# from bs4 import BeautifulSoup
# import requests
# import pandas as pd

# # reading data

# data = pd.read_excel("../data/data.xlsx")
# columns = [data.columns]
# #taking one company for now
# url = "https://careers.moodys.com/jobs?sort_by=update_date"


# html_data = requests.get(url).text
# soup = BeautifulSoup(html_data , 'lxml')
# jobLists = soup.find_all('li' , 'results-list__item')

# moodyData = {
#     'role': [],
#     'nameOfCoordinator': 
# }

# for li in jobLists:
#     role = li.find('a','results-list__item-title--link').text
#     roles.append(role)
# print(roles)
