from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import time

# quote_page = 'http://www.basis.org.bd/index.php/members_area/member_detail/229'

# quote_page = 'http://www.bloomberg.com/quote/SPX:IND'


def myScrapper(quote_page):
    page = urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    # print(soup)

    name_box = soup.find_all('font', attrs={'color':'666666'})
    tag_box = soup.find_all('font', attrs={'color' : '#000088'})

    name_box = soup.find_all('td', attrs={'align':'left'})
    tag_box = soup.find_all('td', attrs={'align' : 'right'})

    tag_req = ['Company Name','Address','E-mail','Company website','Organization’s head in Bangladesh', 'Designation','Mobile/Direct Phone','E-mail ID']

    tag = []
    field = []
    for i in range(len(tag_box)):
        tag.append(tag_box[i].text.strip())

    for i in range(len(name_box)):
        field.append(name_box[i].text.strip())

    # sorter = np.argsort(tag_box)
    # indices = sorter[np.searchsorted(tag, tag_req, sorter=sorter)]

    indices = np.in1d(tag[0:15] , tag_req).nonzero()[0]
    field = np.array(field)

    tag = np.array(tag)
    tag_found = tag[indices]
    tag = list(tag)
    # print(tag)
    # print(field)
    # print(list(field[indices]))

    data = ""
    # print(tag_found)
    # print(max(indices))
    # print(indices)
    for i in range(len(tag_req)):
        # print(tag_req[i])
        if tag_req[i] in tag_found:
            data += field[tag.index(tag_req[i])].replace(',','') + ','
        else:
            data += ','

    # data += field[-4] +','+ field[-3] +','+ field[-2] +','+ field[-1]
    # print(data)

    return data



for i in range(11,1418): #1418
    quote_page = 'http://www.basis.org.bd/index.php/members_area/member_detail/' + str(i)
    try:
        singleData = myScrapper(quote_page)
        print('fetched ....'+ str(i))
        print(singleData)
        if len(singleData)>10:
            print('writing .... '+ str(i))
            with open('test.csv','a') as f:
                f.write(singleData+'\n')
    except:
        pass

    time.sleep(.5)