#!/usr/bin/python3

import requests
import json
import os
import socket
import pyfiglet
from colorama import Fore
from dotenv import load_dotenv
from threading import Thread
import argparse
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

def banner():
	initialBanner = pyfiglet.figlet_format('NIX')
	print(initialBanner)
 
	print('')
	print('======== The all-in-one script ツ ========')
	print('')

# banner Grabbing
def bannerGrabbing():
	print('')
	print(Fore.BLUE + f'[INFO] Performing Banner Grabbing in {target} in port {port}:\n')

	try:
		mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mysocket.connect((target,int(port)))
		banner = mysocket.recv(1024)
		print(f'{banner}')
	except:
		print(Fore.RED + '[ERROR] Not able to perform the Banner Grabbing on this port.')
		print('')

	
# port scanning
def portScanning():
	print('')
	print(Fore.BLUE + f'[INFO] Performing a minimum port scanning on {target}:\n')

	targetSc = socket.gethostbyname(target)

	for port in range(1,8088):
		try:
			mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			conn = mysocket.connect_ex((targetSc, port))
			if conn == 0:
				print(Fore.GREEN + f'[FOUND] {port} - OPEN')
			mysocket.close()
		except:
			print(Fore.RED + '[ERROR] Not able to perform a port scanning.')
			print('')

# DIR finder
def dirFinder():
	print(Fore.BLUE + f'[INFO] Performing bruteforce to find directories in {target}:\n')
	res = requests.get(f'https://{target}', verify=False)
	if res.status_code == 200:
		file = open(wordlist, 'r')
		try:
			for line in file:
				line = line.strip('\n')
				fullUrl = target + '/' + line
				response = requests.get(f'https://{fullUrl}', verify=False)
				if response.status_code == 200:
					print(Fore.GREEN + f'[FOUND] https://{fullUrl}')
				elif response.status_code == 403:
					print(Fore.YELLOW + f'[FORBIDDEN] https://{fullUrl}')
				elif response.status_code == 503:
					print(Fore.RED + f'[SERVICE ISSUE] https://{fullUrl}')
		except:
			pass
	else:
		print(Fore.RED + '[ERROR] Problems reaching the target.')

# Subdomains finder
def subdomainFinder():
	print(Fore.BLUE + f'[INFO] Performing bruteforce to find subdomains on {target}:\n')
 
	with open(wordlist,'r') as file:
		name = file.read()
		subdomains = name.splitlines()
    
	for subdomain in subdomains:
		subdomain = subdomain.strip('\n')
		fullSubUrl = f'https://{subdomain}.{target}/'  
  
		try:
			res = requests.get(fullSubUrl, verify=False)
			if res.status_code == 200:
				print(Fore.GREEN + f'[FOUND] {fullSubUrl}')
			elif res.status_code == 403:
				print(Fore.RED + f'[FORBIDDEN] {fullSubUrl}')
			elif res.status_code == 404:
				print(Fore.YELLOW + f'[NOT FOUND] {fullSubUrl}')
        response = requests.get(hunterUrl, verify=True)
	parser.add_argument("-ht", "--hunter", help="Do not forget to put your API key in the .env file. If active, it performs a Hunter.io search and give the results back in a json format.", action='store_true')
	args = parser.parse_args()

	# variables retrieving arguments values
	target = args.target
	port = args.port
	wordlist = args.wordlist
 
	# calling functions
	banner()

	if args.port:
		bannerGrabbing()
		print('')

	if args.port_scan:
		# thread = Thread(target=portScanning)
		# thread.start()
		portScanning()
		print('')

	if args.dir_search:
		dirFinder()
		print('')

	if args.subdomain_finder:
		subdomainFinder()
		print('')

	if args.hunter:
		hunterAPI()
		print('')