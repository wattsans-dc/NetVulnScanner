import scapy.all as sp
import nmap
import random
import concurrent.futures

def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def scan_ip(ip):
    print(f"Scanning {ip}")
    nm = nmap.PortScanner()
    
    try:
        nm.scan(ip, arguments="-F --script vuln")
    except Exception as e:
        print(f"Erreur lors du scan de {ip}: {e}")
        return []
    
    vulnerabilities = []
    
    for host in nm.all_hosts():
        if host == ip:
            if 'vuln' in nm[host].get('scripts', {}):
                for vuln in nm[host]['scripts']['vuln']:
                    vuln_id = vuln.get('id', 'N/A')
                    vuln_name = vuln.get('name', 'N/A')
                    vuln_description = vuln.get('description', 'N/A')
                    vuln_cvss = vuln.get('cvss', 'N/A')
                    vulnerabilities.append((ip, vuln_id, vuln_name, vuln_description, vuln_cvss))
            else:
                print(f"Aucune vulnérabilité trouvée pour {ip}")
    
    return vulnerabilities

public_ips = [generate_random_ip() for _ in range(9000)]

vulnerabilities = []
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(scan_ip, public_ips)
    
    for result in results:
        vulnerabilities.extend(result)

if vulnerabilities:
    with open("public_ip_vulnerabilities.txt", "w") as f:
        f.write("IP Address\tCVE ID\tVulnerability\tDescription\tCVSS Score\n")
        for vuln in vulnerabilities:
            f.write(f"{vuln[0]}\t{vuln[1]}\t{vuln[2]}\t{vuln[3]}\t{vuln[4]}\n")
else:
    print("Aucune vulnérabilité détectée pour les IP scannées.")

print("Scan terminé.")

