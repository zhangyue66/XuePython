from urllib.request import urlopen


def read_text():
  log = open(r"C:\Users\yz632h\Desktop\Yue-old-computer\log1314.log")
  contents_of_file = log.read()
  print(contents_of_file)
  log.close()
  check(log)

def check(text):
  site = "http://www.wdylike.appspot.com/?q="
  #print (site)
  connection = urlopen(site)
  print ( "hello Yue to debug")
  output = connection.read()
  print(output)
  connection.close()

read_text()

print("We are going to check the curse word in log file now! please wait!")




