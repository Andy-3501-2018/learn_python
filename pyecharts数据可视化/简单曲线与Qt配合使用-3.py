#在Qt界面中使用Web浏览器呈现pyecharts生成的html文件
from PyQt5.Qt import *
from pyecharts import Line
import numpy as np
import random
import sys
class My_windsow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.resize(1500,800)
        self.setWindowTitle('动态显示曲线')
        self.web = QWebView(self)
        self.web.setGeometry(20, 20, 1460, 600)
        # self.show_line()
        timer = QTimer(self)
        timer.timeout.connect(self.show_line)
        timer.start(5000)#5000毫秒更新一次即5秒更新一次


        self.show()

    def show_line(self):
        print('展示曲线')
        x = random.randint(0,10)#随机生成0到10之间的一个整数
        X = np.linspace(x-20, x+20, 41)
        Y = X**2 + 1
        print(X)
        print(Y)
        line = Line('定时更新曲线')
        line.width=1440
        line.height = 550
        line.add('曲线', X, Y, xaxis_type='value', yaxis_type='value', xaxis_force_interval=2, is_smooth=True)
        line.render('html/test_3.html')
        self.web.load(QUrl("file:///untitled4/pyecharts数据可视化/html/test_3.html"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = My_windsow()
    sys.exit(app.exec_())



