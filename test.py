# -*- coding:utf-8 -*-
import requests
import json
import sys
import time

token_url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx2e3374731d6a1131&secret=5b3089de41eff811c6fde3b055ece35d'
menu_url='https://api.weixin.qq.com/cgi-bin/menu/create?access_token={0}'
query='https://api.weixin.qq.com/cgi-bin/menu/get?access_token={0}'
data={
    "button":[
    {
    "type":"click",
    "name":"空气查询",
    "key":"V1001_AIR"
    },
    {
    "name":"下单",
    "sub_button":[
    {
    "type":"click",
    "name":"下单说明",
    "key":"V1001_DES"
    },
    {
    "type":"view",
    "name":"直接下单",
    "url":"https://weidian.com/?userid=1120072746&wfr=wechatpo_welcome_shop"
    }]
    },
    {
    "name":"更多",
    "sub_button":[
    {
    "type":"click",
    "name":"常见问题",
    "key":"V1001_QUES"
    },
    {
    "type":"click",
    "name":"商务合作",
    "key":"V1001_COR"
    },
    {
    "type":"view",
    "name":"有关光蓓净",
    "url":"http://www.toshiba.com.cn/renecat/about/index_j.htm"
    }]
    }]
}

token_reponse=json.loads(requests.get(token_url).content)
token=token_reponse['access_token']
#menu_html=requests.post(menu_url.format(token),data=json.dumps(data,ensure_ascii=False)).text
query_html=requests.get(query.format(token)).text
#print menu_html
print query_html
