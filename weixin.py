# -*- coding:utf-8 -*-
def log(func):
	def wrapper():
		print "call %s" %(func.__name__)
		func()
		return func
 	return wrapper
@log
def gift():
	print '2016/11/11'

a=gift
a()