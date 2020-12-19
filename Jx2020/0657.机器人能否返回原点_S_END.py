"""题目说明"""
'''
在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 (0, 0) 处结束。
移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。
如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。
注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。
'''

"""### 解题思路"""
'''
v1.0:
- 最基本的写法了，两个变量记录两个方向的位移，貌似效率很低。
v1.1:
- 官方解答：
- 不用列表的话内存占用一样，但是速度要快一点。
'''

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        judge = [0, 0]
        for i in range(len(moves)):
            if moves[i] == "R":
                judge[0] += 1
            elif moves[i] == "D":
                judge[1] += 1
            elif moves[i] == "L":
                judge[0] -= 1
            elif moves[i] == "U":
                judge[1] -= 1
        return judge == [0, 0]

class Solution_v1_1:
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L':  x -= 1
            elif move == 'R':  x += 1
        return x == y == 0
