# charles = {'name': 'Charles L. Dodgson', 'born': 1832}
# lewis = charles
# print(lewis is charles)

# print(id(charles), id(lewis))

# lewis['balance'] = 950
# print(charles)

# alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
# print(alex == charles)
# print(alex is not charles)




#元组的相对不可变性
#元组的不可变性其实是指 tuple数据结构的物理内容（即保存的引用）不可变，与引用的对象无关
# t1 = (1, 2, [30, 40])
# t2 = (1, 2, [30, 40])
# print(id(t1) == id(t2))
# print(t1 == t2)
# id(t1[-1])
# t1[-1].append(99)
# t1
# id(t1[-1])
# print(t1 == t2)

# l1 = [30, 40]
# l2 = [30, 40]
# print(id(l1) == id(l2))





#默认做浅复制
#浅复制：即复制了最外层容器，副本中的元素是源容器中元素的引用，但是如果源容易内有不可变元素，可能会出现意想不到的问题
# l1 = [3, [55, 44], (7, 8, 9)]
# l2 = list(l1)       #深拷贝？？？
# # l2 = l1           #这个操作是浅复制还是深复制？？？
# # l2 = l1[:]        #浅复制
# print(l2)
# print(l2 == l1)
# print(l2 is l1)


# l1 = [3, [66, 55, 44], (7, 8, 9)] 
# l2 = list(l1) 
# # print(id(l1) == id(l2))   #
# l1.append(100)
# l1[1].remove(55)
# print('l1:', l1) 
# print('l2:', l2) 
# l2[1] += [33, 22] 
# l2[2] += (10, 11)
# print('l1:', l1) 
# print('l2:', l2)



# #深复制
# class Bus: 
#     def __init__(self, passengers=None): 
#         if passengers is None: 
#             self.passengers = [] 
#         else:
#             self.passengers = list(passengers) 

#     def pick(self, name): 
#         self.passengers.append(name) 

#     def drop(self, name): 
#         self.passengers.remove(name)

# import copy
# bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
# bus2 = copy.copy(bus1)   #浅复制
# bus3 = copy.deepcopy(bus1)  #深复制
# print(id(bus1), id(bus2), id(bus3))   #复制出来的对象都不相同
# bus1.drop('Bill')
# print(bus2.passengers)
# print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))  #内部维护的passengers是一个list
# print(bus3.passengers)


#循环引用:b 引用 a，然后追加到 a 中；deepcopy会想办法复制a
# a = [10, 20]
# b = [a, 30]
# a.append(b)   #b[[10, 20], 30]  
# print(a)
# from copy import deepcopy
# c = deepcopy(a)
# print(c)




#函数的参数作为引用
#不可变对象不能修改传入的实参，可变对象的实参可以被修改
# def f(a, b):
#     # a += b 
#     c= list(a)
#     print(id(c))
#     print(id(a))
#     print(c == a)
#     c.remove(1)
    # return a

# x = 1
# y = 2
# f(x, y)
# print(x, y)

# a = [1, 2]
# b = [3, 4]
# f(a, b)
# print(a, b)

# t = (10, 20)
# u = (30, 40)
# f(t, u)
# print(t, u)



#应该避免使用可变类型作为参数的默认值
# class HauntedBus: 
#     """备受幽灵乘客折磨的校车""" 
#     def __init__(self, passengers=[]):
#         self.passengers = passengers 

#     def pick(self, name): 
#         self.passengers.append(name)
        
#     def drop(self, name): 
#         self.passengers.remove(name)

# bus1 = HauntedBus(['Alice', 'Bill'])
# print(bus1.passengers)
# bus1.pick('Charlie')
# bus1.drop('Alice')
# print(bus1.passengers)

# bus2 = HauntedBus()
# bus2.pick('Carrie')
# print(bus2.passengers)

# bus3 = HauntedBus()
# print(bus3.passengers)

# bus3.pick('Dave')
# print(bus2.passengers)

# print(bus2.passengers is bus3.passengers)
# print(bus1.passengers)
# #上面的问题在于：没有指定初始乘客的 HauntedBus 实例会共享同一个乘客列表！！！
# #默认值在定义函数时计算（通常在加载模块时）   因此默认值变成了函数对象的属性

# print(dir(HauntedBus.__init__))
# print(HauntedBus.__init__.__defaults__)
# print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)




#防御可变参数
# class TwilightBus: 
#     """让乘客销声匿迹的校车""" 
#     def __init__(self, passengers=None): 
#         if passengers is None:
#             self.passengers = []
#         else:
#             self.passengers = passengers
#             self.passengers = list(passengers)    #这样子是浅拷贝，里面的操作也会影响到外面把？？？为啥最后没有？

#     def pick(self, name): 
#         self.passengers.append(name)

#     def drop(self, name): 
#         self.passengers.remove(name)

# basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
# bus = TwilightBus(basketball_team)
# bus.drop('Tina')
# bus.drop('Pat')
# print(basketball_team)   




#del和垃圾回收
#del 语句删除名称，而不是对象
#8-16
# import weakref
# s1 = {1, 2, 3}
# s2 = s1
# def bye(): 
#     print('Gone with the wind...') 

# ender = weakref.finalize(s1, bye)    #finalize 持有 {1, 2, 3} 的弱引用
# print(ender.alive)

# del s1     #明确指出 del不会删除对象，但是执行 del 操作后可能会导致对象不可获取，从而被删除
# print(ender.alive)

# s2 = 'spam'
# print(ender.alive)



#弱引用
#弱引用不会增加对象的引用数量，弱引用不会妨碍所指对象被当作垃圾回收
#8-17
#如果对象存在，调用弱引用可以获取对象；否则返回 None
# import weakref
# a_set = {0, 1}
# wref = weakref.ref(a_set)
# print(wref)
# print(wref())
# a_set = {2, 3, 4}
# print(wref())
# print(wref() is None)
# print(wref() is None)




#WeakValueDictionary 类实现的是一种可变映射，里面的值是对象的 弱引用。
# 被引用的对象在程序中的其他地方被当作垃圾回收后，对应的键会自动从 WeakValueDictionary 中删除。
# 因此，WeakValueDictionary 经常用于缓存
# 8-18
# class Cheese: 
#     def __init__(self, kind): 
#         self.kind = kind 
        
#     def __repr__(self): 
#         return 'Cheese(%r)' % self.kind

# import weakref
# stock = weakref.WeakValueDictionary()
# catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

# for cheese in catalog:
#     stock[cheese.kind] = cheese

# print(sorted(stock.keys()))
# del catalog
# print(sorted(stock.keys()))   #临时变量引用了对象，这可能会导致该变量的存在时间比预期长。
# del cheese
# print(sorted(stock.keys()))



#弱引用的局限
#基本的 list 和 dict 实例不能作为所指对象，但是它们的子类可以轻松地 解决这个问题
#int 和 tuple 实例不能作为弱引用的目标，甚至它们的子类也不行。
# import weakref  
# class MyList(list): 
#     """list的子类,实例可以作为弱引用的目标""" 

# a_list = MyList(range(10)) # a_list可以作为弱引用的目标 
# wref_to_a_list = weakref.ref(a_list)



#Python对不可变类型施加的把戏
#8-20
#使用另一个元组构建元组，得到的其实是同一个元组
# t1 = (1, 2, 3) 
# t2 = tuple(t1) 
# print(t2 is t1)
# print(id(t1))
# print(id(t2))
# t3 = t1[:] 
# print(t3 is t1)
# print(id(t3))
#str、bytes 和 frozenset 实例也有这种行为:返回同一个对象的引用，而不是创建一个副本


# t1 = (1, 2, 3) 
# t3 = (1, 2, 3) 
# print(t3 is t1)    #应该是解释器问题，我这里结果和书上的不一样
# s1 = 'ABC'
# s2 = 'ABC'
# print(s2 is s1)

# l1 = [1,2]
# l2 = [1,2]
# print(l1 is l2)

#简单的赋值不创建副本
#对 += 或 *= 所做的增量赋值来说，如果左边的变量绑定的是不可变对象，会创建新对象；如果是可变对象，会就地修改
#为现有的变量赋予新值，不会修改之前绑定的变量。这叫重新绑定：现在变量绑定了其他对象。
# 如果变量是之前那个对象的最后一个引用，对象会被当作垃圾回收。
#函数的参数以别名的形式传递，这意味着，函数可能会修改通过参 数传入的可变对象。
# 这一行为无法避免，除非在本地创建副本，或 者使用不可变对象（例如，传入元组，而不传入列表）。 
# 使用可变类型作为函数参数的默认值有危险，因为如果就地修改了参数，默认值也就变了，这会影响以后使用默认值的调用。

#可变对象还是导致多线程编程难以处理的主要原因，因为某个线程改动对象后，
# 如果不正确地同步，那就会损坏数据。但是过度同步，又会导致死锁。