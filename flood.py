import socks, socket, sys, os, requests, urllib2, subprocess
from sockshandler import SocksiPyHandler
#declarations
numberip = 0
numberport = 0
host = "http://leposteurip.000webhostapp.com"
porttarget = 80


with open("ip.txt") as file_in:
	linesip = []
	for line in file_in:
		linesip.append("http://" + line)
with open("port.txt") as file_anotherin:
	linesport = []
	for lineport in file_anotherin:
		linesport.append(lineport)

while True:
	ip = linesip[numberip]
	port = linesport[numberport]
	s = socks.socksocket()
	numberip +=1
	try:
	#connection
		proxu = { ip : port }
		print(proxu)
		print("Proxy Set...")
		#s.set_proxy(socks.HTTP, ip, port)
		print("Connection...")
		r=requests.get(host, proxies=proxu)
		print("Connected!")
		s.close()
	except:
		print("Erreur !")
	if numberip == 133 or numberport == 133:
		numberip = 0
		numberport = 0
#s.set_proxy(socks.HTTP, lines[linenumber], port)
