import os

resultoff = []
resulton = []

ips = open("iplist.txt", "r")
for hostname in ips:
    response = os.system("ping -n 1 " + hostname)
    if response == 0:
        print (hostname, 'is up!')
        resulton.append("Up "+hostname)
    else:
        print (hostname, 'is down!')
        resultoff.append("Down "+hostname)

txtoff = open("resultoff.txt","w")
txtoff.write("OFFLINE HOST LIST" + "\n")
txtoff.writelines(resultoff)


txton = open("resulton.txt","w")
txton.write("ONLINE HOST LIST" + "\n")
txton.writelines(resulton)
