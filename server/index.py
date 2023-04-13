from Class.ChatServer import ChatServer

if __name__ == "__main__":
    host = "192.168.1.106"
    port = 2222
    chat_server = ChatServer(host, port)
    chat_server.start()
