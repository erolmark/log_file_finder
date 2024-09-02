from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Site İsmini Gir \n(örnek : example.com or www.example.com ): ")
	print "\n\n Mevcut Linkler: \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "Basarili Log Dosyası=> ",req_link

def Credit():
	Space(9); print "#####################################"
	Space(9); print "#   +++ Log Dosyası Bulucu +++   #"
	Space(9); print "#     Developers Veraildez&Medusa   #"
	Space(9); print "#    Versa Community Versa Team   #"
	Space(9); print "#####################################"
	print("daha yapım aşamasındadır. siteyi yazarken sonuna / koymayin!")

Credit()
findAdmin()
