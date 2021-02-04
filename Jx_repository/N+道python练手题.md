# 100道python练手题

- [原始链接](https://github.com/RichardFu123/Python100Cases)

- 以下是本人重写版：

## 实例001：数字组合

**题目：**有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

**程序分析：**遍历全部可能，把有重复的剃掉。


```python
import math


def num_combine(num):
    total = math.factorial(num)
    res = []
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            for k in range(1, num + 1):
                if ((i != j) and (j != k) and (k != i)):
                    res.append((i, j, k))

    return total, res


print(num_combine(4)[0])
```

    24
    

**简便方法：**用itertools中的permutations即可。


```python
def num_combine(num):
    import itertools
    nlist = [i for i in range(1,num+1)]
    res = []
    count = 0
    total = itertools.permutations(nlist, 3)
    for i in total:
        res.append(i)
        count += 1
    return count, res

print(num_combine(4)[0])
```

    24
    

## 实例002：“个税计算”

**题目：**企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

**程序分析：**分区间计算即可。

- 感觉题目出的别扭，利润越高，提成越低。


```python
profit=int(input('Show me the money: '))
bonus=0
thresholds=[10*10**4,10*10**4,20*10**4,20*10**4,40*10**4]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
    if profit<=thresholds[i]:
        bonus+=profit*rates[i]
        profit=0
        break
    else:
        bonus+=thresholds[i]*rates[i]
        profit-=thresholds[i]
bonus+=profit*rates[-1]
print(bonus)
```

    Show me the money: 200000
    17500.0
    

## 实例003：完全平方数

**题目：**一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

__程序分析：设该数为x，第一个完全平方数为m,第二个完全平方数为n，即:__ ```m**2=x+100 and n**2=x+268```

- 我没看懂原链接的代码...（我太菜了吧）


```python
n = 0
while n < 10000:
    if (n+100)**0.5 == int((n+100)**0.5) \
    and (n+268)**0.5 == int((n+268)**0.5):
        break
    n += 1
print(n)
```

    21
    

## 实例004：这天第几天

**题目：**输入某年某月某日，判断这一天是这一年的第几天？

**程序分析：**特殊情况，闰年时需考虑二月多加一天：


```python
date = input("请输入：年-月-日(请用\"-\"隔开)\n您的出生年月日是:")
```

    请输入：年-月-日(请用"-"隔开)
    您的出生年月日是:1995-08-28
    
