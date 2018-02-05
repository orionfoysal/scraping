'''
For windows. Tested on windows 10
- include poppler to windows path variable
- run python try-win.py pdf/1.pdf

'''

import math
import re
import sys
import os
import subprocess
from tqdm import tqdm

# filename = sys.argv[1]

def fileParser(filename):
    args = ['pdftotext', '-layout', '-q', filename, '-']
    # args = ['pdftotext', '-layout', '-q', filename, '-']
    doc = subprocess.check_output(args, universal_newlines=True)

    # print(doc)

    lines = doc.split('\n')

    lineNumber = 0

    nameOne = lines[9].lstrip()
    nameOne = nameOne.split(',')[0]
    # print(nameOne)

    reference = math.nan 

    emailOne = ""
    emailTwo = ""
    emailThree = ""
    orgOne = ""
    nameTwo = ""
    nameThree = ""
    emailOne = ""
    emailTwo = ""
    emailThree = ""
    mobOne = ""
    mobThree = ""
    mobTwo = ""
    desigOne = ""
    desigThree = ""
    desigTwo = ""
    orgOne = ""
    orgThree = ""
    orgTwo = ""
    for line in lines:
        if lineNumber < 30:
            if line.find('Mobile') >= 0:
                mobOne = line.split(':')[1].lstrip()
                mobOne = mobOne.split(',')[0]
                # print(mobOne)
            if line.find('email') >= 0:
                emailOne = line.split(':')[1].lstrip()
                emailOne = emailOne.split(',')[0]
                match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{3})$', emailOne)
                if match != None:
                    pass
                else:
                    emailOne = ''
                # print(emailOne)
        if line.find('Reference ') >= 0:
            reference = lineNumber
        
        if lineNumber > reference:
            try:
                if line.find('Mobile') >= 0:
                    mobile = re.split(':', line)[1].lstrip()
                    mobile = re.split('\s{2,}', mobile)
                    mobTwo = mobile[0]
                    mobThree = mobile[1]
                    # print(mobTwo)
                    # print(mobThree)

                elif line.find('EMail') >= 0:
                    email = re.split(':', line)[1].lstrip()
                    email = re.split('\s{2,}', email)
                    emailTwo = email[0]
                    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{3})$', emailTwo)
                    if match != None:
                        pass
                    else:
                        emailTwo = ''
                    emailThree = email[1]
                    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{3})$', emailThree)
                    if match != None:
                        pass
                    else:
                        emailThree = ''
                    # print(emailTwo)
                    # print(emailThree)
                
                elif line.find('Organization') >= 0:
                    organization = re.split(':', line)[1].lstrip()
                    organization = re.split('\s{2,}', organization)
                    # print(organization)
                    orgTwo = organization[0]
                    orgTwo = re.sub(',', '.', orgTwo)
                    orgThree = organization[1]
                    orgThree = re.sub(',','', orgThree)
                    # print(orgTwo)
                    # print(orgThree)

                elif line.find('Designation') >= 0:
                    designation = re.split(':', line)[1].lstrip()
                    designation = re.split('\s{2,}', designation)
                    desigTwo = designation[0]
                    desigTwo = desigTwo.split(',')[0]
                    desigThree = designation[1]
                    desigThree = desigThree.split(',')[0]
                    # print(desigTwo)
                    # print(desigThree)

                elif line.find('Name') >= 0:
                    name = re.split(':', line)[1].lstrip()
                    name = re.split('\s{2,}', name)
                    nameTwo = name[0]
                    nameThree = name[1]
                    # print(nameThree)
                    # print(nameTwo)

            except:
                pass

        if line.find('Employment History') >= 0:
            emp = lines[lineNumber:10+lineNumber]
            emp = list(filter(None, emp))

            desigOne = emp[2].lstrip()
            desigOne = desigOne[3:desigOne.find('(')]
            desigOne = desigOne.split(',')[0]
            orgOne = emp[3].lstrip()
            orgOne = orgOne.split(',')[0]

        lineNumber += 1

    # print(lines	)

    lines.index('')


    infoOne = nameOne +',' + emailOne + ',' + mobOne + ',' + desigOne + ',' + orgOne
    infoTwo = nameTwo + ',' + emailTwo + ',' + mobTwo + ',' + desigTwo + ',' + orgTwo
    infoThree = nameThree + ',' + emailThree + ',' + mobThree + ',' + desigThree + ',' + orgThree


    # print(infoOne)
    # print(infoTwo)
    # print(infoThree)

    with open('resumes.csv','a') as f:
        f.write(infoOne+'\n')

    
    with open('references.csv','a') as f:
        f.write(infoTwo + '\n')
        f.write(infoThree + '\n')
    

# Folder Containing the PDFs to be parsed 

folder = 'PDF\\'
files = os.listdir(folder)

for file in tqdm(files):
    try:
        fileParser(folder+file)
    except:
        pass


'''
# # Remove the blank rows from the csv file
'''

# with open('resumes.csv') as input, open('resumes_with_no_blank_rows.csv', 'w', newline='') as output:
#     writer = csv.writer(output)
#     for row in csv.reader(input):
#         if any(field.strip() for field in row):
#             writer.writerow(row)