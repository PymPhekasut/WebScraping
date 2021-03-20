from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time


driverpath = r'C:\Users\neera\Desktop\Python_Project\webscrap\chromedriver_win32\chromedriver.exe'

#hide google chrome
opt = webdriver.ChromeOptions()
opt.add_argument('headless')
driver = webdriver.Chrome(driverpath,options=opt)


def TwitterPost(twitter_name):

	url = 'https://twitter.com/{}'.format(twitter_name) #url
	driver.get(url)

	time.sleep(5)

	'''
	# Scrolling
	pixel = 10000
	for i in range(3):
		driver.execute_script("window.scrollTo(0, {})".format(pixel))
		time.sleep(3)
		pixel = pixel + 10000
	'''

	page_html = driver.page_source #print out html
	#print(page_html)

	data = soup(page_html,'html.parser')

	#find_all data might be different depend on each page source 
	posts = data.find_all('span',{'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
	#print(posts)


	#cut unneccessary bot message from website
	founddot = False
	allpost = []

	for p in posts:
		txt = p.text
			
		if founddot == True:
			allpost.append(txt)
			#print(txt)
			#print('----------------')
			founddot = False

		if txt == '·': 
			founddot = True	

	#print(allpost)

	return allpost

#Pull data

checktwitter = ['elonmask','BillGates','cnnbrk','SpaceX']

for ct in checktwitter:
	post = TwitterPost(ct)
	print('--------------- {} -------------'.format(ct))
	for p in post:
		print(p)
		print('=========')

driver.close()