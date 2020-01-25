import os
import random

if not os.path.isfile('./urls.txt'):          
	f = open('./urls.txt',"w+")				
	f.close()


def url_shortener(url):
	suit = 'abcdefghijklmnopqrstuvwxyz1234567890'
	l = list(suit)
	random.shuffle(l)
	sh = ''.join(l)
	link = 'blob.mu/' + sh[:7]
	return link


def url_decoder(url):
	with open ('./urls.txt', 'r') as f:		
		alldata = f.read()
		lst = alldata.split()
		idx = lst.index(url)
		lurl = lst[idx+2]
		return lurl

url = input('Enter your link to encode or decode: ')

if len(url)>15:
	lurl = url
	shurl = url_shortener(lurl)
else:
	shurl = url
	lurl = url_decoder(shurl)


toprint='short link '+ shurl + ' long link ' + lurl
print(toprint)

towrite = '\n' + shurl + ' | ' + lurl 


with open ('./urls.txt', 'r') as f:			
		alltxt = f.read()

if shurl not in alltxt:
		f =  open('./urls.txt', 'a+')			
		f.write(towrite)
		f.close()
