# NetVulnScanner

## Description
NetVulnScanner is a vulnerability scanning tool designed to detect security flaws on random IP addresses. By utilizing Nmap, it identifies potential vulnerabilities and logs them for later analysis.

## Features
- Generation of random IP addresses
- Fast port scanning with Nmap
- Identification of vulnerabilities using Nmap scripts
- Exporting results to a text file

## Prerequisites
- Python 3.x
- Nmap
- Scapy

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/wattsans-dc/NetVulnScanner.git
   cd NetVulnScanner
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the Python script:
```bash
python net_vuln_scanner.py
```

The results will be logged in `public_ip_vulnerabilities.txt`.

## Warning
This script should only be used on networks and devices for which you have permission. Unauthorized use of this tool may be illegal and unethical.

The user assumes full responsibility for any actions taken using this tool. The creator of this script cannot be held responsible for any abuse, damage, or legal consequences resulting from its use.

In accordance with Article 323-1 of the French Penal Code, unauthorized access to a computerized data processing system is punishable by law.
