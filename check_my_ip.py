import sys
import subprocess
import re
import pynma

apikey = "24ea4416232fe9adeb6ada6b0ca2b072e66112bebdb6a94c"
filename = "/tmp/ip_address.txt"

cmd = '''curl checkip.dyndns.org'''
args = cmd.split()
process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

m = re.search(r"Current\sIP\sAddress:\s(\d+\.\d+\.\d+\.\d+)", stdout) 
print "From command" + m.group(1)

try:
  f = open(filename,'r')
  file_ip = f.readline().strip()
  f.close()

  print "up to here"

except:
  print "Going through except, no initial file found"

try:  
  #print "From command" + m.group(1)
  #print "From file:" + file_ip
  if m.group(1) == file_ip:
    print "IP matches file. Doing nothing"
    sys.exit(0)  
except:  
  print "except second"
  
if m:
  ##TODO: Do stuff here:
  p = pynma.PyNMA(apikey)
  p.push("Kodi-Taiwan", "IP-Address", m.group(1))
  f = open(filename,'w')
  f.write(m.group(1))
  f.close()




