import nmap
import requests
from requests.exceptions import RequestException
import socket

def scan_network(network_range):
    """Scan the network for devices with open camera-related ports."""
    try:
        nm = nmap.PortScanner()
        print(f"🔍 Scanning network: {network_range}")
        nm.scan(hosts=network_range, arguments='-p 80,443,554,8080 --open')

        cameras = []
        for host in nm.all_hosts():
            print(f"📡 Found device: {host}")
            device_info = {
                "ip": host,
                "ports": [p for p in nm[host].all_protocols() for p in nm[host][p].keys()],
                "device_type": identify_camera_type(host)
            }
            cameras.append(device_info)

        return cameras
    except Exception as e:
        print(f"❌ Error scanning network: {e}")
        return []

def identify_camera_type(ip):
    """Identify if the device is a camera based on HTTP response or RTSP."""
    try:
        print(f"🌐 Checking HTTP response for {ip}...")
        response = requests.get(f"http://{ip}", timeout=3)
        if "camera" in response.text.lower() or "webcam" in response.text.lower():
            return "Likely Camera (Web Interface Found)"
    except RequestException:
        print(f"⚠ HTTP request failed for {ip}")

    try:
        print(f"📡 Checking RTSP for {ip}...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, 554))  # RTSP Port
        s.send(b"OPTIONS * RTSP/1.0

")  # Corrected line
        data = s.recv(1024)
        s.close()
        if b"RTSP" in data:
            return "IP Camera (RTSP Detected)"
    except:
        print(f"⚠ RTSP request failed for {ip}")

    return "Unknown Device"

network = "192.168.1.0/24"
found_devices = scan_network(network)

print("\n📸 Detected Devices:\n")
for device in found_devices:
    print(f"IP: {device['ip']}, Device Type: {device['device_type']}, Open Ports: {device['ports']}")
    