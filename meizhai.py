#-*- coding:utf-8 -*-
import requests
import sys
from bs4 import BeautifulSoup
from xlwt import *
import re

reload(sys)
sys.setdefaultencoding('utf-8')

login_url='http://meizhai.cn/Agent/User/NormalLogin'
house_list_url='http://meizhai.cn/Agent/house/rent'+'?page={0}'
url='http://meizhai.cn'
update_url='http://meizhai.cn/Agent/house/UpdateTimes'

data={
	'LogName':'18910812366',
	'Password':'15985266'
	}
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
	'Origin':'http://meizhai.cn',
	'Referer':'http://meizhai.cn/home/login'
	}
s=requests.session()
def login():
	r=s.post(login_url,data=data,headers=headers)
	if r.status_code==200:
		print '验证成功'

def main():
	for i in xrange(1,50):
		house_list=s.get(house_list_url.format(i)).text
		soup=BeautifulSoup(house_list)
		x=0
		for j in soup.find_all('h3'):
			ahref=j.next_element.next_element['href']
			house_detail_url=url+ahref
			id_code=re.split(r'/agent/house/detail/',ahref)[1]
			hid=re.split(r'_',id_code)[0]
			house_detail=s.get(house_detail_url).text
			soup=BeautifulSoup(house_detail)
			name=soup.find('h2').em.string.strip()
			rent=soup.find('strong',{'class':'colf60'}).string
			style=soup.find('td',{'width':'126'}).span.string
			area=soup.find('td',{'width':'207'}).span.string.strip()
			sale_type=soup.find('span',{'class':'cola8'}).string.strip()
			print name,rent,style,area,sale_type
			ws.write(x+20*(i-1),0,name.decode('utf-8'))
			ws.write(x+20*(i-1),1,rent.decode('utf-8'))
			ws.write(x+20*(i-1),2,style.decode('utf-8'))
			ws.write(x+20*(i-1),3,area.decode('utf-8'))
			ws.write(x+20*(i-1),4,sale_type.decode('utf-8'))
			update_data={
			'hid':hid,
			'producttype':'2'
			}
			res=s.post(update_url,data=update_data)
			if res.json()['status']==200:
				house_owner_url=url+res.json()['imgUrl']
				ws.write(x+20*(i-1),5,house_owner_url.decode('utf-8'))
				im=requests.get(house_owner_url)
				if im.status_code == 200:
    					open('./'+'owner/'+name+'.jpg', 'wb').write(im.content)
    			elif res.json()['status']==411:
    				ws.write(x+20*(i-1),5,'美宅查看流量已超期')
    			x+=1
			
if __name__=='__main__':
	login()
	w=Workbook(encoding='utf-8')
	ws=w.add_sheet('meizhai')
	main()
	w.save('./'+'owner/'+'meizhai.xls')
		

