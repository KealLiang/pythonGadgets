import socket

def main():
    send_data()

def send_data():
    '''
    udp 发送socket数据
    '''
    # 创建
    udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 使用
    # dest_addr = ("39.97.163.31", 22)
    dest_addr = ("127.0.0.1", 17788)
    udp_s.sendto(b"hahahahahaha", dest_addr)
    # 关闭
    udp_s.close()

# __name__ 是python中的保留变量
# 若在当前被执行程序中其值为__main__
# 若是import进来的其值为其文件名（import的文件都会被先执行，此判断可以避免这种行为）
if __name__ == "__main__":
    main()