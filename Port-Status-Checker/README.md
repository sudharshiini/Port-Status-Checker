# Port Status Checker

## VirtualWorks Cyber Security Internship – Task 2

### Project Description
A Python-based Port Status Checker that determines whether a specified TCP port on a host is open, closed, or unreachable.

### Features
- Accepts host IP address or hostname
- Accepts port number (1–65535)
- Checks TCP connectivity using Python sockets
- Displays OPEN, CLOSED, TIMEOUT, or ERROR results
- Validates user input

### Technologies Used
- Python 3
- Socket Library
- Visual Studio Code

### How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

`python port_checker.py`

5. Enter the host and port number.

### Example Output

**Open Port**

`[OPEN] Port 8000 is OPEN on 127.0.0.1`

**Closed Port**

`[CLOSED] Port 8000 is CLOSED on 127.0.0.1`

### Testing
The application was tested locally using a Python HTTP server on port 8000.

Screenshots are available in the `screenshots` folder.

### Security Note
Only check ports on systems you own or have permission to test.

### Internship
VirtualWorks – Cyber Security Internship

**Task ID:** task2