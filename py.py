import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_titles = []
company_names = []
locations_names = []
skills = []
links = []
salary = []
page_num = 0

while "true":

    result = requests.get(f"https://wuzzuf.net/search/jobs/?a=navbg&q=python&start={0}")

    scr = result.content
    soup = BeautifulSoup(scr, "html.parser")
    page_limit =int (soup.find("strong").text)
    if( page_num > page_limit // 15):
      print("pages ended, terminate")
      break


    job_titles = soup.find_all("h2", {"class": "css-m604qf"})
    company_names = soup.find_all("a", {"class":"css-17s97q8"})
    locations_names = soup.find_all("span", {"class":"css-5wys0k"})
    job_skll = soup.find_all("div", {"class":"css-y4udm8"})


    for i in range(len(job_titles)):

        job_titles.append(job_titles[i].text)
        company_names.append(company_names[i].text)
        locations_names.append(locations_names[i].text)
        job_skll.append(job_titles[i].text)
        page_num +=1
        print("page switched")



    print(job_titles)
    print(company_names)
    print(locations_names)
    print(job_skll)



for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    salaries = soup.find_all("span", {"class":"css-47jx3m"})
    print(salaries.text)
    salary.append(salaries.text)


file_list = [job_titles, company_names, locations_names, skills, salary, links,]
exported = zip_longest(file_list)

