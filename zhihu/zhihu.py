#-*- coding:utf-8 -*-
import zhihu_login
from bs4 import BeautifulSoup
from zhihu_login import *
import requests
import json
from time import sleep,ctime
import os
import re
import time
import random
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import threading

reload(sys)
sys.setdefaultencoding('utf8')
'''设定主要访问链接'''
zhihu_url='https://www.zhihu.com'
question_id='22341406'
topic_id='19776749'
zhihu_question=zhihu_url+'/question/{0}'
zhihu_topic=zhihu_url+'/topic/{0}'
question_follower=zhihu_question+'/followers'
topic_follower=zhihu_topic+'/followers'

Default_headers={
'Host':'www.zhihu.com',
'Origin':'https://www.zhihu.com',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'
}

def main():
	html=s.get(zhihu_url,headers=Default_headers).text
	soup=BeautifulSoup(html)
	data={'start':0,'offset':0,'_xsrf':soup.find('input',attrs={'name':'_xsrf'})['value']}
	headers=dict(Default_headers)
	headers['Referer']=question_follower.format(question_id)
	num=20
	offset=0
	while num==20:
		data['offset']=offset
		time.sleep(random.randint(1,4))
		res=s.post(question_follower.format(question_id),data=data,headers=headers)	
		num=res.json()['msg'][0]
		offset+=num
		soup=BeautifulSoup(res.json()['msg'][1])
		for ob in soup.find_all('a',{'class':'zg-link author-link'}):
			person_url=ob.attrs['href']
			print person_url
			info=s.get(person_url,headers=Default_headers).text
			soup=BeautifulSoup(info)
if __name__=='__main__':
	try:
		s.cookies.load(ignore_discard=True)
	except:	
		print(u"Cookie 文件未能生成，输入%s中验证码完成登入" % os.path.abspath('captcha.gif'))
	if isLogin():
		print '爬虫登入成功！'
	else:
		print '爬虫登入失败！'
		login()
	main()