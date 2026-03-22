import socket

def scan_ports(target, ports):
    print(f"\n[+] Scanning target: {target}\n")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
            else:
                print(f"[CLOSED] Port {port}")

            sock.close()

        except Exception as e:
            print(f"[ERROR] {e}")