"""题目说明"""
'''
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
如果不能形成任何面积不为零的三角形，返回 0。
'''

"""### 解题思路"""
'''
v1.0
- 首先思考如何确定一个三角形
任意两边之和大于第三边，任意两边只差小于第三边。
- OK，题目需要输出周长最大的三角形，很自然的要将数组A排序。排序后的数组A，我们肯定是喜欢直接输出最后三个数，那我们直接研究最后三个数就好了~
1. 假设最后三个数是a,b,c;那么 a<=b<=c;
2. 三角形定理的第一个条件只需要保证最小的两个数a+b>c即可；
3. 三角形定理的第二个条件只需要保证非最小边的差c-b<a即可；
4. 同时满足上述两个条件即可输出最大周长。
- 后面的判定范围就不多叙述了
https://github.com/Jacob-xyb/leetcode
'''
'''
v1.1
### 解题思路
- 首先思考如何确定一个三角形
任意两边之和大于第三边，任意两边只差小于第三边。
- OK，题目需要输出周长最大的三角形，很自然的要将数组A排序。排序后的数组A，我们肯定是喜欢直接输出最后三个数，那我们直接研究最后三个数就好了~
1. 假设最后三个数是a,b,c;那么 a<=b<=c;
2. 三角形定理的第一个条件只需要保证最小的两个数a+b>c即可；
`*3. 三角形定理的第二个条件只需要保证非最小边的差c-b<a即可；*` 这与2相同耶！！
3.所以a<=b<=c情况下，三角形成立的充分必要条件就是 a+b>c；
4. 同时满足上述两个条件即可输出最大周长。
- 后面的判定范围就不多叙述了
[我的github-leetcode](https://github.com/Jacob-xyb/leetcode)
'''
'''
v1.2
反向排序，可以不用循环，直接遍历退出。
'''
class Solution:
    def largestPerimeter(self, A: list) -> int:
        A.sort()
        while len(A) >= 3:
            B = A[-3:]
            if B[0]+B[1] > B[2] and B[2]-B[1] < B[0]:
                return sum(B)
            else:
                A.pop()
        return 0

class Solution_v1_1:
    def largestPerimeter(self, A: list) -> int:
        A.sort()
        while len(A) >= 3:
            B = A[-3:]
            if B[0]+B[1] > B[2]:
                return sum(B)
            else:
                A.pop()
        return 0

class Solution_v1_2:
    def largestPerimeter(self, A:list) -> int:
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i] < A[i+1]+A[i+2]:
                return A[i]+A[i+1]+A[i+2]
        return 0


print(Solution_v1_2().largestPerimeter([2,1,2]))
