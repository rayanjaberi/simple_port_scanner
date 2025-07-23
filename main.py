import socket

def ipRangeScanner (ipAdd):
    protocols = (80 , 8080 , 443 , 53 , 23 , 22 )
    s = socket.socket();
    for i in protocols:
        s.connect_ex((ipAdd , i))
        s.close()

userIp = input("enter ip address :")
print(ipRangeScanner(userIp))