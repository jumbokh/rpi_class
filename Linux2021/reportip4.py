#reportip4.py : send mail by Gmail with TLS
import smtplib
from urllib import request
import re
import socket
import time

class Getmyip:
    def getip(self):
        try:
            myip=self.visit("https://myip.com.tw")
        except:
            try:
                myip=self.visit("http://cmp.nkuht.edu.tw/info/ip.asp")
            except:
                try:
                    myip=self.visit("http://dir.twseo.org/ip-check.php")
                except:
                    print("Fail to get the Network ip.")
                    print("Get the LAN ip.")
                    myip=get_lan_ip()
        return myip
    def visit(self, url):
        opener=request.urlopen(url,timeout=20)
        #print(opener.headers.get_content_charset())
        if url==opener.geturl():
            str=opener.read().decode(opener.headers.get_content_charset())
            print("IP information from", url)
        return re.search('\d+\.\d+\.\d+\.\d+',str).group(0)

def get_network_ip():
    getmyip=Getmyip()
    localip=getmyip.getip()
    return localip

def get_lan_ip():
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1",80))
    ipaddr=s.getsockname()[0]
    s.close()
    return ipaddr
 
#check_network()
ipaddr=get_network_ip()
lanip=get_lan_ip()
emailip=str(ipaddr)+" "+str(lanip)
print("current ip: {}".format(emailip))

smtp=smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("jumbokh@gmail.com", "get-from -google")
from_addr="jumbokh@gmail.com"
to_addr=["1101404110@nkust.edu.tw"]
msg="Subject:My Raspberry IP\n\
From:Raspberry Pi 4\n\
To:My IP\n\
Cc:jumbokh@gmail.com\n\
{}".format(emailip)
status=smtp.sendmail(from_addr, to_addr, msg)
if status=={}:
    print("郵件傳送成功!")
else:
    print("郵件傳送失敗!")
smtp.quit()
