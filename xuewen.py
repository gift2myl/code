# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import xlrd
import xlwt
import time
import random
url='https://xuewen.ziroom.com/?/sort_type-new__day-0__is_recommend-0__page-{0}'

s=requests.Session()
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
'Cookie':'_ga=GA1.2.1921438511.1461038367; Hm_lvt_038002b56790c097b74c818a80e3a68e=1477274423,1477383098,1478255531,1478485633; __utma=18275762.1921438511.1461038367.1478587991.1478601210.249; __utmz=18275762.1478601210.249.239.utmcsr=z.ziroom.com|utmccn=(referral)|utmcmd=referral|utmcct=/; gfx__Session=v7794i4lqf9c9kqukflb8vocg3; gfx__user_login=cast-256%7C6A3B2893B40AECBF7973A25E3BA4984B66926E04CE9CB8DA2503556C3E02AE7006B2977382F15C3F80AD0A5F4204CE24A62189D363153C4F5E8E0B061396F953E1B2B1C2632B5A4CA61958489C7C86998A0706A369A4B306242457683AE6C41D'
}
n=0
f=xlwt.Workbook()
sheet1=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
for i in range(88):
	html=s.get(url.format(i),headers=headers)
	soup=BeautifulSoup(html.text)
	for content in soup.find_all('div',{'class':'aw-question-content'}):
		time.sleep(random.randint(1,3))
		question_url=content.find('h4').next_element.next_element['href']
		question=content.find('h4').next_element.next_element.string
		subject=content.find('a',{'class':'aw-question-tags'}).string
		print question,subject
		detail_html=s.get(question_url,headers=headers).text
		soup=BeautifulSoup(detail_html)
		detail=soup.find_all('div',{'class':'markitup-box'})
		try:
			answer=detail[1].string
			question=detail[0].string
		except:
			pass
		n+=1
		sheet1.write(n,0,question)
		sheet1.write(n,1,subject)
		sheet1.write(n,2,question)
		sheet1.write(n,3,answer)
		
f.save("D://gift.xls")

		