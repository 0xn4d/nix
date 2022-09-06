# nix - a good folder to use in certifications exams

### nix.py

Nix was designed to perform a fast recon in a host. The things that it does are listed below:

    1. Banner Grabbing;
    2. Port Scanner;
    3. Subdomain Finder;
    4. Directory Finder; and
    5. Search for possible email addresses using Hunter API. For this, you'll have to set it as an env. variable in a .env file, like:
    
   ```HUNTER_API = your_generated_api_token_here```

Besides that, I will implement it to be able to look for some vulnerabilities such as:

    1. Subdomain Takeover;
    2. SQL Injection;
    3. XSS;
    4. IDOR (maybe, still thinking about it :P); and
    5. Git Exposed.

Usage:

1. Cloning the repo:

```git clone https://www.github.com/nix/nix.git```

2. Example:

```./nix.py host port wordlist```

```./nix.py target.com 21 endpoints.txt```

#

### metasearch.sh

Basically, metasearch.sh is able to perform a specific query on Google to look for different types of files within a host.

Usage:

```./metasearch host filetype```

```./metasearch target.com pdf```
