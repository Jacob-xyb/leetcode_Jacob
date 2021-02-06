from typing import List
"""题目描述"""
'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
'''

"""示例"""
'''
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
'''

"""解题思路"""
'''
v1.0:
- 画了很多时间最后放弃优化了，204ms，深深感到自己有多菜。（下面看看大佬们的代码）
v1.1:
- 标答：回朔算法
v1.2:
- 根据官方解答，v1.0的改版。需要注意的是加入到`resArray`后需要return，不然会因为`#直接跳过`而重复添加。
- 对于这类寻找所有可行解的题，我们都可以尝试用「搜索回溯」的方法来解决。
    回到本题，我们定义递归函数 dfs(target, combine, idx) 表示当前在 candidates 数组的第 idx 位，
    还剩 target 要组合，已经组合的列表为 combine。递归的终止条件为 target <= 0 或者 candidates 数组被全部用完。
    那么在当前的函数中，每次我们可以选择跳过不用第 idx 个数，即执行 dfs(target, combine, idx + 1)。
    也可以选择使用第 idx 个数，
    即执行 dfs(target - candidates[idx], combine, idx)，注意到每个数字可以被无限制重复选取，因此搜索的下标仍为 idx。
v1.3:
- 最效率范例
- 相当简洁明了
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        resArray=[]
        def findArray(condidates,tar,a=[]):
            for i in [c for c in candidates if c <= tar]:
                a.append(i)
                if tar-i == 0 and a == sorted(a):
                    resArray.append(a[:])
                else:
                    findArray(candidates,tar-i,a)
                a.pop()
        findArray(candidates,target)
        return resArray

class Solution_v1_1:
    def combinationSum(self, candidates, target):
        ans = []
        temp = []
        def recursion(idx, res):
            if idx >= len(candidates) or res >= target:
                if res == target:
                    ans.append(temp[:])
                return
            temp.append(candidates[idx])
            recursion(idx, res + candidates[idx])
            temp.pop()
            recursion(idx + 1, res)
        recursion(0, 0)
        return ans

class Solution_v1_2:
    def combinationSum(self, candidates, target):
        resArray=[]
        n = len(candidates)
        def findArray(idx, target, a=[]):
            if idx == n:
                return
            if target == 0:
                resArray.append(a[:])
                return
            # 直接跳过
            findArray(idx+1, target, a)
            # 选择当前
            if target-candidates[idx] >=0:  # 剪枝
                a.append(candidates[idx])
                findArray(idx, target-candidates[idx], a)
                a.pop()

        findArray(0, target)
        return resArray


class Solution_v1_3:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        t = []
        res = []
        n = len(candidates)

        def func(i, target):
            # if target < 0:
            #     return
            # if target == 0:
            #     res.append(t.copy())
            #     return

            for j in range(i, n):
                c = candidates[j]

                if c > target:
                    return
                if c == target:
                    t.append(c)
                    res.append(t.copy())
                    t.pop()
                    return

                t.append(c)
                func(j, target - c)
                t.pop()

        func(0, target)
        return res