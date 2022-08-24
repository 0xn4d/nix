#!/usr/bin/python3

import argparse
import requests
import sys
import os
import socket

print('')
print('#########################################')
print('======== NIX - All in one script ========')
print('#########################################')
print('')
print('')

parser = argparse.ArgumentParser('./nix.py', description='You can use NIX to get your recon faster.')
parser.add_argument('-bg', help='Activates the Banner Grabbing.')
parser.add_argument('-sb', help='Activates the Subdomain Finder.')
parser.add_argument('-ps', help='Activates the Port Scanning.')
parser.add_argument('-df', help='Activates the DIR Finder')
parser.add_argument('-w', help='Select the wordlist to use in the tests.')

# Banner Grabbing

def bannerGrabbing():
	print('')
	print('######################################################################')
	print(f'Performing Banner Grabbing in {sys.argv[1]} in port {sys.argv[2]}:\n')

	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysocket.connect((sys.argv[1],int(sys.argv[2])))
	banner = mysocket.recv(1024)

	print(f'{banner}')
	print('######################################################################')
	print('')

try:
	bannerGrabbing()
	print('')
except:
	print('Not able to do the Banner Grabbing in this port.')
	print('######################################################################')
	print('')

# Subdomains finder

with open('endpoints.txt') as f: s = f.read()

def subdomainFinder():
	print('##############################################################')
	print(f'Performing bruteforce to find subdomains in {sys.argv[1]}:\n')

	for endpoint in s:
		request = requests.get(f'{sys.argv[1]}/{endpoint}')
		if request == 0:
			print(f'{endpoint} - 200')

try:
	subdomainFinder()
	print('##############################################################')
	print('')
except:
	print('Not able to enumerate the subdomains in this host.')
	print('##############################################################')
	print('')

# Port scanning

#print(f'Executing a minimum port scanning in {}:\n',sys.argv[1])


# DIR finder

#print(f'Executing bruteforce to find directories in {}:\n',sys.argv[1])


