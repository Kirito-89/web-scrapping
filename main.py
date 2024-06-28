from bs4 import BeautifulSoup
import requests
import time


# enter the skill on which you want to perform filtering
print('put some skill that you are not familier with')
unfamilier=input('>')
print(f"Filtering out {unfamilier}")

# function to get information from the website
def find_job():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        company_name=job.find('h3',class_='joblist-comp-name').text.replace( ' ','')
        skills=job.find('span',class_='srp-skills').text
        published_date=job.find('span',class_='sim-posted').span.text
        more_info=job.header.h2.a['href']
        if unfamilier not in skills:
            print(f"COMPANY_NAME:{company_name.strip()}")
            print(f"SKILLS:{skills.strip()}")
            print(f"PUBLISHED_DATE:{published_date.strip()}")
            print(f"MORE_INFO:{more_info.strip()}")
            print()
        
# running the function after fixed intervals(here 10 minutes)
if __name__=='__main__':
    while True:
        find_job()
        tine_wait=10
        print(f"waiting {tine_wait} minutes")
        time.sleep(600)


    
