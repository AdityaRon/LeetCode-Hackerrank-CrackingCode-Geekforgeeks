class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.words = words
        self.order = order
        def compare(u: str, v: str) -> bool:
            for c, d in zip(u, v):
                if map[c] > map[d]:
                    return False   
                elif map[c] < map[d]:
                    return True
            return len(u) <= len(v)  
        map = {c : i for i, c in enumerate(order)}
        return all(compare(words[i - 1], words[i]) for i in range(1, len(words)))
