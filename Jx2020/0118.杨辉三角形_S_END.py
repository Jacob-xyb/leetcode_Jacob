"""题目说明"""
'''给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。'''

"""示例"""
'''
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

"""解题思路"""
'''
v1.0:
- 就是直接暴力的解法，先用i标记是哪一行，再用j处理这一行的内容。
'''
class Solution:
    def generate(self, numRows: int) -> list:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            resList = [[1], [1, 1]]
            for i in range(numRows-2):  # 进入某一行
                addList = [1]
                for j in range(i+1):  # 计算某一行
                    nums = resList[i+1][j]+resList[i+1][j+1]
                    addList.append(nums)
                addList.append(1)
                resList.append(addList)
            return resList

if __name__ == '__main__':
    print(Solution().generate(3))

