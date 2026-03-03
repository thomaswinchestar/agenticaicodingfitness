import socket
import concurrent.futures

def scan_port(ip, port=80, timeout=1.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            return ip
    except:
        return None

ips_to_scan = [f"192.168.68.{i}" for i in range(1, 255)]
open_ips = []

print("Scanning for devices on 192.168.68.* with port 80 open...")
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(scan_port, ips_to_scan)
    for result in results:
        if result:
            open_ips.append(result)

print("IPs with port 80 open:", open_ips)
