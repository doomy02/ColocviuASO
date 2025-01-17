#!/usr/bin/env python3
import nmap

def scan_services(network_range='10.11.14.0/24'):
    nm = nmap.PortScanner()
    nm.scan(hosts=network_range, arguments='-sV')
    results = {}
    for host in nm.all_hosts():
        open_ports = []
        if 'tcp' in nm[host]:
            for port in nm[host]['tcp']:
                if nm[host]['tcp'][port]['state'] == 'open':
                    service_name = nm[host]['tcp'][port]['name']
                    service_product = nm[host]['tcp'][port]['product']
                    service_version = nm[host]['tcp'][port]['version']
                    open_ports.append({
                        'port': port,
                        'service': service_name,
                        'product': service_product,
                        'version': service_version
                    })
        if open_ports:
            results[host] = open_ports
    return results

if __name__ == "__main__":
    vlan_range = "10.11.14.0/24"
    scan_result = scan_services(vlan_range)
    for host, ports in scan_result.items():
        print(f"{host}:")
        for p in ports:
            print(f"  Port: {p['port']}, Name: {p['service']}, Version: {p['version']}, Product: {p['product']}")
