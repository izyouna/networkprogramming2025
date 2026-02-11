# Step 1: Create Broadcast Sender
# broadcaster.py
import socket
from config import BROADCAST_IP, PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

message = "DISCOVERY: Who is online?"
sock.sendto(message.encode(), (BROADCAST_IP, PORT))

print("[BROADCASTER] Message sent ควยยย")
sock.close()
