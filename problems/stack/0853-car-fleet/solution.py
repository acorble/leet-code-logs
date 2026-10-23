"""853. Car Fleet

https://leetcode.com/problems/car-fleet/
"""


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # sort position and speed in ascending order of position
        merged = []
        for i in range(len(position)):
            merged.append((position[i], speed[i]))
        sortedMerged = sorted(merged)

        # compute the time to reach the target of every car
        time = []
        for entry in sortedMerged:
            time.append((target - entry[0]) / entry[1]) # distance / speed

        # count the number of car fleets
        ans = 1
        last = time.pop()
        while time:
            popped = time.pop()
            if last < popped:
                ans += 1
                last = popped

        return ans
