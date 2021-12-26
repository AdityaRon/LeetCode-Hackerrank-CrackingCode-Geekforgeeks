class Solution:
    def countPoints(self, rings: str) -> int:
        self.rings = rings
        colors = []
        rods = []
        results = defaultdict(list)
        count = 0
        for i in rings:
            if i == 'B' or i == 'R' or i == 'G':
                colors.append(i)
            else:
                rods.append(i)
        for i,j in zip(rods, colors):
            results[i].append(j)
        for i,j in results.items():
            if len(set(j)) >= 3:
                count+=1
        return count
