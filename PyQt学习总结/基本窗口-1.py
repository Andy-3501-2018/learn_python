from PyQt5.Qt import *
import sys

class My_window(QWidget):
    def __init__(self):#初始化函数，运行该窗口类时首先运行该初始化函数。
        super(My_window, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('基本窗口')
        self.resize(1600,800)
        self.show()


if __name__ == '__main__':
    #运行窗口固定代码格式
    app = QApplication(sys.argv)
    win = My_window()
    sys.exit(app.exec_())