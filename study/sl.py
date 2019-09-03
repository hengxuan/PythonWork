import easygui
class Pets():
    def __init__(self,x,y,y1,y2,y3):
        self.x = float(x)
        self.y = float(y)
        self.y1 = float(y1)
        self.y2 = float(y2)
        self.y3 = float(y3)

    def single(self):
        z = self.y * 0.2565 + self.x * 89.5865 + 37.767
        z1 = self.y1 * 0.2565 + self.x * 89.5865 + 37.767
        z2 = self.y2 * 0.2565 + self.x * 89.5865 + 37.767
        z3 = self.y3 * 0.2565 + self.x * 89.5865 + 37.767
        s = easygui.buttonbox(msg=['满级满星斗志属性：', z,'满级满星健体属性:',z1], title='计算结果', choices=('再来一次', '结束'))
        return s

    def score(self):
        Y1 = (96.4 - 0.0035 * self.y) * self.x + 0.2886 * self.y - 26.26
        Y2 = (96.4 - 0.0035 * self.y2) * self.x + 0.2886 * self.y2 - 26.26
        z = Y1 / 1698 * 66.7 + Y2 / 1693 * 33.3
        s = easygui.buttonbox(msg=('该属性为：', z), title='计算结果', choices=('再来一次', '结束'))
        return s