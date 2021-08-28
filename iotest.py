# from pyhive import hive
import sys, pprint

#
# class Item:
#     def __init__(self, price):
#         self.price = price
#
#     def __repr__(self):
#         return 'Item[price=%g]' % self.price
#
#
# def print_blank_triangle(n):
#     if n <= 0:
#         raise ValueError('n必须大于0')
#     for i in range(n):
#         print(' ' * (n - i - 1), end='')
#         print('*', end='')
#         if i != n - 1:
#             print(' ' * (2 * i - 1), end='')
#         else:
#             print('*' * (2 * i - 1), end='')
#         if i != 0:
#             print('*')
#         else:
#             print(' ')
#
#
# print_blank_triangle(8)
# def print_multiple_chart(n):
#     for i in range(n):
#         for j in range(i + 1):
#             print('%d * %d = %2d' % ((j + 1), (i + 1), (j + 1) * (i + 1)))
#         print(' ')
#
#
# print_multiple_chart(9)
# print(sys.argv[0])
# pprint.pprint(sys.path)
# def print_triangle(n):
#     '''打印由星号组成的一个三角形'''
#     if n <= 0:
#         raise ValueError('n必须大于0')
#     for i in range(n):
#         print(' ' * (n - i - 1), end=' ')
#         print('*' * (2 * i + 1), end=" ")
#         print(' ', i)
#
#
# def test_print_triangle():
#     print_triangle(3)
#     print_triangle(4)
#     print_triangle(7)
#
#
# if __name__ == '__main__': test_print_triangle()

# def square_gen(val):
#     i = 0
#     out_val = None
#     while True:
#         out_val = (yield out_val ** 2) if out_val is not None else (yield i ** 2)
#         if out_val is not None: print("====%d" % out_val)
#         i += 1
#
#
# sg = square_gen(5)
# print(sg.send(None))
# print(next(sg))
# print(next(sg))
# print('------------')
# print(sg.send(9))
# print(next(sg))

# def test(val, step):
#     print("------函数开始执行-------")
#     cur = 0
#     for i in range(val):
#         cur += i * step
#         print(i,i*step)
#         yield cur
#
# t = test(10, 2)
# print('==================')
# # print(next(t))
# # print(next(t))
# for ele in t:
#     print(ele, end=' ')
# print('Python 是一个非常棒的编程语言，不是吗？')
#
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
#
# for name, number in table.items():
#     print('{0:10} ==> {1:10d}'.format(name, number))
#
# # str = input("请输入：")
# # print("你输入的内容是：", str)
#
# f = open("./test.txt", "w", encoding="utf-8")
# f.write("Python是一门非常棒的编程语言")
# f.close()
#
#
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)
#
#
# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)
#
# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()
