import asyncio
import logging
import socket
from asyncio import AbstractEventLoop, get_event_loop


async def echo(connection: socket.socket):
    loop = get_event_loop()
    try:
        while data := await loop.sock_recv(connection, 1024):
            if data == b"c":  # simulating a crash
                raise Exception("Unexpected network error")
            await loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()


async def listen_for_connection(server_socket: socket.socket):
    while True:
        connection, address = await get_event_loop().sock_accept(server_socket)
        print(f"Connection received from {address}")
        asyncio.create_task(echo(connection))


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    await listen_for_connection(server_socket)


asyncio.run(main())
