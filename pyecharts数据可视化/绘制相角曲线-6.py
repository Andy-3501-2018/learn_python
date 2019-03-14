from pyecharts import Line
import numpy as np

l_1 = Line('正弦信号曲线')
l_2 = Line('正弦信号幅值与相角的关系')
phase=[]
p=[]

i=np.linspace(0,1,100000)
s=np.cos(2*np.pi*i+60/180*np.pi)
l_1.add('正弦信号',i,s,is_smooth=True,xaxis_type='value',yaxis_type='value',xaxis_name='时间',xaxis_name_pos='end')
l_1.render('html/test_6.html')


for j in range(1000):
    sr=np.cos(2*np.pi*i+j/1000*np.pi-np.pi/2)
    phase.append((j/1000*np.pi-np.pi/2)/np.pi*180)
    p.append(sum(s*sr)/1000)
print(p)
x = []
for i in range(60):
    x.append(60)

y = np.linspace(0,1,60)
l_2.add('正弦信号幅值与相角的关系',phase,p,is_smooth=True,xaxis_type='value',yaxis_type='value',xaxis_name='相角',xaxis_name_pos='end',mark_point=['max',],line_width=1,xaxis_force_interval=10)
l_2.add('',x,y,is_smooth=True,line_type='Polar',xaxis_type='value',yaxis_type='value',is_datazoom_show=True,is_datazoom_extra_show=True,xaxis_force_interval=1)
l_2.render('html/test_7.html')