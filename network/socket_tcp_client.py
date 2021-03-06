import socket

def main():
    # 创建
    tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接
    svr_addr = ("127.0.0.1", 18080)
    tcp_s.connect(svr_addr)
    # 收发数据
    tcp_s.send("您好，我是客户端".encode('utf-8'))
    print(tcp_s.recv(1024).decode()) # 接收数据
    # 关闭
    tcp_s.close()


if __name__ == "__main__":
    main()