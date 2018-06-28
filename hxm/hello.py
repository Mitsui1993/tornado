import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
# options用于从命令行中读取设置，启动文件时用--name=xx传入
define('port', default=8000, help='run on the given port', type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        """
        HTTP GET时执行的方法
        :return:
        """
        # 获取参数，未传获取Hello
        greeting = self.get_argument('greeting', 'Hello')
        # 返回字符串响应
        self.write(greeting + ', friendly user!')


if __name__ == '__main__':
    # options模块解析命令行
    tornado.options.parse_command_line()
    # handlers对应路由，告诉Tornado应该用哪个类响应请求
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    # 将app传递给HTTPServer对象
    http_server = tornado.httpserver.HTTPServer(app)
    # 使用命令行指定的端口进行监听
    http_server.listen(options.port)
    # 创建IOLoop实例开启进程
    tornado.ioloop.IOLoop.instance().start()

