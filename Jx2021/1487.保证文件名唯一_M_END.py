"""题目描述"""
'''
给你一个长度为 n 的字符串数组 names 。你将会在文件系统中创建 n 个文件夹：在第 i 分钟，新建名为 names[i] 的文件夹。
由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，
        系统会以 (k) 的形式为新文件夹的文件名添加后缀，其中 k 是能保证文件名唯一的 最小正整数 。
返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的实际名称。
'''

"""示例"""
'''
输入：names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
输出：["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]

输入：names = ["kaido","kaido(1)","kaido","kaido(1)"]
输出：["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
'''

"""解题思路"""
'''
v1.0:
- 比较简单，遍历出现的次数，但是超时
v1.1:
- 在v1.0基础上改进，每次记录最大值，减少前面的重复次数。
v1.2:
- 最快范例，似乎思路相同，但是代码极其简洁。
'''


class Solution:
    def getFolderNames(self, names: list) -> list:
        from collections import defaultdict
        ans = []
        black = defaultdict(int)
        for i in names:
            if black[i]:
                k = 1
                temp = i + "(" + str(k) + ")"
                while black[temp]:
                    k += 1
                    temp = i + "(" + str(k) + ")"
                ans.append(temp)
                black[temp] = 1
            else:
                ans.append(i)
                black[i] += 1
        return ans


class Solution_v1_1:
    def getFolderNames(self, names: list) -> list:
        from collections import defaultdict
        ans = []
        black = defaultdict(int)
        for i in names:
            if black[i]:
                k = black[i]
                temp = i + "(" + str(k) + ")"
                while black[temp]:
                    k += 1
                    temp = i + "(" + str(k) + ")"
                ans.append(temp)
                black[temp] = 1
                black[i] = k + 1
            else:
                ans.append(i)
                black[i] += 1
        return ans

class Solution_v1_2:
    def getFolderNames(self, names: list) -> list:
        created, nMap = [], {}
        for name in names:
            n = name
            while n in nMap:
                n = f'{name}({nMap[name]})'
                nMap[name] += 1
            created.append(n)
            nMap[n] = 1
        return created


