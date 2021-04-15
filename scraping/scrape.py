'''
Scrapes lessons information from aca page -> writes in result.txt file
Then saves information in sql database
Checkes if new lesson has been added sends email
'''
import requests
from bs4 import BeautifulSoup
import json
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers.models import Course,DB_NAME
from helpers.helpers import send_email_for
#import  helpers.__init__ as foo
#from .models import Course,DB_NAME

from bs4 import SoupStrainer
current = os.getcwd()
import xml.etree.ElementTree as ET


def save_html_files(endpoint,file_name):

    response = requests.get(endpoint)

    if response.status_code == 200:
        with open(file_name, 'w+b') as html_file:
            html_file.write(response.content)
    else:
        print(response.text)


def url_request(ENDPOINT):
    #save_html_files(ENDPOINT, 'aca_content_en.html')

    with open('aca_content_en.html', 'r+', encoding='utf8') as f:
        text = f.read()
    soup = BeautifulSoup(text,'html.parser')
    div = soup.find('div', attrs={'id': 'courses'})
    all_a = div.find_all('a')
    couses_id = {}
    for link in all_a:
        if(link.get('href') != None):
            if('https:'in link.get('href')):
                subpage = (link.get('href')).rstrip('/')
            else:
                subpage = f"{ENDPOINT}{link.get('href')}".rstrip('/')
            #save_html_files(subpage, f"{subpage.split('/')[-1].replace('.','_')}.html")
            couses_id[subpage] = subpage.split('/')[-1].replace('.','_')
    return couses_id

engine = create_engine(f'sqlite:///{current}/helpers/{DB_NAME}')
session = sessionmaker(bind=engine)()



def parse_file(course_id,course_url):
    new_course_added = []
    with open (f'{course_id}.html',encoding='utf8') as f:
        text =f.read()

    soup =BeautifulSoup(text, 'html.parser')

    if(not soup.find('div',attrs={'id': 'content'}) or (not soup.find('div', attrs={'id': 'tutors'})) ):
        return ('course_id = {} -> None '.format(course_id))
    div =soup.find('div',attrs={'id': 'content'}).find_all('tr')

    a = []
    for el in div:
        a.append(el.text)

    price = ''
    level = ''
    for el in a:
        if 'Price' in el :
            price = el.split(':')[-1].strip('\n')
        if 'Level' in el :
            level = el.split(':')[-1].strip('\n')
    course_name = soup.find('h1').text

    div = soup.find('div', attrs={'id': 'tutors'})
    work_place = div('p')

    teach_list = []
    for i in range(len(div('h3'))):
        if(len(div('h3')[i]) == 2 ):
            teach_list.append(div('h3')[i].text.split('\n')[0].strip())
        elif(len(div('h3')[i]) == 1):
            teach_list.append(div('h3')[i].text.strip())

    teachers = []
    for i in range(len(work_place)):
         one_teach = {'full_name': teach_list[i] ,
                      'company': work_place[i].text.strip()
                      }
         teachers.append(one_teach)
         #print(teach_list[i],work_place[i].text.strip())


    one_subject ={
        "course_name": str(course_name),
        "course_id": course_id,
        "course_url": course_url,
        "price": price,
        "level": level,
        "teachers": teachers
    }

    if session.query(Course).filter_by(course_id = course_id).count() <1:
        new_course =Course(**{
            "course_name": str(course_name),
            "course_id": course_id,
            "course_url": course_url,
            "price": price,
            "level": level,
            "teachers": str(teachers)
        })
        session.add(new_course)
        session.commit()
        new_course_added.append(course_id)

    send_email_for(new_course_added,session)
    return one_subject

if __name__ == '__main__':
    ENDPOINT = 'https://aca.am/en/'
    url_dict = url_request(ENDPOINT)
    content_list = []
    cnt = 0
    for el in url_dict:
        cnt+=12
        content_list.append(parse_file(url_dict[el],el))

        if cnt ==1:
            break
    print(session.query(Course.course_name).all())
    result =(json.dumps(content_list, indent=4, sort_keys=True))
    print(result)
    with open('results.txt', 'w+' )as f:
        f.write(result)