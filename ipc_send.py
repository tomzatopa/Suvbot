#!/usr/bin/env python3
"""Send a command to Suvbot via IPC socket."""
import socket
import sys

SOCKET_PATH = "/tmp/suvbot.sock"

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <command>")
        sys.exit(1)

    cmd = sys.argv[1]
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        sock.connect(SOCKET_PATH)
        sock.sendall(cmd.encode())
        response = sock.recv(1024).decode().strip()
        print(response)
    except FileNotFoundError:
        print(f"Socket not found: {SOCKET_PATH} (is the bot running?)")
        sys.exit(1)
    finally:
        sock.close()

if __name__ == "__main__":
    main()