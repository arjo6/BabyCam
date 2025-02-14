# BabyCam

BabyCam is a network scanning tool designed to detect and identify IP cameras on a local network, even if ONVIF is not enabled.

## Features
- Detects cameras with open ports (HTTP, HTTPS, RTSP)
- Identifies device type based on HTTP response and RTSP handshake
- Scans open ports (80, 443, 554, 8080)
- Provides detailed scan results

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/arjo6/BabyCam.git
   cd BabyCam
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the tool:
   ```sh
   python3 BabyCam.py
   ```

## Requirements
- Python 3.x
- `nmap`, `requests`
- Root privileges for scanning

## License
This project is licensed under the MIT License.
    
