# from urllib.request import urlopen, Request
# from bs4 import BeautifulSoup
# import numpy as np
# import time
# import re


# def myScrapper(quote_page):
#     req = Request(quote_page, headers={'User-Agent': 'Mozilla/5.0'})

#     page = urlopen(req).read()

#     soup = BeautifulSoup(page, 'html.parser')

#     # print(soup)
#     all_text = soup.getText()
#     # all_text = re.sub(r'\n{2,}','\n',all_text)
#     # print(all_text)

#     list_all_text = all_text.splitlines()

#     # print(list_all_text)
#     info = ""
#     if 'Company Name :' in list_all_text:
#         company_name = list_all_text[list_all_text.index('Company Name :')+1]
#         print(company_name)

#     if 'BKMEA Membership Number :' in list_all_text:
#         mem_id = list_all_text[list_all_text.index('BKMEA Membership Number :')+1]
#         print(mem_id)

#     if 'Contact Person Name :' in list_all_text:
#         con_person = list_all_text[list_all_text.index('Contact Person Name :')+1]
#         print(con_person)
    
#     if 'Contact Person Mobile Number :' in list_all_text:
#         contact_mobile = list_all_text[list_all_text.index('Contact Person Mobile Number :')+1]
#         print(contact_mobile)

#     if 'Contact Person Designation :' in list_all_text:
#         designation = list_all_text[list_all_text.index('Contact Person Designation :')+1]
#         print(designation)

    
#     #     # print(contact_info)
#     #     if 'Name ' in contact_info:
#     #         info += contact_info[contact_info.index('Name ') + 1] + ','
        
#     #     if 'Designation ' in contact_info:
#     #         info += contact_info[contact_info.index('Designation ') + 1] + ','

#     #     if 'Mobile ' in contact_info:
#     #         info += contact_info[contact_info.index('Mobile ') + 1] + ','

#     #     if 'E-mail ' in contact_info:
#     #         info += contact_info[contact_info.index('E-mail ') + 1] + ','

        
#     #     # print(info)



#     # name_box = soup.find_all('font', attrs={'color':'666666'})
#     # tag_box = soup.find_all('font', attrs={'color' : '#000088'})

#     # name_box = soup.find_all('td', attrs={'align':'left'})
#     # tag_box = soup.find_all('tr', attrs={'class' : 'normal', 'onMouseOver':"this.className='highlight'", 'onMouseOut':"this.className='normal'"})

#     # print(tag_box)
#     # print(tag_box.text.strip())

#     # tag_req = ['Company Name','Address','E-mail','Company website','Organization’s head in Bangladesh', 'Designation','Mobile/Direct Phone','E-mail ID']

#     # tag = []
#     # field = []
#     # for i in range(len(tag_box)):
#     #     tag.append(tag_box[i].text.strip())

#     # for i in range(len(name_box)):
#     #     field.append(name_box[i].text.strip())

#     # # sorter = np.argsort(tag_box)
#     # # indices = sorter[np.searchsorted(tag, tag_req, sorter=sorter)]

#     # indices = np.in1d(tag[0:15] , tag_req).nonzero()[0]
#     # field = np.array(field)

#     # tag = np.array(tag)
#     # tag_found = tag[indices]
#     # tag = list(tag)
#     # # print(tag)
#     # # print(field)
#     # # print(list(field[indices]))

#     # data = ""
#     # # print(tag_found)
#     # # print(max(indices))
#     # # print(indices)
#     # for i in range(len(tag_req)):
#     #     # print(tag_req[i])
#     #     if tag_req[i] in tag_found:
#     #         data += field[tag.index(tag_req[i])].replace(',','') + ','
#     #     else:
#     #         data += ','

#     # data += info
#     # # print(data)

#     return list_all_text


# a = myScrapper('http://www.bkmea.com/member/member_details.php?BackView&Page=1&Index=a&MID=1469')


# # for i in range(9,1418): #1418
# #     quote_page = 'http://www.basis.org.bd/index.php/members_area/member_detail/' + str(i)
# #     try:
# #         singleData = myScrapper(quote_page)
# #         print('fetched ....'+ str(i))
# #         # print(singleData)
# #         if len(singleData)>10:
# #             print('writing .... '+ str(i))
# #             with open('basis.csv','a') as f:
# #                 f.write(singleData+'\n')
# #     except:
# #         print('failed to get data')

# #     time.sleep(.1)

import re

with open('bkmea.csv','r') as f:
    lines = f.readlines()[1:]

lineNumber = 0

for line in lines:
    splitted = line.split('\"')
    personal_info = splitted[1]
    # print(personal_info)
    company = re.split(r'\s{2,}', personal_info)[2]
    # print(company)
    contact_info = splitted[3]
    contact_info = re.split(r'\s{2,}', contact_info)
    name = contact_info[2]

    mobile = contact_info[4]
    if mobile == 'Contact Person Designation :':
        mobile = 'Unavailable'

    ind_designation = contact_info.index('Contact Person Designation :')
    designation = contact_info[ind_designation + 1]

    ind_office_add = contact_info.index('Office')
    office_add = contact_info[ind_office_add + 2]
    office_add = re.sub(',',';',office_add)

    emails = re.findall(r'[\w\.-]+@[\w\.-]+', splitted[3])

    web = re.findall(r'www.+[\w-]+.[a-zA-Z]', splitted[3])
    # web = re.findall('(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', splitted[3])
    web = ''.join(web)
    emails = ''.join(emails)

    rows = company + ',' + name +','+ mobile + ',' +designation + ',' +office_add + ',' +emails +',' + web

    with open('BKMEA_data.csv', 'a') as f:
        f.writelines(rows + '\n')

    print(rows)

