# nix - a good folder to use in certifications exams

### nix.py

Nix was designed to perform a fast recon in a host. The things that it does are listed below:

    1. Banner Grabbing;
    2. Port Scanner;
    3. Directory Finder; and
    4. Search for possible email addresses using Hunter API. Set the API token as an env. variable in a .env file, like:
    
   ```HUNTER_API = your_generated_api_token_here```

Usage:

1. Cloning the repo:

```git clone https://www.github.com/nix/nix.git```

2. Example:

Banner Grabbing:

![image](https://github.com/0xn4d/nix/assets/85083396/8fc3d26a-434e-4221-9b40-95384190d6d7)

Hunter's Hunt (don't forget to create your own .env file and set the "HUNTER_API" variable there:

![image](https://github.com/0xn4d/nix/assets/85083396/8e39df4a-16fe-4b2b-9c5d-d0f98699b75d)

#

### metasearch.sh

Basically, metasearch.sh is able to perform a specific query on Google to look for different types of files within a host.

Usage:

```./metasearch host filetype```

```./metasearch target.com pdf```

#

### subtakeover.sh

subtakeover.sh is able to perform subdomain bruteforce and bring us possible subdomains to test a Subdomain Takeover.

Usage:

```./subtakeover.sh host wordlist```

```./subtakeover.sh target.com endpoints.txt```
