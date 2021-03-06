import socket

def main():
    recive_data()

def recive_data():
    # 创建
    udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 设置绑定接收的地址and端口，接收结果
    loc_addr = ("", 17788) # 因为是本机接收，第一个参数ip可省略
    udp_s.bind(loc_addr)
    data = udp_s.recvfrom(1024) # buffer大小
    # 消费结果
    print(data)
    # 关闭
    udp_s.close()

if __name__ == "__main__":
    main()