import urllib.request

#jaeger_url = "http://107.250.139.219/search?end=1613027700000000&limit=20&lookback=custom&maxDuration&minDuration&service=npcf-smpolicycontrol&start=1612983600000000"
jaeger_url = "http://107.250.139.219/api/traces?end=1515912680000000&limit=20&lookback=custom&maxDuration&minDuration&service=npcf-policyauthorization&start=1515912560000000"
#jaeger_url = "http://107.250.139.219"
#jaeger_url = "http://www.att.com"
proxy = urllib.request.ProxyHandler({"http":"http://autoproxy.sbc.com/autoproxy.cgi"})
jaeger_header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

req = urllib.request.Request(url=jaeger_url,headers=jaeger_header)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

# opener = urllib.request.build_opener(proxy)
# yz = opener.open(jaeger_url)
# print(yz.read())