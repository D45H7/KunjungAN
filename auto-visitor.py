#!/usr/bin/python39
#EasyMade by EtcAug10

import os

try:
	import requests,urllib
except:
	os.system("pip install requests && pip install urllib")
	quit("Silahkan jalankan ulang skrip")

banner = """
/))                     ((\\
/))    Auto Visit bot   ((\\
/))   Made by EtcAug10  ((\\
/))     ©2020 D45H7     ((\\
"""

def visit(t,u):
	h = {'user-agent':u}
	req = requests.post(t,headers=h)
	if req.status_code == 200:
		print("\033[00;0mSedang mengunjungi \033[32;1m",t,"\033[00;0m dengan \033[31;1m",u)
	else:
		print("\033[35;1mGagal, \033[00;0mterdapat error \033[31;1m",req.status_code)

print("\033[00;0m",banner)
print("\nAuto Visitor bot requests for bind in system")
url = input("Masukkan url target (http): ")
useragents = urllib.request.urlopen("https://raw.githubusercontent.com/cvandeplas/pystemon/master/user-agents.txt").read()
useragents = useragents.decode("utf-8").splitlines()
for ua in useragents:
	visit(url,ua)
	continue

quit("Hadeh.. Capek gan.. Istirahat dulu.. :D")