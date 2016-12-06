#-*- coding:utf-8 -*-
import requests
import sys
from bs4 import BeautifulSoup
import re
import os.path
import json
import urllib
import time
try:
    import cookielib
except:
    import http.cookiejar as cookielib

reload(sys)
sys.setdefaultencoding('utf-8')
url='https://www.zhihu.com'
url_login='http://www.zhihu.com/login/email'
s=requests.session()
s.cookies=cookielib.LWPCookieJar(filename='cookies')

post_header={
 			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
 			'Accept-Encoding': 'gzip, deflate, sdch',
 			'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
 			'Connection': 'keep-alive',
 			'Host': 'www.zhihu.com',
 			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36', 
 			'Referer': 'http://www.zhihu.com/'
 			}

def get_xsrf():
	r=s.get(url,headers=post_header)
	xsrf=re.search(r'name="_xsrf" value="(.*)"',r.text)
	return xsrf.group(1)
def get_captcha():
	t = str(int(time.time()*1000))
	captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
	captcha_data=s.get(captcha_url,headers=post_header).content
	with open('captcha.gif','wb') as f:
		f.write(captcha_data)
	captcha_str = raw_input('请输入您的验证码\n>>>')
	return captcha_str

	
def login():
	
	login_data={
	'_xsrf':get_xsrf(),
	'email':'20037489@qq.com',
	'password':'gift1986',
	'remember_me':'true',
	'captcha':get_captcha()
	}
	data=urllib.urlencode(login_data)
	res=s.post(url_login,data=login_data,headers=post_header)
	print res.status_code
	m_cookies=res.cookies
	s.cookies.save(ignore_discard=True,ignore_expires=True)
#ignore_discard: save even cookies set to be discarded. 
#ignore_expires: save even cookies that have expired.The file is overwritten if it already exists
def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    login_code = s.get('https://www.zhihu.com/settings/profile',headers=post_header,allow_redirects=False)
    if int(x=login_code.status_code) == 200:
        return True
    else:
        return False

if __name__=='__main__':
	try:
		s.cookies.load(ignore_discard=True)
	except:	
		print(u"Cookie 文件未能生成，输入%s中验证码完成登入" % os.path.abspath('captcha.gif'))
	if isLogin():
		print'登入成功!'
	else:
		login()
	
	