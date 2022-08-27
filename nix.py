#!/usr/bin/python3

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
	print('Not able to perform the Banner Grabbing on this port.')
	print('#' * 63)
	print('')

# Port scanning

def portScanning():
	print('')
	print('#' * 63)
	print(f'Performing a minimum port scanning on {sys.argv[1]}:\n')

	target = socket.gethostbyname(sys.argv[1])

	try:
		for port in range(1,65535):
			mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			conn = mysocket.connect_ex((target, port))
			if conn == 0:
				print(f'[+] {port} - OPEN')
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

print('')
print('#' * 63)
print(f'Performing bruteforce to find directories in {sys.argv[1]}:\n')

def dirFinder(url):	
	try:
		return requests.get('http://' + url)

	except requests.exceptions.ConnectionError:
		pass

targetUrl = sys.argv[1]
file = open('sys.argv[3]', 'r')
for line in file:
	line = line.strip('\n')
	fullUrl = targetUrl + '/' + line
	response = dirFinder(fullUrl)
	if response:
		print('[+] - Found at: ' + fullUrl)
		
# Subdomains finder

print('')
print('')
print('#' * 63)
print(f'Performing bruteforce to find subdomains on {sys.argv[1]}:\n')

def subdomainFinder(domainname, subdomains):
	for subdomain in subdomains:
		subdomain = subdomain.strip('\n')
		fullSubUrl = f'{subdomain}.{sys.argv[1]}'
		try:
			requests.get(fullSubUrl)
			print(f'[+] Found at: {fullSubUrl}')
		except requests.ConnectionError:
			pass

domainname = sys.argv[1]

with open('sys.argv[3]','r') as file:
	name = file.read()
	subdomains = name.splitlines()

subdomainFinder(domainname, subdomains)

# Implement the Hunter API key - get possible email address related to the domain

print('')
print('')
print('#' * 63)
print('Performing a email address search using Hunter API.')

def hunterAPI():
	hunter_api = os.getenv('hunter_api')

	hunterUrl = f'https://api,hunter.io/v2/domain-search?domain='+sys.argv[1]+'&api_key='+hunter_api
	try:
		requests.get(hunterUrl)
	except:
		pass

try:
	print('')
	print('#' * 63)
	hunterAPI()
except:
	print('Not able to perform the Hunter search.')
