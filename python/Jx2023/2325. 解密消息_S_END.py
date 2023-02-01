"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/2/1 11:28"
"""


# https://leetcode.cn/problems/decode-the-message/

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        text = key.replace(" ", "")
        table = {}
        chr_id = 0
        idx = 0
        while idx < len(text) and chr_id < 26:
            tmp = text[idx]
            if not table.get(tmp):
                table[tmp] = chr(97 + chr_id)
                chr_id += 1
            idx += 1
        res = ""
        for c in message:
            res += table.get(c, c)
        return res

    def decodeMessageV1_1(self, key: str, message: str) -> str:
        import string
        mp, it = {}, iter(string.ascii_lowercase)
        for c in key:
            if c != ' ' and c not in mp:
                mp[c] = next(it)
        return ''.join(mp.get(c, c) for c in message)


if __name__ == '__main__':
    key = "eljuxhpwnyrdgtqkviszcfmabo"
    message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
    print(Solution().decodeMessage(key, message))

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/2/1 13:30"
"""
