import requests
import concurrent.futures

ips = ['192.168.68.1', '192.168.68.54', '192.168.68.55', '192.168.68.56', '192.168.68.57', '192.168.68.58', '192.168.68.59', '192.168.68.60', '192.168.68.61', '192.168.68.63', '192.168.68.64', '192.168.68.65', '192.168.68.66', '192.168.68.69', '192.168.68.70', '192.168.68.71', '192.168.68.72', '192.168.68.73', '192.168.68.74', '192.168.68.75', '192.168.68.76', '192.168.68.77', '192.168.68.78', '192.168.68.79', '192.168.68.80', '192.168.68.81', '192.168.68.82', '192.168.68.83', '192.168.68.84', '192.168.68.85', '192.168.68.86', '192.168.68.87', '192.168.68.88', '192.168.68.89', '192.168.68.90', '192.168.68.91', '192.168.68.92', '192.168.68.93', '192.168.68.94', '192.168.68.95', '192.168.68.96', '192.168.68.97', '192.168.68.98', '192.168.68.99', '192.168.68.100', '192.168.68.101', '192.168.68.103', '192.168.68.104', '192.168.68.105', '192.168.68.106', '192.168.68.107', '192.168.68.108', '192.168.68.109', '192.168.68.110', '192.168.68.111', '192.168.68.112', '192.168.68.113', '192.168.68.114', '192.168.68.115', '192.168.68.116', '192.168.68.117', '192.168.68.119', '192.168.68.123', '192.168.68.135', '192.168.68.240']

def check_app(ip):
    try:
        r = requests.get(f"http://{ip}/", timeout=1.0)
        return ip, "Success", dict(r.headers)
    except Exception as e:
        return ip, "Error", str(e)

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(check_app, ips)
    for ip, status, headers in results:
        if status == "Success":
            if "Server" in headers:
                print(f"{ip}: Server = {headers['Server']}")
            else:
                print(f"{ip}: No Server header, headers = {headers}")
        else:
            if "ConnectionResetError" in headers or "ReadTimeout" in headers or "ConnectTimeout" in headers:
                pass
            elif "RemoteDisconnected" in headers:
                print(f"{ip}: RemoteDisconnected (possible raw socket TCP service like Tapo)")
            else:
                pass
