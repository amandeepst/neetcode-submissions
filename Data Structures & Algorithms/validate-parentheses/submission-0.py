class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = { ")" : "(", "}" : "{", "]" : "["}
        for c in s:
            if c in d:
                if stk and stk[-1] == d[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return True if not stk else False



        


        