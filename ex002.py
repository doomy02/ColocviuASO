#!/usr/bin/env python3
import subprocess
import re

def discover_hosts(network_cidr="10.11.14.0/24"):
    cmd = ["nmap", "-sn", network_cidr]
    result = subprocess.run(cmd, capture_output=True, text=True)
    ips = []
    for line in result.stdout.splitlines():
        match = re.search(r"for [^(]+\(([^)]+)\)", line)
        if match:
            ips.append(match.group(1))
    return ips

if __name__ == "__main__":
    active_ips = discover_hosts("10.11.14.0/24")
    for ip in active_ips:
        print(ip)
