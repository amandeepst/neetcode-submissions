from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit_up = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit_up + lock[i+1:])
                digit_down = str((int(lock[i]) -1 + 10) % 10)
                res.append(lock[:i] + digit_down + lock[i+1:])
            return res
            

        vis = set(deadends)
        q = deque([("0000",0)])
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in vis:
                    vis.add(child)
                    q.append((child, turns +1))
        return -1




        