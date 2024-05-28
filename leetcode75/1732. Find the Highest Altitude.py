class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = gain[0]
        altitude = [0]
        altgain = 0
        for i in gain:
            altgain += i
            altitude.append(altgain)
        #     altgain += start
        #     altitude.append(altgain)
        #     start = i
        return max(altitude)
