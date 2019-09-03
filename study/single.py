# 属性点=资质点×0.2565+成长率×89.5865+37.767
import easygui

# x = input("请输入宠物成长率：")
# y = input("请输入资质点：")
# x = float(x)
# y = float(y)
# z = y*0.2565+x*89.5865+37.767
# print("属性数值为：" ,z)

def single(x,y):
    x = float(x)
    y = float(y)
    # global z
    z = y * 0.2565 + x * 89.5865 + 37.767

    # easygui.msgbox(msg=('该属性为：',z),title='计算结果：')
    s = easygui.buttonbox(msg=('该属性为：',z),title='计算结果',choices=('再来一次','结束'))
    return s
    # easygui.ccbox(msg=('该属性为：',z),title='结果页',choices=('再来一次','结束'))
    # print("单项属性数值为：", z)