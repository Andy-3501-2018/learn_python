from pyecharts import Line
import numpy as np
#显示负数时如果不处理横纵坐标的类型会出现显示错误，因此一定要设置横纵坐标为数据类型即value。
x = np.linspace(-10,10,21)
y1 = x*2 +1
y2 = x**2 +1
l = Line('pyecharts曲线测试')
l.height=600
l.width = 1300
l.add('直线',x,y1,is_smooth=True,line_width=3)
l.add('抛物线',x,y2,is_smooth=True,xaxis_type='value',yaxis_type='value',xaxis_force_interval=2,line_width=3)
l.render('html/test_1.html')
