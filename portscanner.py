import socket # this is the module to enable me use the socket functions
import time # this is the module to enable me use the time functions

def scan_localhost(start_port, end_port):
    target_ip = "127.0.0.1" # this is the IP address of the localhost
    print(f"Starting scan on host {target_ip}")
    print(f"Scanning ports {start_port} to {end_port}...\n")


    start_time = time.time() # this is the start time of the scan
    
    open_ports = [] # this is the list to store the open ports

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # this is the socket object to create a TCP connection
            s.settimeout(0.5) # this is the timeout for the socket connection
            
            result = s.connect_ex((target_ip, port)) # this is the function to check if the port is open or closed

            if result == 0:
                print(f"Port {port} is open") # this is the message to print if the port is open
                open_ports.append(port) # this is the function to add the open port to the list

    end_time = time.time() # this is the end time of the scan

    print(f"\nScan completed in {end_time} - {start_time:.2f} seconds") # this is the message to print the time taken for the scan
    print(f"Open ports: {open_ports}")
if __name__ == "__main__":

    scan_localhost(start_port=1, end_port=1024) # this is the function to call the scan_localhost function with the start and end port