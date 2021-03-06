import socket

def main():
    # 创建
    tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定地址
    tcp_s.bind(("", 18080))
    # 开启监听（让默认的套接字由主动变为被动）
    tcp_s.listen(128) # 这个值影响同时能有多少个客户端连接
    # 收发数据（返回的sock是为此客户端服务的socket，addr是客户端的地址）
    sock, addr = tcp_s.accept()
    print('sock ==>', str(sock))
    print('addr ==>', addr)
    print('client data ==>', sock.recv(1024).decode('utf-8')) # 接收数据
    sock.send(b'I am SERVER, get your message, thank you')
    sock.close() # 关闭客户端的sock
    # 关闭
    tcp_s.close()

if __name__ == "__main__":
    main()