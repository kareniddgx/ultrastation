import ctypes
import time
import subprocess
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def sync_time_with_ntp():
    try:
        # Use w32tm to sync time with internet time servers
        subprocess.check_call(['w32tm', '/resync'])
        print("System time successfully synchronized with internet time servers.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to synchronize time. Error: {e}")
        sys.exit(1)

def main():
    if not is_admin():
        print("Admin privileges are required to change system time settings.")
        print("Please run the program as an administrator.")
        sys.exit(1)

    print("Starting UltraStation...")
    while True:
        sync_time_with_ntp()
        print("Waiting for 1 hour before the next synchronization...")
        time.sleep(3600)  # Wait for 1 hour before the next sync

if __name__ == "__main__":
    main()