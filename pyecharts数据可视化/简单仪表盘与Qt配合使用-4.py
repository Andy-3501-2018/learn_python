from PyQt5.Qt import *
from pyecharts import Gauge
import sys
import random

class My_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.resize(1600,800)
        self.setWindowTitle('定时更新仪表盘')
        self.Web = QWebView(self)
        self.Web.setGeometry(20,20,1460,600)
        timer = QTimer(self)
        timer.timeout.connect(self.show_gauge)
        timer.start(5000)
        self.show()

    def show_gauge(self):
        X = random.randint(0,200)
        gauge = Gauge('定时更新仪表盘')

        gauge.add('电压','V',X,scale_range=[0,200])
        gauge.render('html/test_4.html')
        self.Web.load(QUrl('file:///untitled4/pyecharts数据可视化/html/test_4.html'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = My_window()
    sys.exit(app.exec_())
