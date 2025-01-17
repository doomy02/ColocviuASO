#!/usr/bin/env python3
import subprocess

def ping_host(ip):
    try:
        result = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except:
        return False

def scan_network(network_prefix, start=1, end=254):
    active_ips = []
    for host in range(start, end + 1):
        ip = f"{network_prefix}.{host}"
        if ping_host(ip):
            active_ips.append(ip)
    return active_ips

if __name__ == "__main__":
    network_prefix = "10.11.14"
    start_ip = 1
    end_ip = 254
    active_ips = scan_network(network_prefix, start_ip, end_ip)
    if active_ips:
        for ip in active_ips:
            print(ip)
    else:
        print("No active hosts found.")
