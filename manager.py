
import sys
import os


if __name__ == '__main__':
    action = sys.argv[1]
    if action == "route":
        #python3 manage.py route interfaceName 53,989
        #python3 manage.py route interfaceName 53,989,1002,2000,4000
        print("this argument is better run in a service")
        if len(sys.argv) < 4:
            print("Is mandatory netInteface and exlcuded port, separated by comma ex: 53,7300,8989")
            sys.exit(1)

        netInterface = sys.argv[2]
        portsArg = sys.argv[3]
        ports = [int(num) for num in portsArg.split(",")]
        ports = sorted(ports)
        start = 1
        for n in ports:
            if n == 1:
                start+1
                continue

            cmd = "sudo iptables -t nat -I PREROUTING -i "+netInterface+" -p udp --dport "+str(start)+":"+str(n-1)+" -j REDIRECT --to-ports 8989"
            os.system(cmd)
            start = n+1    
        if ports[len(ports)-1] != 65535:
            cmd = "sudo iptables -t nat -I PREROUTING -i "+netInterface+" -p udp --dport "+str(start)+":65535 -j REDIRECT --to-ports 8989"
            os.system(cmd)
        print("IPTABLES SUCESS")
    if action == "userlist":
        #python3 manage.py userlist
        os.system("sudo docker exec -it udpreq python3 manage.py userlist")
           
    if action == "adduser":
        # python3 manage.py adduser name subs hwid
        name_i = sys.argv[2]
        subs_i = sys.argv[3]
        hwd_i = sys.argv[4]
        os.system("sudo docker exec -it udpreq python3 manage.py "+sys.argv[1]+" "+name_i+" "+subs_i+" "+hwd_i+"")
        
    if action == "deleteUser":
        # python3 manager.py deleteUser hwd
        
        os.system("sudo docker exec -it udpreq python3 manage.py "+sys.argv[1]+" "+sys.argv[2]+"")    



