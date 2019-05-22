# Python 学习笔记
## 一、类型
## 二、表达式
## 三、函数

### 3.1 定义

> + 减少外部依赖、可测试、可维护
> + 尽可能小：`查询`和`修改`应该分开写2个函数
> + 及时清理不再使用的`参数、代码、注释`
> + 函数可以作为`参数和返回值`传递
> + 函数支持嵌套，甚至`内层与外层同名`
```python
def test():
    print('outer test')
    
    def test():
        print('inner test')
    
    return test
x = test()
x()
'''
输出结果是： outer test
return的test是内部的这个函数，这里，函数作为返回值，所以，x是一个函数
x()
相当于执行这个函数，输出： inner test
''' 
```
> + 匿名函数：===lambda表达式，也就是没有默认的函数名，不再调用了

**lambda表达式的`：`前面是参数，后面是表达式，返回的是表达式的运算结果**
```python3
add = lambda x, y: x + y

add(1, 2)
add = 3

#另外一个有意思的用法：构建方法表
ops = {
        'add': lambda x, y : x + y,
        'sub': lambda x, y : x - y,
        }

ops['add'](2, 3)
#输出5

# lambda的嵌套，支持闭包：
 test =  lambda x : (lambda x , y : x + y)
 
 add = test(2)
 add(3)
 #输出=5  
 #也就是说， lambda表达式后面的（）里面就是它的参数的值
```

### 3.2 参数

> + 参数分为`位置参数arg`和`键值参数*kwarg`两种
>
> + 可以设置 默认值，也可以`设置变参收集多余的参数`
>
> + 不管实参是`指针、引用还是名字`，都是以`值复制的方式`传递，所以形参变化不会影响实参
>
>   ```python
>   '''
>   函数调用时传参的方式：
>   1.忽略有默认值的 `res = test(1,2)`
>   2.给默认值显示提供实参 `res = test(1,2,15)`
>   3.按*展开： `res = test(*(1,2,15))`
>   4.命名传递：`res = test(b=2, a=1)`
>   5.键值展开，等同于命名传递：`res = test(**{'a':1, 'b':2})`
>   '''
>   ```
>
> + 位置参数：`带*args的收集参数只能有一个`（简单说就是传参多了的话丢到这个*args中），但是，不能对收集参数传参
>
>   ```python
>   #示例：
>   def test(a, b, *args, **kwargs):
>       print(kwargs)	#注意这里没有**
>       
>   test(a=1, b=2, x=1, y=2)
>   #输出是：
>   {'x':1,'y':2}
>   #**kwargs只收集多余的===键值参数，存成字典===    
>   def test(**kwargs):
>       print(kwarg)
>   # test(x=1, y=2)等价于test(**{'x':1,'y':2})
>   ```

### 3.3 返回值

> + 当返回多个值时，都会被`打包成一个tuple`

### 3.4 闭包

> 指的是函数在离开生成环境后，仍然可以记住，并且持续引用词法作用域里面的外部变量。
>
> 闭包所引用的环境变量称为**自由变量**
>
> + 返回的必须是个`函数对象`
> + 自引用：函数内引用自己，也可以形成闭包
> + 延迟绑定：闭包只是绑定自由变量，不会立即计算引用内容，只有闭包函数执行时，才会访问引用的目标对象，称为‘late binding’
> + 
>
> 创建闭包：等同于“新建函数对象，附加自由变量”
>
> ```python
> #举例： 在函数外部，函数内参数因为是局部变量，生命周期已经结束，但是仍然可以被访问到
> def make():
>     x = [1, 2]
>     return lambda : print(x)
> a = make()
> a()
> #a是返回的lambda表达式，a()又访问到了x，这就是闭包
> ```
>
> ```python
> # 自引用形成闭包
> def make(x):
>     def test():
>         test.x = x			#引用自己
>         print(test.x)		#引用当前函数的实例，相当于this
>     return test
> 
> a = make(1234)
> b = make([1,2])
> a()		#1234
> b()		#[1, 2]
> ```
>
> 闭包的优缺点：
>
> + 优点：具备封装特征，可以实现隐式的上下文状态，减少参数，可以部分替代全局变量，将执行环境和接口分离；
> + 缺点：隐式依赖自由变量，提高代码复杂度。另外，自由变量的生命周期增长，提高内存占用。

## 四、迭代器

> 参考：[迭代器和生成器](https://www.cnblogs.com/coder2012/p/4305935.html)

> 迭代：从对象中重复的获取数据，直至结束；
>
> 概括：使用`__iter__`方法返回一个迭代器对象，这个迭代器对象实现了`__next__`方法；
>
> `__iter__`方法：表示目标是可迭代类型，允许新建并返回一个迭代器实例(iterator),然后使用`iterator__next__`依次返回结果，直到StopIteration异常；
>
> **辅助函数**：
>
> > + iter函数：可以为序列对象自动创建迭代器包装，也可以为函数、方法等可调用类型(callable)进行迭代器包装；
> >
> > ```python
> > x = lambda : input('n : ')		#可以被__next__调用，无参数
> > 
> > for i  in iter(x, 'end'):		#函数x 的返回值等于end时候结束迭代
> >     print(i)
> > 
> > #输出：
> > n : 1
> > 1
> > n : 2
> > 2
> > n : end
> > ```
> >
> > + next函数：用于手工迭代；
> >
> >   ```python
> >   x = iter([1, 2])
> >   while True:
> >       try:
> >           print(next(x))
> >       except StopIteration:
> >           break
> >   #输出：
> >   １
> >   ２
> >   ```
>
> **自动迭代**：也就是`for i in list0:`这种语句实现的

> **生成器**：
>
> + 生成器是迭代器的进化版本，使用`函数和表达式`替换接口方法，简化编码过程，提供更多控制能力。
>
> + ++内部以`yield`返回迭代数据++
> + 执行时：执行到yield指令时，设置好返回值后，解释器会*保存线程状态，挂起当前函数流程*,只有当再次调用`__next__`方法，才会恢复状态，继续执行，以yield为切换分界线，往复交替，直到函数结束。
>
> + 生成器无论内部逻辑如何，函数总是返回生成器对象，然后，以普通迭代器方式继续操作；
>
> + 每条yield语句对应一次`__next__`调用，可以分列多条，或者出现在循环语句中，*只要结束函数流程*，相当于抛出StopIteration异常。
>
>   ```python
>   def test():
>       for i in range(10):
>           yield i + 100
>           if i >= 1:
>               return		#返回生成器对象，以普通迭代方式操作，函数结束，抛出异常迭代终止
>   x = test()
>   print(next(x))
>   next(x)
>   next(x)
>   ```
>
>   
>
> + 子迭代器：如果数据本身就是可迭代对象，那么可以使用`yield from`子迭代器语句，它和在for循环中使用yield没有差别，更加简洁；
>
>   ```python
>   def test():
>       yield from 'ab'		#也就类似于for循环中，循环2次，两句yield
>       yield from range(3)
>       
>   for o in test():
>       print(o)
>   ```
>
> + **生成器表达式**：可以用作函数调用参数
>
>   ```python
>   x = (i + 100 for i in range(8) if i % 2 == 0)
>   #理解：生成器表达式做参数，先print x只输出了这个表达式，再for i in gen,print i
>   def test(x):
>       print(x)
>       for i in x: print(i)
>   test(i for i in range(3))
>   ```
>
> + 生成器的方法：不仅是数据提供方，还可以作为接收方。生成器也能在外部停止迭代。
>
>   + send方法：可向yield传递数据，其他和next一样；在send之前，必须确保生成器已经启动；
>
>   + close方法： 解释器会终止生成器的迭代；
>
>   + throw方法： 使用throw方法还可以向生成器指定异常作为信号
>
>     ```python
>     def test():
>         for i in range(10):
>             try:
>                 yield i
>             finally:
>                 print('finally')
>     x = test()
>     next(x)
>     next(x)
>     x.close()
>     next(x)
>     
>     # 使用throw方法还可以向生成器指定异常作为信号
>     class ExitException(Exception): pass
>     class ResetException(Exception): pass
>     def test():
>         while True:
>             try:
>                 v = yield
>                 print(f'v   {v}')
>             except ResetException:
>                 print('reset')
>             except ExitException:
>                 print('exit')
>                 return
>             
>     x = test()
>     x.send(None)
>     x.throw(ResetException)
>     x.send(1)
>     x.throw(ExitException)
>     x.send(2)
>     ```
>
> + 模式：
>
>   1. 生产消费模型：在不借助并发框架时，实现生产、消费协作
>
>   > 消费者启动之后，通过yield将执行权限交给生产者，等待生产者发送数据
>   >
>   > ```python
>   > def consumer():
>   >     while True:
>   >         v = yield
>   >         print(f'consumer:  {v}')
>   > def producer(c):
>   >     for i in range(10, 13):
>   >         c.send(i)
>   >         
>   > c = consumer()
>   > c.send(None)
>   > producer(c)
>   > c.close()
>   > ```
>
>   2. 消除回调：回调使代码碎片化，使用生成器可以消除回调
>
>   > ```python
>   > def target(request, callback):
>   >     s = time.time()
>   >     request()
>   >     time.sleep(2)
>   >     callback(f'done: {time.time() - s}')
>   >     
>   > def service(request, callback):
>   >     threading.Thread(target = target, args = (request, callback)).start()
>   > def request():
>   >     print("start")
>   > def callback(x):
>   >     print(x)
>   >     
>   > service(request, callback)
>   > ```
>   >
>   > 

## 五、类

函数具有单一入口和出口，可以完成一次计算。但是类有不同的方法，方法的调用顺序不同，输出结果就不同。

如果class在模块中，那它的生命周期和模块一样；如果class在函数中，那么每次调用函数都新建一个class，这些class不是同一个。

> 类存在两种关系：继承(自某个族类)——–组合(哪些部件)
>
> 类擅长对有持续状态、生命周期、遗传特性的物体进行抽象模拟；
>
> 元类，用于创建自定义的类型对象，继承自：
>
> `函数内定义的类型`对象，会在所有的类的实例死亡后，被回收。若是`模块中的类型`，生命周期与模块一致；

+ 类字段和实例字段，名字空间：

```python
class A:
    a = 100			#类字段
    
    def __init__(self, x):	#实例初始化
        self.x = x		#实例字段
        
    def get_x(self):	#实例方法
        return self.x
    
 class B(A):		#继承自A
    b = 'hello'
    
    def __init__(self, x, y):
        super().__init__(x)		#调用了父类的初始化方法
        self.y = y
    def get_y(self):
        return self.y

#实例会存储所有继承层次的实例字段，成为它的私有特征    
o = B(1,2)
print(o.a)
print(o.b)
print(o.get_y())
```

+ 祖先类的新增功能可以直接`广播`到所有的后代
+ 继承层次不同的名字空间中允许出现同名成员，按顺序优先命中；成员的查找规则不是LEGB，而是基于继承体系；

```python
x = 100
class A:
    def __init__(self, x):
        self.x = x
    def test(self):
        print(x)		#LEGB,指向x=100,class内部以函数方式运行
        print(self.x)	#指定self搜索目标
o = A('abc')
o.test()
#100
#abc
```

+ 类型字段在class中直接定义，实例字段比系统给实例引用self赋值定义

+ 字段赋值：类型字段赋值：`X.a = 100`；实例字段赋值：`o = X()  o.b = 200`

+ 修改实例字段不会影响类型字段的值，即使同名；

+ 私有字段：按`__name`方式命名，而`__init__或__hash__`是系统‘方法’，私有字段这种命名会使编译器给它加上类型前缀，导致用户访问变成`_X__name`，不容易产生危险，同时，会导致继承类型不能访问重命名后的基类成员，可以将`__table`改成`_table`，就不会自动重命名了；

+ **属性：**property，实现将 读写删除 操作映射到指定的方法调用上，实现操作控制；另外，属性的优先级比同名的实例字段高；

+ ```python
  class X:
      def __init__(self, name):
          self.__name = name
      @property
      def name(self):
          return self.__name
      
      @name.setter
      '''
      '''
      @name.deleter
      '''
      要求：多个方法名一样，从@property处读开始，然后以属性名定义写和删除操作
      '''
  ```

+ **方法：**实例方法与实例对象绑定，使用时无需显式传入第一实参self；类型方法：用来向族群维护和提供接口，第一实参是cls，需要指定装饰器`@classmethod`；静态方法：不接收实例引用，也不参与类型处理，不需要自动传入第一参数(就相当于一个普通的函数)，装饰器`@staticmethod`；这些方法都不能重名；

+ **继承：**`class B(A)`使用`B.__bases__`返回基类，`A.__subclasses__`返回子类

+ 初始化: 如果子类中没有新的构造参数，则没必要创建`__init__`，所以，需要在子类中显式调用基类的方法；可以使用`super().__init__(x)`返回基类代理

+ 覆盖:在搜索优先级更高的名字空间中定义同名方法即可；但是覆盖要注意不能改变参数和返回值的类型，否则会影响原有的调用代码；

+ **只有属性才能出现同名函数，别的不行**

+ 抽象类：表示部分完成，且不能实例化的类型；从抽象类继承，必须实现所有层级的未被实现的抽象方法。

+ 运算符重载：`__call__`让对象可以向函数那样调用

## 六、异常

```python
#顺序
try:
    pass
except:
    pass
else:
    pass(未发生异常，执行这一句)
finally:
    pass(是否发生异常都要执行这个)

#else的另一个用法
while:
    pass
else:
    pass #当while的循环顺利执行完毕，包括是continue，则可以执行这句else

#assert
#assert的异常参数，其实就是在断言表达式后添加字符串信息，用来解释断言并更好的知道是哪里出了问题。
assert 2==1,'2不等于1'
```



## 七、元编程 

> 元编程将程序当成数据，火灾运行期间完成编译期的工作。

+ **装饰器**：加个包装，`add = log(add)`

> 装饰器可以嵌套使用：`test = a(b(test))`
>
> 装饰器可以添加参数：`@log('demo')	def test: pass`====>`decorator = log('demo')  test = decorator(test)`
>
> 装饰器也可以用于类型

+ **描述符：**数据描述符定义了`__set__`和`__delete__`方法，如果只有`__get__`方法，则是非数据描述符；数据描述符的优先级高于实例名字空间的同名成员。属性(property)就是数据描述符，所以优先级高。
+ 静态类：阻止类型创建实例对象；
+ 密封类：阻止类型被继承；

## 待补充下卷：并发、异步编程、线程、进程、协程、序列化

> 将对象转换为可通过网络传输或可以存储到本地磁盘的数据格式（如：XML、JSON或特定格式的字节串）的过程称为序列化；反之，则称为反序列化。