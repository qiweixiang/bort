__version__ = "0.1.0"
__author__ = "qwx"
__all__ = ["myFunc", "my"]

# .myFunc代表的是从当前文件夹下的myFunc.py文件中导入一个jiajia的类或者方法 然后才可以被更多的模块引用
from .myFunc import jiajia

titleaa  = '你好111'