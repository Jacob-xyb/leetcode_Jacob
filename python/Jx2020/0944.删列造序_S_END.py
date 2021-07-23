"""题目说明"""
'''
给定由 N 个小写字母字符串组成的数组 A，其中每个字符串长度相等。
你需要选出一组要删掉的列 D，对 A 执行删除操作，使 A 中剩余的每一列都是 非降序 排列的，然后请你返回 D.length 的最小可能值。
删除操作的定义是：选出一组要删掉的列，删去 A 中对应列中的所有字符，形式上，
    第 n 列为 [A[0][n], A[1][n], ..., A[A.length-1][n]]）。（可以参见 删除操作范例）
'''

"""示例"""
'''
输入：["cba", "daf", "ghi"]
输出：1
解释：
当选择 D = {1}，删除后 A 的列为：["c","d","g"] 和 ["a","f","i"]，均为非降序排列。
若选择 D = {}，那么 A 的列 ["b","a","h"] 就不是非降序排列了。
'''

"""解题思路"""
'''
v1.0:
- 用栈的思想解决，就是入栈之前比较的问题，然后发现实际上只需要运用思想，而不需要用到栈的数据类型。(比较简单)
v1.1:
- 官方解答，感觉思路和我相同，但是代码写的很高级。
'''


class Solution:
    def minDeletionSize(self, A: list) -> int:
        # word = 'abcdefghijklmnopqrstuvwxyz'  # 字母是可以直接比较的，用不到index
        D = 0
        for col in range(len(A[0])):
            #     Stack = []  # 每列都用一个空栈来做分析
            #     # 突然发现不用建站栈。。
            for row in range(len(A)-1):  # 非降序的意思居然是不能出现任何降序，那不就是结果都要是升序的吗？？
                if A[row][col] > A[row+1][col]:
                    D += 1
                    break
        return D

class Solution_v1_1(object):
    def minDeletionSize(self, A):
        ans = 0
        for col in zip(*A):
            if any(col[i] > col[i+1] for i in range(len(col) - 1)):
                ans += 1
        return ans
