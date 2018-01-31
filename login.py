import requests

with requests.Session() as c:
    url = 'https://corporate3.bdjobs.com/corporate_submit.asp'
    USERNAME = 'orelco'
    PASSWORD = 'Login1#'

    c.get(url)
    login_data = dict(NAME = USERNAME, PASS = PASSWORD)
    r = c.post(url, data=login_data, headers={"Referer": "https://corporate3.bdjobs.com/"})
    # print(r.text)
    page = c.get('https://corporate3.bdjobs.com/view_resume.asp?Idn=28056952035ID1400864&key=University+of+Dhaka&keytype=')
    
    page = page.text

    with open('resume_sample.html', 'w') as f:
        f.write(page)


# import codecs
# f = codecs.open('resume.html', 'r', 'utf-8')
# doc = BeautifulSoup(f.read(), 'html.parser').get_text()
# print(doc)