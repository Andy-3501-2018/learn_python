from pyecharts import Line
import numpy as np
sb_col = ['#DC143C', '#0000FF', '#00FF7F', '#FFFF00']  # 点的颜色必须为16进制颜色表示
xz = ['circle', 'rect', 'triangle', 'diamond']  # 点的形状
x = np.linspace(-20,20,21)
y_1 = x*2+3
y_2 = x**2+x**3
y_3 = np.sin(x)
y_4 = np.cos(x)
l = Line('自定义曲线颜色')
lines = [y_1,y_2,y_3,y_4]
lines_name = ['直线','抛物线','正弦曲线','余弦曲线']
for i in range(4):
    l.add(lines_name[i], x, lines[i], symbol=xz[i],symbol_size=8,is_smooth=True, xaxis_force_interval=2, xaxis_type='value', yaxis_type='value')
    l._option['series'][i]['itemStyle'] = {#修改线的颜色和图例的形状
        'normal': {
            'color': sb_col[i],
        }
    }

l.render('html/test_5.html')


