# #装饰器写法1
# @decorate 
# def target(): 
#     print('running target()')

# #装饰器写法2
# def target(): 
#     print('running target()') 
    
# target = decorate(target)





# #装饰器的一大特性是，能把被装饰的函数替换成其他函数。
# # 第二 个特性是，装饰器在加载模块时立即执行
# def deco(func): 
#     def inner(): 
#         print('running inner()')  
#     return inner

# @deco 
# def target():
#     print('running target()') 

# target()



# #装饰器的一个关键特性：在被装饰的函数定义之后立即运行
# registry = [] 
# def register(func):
#     print('running register(%s)' % func) 
#     registry.append(func)
#     return func

# @register
# def f1(): 
#     print('running f1()') 

# @register 
# def f2(): 
#     print('running f2()') 
    
# def f3():
#     print('running f3()') 
    
# def main(): 
#     print('running main()') 
#     print('registry ->', registry) 
#     f1() 
#     f2() 
#     f3() 

# if __name__=='__main__': 
#     main() 





# #使用注册装饰器可以改进 6.1 节中的电商促销折扣示例
# promos = []

# def promotion(promo_func): 
#     promos.append(promo_func) 
#     return promo_func

# @promotion 
# def fidelity(order): 
#     """为积分为1000或以上的顾客提供5%折扣""" 
#     return order.total() * .05 if order.customer.fidelity >= 1000 else 0

# @promotion 
# def bulk_item(order): 
#     """单个商品为20个或以上时提供10%折扣""" 
#     discount = 0 
#     for item in order.cart: 
#         if item.quantity >= 20: 
#             discount += item.total() * .1 
#     return discount

# @promotion 
# def large_order(order): 
#     """订单中的不同商品达到10个或以上时提供7%折扣""" 
#     distinct_items = {item.product for item in order.cart} 
#     if len(distinct_items) >= 10: 
#         return order.total() * .07 
#     return 0

# def best_promo(order):
#     """选择可用的最佳折扣""" 
#     return max(promo(order) for promo in promos)




# #python变量作用域规则
# def f1(a): 
#     print(a)
#     print(b)

# # b = 6  #注释掉会报找不到b的错
# f1(3)


# b = 6 
# def f2(a): 
#     print(a) 
#     print(b) 
#     b = 9 
    
# f2(3)


# b = 6 
# def f3(a): 
#     global b 
#     print(a) 
#     print(b) 
#     b = 9 
    
# f3(3)
# print(b)
# f3(3) 
# b = 30 
# print(b)





#闭包指延伸了作用域的函数，其中包含函数定义体中引用、但是 不在定义体中定义的非全局变量。
# 函数是不是匿名的没有关系，关键是 它能访问定义体之外定义的非全局变量。

#移动平均值的类
# class Averager(): 
#     def __init__(self): 
#         self.series = [] 
#     def __call__(self, new_value):
#         self.series.append(new_value) 
#         total = sum(self.series) 
#         return total/len(self.series)

# avg = Averager()
# print(avg(10))
# print(avg(11))
# print(avg(12))


#另一种实现方式
# def make_averager(): 
#     series = [] 

#     def averager(new_value): 
#         series.append(new_value) 
#         total = sum(series) 
#         return total/len(series) 
#     return averager

# avg = make_averager()
# print(avg(10))
# print(avg(11))
# print(avg(12))
# print(avg.__code__.co_varnames)   #局部变量
# print(avg.__code__.co_freevars)  #自由变量
# print(avg.__closure__)
# print(avg.__closure__[0].cell_contents)   
#总结：闭包是一种函数，它会保留定义函数时存在的自由变量的绑定， 这样调用函数时，虽然定义作用域不可用了，但是仍能使用那些绑定
#只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中的外部变量







#nonlocal
# def make_averager(): 
#     count = 0 
#     total = 0 
    
#     def averager(new_value): 
#         #对数字、字符串、元组等不可变类型来说，只能读取，不能更新。 
#         # 如果尝试重新绑定，例如 count = count + 1，其实会隐式创建局部 变量 count。
#         # 这样，count 就不是自由变量了，因此不会保存在闭包 中
#         count += 1    #当 count是数字或任何不可变类型时，count += 1 语句的作用其实与 count = count + 1 一样
#         total += new_value 
#         return total / count 
#     return averager

# avg = make_averager()
# print(avg(10))


#nonlocal它的作用是把变量标记为自由变量，即使在函数中为变量赋予新值了，也会变成自由变量。
# def make_averager(): 
#     count = 0 
#     total = 0 
#     def averager(new_value): 
#         nonlocal count, total 
#         count += 1 
#         total += new_value 
#         return total / count 
#     return averager

# avg = make_averager()
# print(avg(10))
# print(avg(11))





#实现一个简单的装饰器
# import time 

# def clock(func): 
#     def clocked(*args): 
#         t0 = time.perf_counter() 
#         result = func(*args) 
#         elapsed = time.perf_counter() - t0 
#         name = func.__name__ 
#         arg_str = ', '.join(repr(arg) for arg in args) 
#         print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result)) 
#         return result
#     return clocked

# #使用装饰器
# import time  
# @clock 
# def snooze(seconds): 
#     time.sleep(seconds) 
    
# @clock
# def factorial(n): 
#     return 1 if n < 2 else n*factorial(n-1) 
    
# if __name__=='__main__': 
#     print('*' * 40, 'Calling snooze(.123)') 
#     snooze(.123) 
#     print('*' * 40, 'Calling factorial(6)') 
#     print('6! =', factorial(6))
#把被装饰的函数替换成新函数，二者接受相同 的参数，
# 而且（通常）返回被装饰的函数本该返回的值，同时还会做些额外操作



#上述代码装饰器缺点：不支持关键字参数，而且遮盖了被装饰函数的 __name__ 和 __doc__ 属性。
#改进版的装饰器
#functools.wraps 装饰器把相关的属性从 func 复制到 clocked 中。 此外，这个新版还能正确处理关键字参数
# import time 
# import functools 
# def clock(func): 
#     @functools.wraps(func) 
#     def clocked(*args, **kwargs): 
#         t0 = time.time() 
#         result = func(*args, **kwargs) 
#         elapsed = time.time() - t0 
#         name = func.__name__ 
#         arg_lst = [] 
#         if args: 
#             arg_lst.append(', '.join(repr(arg) for arg in args)) 
#         if kwargs: 
#             pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())] 
#             arg_lst.append(', '.join(pairs)) 
#         arg_str = ', '.join(arg_lst) 
#         print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result)) 
#         return result 
#     return clocked






#使用functools.lru_cache做备忘,它实现了备忘 （memoization）功能

#性能不行
# @clock 
# def fibonacci(n): 
#     if n < 2: 
#         return n 
#     return fibonacci(n-2) + fibonacci(n-1) 
    
# if __name__=='__main__': 
#     print(fibonacci(6))



# import functools

# @functools.lru_cache()    #如果增加两行代码，使用 lru_cache，性能会显著改善，可以盖上优化递归算法
# @clock 
# def fibonacci(n): 
#     if n < 2: 
#         return n 
#     return fibonacci(n-2) + fibonacci(n-1) 
    
# if __name__=='__main__': 
#     print(fibonacci(6))



#单分派泛函数  
# @singledispath 的优点是支持模块化扩展：各个模块可以为 它支持的各个类型注册一个专门函数
# from functools import singledispatch 
# from collections import abc 
# import numbers 
# import html 
# @singledispatch 
# def htmlize(obj): 
#     content = html.escape(repr(obj)) 
#     return '<pre>{}</pre>'.format(content) 
    
# @htmlize.register(str) 
# def _(text): 
#     content = html.escape(text).replace('\n', '<br>\n') 
#     return '<p>{0}</p>'.format(content) 
    
# @htmlize.register(numbers.Integral) 
# def _(n): 
#     return '<pre>{0} (0x{0:x})</pre>'.format(n) 

# @htmlize.register(tuple) 
# @htmlize.register(abc.MutableSequence) 

# def _(seq): 
#     inner = '</li>\n<li>'.join(htmlize(item) for item in seq) 
#     return '<ul>\n<li>' + inner + '</li>\n</ul>'‘




#叠放装饰器
#相当于f = d1(d2(f))
# @d1 
# @d2 
# def f(): 
#     print('f')



