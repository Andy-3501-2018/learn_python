#仪表盘简单使用
from pyecharts import Gauge

gauge = Gauge('仪表盘示例')
gauge.add('电压值','V',300,scale_range=[0,500],)
#  add(name, attr, value,
# scale_range=None,
# angle_range=None, **kwargs)
# name -> str 图例名称
# attr -> list属性名称
# value -> list属性所对应的值
# scale_range -> list仪表盘数据范围。默认为 [0, 100]
# angle_range -> list仪表盘角度范围。默认为 [225, -45]
gauge.render('html/test_2.html')

