import selectors
import socket
from selectors import SelectorKey
from typing import Any, List, Tuple

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector = selectors.DefaultSelector()
_ = selector.register(fileobj=server_socket, events=selectors.EVENT_READ)

# ┌──────────────────────────────────────────┐
# │  selector.select(timeout=1)  ← SLEEPS    │
# │         (only blocking call)             │
# └──────────────┬───────────────────────────┘
#                │ OS: "server_socket is readable!"
#                ▼
# ┌──────────────────────────────────────────┐
# │  event.fileobj == server_socket?  YES    │
# │    → accept()  (succeeds instantly)      │
# │    → register new connection for READING │
# └──────────────┬───────────────────────────┘
#                │ loop back
#                ▼
# ┌──────────────────────────────────────────┐
# │  selector.select(timeout=1)  ← SLEEPS    │
# │         (waiting for client data)        │
# └──────────────┬───────────────────────────┘
#                │ OS: "connection is readable!"
#                ▼
# ┌──────────────────────────────────────────┐
# │  event.fileobj == server_socket?  NO     │
# │    → recv(1024)  (succeeds instantly)    │
# │    → send(data)  (echo back)             │
# └──────────────┬───────────────────────────┘
#                │ loop back, sleep again

while True:
    events = selector.select(timeout=1)  # OS! wake me when ready
    if len(events) == 0:
        print("No events, waiting a bit more")

    for event, _ in events:
        event_descriptor: Any = event.fileobj

        if event_descriptor == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f"I got a connection from {address}")
            _ = selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_descriptor.recv(1024)
            print(f"{event}")
            print(f"I got some data: {data}")
            event_descriptor.send(data)
