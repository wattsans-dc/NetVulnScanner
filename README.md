# NetVulnScanner

## Description
NetVulnScanner est un outil de scan de vulnérabilités conçu pour détecter des failles de sécurité sur des adresses IP aléatoires. En utilisant Nmap, il identifie les vulnérabilités potentielles et les enregistre pour une analyse ultérieure.

## Fonctionnalités
- Génération d'adresses IP aléatoires
- Scan rapide des ports avec Nmap
- Identification des vulnérabilités à l'aide de scripts Nmap
- Exportation des résultats dans un fichier texte

## Prérequis
- Python 3.x
- Nmap
- Scapy

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/wattsans-dc/NetVulnScanner.git
   cd NetVulnScanner
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation
Exécutez le script Python :
```bash
python net_vuln_scanner.py
```

Les résultats seront enregistrés dans `public_ip_vulnerabilities.txt`.

## Avertissement
Ce script doit être utilisé uniquement sur des réseaux et des dispositifs pour lesquels vous avez l'autorisation. L'utilisation non autorisée de cet outil peut être illégale et contraire à l'éthique. 

L'utilisateur assume l'entière responsabilité des actions entreprises à l'aide de cet outil. Le créateur de ce script ne peut être tenu responsable des abus, des dommages ou des conséquences juridiques résultant de son utilisation.

Conformément à l'article 323-1 du Code pénal français, l'accès frauduleux à un système de traitement automatisé de données est puni par la loi.

