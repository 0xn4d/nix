# nix - all in one script

Nix was designed to perform a fast recon in a host. The things that it does are listed below:

    1. Banner Grabbing;
    2. Port Scanner;
    3. Subdomain Finder;
    4. Directory Finder; and
    5. Search for possible email addresses using Hunter API (you have to set it as an env. variable)

Besides that, I will implement it to be able to look for some vulnerabilities such as:

    1. Subdomain Takeover;
    2. SQL Injection;
    3. XSS;
    4. IDOR (maybe, still thinking about it :P); and
    5. Git Exposed.

Usage:

1. Cloning the repo:

```git clone https://www.github.com/nix/nix.git```

2. Usage:

```./nix.py host port wordlist```

```./nix.py businesscorp.com.br 21 /usr/share/wordlist/dirb/big.txt```
