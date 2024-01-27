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
					print(Fore.GREEN + f'[FOUND] {fullUrl}')
				elif response.status_code == 403:
					print(Fore.YELLOW + f'[FORBIDDEN] {fullUrl}')
				elif response.status_code == 503:
					print(Fore.RED + f'[SERVICE ISSUE] {fullUrl}')
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
		except requests.exceptions.ConnectionError:
			print(Fore.RED + "Connection error.")
			#print(Fore.RED + '[ERROR] Something went wrong while reaching the target.')
			pass

# Implement the Hunter API key - get possible email addresses related to the domain
def hunterAPI():
	print(Fore.BLUE + '[INFO] Performing a email address search using Hunter API.')
    
	HUNTER_API = os.getenv('HUNTER_API')

	hunterUrl = f'https://api.hunter.io/v2/domain-search?domain={target}&api_key={HUNTER_API}'
	
	try:
		response = requests.get(hunterUrl, verify=False)
		resjson = response.json()
		print(json.dumps(resjson, indent=4))
	except:
		print('')
		print(Fore.RED + '[ERROR] Not able to perform the Hunter search.')
  
# uso da função mainf
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Recon Automation.")
	parser.add_argument("-t", "--target", help="Your target.")
	parser.add_argument("-p", "--port", help="Port to perform the banner grabbing.")
	parser.add_argument("-w", "--wordlist", help="Wordlist to use.")
	parser.add_argument("-ps", "--port-scan", help="If active, it performs a port scan in range 1,65535.", action='store_true')
	parser.add_argument("-ds", "--dir-search", help="If active, it performs a directory search using the given wordlist.", action='store_true')
	parser.add_argument("-sf", "--subdomain-finder", help="If active, it performs a subdomain search.", action='store_true')
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