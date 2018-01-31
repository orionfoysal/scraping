from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

link = 'http://www.bgmea.com.bd/member/details/19555'

def scrapper(url_link):
    page = urlopen(url_link)
    soup = BeautifulSoup(page, 'html.parser')

    name = soup.find('td', attrs = {'style':'font-size:18px; width:75%; padding-left:10px;'}).getText()
    name = name.strip()
    data = soup.find('tr', attrs={'id':'director_row0'}).getText()

    data = re.sub('[\t{1:}]','',data).lstrip()
    # data = re.sub('\n{2,}', '\n', data).strip()

    data = data.split('\n')

    info = name + ','

    designation = data[0]
    contact_name = data[3]
    mobile = data[5]
    email = data[7]

    info += designation + ',' + contact_name + ',' + mobile + ',' + email + '\n'

    return info


link_init = 'http://www.bgmea.com.bd/member/details/'

for i in range(19550, 23913): #23913
    link = link_init + str(i)
    
    try:
        info = scrapper(link)
        print('writing ....' + str(i))
        with open('BGMEA_data.csv', 'a') as f:
            f.writelines(info)

    except:
        print('failed writing ...' + str(i))