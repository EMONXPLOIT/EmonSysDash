#!/usr/bin/env python3
# OWNER: EMON KHAN

import sys
import platform
import argparse
import requests
import os

# টার্মিনাল কালার কোড
R = '\033[31m'  # Red
G = '\033[32m'  # Green
C = '\033[36m'  # Cyan
W = '\033[0m'   # White
Y = '\033[33m'  # Yellow

VERSION = '1.0.0'
AUTHOR = 'Emon Khan'

def clear_screen():
    # রান করার সাথে সাথে টার্মিনাল স্ক্রিন পরিষ্কার করার জন্য
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def banner():
    art = r"""
 _____                     ____             _     
| ____| _ __ ___    ___   |  _ \           | |    
|  _|  | '_ ` _ \  / _ \  | | | | __ _  ___| |__  
| |___ | | | | | || (_) | | | |/ _` |/ __| '_ \ 
|_____||_| |_| |_| \___/  |/ /| (_| | (__| | | |
                          \____/  \__,_|\___|_| |_|"""
    
    print(f"{G}{art}{W}\n")
    print(f"{G}[>] {C}Tool Name    : {Y}EmonSysDash{W}")
    print(f"{G}[>] {C}Created By   : {W}{AUTHOR}")
    print(f"{G}[>] {C}Version      : {W}{VERSION}")
    print(f"{G}[+] {C}Status       : {G}Ready to Scan{W}\n")
    print("-" * 55)

def get_system_info():
    print(f"\n{Y}[!] Collecting Local System Specs...{W}\n")
    info = {
        "OS Type": platform.system(),
        "OS Release": platform.release(),
        "Architecture": platform.machine(),
        "Processor": platform.processor() or "ARM Processor",
        "Python Version": platform.python_version()
    }
    
    for key, value in info.items():
        print(f"{G}[+] {C}{key:<16} : {W}{value}")

def get_public_ip_info():
    print(f"\n{Y}[!] Fetching Public Network Information...{W}\n")
    try:
        # ইন্টারনেট কানেকশন চেক করার জন্য রিকোয়েস্ট
        response = requests.get('https://ipwho.app/json/', timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('success', True):
                print(f"{G}[+] {C}Public IP        : {W}{data.get('ip')}")
                print(f"{G}[+] {C}City             : {W}{data.get('city')}")
                print(f"{G}[+] {C}Region           : {W}{data.get('region')}")
                print(f"{G}[+] {C}Country          : {W}{data.get('country')}")
                print(f"{G}[+] {C}ISP Provider     : {W}{data.get('isp')}")
            else:
                print(f"{R}[-] API Error: Unable to resolve IP data.{W}")
        else:
            print(f"{R}[-] Data fetch failed. Code: {response.status_code}{W}")
    except requests.exceptions.ConnectionError:
        print(f"{R}[-] Error: No Internet Connection! Please turn on Mobile Data or WiFi.{W}")
    except Exception as e:
        print(f"{R}[-] Network Timeout or Error: {str(e)}{W}")

def main():
    parser = argparse.ArgumentParser(description="EmonSysDash - A professional system and network diagnostics tool.")
    parser.add_argument('-s', '--system', action='store_true', help='Show only local system info')
    parser.add_argument('-n', '--network', action='store_true', help='Show only network info')
    
    args = parser.parse_args()
    
    # স্ক্রিন ক্লিয়ার করে নতুন পেজে ব্যানার দেখাবে
    clear_screen()
    banner()
    
    if not args.system and not args.network:
        get_system_info()
        get_public_ip_info()
    else:
        if args.system:
            get_system_info()
        if args.network:
            get_public_ip_info()
            
    print("\n" + "-" * 55)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[-] Process stopped by user (Ctrl+C).{W}")
        sys.exit()