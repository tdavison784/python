#!/usr/bin/python
import json
from OnCall import OnCall

filename = "Oncall.json"
url = 'https://g46pilc3cmpub01.voice.ccm.state.mn.us/ucmuser/'

my_user = OnCall(url)

user = 'pwtwd35'
passwd = '02022018'

my_user.load_web_browser(user, passwd)

number = ['96517855140', '96512168066']
#Date format needs to be like so: mm-dd-Y H:M
#date = "02-02-2018 14:14"

my_user.change_oncall_number(number)