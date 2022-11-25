import re
print("Inserisci IP: ", end="")
ipAddress = input() #192.168.0.
print("Inserisci Subnet: ", end="")
subnet =  input() #255.255.255.


def main():

    netId = int(ipAddress.split(".")[0])

    if netId < 128:
        class_a()
    elif netId < 192:
        class_b()
    elif netId < 224:
        class_c()
    else:
        print("controlla meglio la stronzata che hai scritto, il net id per le reti di classe c finisce a 223")


def class_a():

    secondo = bin(int(subnet.split(".")[1]))
    secondo = re.sub("0b","",secondo)
    #print(secondo)
    calc = 1
    for i in range(len(str(secondo))):
        if secondo[i] == "1":
            calc = calc * 2
    print("Numero di sottoreti: "+ str(calc))    
    nDiHostPerRete= int(256/calc)
    print("Numero di host per sottoreterete: " + str(nDiHostPerRete-2) )

    ip1= int(ipAddress.split(".")[0])
    ip2 = int(ipAddress.split(".")[1])
    ip3 = int(ipAddress.split(".")[2])
    ip4 = int(ipAddress.split(".")[3])

    increment = 0

    print()
    for i in range(calc):
        i = i+1
        print("Sottorete numero " + str(i) + ":")
        print("     Net ID: " + str(ip1) + "." +str(increment) + "." + str(0)+"." + str(0))
        print("     Range: " + str(ip1) + "." +str(increment) + "." + str(0)+"." + str(1) + " ----> " + str(ip1) + "." + str(increment+nDiHostPerRete-1) + "." + str(255)+"." + str(254))
        print("     Broadcast: " + str(ip1) + "." + str(increment+nDiHostPerRete-1)+ "." + str(255)+"." + str(255))
        print()
        increment = increment + nDiHostPerRete
        

    

def class_b():
    terzo = bin(int(subnet.split(".")[2]))
    terzo = re.sub("0b","",terzo)

    calc = 1
    for i in range(len(str(terzo))):
        if terzo[i] == "1":
            calc = calc * 2
    print("Numero di sottoreti: "+ str(calc))    
    nDiHostPerRete= int(256/calc)
    print("Numero di host per rete: " + str(nDiHostPerRete-2) )

    ip1= int(ipAddress.split(".")[0])
    ip2 = int(ipAddress.split(".")[1])
    ip3 = int(ipAddress.split(".")[2])
    ip4 = int(ipAddress.split(".")[3])

    increment = 0

    print()
    for i in range(calc):
        i = i+1
        print("Sottorete numero " + str(i) + ":")
        print("     Net ID: " + str(ip1) + "." +str(ip2) + "." + str(increment)+"." + str(0))
        print("     Range: " + str(ip1) + "." +str(ip2) + "." + str(increment)+"." + str(1) + " ----> " + str(ip1) + "." + str(ip2) + "." + str(increment+nDiHostPerRete-1)+"." + str(254))
        print("     Broadcast: " + str(ip1) + "." + str(ip2)+ "." + str(increment+nDiHostPerRete-1)+"." + str(255))
        print()
        increment = increment + nDiHostPerRete


def class_c():
    quarto = bin(int(subnet.split(".")[3]))
    quarto = re.sub("0b","",quarto)

    
    calc = 1
    for i in range(len(str(quarto))):
        if quarto[i] == "1":
            calc = calc * 2
    print("Numero di sottoreti: "+ str(calc))    
    nDiHostPerRete= int(256/calc)
    print("Numero di host per rete: " + str(nDiHostPerRete-2) )

    ip1= int(ipAddress.split(".")[0])
    ip2 = int(ipAddress.split(".")[1])
    ip3 = int(ipAddress.split(".")[2])
    ip4 = int(ipAddress.split(".")[3])

    increment = 0

    print()
    for i in range(calc):
        i = i+1
        print("Sottorete numero " + str(i) + ":")
        print("     Net ID: " + str(ip1) + "." +str(ip2) + "." + str(ip3)+"." + str(increment))
        print("     Range: " + str(ip1) + "." +str(ip2) + "." + str(ip3)+"." + str(increment+1) + " ----> " + str(ip1) + "." + str(ip2) + "." + str(ip3)+"." + str(increment+nDiHostPerRete-2))
        print("     Broadcast: " + str(ip1) + "." + str(ip2)+ "." + str(ip3)+"." + str(increment+nDiHostPerRete-1))
        print()
        increment = increment + nDiHostPerRete

main()