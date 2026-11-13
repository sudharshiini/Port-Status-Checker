
import socket

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=3):
            print(f"[OPEN] Port {port} is OPEN on {host}")

    except ConnectionRefusedError:
        print(f"[CLOSED] Port {port} is CLOSED on {host}")

    except socket.timeout:
        print(f"[TIMEOUT] Port {port} did not respond")

    except OSError as error:
        print(f"[ERROR] Unable to connect: {error}")


def main():
    print("================================")
    print("       PORT STATUS CHECKER")
    print("================================")

    host = input("Enter host (e.g. 127.0.0.1): ").strip()

    if not host:
        print("Error: Host cannot be empty.")
        return

    try:
        port = int(input("Enter port number: "))

        if not 1 <= port <= 65535:
            print("Error: Port must be between 1 and 65535.")
            return

        check_port(host, port)

    except ValueError:
        print("Error: Enter a valid port number.")


if __name__ == "__main__":
    main()
