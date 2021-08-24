print('Python 是一个非常棒的编程语言，不是吗？')

table = {'Google':1, 'Runoob':2, 'Taobao':3}

for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

str = input("请输入：")
print("你输入的内容是：", str)