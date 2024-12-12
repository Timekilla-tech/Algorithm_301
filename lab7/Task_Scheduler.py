class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for i in tasks:
            count[ord(i) - ord('A')]+=1
        count.sort()
        mx = count[25]
        idle = (mx - 1 ) * n
        for i in range(24,-1, -1):
            idle -= min(mx - 1, count[i])
        
        return len(tasks) + max(idle, 0)