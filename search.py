#!/usr/bin/env python
# encoding=utf-8

import tornado.web
import tornado.ioloop
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import random
import os


class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("user_id"):
            self.set_secure_cookie("user_id", str(random.randint(100, 10000)))
            self.write("Cookie is already seted, please frash to conitue !")
        else:
            self.render("index.html")

    def post(self):
        name = self.get_argument("name")
        password = self.get_argument("password")
        email = self.get_argument("email")
        param = dict(name=name, password=password, email=email)
        self.render("confirm.html", **param)
        # self.render("confirm.html", name=name, password=password, email=email)
        # 这一句和上面用**param的含义是一样的，都是将键值对传到模板上


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "rui_zhao_together",
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "debug": True
}

url_map = []

url_map.append((r"/", SearchHandler))
url_map.append((r"/static/(.*)", tornado.web.StaticFileHandler, dict(path=settings["static_path"])))

application = tornado.web.Application(url_map, **settings)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        port = sys.argv[1]
    else:
        port = 8888

    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
