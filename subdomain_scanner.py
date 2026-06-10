import socket
from concurrent.futures import ThreadPoolExecutor

def scan_manager(website, type, max_threads):
    try:
        socket.getaddrinfo(website, 0)

    except socket.gaierror: ## [Errno 8] nodename nor servname provided, or not known
        print("Unknown server or website")
        return

    
    if type == "s":
        subdomains = open("subdomains/subdomains-5000.txt", "r").read().split()
            
    elif type == "m":
        subdomains = open("subdomains/subdomains-20000.txt", "r").read().split()

    else:
        subdomains = open("subdomains/subdomains-1100000.txt", "r").read().split()
    

    with ThreadPoolExecutor(max_workers=max_threads) as threader:
            results = threader.map(lambda subdomain: scan(subdomain + "." + website), subdomains)
        
    with open(f"reports/{website}-subdomains", "w") as file:
        i = 0
        for result in results:
            if result:
                file.write(f"{subdomains[i]}.{website} : {result}\n")
            i += 1

def scan(website):
    try:
        ip = socket.getaddrinfo(website, 0)
        if len(ip) < 3:
            return socket.getaddrinfo(website, 0)[1][4][0]
        else:
            return socket.getaddrinfo(website, 0)[3][4][0]
    except:
        pass
