# replace the offcial website python code with thi
#replace protocol,username,password,,host,port with youself
#This only add proxy  depend on offcial website 

import urllib2,os; protocol='http';username='username';password='pwd';host='192.168.1.112';port='8080'; porxyadd = '%s://%s:%s@%s:%s' %  (protocol,username,password,host,port) ; pf='Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler({protocol : porxyadd}))); open( os.path.join( ipp, pf), 'wb' ).write( urllib2.urlopen( 'http://sublime.wbond.net/' +pf.replace( ' ','%20' )).read()); print( 'Please restart Sublime Text to finish installation')
