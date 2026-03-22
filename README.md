# 🛡️ Penetration Testing Toolkit

## 📌 Project Overview
The Penetration Testing Toolkit is a Python-based modular application designed to perform basic security testing on systems and web applications. It includes multiple tools such as a Port Scanner and a Brute Force Login module, demonstrating fundamental penetration testing techniques. This project is developed as part of a Cyber Security Internship Task (Task 3).

## 🎯 Objective
To design and implement a modular penetration testing toolkit that:
- Performs network scanning to identify open ports  
- Simulates brute force attacks on login systems  
- Demonstrates core concepts of ethical hacking and security testing  
- Provides a structured and extensible framework for adding more tools  

## 🛠️ Technologies Used
- Python 3  
- socket – for network communication and port scanning  
- requests – for sending HTTP requests  
- Modular programming concepts in Python  

## ⚙️ Features
- Modular design with separate components for each tool  
- Port Scanner to identify open and closed ports on a target system  
- Brute Force Login tool to test weak credentials  
- Command-line interface for easy interaction  
- Error handling for stable execution  
- Easily extendable architecture for future enhancements  

## 📂 Project Structure
penetration-testing-toolkit/  
├── main.py                     # Main entry point  
└── modules/  
  ├── port_scanner.py          # Port scanning module  
  ├── brute_forcer.py          # Brute force module  
  └── __init__.py              # Package initializer  

## ▶️ How to Run the Project
Step 1: Clone the Repository  
git clone https://github.com/your-username/penetration-testing-toolkit.git  

Step 2: Navigate to the Project Directory  
cd penetration-testing-toolkit  

Step 3: Install Required Dependency  
pip install requests  

Step 4: Run the Toolkit  
python main.py  

Step 5: Select Tool  
Choose from the available options:
1. Port Scanner  
2. Brute Force Login  

## 🧪 Sample Usage

### Port Scanner
Enter target (IP or domain): scanme.nmap.org  
Output:  
[OPEN] Port 80  
[CLOSED] Port 22  

### Brute Force Login
Enter login URL: http://testphp.vulnweb.com/login.php  
Enter username: test  
Output:  
[FAILED] admin  
[FAILED] 1234  
[FAILED] password  
[INFO] Brute force completed. Password not found.  

## 🔍 How It Works
The toolkit provides a menu-driven interface where users can select different security testing modules. The port scanner attempts to establish socket connections to identify open ports, while the brute force module sends repeated login requests using different password combinations to test authentication strength.

## 📌 Use Cases
- Learning penetration testing concepts  
- Practicing ethical hacking techniques  
- Identifying weak network configurations  
- Testing login security mechanisms in controlled environments  

## ⚠️ Disclaimer
This tool is developed strictly for educational and ethical purposes only.  
- Do NOT use this toolkit on systems without proper authorization  
- Only test on your own systems or intentionally vulnerable platforms  
Unauthorized use may lead to legal consequences  

## 🚀 Future Enhancements
- Multi-threaded port scanning for faster performance  
- Advanced brute force techniques with wordlists  
- Directory and subdomain scanning modules  
- GUI-based interface  
- Automated reporting system  

## 👨‍💻 Author
Neeraj Bhujbal  
  

## 📎 Submission Note
This project is submitted as part of the Cyber Security Internship Task (Task 3), following the provided instructions and guidelines.
