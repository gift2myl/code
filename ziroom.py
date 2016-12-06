#-*- coding:utf-8 -*-
import requests
import sys
from bs4 import BeautifulSoup
from xlwt import *
reload(sys)
sys.setdefaultencoding('utf-8')
def main(num):
	url='http://www.ziroom.com/z/nl/?p=%d' % num
	r=requests.get(url)
	soup=BeautifulSoup(r.text)
	x=0
	for house in soup.find_all('li',{'class':'clearfix'}):
		for price in house.find_all('p',{'class':'price'}):
			print price.next_element
			ws.write(x+21*num,0,price.next_element.decode('utf-8'))
		for address in house.find_all('a',{'class':'t1'}):
			print address.next_element
			ws.write(x+21*num,1,address.next_element.decode('utf-8'))
		for detail in house.find_all('div',{'class':'detail'}):
			print detail.select('span')[0].string
			ws.write(x+21*num,2,detail.select('span')[0].string.decode('utf-8'))
			ws.write(x+21*num,3,detail.select('span')[1].string.decode('utf-8'))
			ws.write(x+21*num,4,detail.select('span')[2].string.decode('utf-8'))
		x+=1


if __name__=='__main__':
	w=Workbook()
	ws=w.add_sheet('ziroom')
	for i in xrange(0,251):
		main(i)
	w.save('ziroom.xls')
	
		

