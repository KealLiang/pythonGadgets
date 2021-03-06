from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def firstNode():
    # debug模式开启后，可以把服务端的错误显示在客户端，方便调试
    # i = 1/0
    return "Hello Flask!"


if __name__ == '__main__':
    app.run(debug=True)
