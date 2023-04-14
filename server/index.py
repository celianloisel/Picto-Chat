from Class.ChatServer import ChatServer

if __name__ == "__main__":
    host = "10.57.33.217"
    port = 2222
    chat_server = ChatServer(host, port)
    chat_server.start()
