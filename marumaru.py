#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib
import urllib2
import os


def getImgFunction( link , title ) :
	print ('%s , %s') % ( link, title )
	
	req = urllib2.Request( link )
	user_agent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"

	req.add_header("User-agent", user_agent)

	res = urllib2.urlopen ( req ).read().decode('utf-8')
	soup = BeautifulSoup(res, 'html.parser')
	
	imgList = soup.find_all('img', {'class': 'lz-lazyload'})

	img_number = 0

	title = title.replace(' ', '')
	title = title.replace(u' ', '')
	absoluteFilePath = u"/Users/yongseokson/만화책/" + title
	print absoluteFilePath

	if os.path.exists( absoluteFilePath ) == False :
		os.makedirs( absoluteFilePath )

	for img in imgList :
		imgUrl = 'http://wasabisyrup.com' + img['data-src']

		img_number = img_number + 1
		img_name = ('%s_%03d.jpg') % ( title , img_number)

		imgPath = (u"%s/%s") % ( absoluteFilePath , img_name )

		commandExec = 'curl %s -o %s' % ( imgUrl , imgPath )
		os.system( commandExec.encode('utf-8') )


def getTitleLinkLit() :
	query = u'완결'.encode('utf-8')  
	url = 'http://marumaru.in/?c=1/33&cat=' + query + '&p=6&uid=168760'

	#res = urllib.urlopen( url ).read().decode('utf-8')

	url = 'http://marumaru.in/b/manga/131676'
	req = urllib2.Request(url)
	user_agent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"

	req.add_header("User-agent", user_agent)

	res = urllib2.urlopen ( req ).read().decode('utf-8')
	soup = BeautifulSoup(res, 'html.parser')

	#print( type ( soup ) )

	contentList = soup.find_all('div', {'id': 'vContent'})
	titleLists = contentList[0].find_all('a')

	for title in titleLists :

		if title.text.find(u'권') == -1 :
			continue

		getImgFunction( title['href'] , title.text )

	print 'test'
	print 'test2'
	
if __name__ == "__main__" :
	getTitleLinkLit()