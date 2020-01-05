#!/usr/bin/python3
import nmap
import sys

nm = nmap.PortScanner()
network = sys.argv[1]
nmap_args = "-sV -T4 "

print ("\n    KdOMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0lO    ")
print ("    l.:XMMMMMM   Lost Rabbit Labs   MMMW0; :    ")
print ("    '  lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl.  '    ")
print ("    .   'x  github.com/lostrabbitlabs x.   .    ")
print ("    .    .:dKWMMMMMMMMMMMMMMMMMMMMXkc.     .    ")
print ("    .     .';oKMMM  nmap2csv  MMNx:,.      ,    ")
print ("    .      .,.'dXMMMMMMMMMMMMMWk;.'.       c    ")
print ("    ,       .;. ;0WMMMMMMMMMMXl..;.       .k    ")
print ("    d.       ,:. 'OWMMMMMMMMK; .:,        cN    ")
print ("    K,       .:,  ,0MMMMMMMK:  ,:.       ;KM    ")
print ("    WO'       ;;   cNMMMMMWo   ;:       cKMM    ")
print ("    MWKl.     :;   .kMMMMMK,   ';     .dNMMM    ")
print ("    MMMWO;   .:.    ,ooodxc.   .,.   ,kWMMMM    ")
print ("    MMMMMNd. .:.               .;. .lKMMMMMM    ")
print ("    MMMMMMWKl...                ..;OWMMMMMMM    ")
print ("    MMMMMMMMWk'                 .dNMMMMMMMMM    ")
print ("    MMMMMMMMMXd:. .         .  'cOWMMMMMMMMM    ")
print ("    MMMMMMMMWXNW0,.'.      ...oXNKNMMMMMMMMM    ")
print ("    MMMMMMWKl'c303'.'     .'.414d,:OWMMMMMMM    ")
print ("    MMMMMNx'   .,:...      ..;:.   .lXMMMMMM    ")
print ("    MMMMMO.                         .dWMMMMM    ")
print ("    MMMMMK;    .'.           .'.    'OMMMMMM    ")
print ("    MMMMMM0;  .;.             .;.  ,OWMMMMMM    ")
print ("    MMMMMMMKc..:.    .,;'.    .;. :KMMMMMMMM    ")
print ("    MMMMMMMMNxcl:     ',.     ;lcxNMMMMMMMMM    ")
print ("    MMMMMMMMMMWNXxc'........:xXWWMMMMMMMMMMM    ")
print ("    MMMMMMMMMMMMMMMNx:''';oKWMMMMMMMMMMMMMMM    ")
print ("    MMMMMMMMMMMMMMMMMWXXNNMMMMMMMMMMMMMMMMMM    ")

print ("\n    Now running 'nmap2csv' - please wait... \n")
try:
    try:
        filename = network.split("/")
        filename = filename[0]
    except:
        pass
        filename = "error"
    nm.scan(network, arguments=nmap_args)
    all_hostnames = nm.all_hosts()
    all_data = nm.csv()
    for hosts in all_hostnames:
        try:
            service_ports = nm[hosts]['tcp'].keys()
        except:
            pass
            service_ports = []
        try:
            with open("targets.txt", "a") as output_file0:
                for ports in service_ports:
                    ports_str = str(ports)
                    data =  (hosts + ":" + ports_str + "\n")
                    output_file0.write(data)
        except:
            pass
    output_filename = "NMAP-output-" + filename + ".csv"
    with open(output_filename, "a") as output_file:
        output_file.write(all_data)
except:
    pass

print ("Completed 'nmap2csv' for the following hosts: ")
for hosts in all_hostnames:
    print (hosts)

print ("\nOutput files " + output_filename + " and targets.txt created. \n ")

sys.exit()

