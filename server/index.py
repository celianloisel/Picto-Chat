import sys

from Class.ChatServer import ChatServer

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Syntax: python ChatServer <port-number>')
        exit(201)

    chat_server = ChatServer(sys.argv[1])
    chat_server.execute()
