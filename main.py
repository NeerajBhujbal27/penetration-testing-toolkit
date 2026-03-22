from modules.port_scanner import scan_ports
from modules.brute_forcer import brute_force_login


def main():
    print("=== Penetration Testing Toolkit ===\n")
    print("1. Port Scanner")
    print("2. Brute Force Login\n")

    choice = input("Select an option: ")

    if choice == "1":
        target = input("Enter target (IP or domain): ")
        ports = [21, 22, 23, 80, 443]

        scan_ports(target, ports)

    elif choice == "2":
        url = input("Enter login URL: ")
        username = input("Enter username: ")

        passwords = ["admin", "1234", "password", "admin123"]

        brute_force_login(url, username, passwords)

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()