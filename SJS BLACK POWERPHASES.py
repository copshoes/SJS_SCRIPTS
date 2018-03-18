# -*- coding: utf-8 -*-
import requests
import time
from random import getrandbits
import itertools
import names
import threading
from threading import Thread
from itertools import cycle
import random


print(time.strftime("%H:%M:%S") + " - FOR STRIKE SHOES")
print(time.strftime("%H:%M:%S") + " - For: For Black Powerphases" + "\n")

threads = int(input((time.strftime("%H:%M:%S") + " - Thread number:")))

def enter(threads):

 first = names.get_first_name()
 second = names.get_last_name()
 dob = "05/12/1989"
 email = "COPSTRIKE+" + str(getrandbits(40)) + "@gmail.com"  # Change COPSTRIKE to ur email
 phone = str(getrandbits(40))  # random phone number
 sizes = ["7", "7 ½", "8", "8 ½", "9", "9 ½", "10", "10 ½", "11", "11 ½", "12", "12 ½", "13"]
 size = random.choice(sizes)
 city = "New York" # Change Your city

 off_url = "https://slamjamsocialism-drops.com/drops/52"
 sitekey = "6LfYhz0UAAAAAJFKp28Sg0NnAEIPMfKI1RJSGsdB"

 api_key = ""  # 2CAP API KEY HERE

 captcha_id = requests.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(api_key, sitekey,off_url)).text.split('|')[1]
 recaptcha_answer = requests.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(api_key, captcha_id)).text
 while 'CAPCHA_NOT_READY' in recaptcha_answer:
     time.sleep(5)
     recaptcha_answer = requests.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(api_key, captcha_id)).text
 token = recaptcha_answer.split('|')[1]
 print(time.strftime("%H:%M:%S") + " - Got captcha from 2captcha!")

 headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

 data = {"query":"mutation RequestOrdertMutation($data: OrderRequestInput!) {\n  requestOrder(data: $data)\n}\n","operationName":"RequestOrdertMutation","variables":{"data":{"firstName":first,"lastName":second,"email":email,"phone":phone,"country":"840","city":city,"order":[{"product":"45","size":"9 ½"}],"raffle":"49","captcha":token,"date":"2018-02-27T19:22:10+00:00"}}}

 res = requests.post('https://slamjamsocialism-drops.com/graphql', headers=headers, json=data)
 if 'true' in res.text:
     print((time.strftime("%H:%M:%S")) + " - [SUCCESS - @STRIKESHOES] - Entered raffle: " + size + " - " + first + " " + second + " - " + email)
     enter(threads)
 else:
     print((time.strftime("%H:%M:%S")) + " - [FAILED - @STRIKESHOES] - Failed to enter raffle: " + email)
     enter(threads)


for i in range(threads):
    t = Thread(target=enter, args=(i,))
    t.start()
