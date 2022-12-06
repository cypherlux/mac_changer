#!/usr/bin/env python

# imports the subprocess module
import subprocess


# module.function() , this functions runs everything and waits for it to finish be moving on
# "" = argument
subprocess.call("ifconfig eth0 down", shell=True) # disables interface
subprocess.call("ifconfig eth0 hw ether 00:11:11:11:11:11", shell=True) # changes MAC address
subprocess.call("ifconfig eth0 up", shell=True) #enables interface
