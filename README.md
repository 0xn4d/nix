# nix - all in one script

Nix was designed to perform a rapid recon in a host. The things that this script does are listed below:

    1. Banner Grabbing;
    2. Port Scanner;
    3. Subdomain Finder; and
    4. Directory Finder.

Besides that, I will implement the script to be able to perform some great - possible - vulnerabilities such as:

    1. Subdnomain takeover;
    2. SQL Injection;
    3. XSS;
    4. IDOR (maybe, still thinking about it :P); and
    5. Git Exposed.

Usage:

1. Cloning the repo:

```git clone https://www.github.com/nix/nix.git```

2. Usage:

```./nix.py host port wordlist```

e.g.: 

```./nix.py businesscorp.com.br 21 /usr/share/wordlist/dirb/big.txt```