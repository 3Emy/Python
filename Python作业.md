#### sys模块platform属性
可以帮助我们了解运行解释器的系统，**即电脑的系统**

```
import sys
sys.platform
```

#### sys模块print函数
可以帮助我们了解在运行的Python版本

```
print(sys.version)
```

#### getcwd函数
可以帮助我们知道代码所在的文件夹的名字

```
import os
os.getcwd()
```

#### environ属性
可以访问系统的全部变量

```
os.environ
```

#### getenv函数
可以单独访问某一环境变量

```
os.getenv
```

#### datetime模块date.today函数
可以帮助我们知道今天的日期。

```
import datetime
datetime.date.today()
```

**在date.today函数后追加日，月和年值可单独访问某一值**

```
datetime.date.today().day
datetime.date.today().month
datetime.date.today().year
```
#### 使用date.isoformat函数并加入今日日期，可以更好的方式显示日期，日期会由isoformat转换成字符串

```
datetime.date.isoformat(datetime.date.today())
```

#### 导入time模板，调用strftime函数可指定以什么方式显示时间。以24小时制为例。

```
import time
time.strftime("%H:%M")
```

**看星期几，和上午还是下午，可使用%A %p规范即可**

```
time.strftime("%A &p")
```

#### unescape函数可对HTML中麻烦的标记做编码，也可把一些编码的HTML恢复成原来形式,示例

```
import html
html.escape("This HTML fragment contains a <script>script</script> tag.")
```

以及

```
html.unescape("I &hearts; Python's &lt;standard library;.")
```

#### 冒号（：）引入一个必须向右缩进的代码组。如果忘记在冒号后引入缩进代码，解释器会报错。
**If语句结果为True或者是False，if是属于条件**
**else语句指示对应的if语句返回一个False值时要执行的代码块**
**elif是对应if语句中多个需要检查的条件**

```
from datetime import datetime
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 52, 53, 55, 57, 59,]
right_this_minute = datetime.today() .minute
if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute")
```

#### 迭代类似于多次循环更新的意思
##### for循环数字列表，迭代处理列表中的每一个数字，在屏幕上显示当前数字。

```
for i in [1, 2, 3]:
          print(i)
```

##### for迭代处理一个字符串，每次迭代时处理字符串中的一个字符。

```
for ch in "Hi!":
          print(ch)
```

##### 使用内置函数range可以指示for循环要运行多少次。

```
for num in range(5):
          print('Head First Rocks!')
```

#### random模块
random模块中的randint函数可以帮助查看文档并可以生成两个定值中的一个随机数。
#### time模块
time模块主要提供各种与时间相关的功能。
