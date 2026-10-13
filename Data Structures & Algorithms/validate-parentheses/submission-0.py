class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(',']':'[','}':'{'}
        stk = []

        for x in s:
            if x not in pair:
                stk.append(x)
            else:
                if stk and stk[-1] == pair[x]:
                    stk.pop()
                else:
                    return False

        return False if stk else True