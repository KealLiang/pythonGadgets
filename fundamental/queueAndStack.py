import queue as q
'''
    * queue模块里的容器是线程安全的
'''


def queueDemo():
    '''
        先进先出：FIFO
    '''
    q1 = q.Queue(4)
    for x in range(4):
        q1.put(x)
    
    for i in range(q1.qsize()):
        print('第%d个元素是：%s' % (i, q1.get()))

def stackDemo():
    '''
        后进先出：LIFO
    '''
    q2 = q.LifoQueue(4)
    for x in range(4):
        q2.put(x)
    
    for i in range(q2.qsize()):
        print('第%d个元素是：%s' % (i, q2.get()))


if __name__ == "__main__":
    queueDemo()
    print('-' * 50)
    stackDemo()

