from flask import Flask, render_template
import nmap

app = Flask(__name__)

@app.route('/')
def scan_network():
    scanner = nmap.PortScanner()
    ip_range = "192.168.1.0/24"  # Apne network range ke hisab se change karo
    scanner.scan(hosts=ip_range, arguments='-sn')
    
    hosts = []
    for host in scanner.all_hosts():
        mac = scanner[host]['addresses'].get('mac', 'N/A')
        hosts.append({
            'ip': host,
            'mac': mac,
            'status': scanner[host].state()
        })
    print("Scanned Hosts:", hosts)  # ✅ ADD THIS LINE
    
    return render_template("index.html", hosts=hosts)

if __name__ == '__main__':
    app.run(debug=True)
