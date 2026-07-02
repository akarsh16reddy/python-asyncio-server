import asyncio
import socket


class ConnectedSocket:
    def __init__(self, server_socket: socket.socket) -> None:
        self._server_socket: socket.socket = server_socket
        self._connection: socket.socket | None = None

    async def __aenter__(self):
        print("Entering context manager, waiting for connection")
        loop = asyncio.get_running_loop()
        connection, address = await loop.sock_accept(self._server_socket)
        self._connection = connection
        print(f"Accepted a connection {address}")
        return self._connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context manager")
        self._connection.close() if self._connection is not None else None
        print("Close connection")


async def main():
    loop = asyncio.get_running_loop()
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ("127.0.0.1", 8000)
    server_socket.bind(server_address)
    server_socket.listen()

    async with ConnectedSocket(server_socket) as connection:
        data = await loop.sock_recv(connection, 1024)
        print(data)


asyncio.run(main())
