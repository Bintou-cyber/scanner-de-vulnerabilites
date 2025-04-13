import socket
import requests


def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception as e:
        print(f"Erreur sur le port {port}: {e}")
        return False

def scan_ports(ip, ports):
    print(f"\n📡 Scan des ports sur {ip}...\n")
    for port in ports:
        if scan_port(ip, port):
            print(f"[+] Port {port} ouvert")
        else:
            print(f"[-] Port {port} fermé")


def scan_http(url):
    print(f"\n Analyse HTTP de : {url}\n")
    try:
        response = requests.get(url, timeout=3)
        print(f"[] Statut HTTP : {response.status_code}\n")
        print(" En-têtes HTTP :")
        for header, value in response.headers.items():
            print(f" - {header}: {value}")

      
        server = response.headers.get("Server")
        if server:
            print(f"\n[!] Serveur détecté : {server}")
            if "Apache" in server or "nginx" in server:
                print("[] Attention : certaines versions de ce serveur peuvent contenir des failles.")
        else:
            print("[!] Aucun serveur détecté dans les en-têtes.")

    except requests.exceptions.RequestException as e:
        print(f"[✗] Erreur HTTP : {e}")


if __name__ == "__main__":
    print("===== Scanner de Vulnérabilités Basique =====")

   
    target_ip = input("\nEntrez l'adresse IP à scanner (ex: 127.0.0.1) : ").strip()
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 8080]
    scan_ports(target_ip, ports_to_scan)

    
    target_url = input("\nEntrez l'URL à analyser (ex: http://example.com) : ").strip()
    scan_http(target_url)








