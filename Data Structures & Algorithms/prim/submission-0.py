import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst , wt in edges:
            adj[src].append([dst, wt])
            adj[dst].append([src, wt])
        
        minHeap = []
        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, neighbor])

        mst = []
        visit = set()
        visit.add(0)
        res = 0
        while minHeap and len(visit) < n:
            weight, n1 , n2 =heapq.heappop(minHeap)
            if n2 in visit:
                continue
            
            res += weight
            mst.append([n1, n2])
            visit.add(n2)
            for neighbor , weight in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, n2, neighbor])
        
        return res if len(visit) == n else -1