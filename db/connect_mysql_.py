'''
安装命令：pip3 install pymysql
pymysql连接mysql
知识点：
1、创建连接、游标，关闭连接、游标
2、使用实现上下文管理器的对象连接mysql（with语句）
'''
from pymysql import connect

class MysqlConn(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = 'utf8'
        self.__conn = None

    @property
    def m_connect(self):
        if self.__conn:
            return self.__conn
        else:
            try:
                # self.__conn = connect(host='localhost', port=3306, user='root', password='root', database='sakila', charset='utf8')
                self.__conn = connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database, charset=self.charset)
            except Exception as e:
                print("数据库连接失败！", e)
            else:
                return self.__conn

    @property
    def cursor(self):
        return self.m_connect.cursor()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if self.cursor:
            self.cursor.close()
        self.m_connect.close()

def connect_mysql():
    """手动连接"""
    # 获取连接，游标
    conn = connect(host='localhost', port=3306, user='root', password='root', database='sakila', charset='utf8')
    cursor = conn.cursor()

    rows = cursor.execute("select * from actor;")
    print(rows)

    # 关闭连接、游标
    cursor.close()
    conn.close()

def obj_connect():
    """使用实现了上下文管理的对象连接"""
    with MysqlConn('localhost', 3306, 'root', 'root', 'sakila') as conn:
        cur = conn.cursor
        params = ["'JENNIFER' or 1=1", "JENNIFER"]
        # rows = cur.execute("select * from actor where first_name = %s" % (params[0]))
        rows = cur.execute("select * from actor where first_name = %s", params[1]) # 用execute自带的传参，防止sql注入
        print("查询结果：", rows)
        # print(cur.fetchone())
        # print(cur.fetchall())
        print(cur.fetchmany(3))

def obj_connect_modify():
    with MysqlConn('localhost', 3306, 'root', 'root', 'order') as conn:
        cur = conn.cursor
        cur.execute("""insert into aa (name) values("python插入的")""") # 使用三个引号避免转义“
        # conn.m_connect.rollback()
        conn.m_connect.commit()


if __name__ == "__main__":
    # connect_mysql()
    obj_connect()
    # obj_connect_modify()