# -*- coding:utf-8 -*-
import requests



s=requests.session()
reponse=s.post('http://ami.ziroom.com/AMI/houseStatusAndRoomStatusInterface/houseStatusAndRoomStatusInterface!getRoomLockHouseInfo.do?house_source_code=BJZRTZ20822241')
print reponse.