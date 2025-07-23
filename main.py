import socket


def getIp(ip_add, port_nu):
    s = socket.socket()
    res = s.connect_ex((ip_add, port_nu))
    s.close()
    return res


userInput = input("enter your ip address :")
userInput2 = int(input("enter your port number :"))
result = getIp(userInput, int(userInput2))

if result ==0:
    print (f"{userInput2} is open on {userInput}")

else:
    print (f"{userInput2} is close on {userInput}")
