import socket, sys

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.10", 5000))

# 0xAA 0xBB 0x03 0x01 0x0n 0xEE
data = bytes.fromhex(f"AABB0301{int(sys.argv[1]):02x}EE")
s.send(data)
