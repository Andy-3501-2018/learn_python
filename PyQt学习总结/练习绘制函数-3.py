from PyQt5.Qt import *
import sys
import numpy as np
class My_window(QWidget):
    def __init__(self):#初始化函数，运行该窗口类时首先运行该初始化函数。
        super(My_window, self).__init__()

        self.initUi()

    def initUi(self):
        self.setWindowTitle('基本窗口')
        self.resize(1600,900)

        self.update()
        self.show()

    def paintEvent(self, e):#重写父类中的绘制函数
        qp = QPainter()
        qp.begin(self)
        self.draw_pic(qp)
        qp.end()
    def draw_pic(self,qp):
        pen = QPen(Qt.black,2,Qt.SolidLine)
        #绘制坐标轴
        x_0 = 400
        y_0 = 450
        x_1 = 800
        y_1 = 50
        qp.setPen(pen)
        qp.drawLine(x_0,y_0,x_0+800,y_0)
        qp.drawLine(x_1,y_1,x_1,y_1+800)
        for i in range(9):
            qp.drawLine(x_0+100*i,y_0,x_0+100*i,y_0-5)
            qp.drawLine(x_1,y_1+100*i,x_1+5,y_1+100*i)
        pen = QPen(Qt.red,3)
        qp.setBrush(QColor(255,0,0))
        qp.setPen(pen)
        qp.drawEllipse(200,100, 100, 100)#第一位表示圆的左侧的横坐标，第二位表示圆的顶部的纵坐标,后面两个表示圆的半径
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(150, 150, 190, 150)


    def draw_sun(self):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.red,2,Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(150,200,190,200)







if __name__ == '__main__':
    #运行窗口固定代码格式
    app = QApplication(sys.argv)
    win = My_window()
    sys.exit(app.exec_())


