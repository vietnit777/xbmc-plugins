import CommonFunctions as common
import urllib
import urllib2
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import urlfetch
from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.hdplay')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
thumbnails = xbmc.translatePath( os.path.join( home, 'thumbnails\\' ) )

def _makeCookieHeader(cookie):
      cookieHeader = ""
      for value in cookie.values():
          cookieHeader += "%s=%s; " % (value.key, value.value)
      return cookieHeader

def make_request(url, headers=None):
        if headers is None:
            headers2 = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
                       'Referer' : 'http://www.google.com'}
        try:
            req = urllib2.Request(url,headers=headers2)
            f = urllib2.urlopen(req)
            body=f.read()
            return body
        except urllib2.URLError, e:
            print 'We failed to open "%s".' % url
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            if hasattr(e, 'code'):
                print 'We failed with error code - %s.' % e.code


def get_categories():
    add_link('', 'AXN HD', 0, 'http://117.103.206.21:88/channel/GetChannelStream?path=AXNHD/AXNHD_live.smil', thumbnails + 'AXN HD.jpg', '')
    add_link('', 'Star Movies HD', 0, 'http://117.103.206.21:88/channel/GetChannelStream?path=StarMovieHD/StarMovieHD_live.smil', thumbnails + 'Star_Movies_HD_Asia.jpg', '')
    add_link('', 'HBO HD', 0, 'http://117.103.206.21:88/channel/GetChannelStream?path=VTCHD3/VTCHD3_live.smil', thumbnails + 'HBO-HD.png', '')
    add_link('', 'ITV HD', 0, 'http://hlscache.fptplay.net.vn/live/itvHD_2500.stream/playlist.m3u8', thumbnails + 'ITV-HD.jpg', '')
    add_link('', 'VTC HD1', 0, 'http://117.103.206.21:88/channel/GetChannelStream?path=VTCHD1/VTCHD1_live.smil', thumbnails + 'VTC HD1.jpg', '')
    add_link('', 'VTC HD2', 0, 'http://203.162.235.26/lives/origin03/vtchd2hd.isml/vtchd2hd-2096k.m3u8', thumbnails + 'vtc-hd2.jpg', '')
    add_link('', 'VTC HD3', 0, 'http://117.103.206.21:88/channel/GetChannelStream?path=HBOHD/HBOHD_live.smil', thumbnails + 'VTC-HD3.jpg', '')
    add_link('', 'VTV3 HD', 0, 'http://117.103.206.26:1935/live/_definst_/VTV3HD/VTV3HD_live.smil/playlist.m3u8', thumbnails + 'VTV3 HD.jpg', '')
    add_link('', 'VTV6 HD', 0, 'http://117.103.206.26:1935/live/_definst_/VTV6HD/VTV6HD_live.smil/playlist.m3u8', thumbnails + 'VTV6.jpg', '')
    add_link('', 'FOX SPORTS PLUS HD', 0, 'http://113.160.49.34/lives/origin03/foxhd.isml/foxhd.m3u8', thumbnails + 'FOX SPORTS PLUS HD.jpg', '')
    add_link('', 'HTV7 HD', 0, 'http://frdlzsmb.cdnviet.com/psczntp/_definst_/htv7.720p.stream/playlist.m3u8', thumbnails + 'HTV7 HD.png', '')
    add_link('', 'HTV9 HD', 0, 'http://frdlzsmb.cdnviet.com/psczntp/_definst_/htv9.720p.stream/playlist.m3u8', thumbnails + 'htv9hd.png', '')
    add_link('', 'Thuan Viet HD', 0, 'http://frdlzsmb.cdnviet.com/psczntp/_definst_/thuan_viet.720p.stream/playlist.m3u8', thumbnails + 'thuanviet_hd.png', '')
    add_link('', 'HTVC Phim HD', 0, 'http://frdlzsmb.cdnviet.com/psczntp/_definst_/htvc_movies.720p.stream/playlist.m3u8', thumbnails + 'htvc_hd.png', '')
    #add_link('', 'HBO HD', 0, '', '', '')
    #add_link('', 'HBO HD', 0, '', '', '')
    #add_link('', 'HBO HD', 0, '', '', '')
    #add_link('', 'HBO HD', 0, '', '', '')
    #add_link('', 'HBO HD', 0, '', '', '')
    #add_link('', 'HBO HD', 0, '', '', '')
    #add_link('', 'HBO HD', 0, '', '', '')
    #add_link('', 'HBO HD', 0, '', '', '')
    #add_link('', 'HBO HD', 0, '', '', '')
		

def searchMenu(url, query = '', type='f', page=0):
  add_dir('New Search', url, 2, icon, query, type, 0)
  add_dir('Clear Search', url, 3, icon, query, type, 0)

  searchList=cache.get('searchList').split("\n")
  for item in searchList:
    add_dir(item, url, 2, icon, item, type, 0)

def resolve_url(url):

  if 'GetChannelStream' in url:
    content = make_request(url)
    url = content.replace("\"", "")
  item = xbmcgui.ListItem(path=url)
  xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
  return

def add_link(date, name, duration, href, thumb, desc):
    description = date+'\n\n'+desc
    u=sys.argv[0]+"?url="+urllib.quote_plus(href)+"&mode=4"
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumb)
    liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Duration": duration})
    liz.setProperty('IsPlayable', 'true')
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)



def add_dir(name,url,mode,iconimage,query='',type='f',page=0):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&query="+str(query)+"&type="+str(type)+"&page="+str(page)#+"&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
            params=sys.argv[2]
            cleanedparams=params.replace('?','')
            if (params[len(params)-1]=='/'):
                params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}
            for i in range(len(pairsofparams)):
                splitparams={}
                splitparams=pairsofparams[i].split('=')
                if (len(splitparams))==2:
                    param[splitparams[0]]=splitparams[1]

        return param

xbmcplugin.setContent(int(sys.argv[1]), 'movies')

params=get_params()

url=''
name=None
mode=None
query=None
type='f'
page=0

try:
    type=urllib.unquote_plus(params["type"])
except:
    pass
try:
    page=int(urllib.unquote_plus(params["page"]))
except:
    pass
try:
    query=urllib.unquote_plus(params["query"])
except:
    pass
try:
    url=urllib.unquote_plus(params["url"])
except:
    pass
try:
    name=urllib.unquote_plus(params["name"])
except:
    pass
try:
    mode=int(params["mode"])
except:
    pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "type: "+str(type)
print "page: "+str(page)
print "query: "+str(query)

if mode==None:
	get_categories()
#    fslink_get_video_categories(FSLINK+'/phim-anh.html')

elif mode==1:
    searchMenu(url, '', type, page)

elif mode==2:
   search(url, query, type, page)

elif mode==3:
    clearSearch()

elif mode==4:
    resolve_url(url)
elif mode==11:
   __settings__.openSettings()
   
xbmcplugin.endOfDirectory(int(sys.argv[1]))