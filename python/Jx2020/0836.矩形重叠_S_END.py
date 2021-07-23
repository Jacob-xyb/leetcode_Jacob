"""题目说明"""
'''
矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
矩形的上下边平行于 x 轴，左右边平行于 y 轴。
如果相交的面积为 正 ，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
给出两个矩形 rec1 和 rec2 。如果它们重叠，返回 true；否则，返回 false 。
'''

"""示例"""
'''
输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true
'''

"""解题思路"""
'''
v1.0 
- 排除False的情况，大致分为四种
- 发现输入的矩阵还可以是线性的，那就也排除掉它！
> 双评都不高，但是思路挺简单的
v1.1(官方解答)
- 采用投影的方法，将矩形投影到x,y坐标轴上 
'''


class Solution:
    def isRectangleOverlap(self, rec1: list, rec2: list) -> bool:
        if rec2[2] <= rec1[0] or rec2[3] <= rec1[1] or \
                rec1[2] <= rec2[0] or rec1[3] <= rec2[1]:
            return False
        else:
            for i in range(2):
                if rec1[i] == rec1[i + 2] or rec2[i] == rec2[i + 2]:
                    return False
            return True

class Solution_v1_1:
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):    # 判断两投影线段是否有交集
            return min(p_right, q_right) > max(p_left, q_left)
        def is_rec(rec1, rec2):
            for i in range(2):
                if rec1[i] != rec1[i + 2] or rec2[i] != rec2[i + 2]:
                    return True
            return False
        return is_rec(rec1, rec2) and \
            ((intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3])))
