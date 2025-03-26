# -*- coding: utf-8 -*-
"""
Created on Tue March  26 08:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("LWM2M Client")
print(Fore.GREEN+font)

import asyncio
from aiocoap import Context, Message, GET, PUT

class LWM2MClient:
    def __init__(self, server_ip='localhost', server_port=5683):
        self.server_ip = server_ip
        self.server_port = server_port

    async def send_get(self, resource_name):
        context = await Context.create_client_context()
        uri = f'coap://{self.server_ip}:{self.server_port}/{resource_name}'
        request = Message(code=GET, uri=uri)
        response = await context.request(request).response
        print(f"Response from server: {response.payload.decode()}")

    async def send_put(self, resource_name, value):
        context = await Context.create_client_context()
        uri = f'coap://{self.server_ip}:{self.server_port}/{resource_name}'
        request = Message(code=PUT, uri=uri, payload=value.encode())
        response = await context.request(request).response
        print(f"Response from server: {response.payload.decode()}")

def main():
    server_ip = input("Enter server IP address (default: 'localhost'): ") or 'localhost'
    server_port = int(input("Enter server port (default: 5683): ") or 5683)

    client = LWM2MClient(server_ip, server_port)

    while True:
        action = input("Choose action (GET/PUT/quit): ").lower()

        if action == "quit":
            break
        elif action == "get":
            resource_name = input("Enter resource name:")
            asyncio.run(client.send_get(resource_name))
        elif action == "put":
            resource_name = input("Enter resource name:")
            value = input(f"Enter value to set for resource:")
            asyncio.run(client.send_put(resource_name, value))

if __name__ == "__main__":
    main()
