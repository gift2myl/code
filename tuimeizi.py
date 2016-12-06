#-*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import requests
import urllib
import os
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
def gethtml(n):
	html=urllib2.urlopen('http://www.douban.com/group/haixiuzu/discussion?start=%d' %n)
	return html.read()
def downxiushe(number):
	folder='./羞射'
	folder1=folder.unicode("").encode("utf-8")
	if not os.path.isdir(folder1):
		os.makedirs(folder1)
	else:
		html_context=gethtml(number)
		soup=BeautifulSoup(html_context)
		topic=soup.find_all('td',attrs={'class':'title'})
		for topic_url in topic:
			href=topic_url.find('a')
			url=href.get('href')
			title=href.attrs['title']
			print url,title
			title1=title.decode('utf-8').encode('gbk')
			os.makedirs(os.path.join(folder1,title1))
			url_html=requests.get(url)
			soup1=BeautifulSoup(url_html.text)
			figure=soup1.find_all('div',attrs={'class':'topic-figure cc'})
			person=soup1.find_all('span',attrs={'class':'from'})
			for person_one in person:
				information=person_one.find('a')
				zhuye=information.get('href')
				name=information.next_element
				f=open(folder+'/'+title+'/'+name+'.txt','a+')
				f.write(zhuye)
				f.close()
			for image in figure:
				photo=image.find('img')
				photo_src=photo.attrs['src']
				number=random.randint(1,99)
				urllib.urlretrieve(photo_src,folder+'/'+title1+'/'+name+'number'+'.jpg')

if __name__=='__main__':
	for n in range(0,201,25):
		downxiushe(n)