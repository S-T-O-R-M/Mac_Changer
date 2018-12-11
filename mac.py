#/usr/bin/env  python3

import subprocess
import optparse
import re

def change_mac(interface,new_mac):

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Changing Mac Adress for " + str(interface) + " to " + str(new_mac))


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC of ")
    parser.add_option("-m", "--mac", dest="newmac", help="New Mac for the interface ")
    (options, arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[+] Please specify interface \n")
    elif not options.newmac:
        parser.error("[+] Please specify new MAC address \n")
    return options


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("Could not read MAC address")



options = get_arguments()
current_mac = get_current_mac(options.interface)
print ("Current MAC Address = "+str(get_current_mac(options.interface)))
change_mac (options.interface,options.newmac)

current_mac = get_current_mac(options.interface)

if current_mac == options.newmac:
    print("[+] MAC address was succesfully changed to "+current_mac)
else:
    print("[+] MAC address did not get changed")
