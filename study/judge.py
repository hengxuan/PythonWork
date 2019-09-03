from sl import *
import easygui
import sys

# C = Pets()
s = '再来一次'
while s == '再来一次':

    ret=easygui.buttonbox(msg='请选择计算单项资质或总评分',title='选择页',choices=('单项属性计算','计算总评分'),image='')
    if ret == '单项属性计算':
        zet = easygui.multenterbox(msg='请输入相关数据',title='数据填写',fields=['宠物成长率','斗志','健体','忠心','灵动'])
        x = zet[0]
        y = zet[1]
        y1 = zet[2]
        y2 = zet[3]
        y3 = zet[4]
        C = Pets(x,y,y1,y2,y3)
        s = C.single()
        pass

    else:
        cet = easygui.multenterbox(msg='请输入相关数据', title='数据填写', fields=['主属性资质', '副属性资质','宠物成长率'])
        x = cet[2]
        y = cet[0]
        y2 = cet[1]
        C = Pets(x, y, y2)
        s = C.score()
else:
    sys.exit(0)
