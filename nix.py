#!/usr/bin/python3

import argparse
import requests
import sys
import os
import socket
import pyfiglet

def banner():
	initialBanner = pyfiglet.figlet_format('NIX')
	print(initialBanner)

try:
	banner()
except:
	print('There is a problem getting the banner ready :P')

print('')
print('======== The all-in-one script ツ========')
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
	print('#' * 63)
	print(f'Performing Banner Grabbing in {sys.argv[1]} in port {sys.argv[2]}:\n')

	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysocket.connect((sys.argv[1],int(sys.argv[2])))
	banner = mysocket.recv(1024)

	print(f'{banner}')
	print('#' * 63)
	print('')

try:
	bannerGrabbing()
	print('')
except:
	print('Not able to do the Banner Grabbing in this port.')
	print('#' * 63)
	print('')

# Subdomains finder

with open('../endpoints.txt') as f: s = f.read()

def subdomainFinder():
	print('#' * 63)
	print(f'Performing bruteforce to find subdomains in {sys.argv[1]}:\n')

	for endpoint in s:
		request = requests.get(f'{sys.argv[1]}/{endpoint}')
		if request == 0:
			print(f'{endpoint} - 200')

try:
	subdomainFinder()
	print('#' * 63)
	print('')
except:
	print('Not able to enumerate the subdomains in this host.')
	print('#' * 63)
	print('')

# Port scanning

def portScanning():
	print('')
	print('#' * 63)
	print(f'Executing a minimum port scanning in {sys.argv[1]}:\n')

	target = socket.gethostbyname(sys.argv[1])

	try:
		for port in range(1,65535):
			mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			conn = mysocket.connect_ex((target, port))
			if conn == 0:
				print(f'{port} - OPEN')
			mysocket.close()
	except socket.gaierror:
		print('\nSomething went wrong with the hostname.')
		sys.exit()
	except socket.error:
		print('\nThe server is not responding.')
		sys.exit()
try:
	portScanning()
	print('#' * 63)
	print('')
except:
	print('Not able to perform a port scanning.')
	print('#' * 63)
	print('')

# DIR finder

#print(f'Executing bruteforce to find directories in {}:\n',sys.argv[1])


