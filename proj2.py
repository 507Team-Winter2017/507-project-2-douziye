#proj2.py
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import ssl

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.nytimes.com'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

headlines = soup.find_all(class_ = "story-heading")
for (headline, i) in zip(headlines, range(1, 11)):
	if headline.a:
		print(headline.a.text.replace("\n", " ").strip())
	else:
		print(headline.contents[0].strip())

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.michigandaily.com/'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

headlines = soup.find_all("div", class_ = "view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-99658157999dd0ac5aa62c2b284dd266")
for headline in headlines:
	print (headline.get_text())

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://newmantaylor.com/gallery.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

imgs = soup.find_all('img')
for img in imgs:
	try:
		alt_text = img['alt']
		print(alt_text)
	except:
		print('No alternative text provided!!')


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

prefix = "https://"
host = "www.si.umich.edu"
count = 1

def print_email(href, count):
	url = prefix + host + href
	req = urllib.request.Request(url, None, {'User-Agent':'SI_CLASS'})
	html = urlopen(req, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")

	emails = soup.find_all('div', class_ = "field field-name-field-person-email field-type-email field-label-inline clearfix")
	for email in emails:
		prof_email = email.find('div', class_ = 'field-item even')
		print(count, prof_email.get_text())

def faculty_email(link_href, count):
	url = prefix + host + link_href
	req = urllib.request.Request(url, None, {'User-Agent':'SI_CLASS'})
	html = urlopen(req, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	contact_details = soup.find_all('div', class_ = 'field field-name-contact-details field-type-ds field-label-hidden')
	for contact in contact_details:
		prof = contact.find('div', class_ = 'field-item even')
		href = prof.a['href']
		print_email(href, count)
		count += 1
	next_link = soup.find('li', class_ = 'pager-next last')
	if next_link.a:
		link_href = next_link.a['href']
		faculty_email(link_href, count)
	else:
		exit()

initial_href = '/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
faculty_email(initial_href, count)



