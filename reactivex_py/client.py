import socket


HOST = "127.0.0.1"
PORT = 8888


def main():
    with socket.create_connection((HOST, PORT)) as sock:
        message = input("Введите сообщение: ")

        # Важно: сервер читает reader.readline(),
        # поэтому нужен перевод строки \n
        sock.sendall((message + "\n").encode("utf-8"))

        data = sock.recv(1024)
        print("Ответ сервера:", data.decode("utf-8"))


if __name__ == "__main__":
    main()