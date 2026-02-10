__all__ = ['cale', 'add', 'A']
def cale(x, y):
    return x + y

def add(x, y):
    return x + y

class A:

    # 这是类属性
    name = 'qwx'

    # 初始化方法
    def __init__(self, a, b, name):
        self.a = a
        self.b = b
        self.name = name

    def run(self,a, b):
        print(f"这是run{self.a}")

#    魔法方法 __xx__ 魔法方法不需要自己调用 由解释器调用  在合适的时机触发
    def __str__(self):
        return "1222"
    def __eq__(self, other):
        print("比较大阿晓")
        return self.a == other.a and self.b == other.b

    def __le__(self, other):
        return self.a <= other.a and self.b <= other.b


# print(__name__)
if __name__ == '__main__':
    print(cale(3, 4))


