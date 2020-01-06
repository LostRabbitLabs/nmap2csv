

# nmap2csv.py
Python3 script to generate a CSV output file from an Nmap port scan.

     Language: Python 3
     Libraries: sys, python-nmap
     Purpose: Penetration Testing / Network Scanner


# Install
Follow the steps below to install 'nmap2csv'.

     git clone https://github.com/lostrabbitlabs/nmap2csv
     cd nmap2csv
     chmod 655 nmap2csv.py
     pip3 install python-nmap


# Usage
Simply provide a network or host (with CIDR notation) and run the script. NOTE: Modify the 'nmap2csv.py' file as needed to change 'nmap_args' (default below):
  
  nmap_args = "-sV -T4 "

     ./nmap2csv.py 10.0.0.0/24


# Output
When completed will create two (2) output files:

     NMAP-output-network.csv (all Nmap results)
     targets.txt (hostname:port)

