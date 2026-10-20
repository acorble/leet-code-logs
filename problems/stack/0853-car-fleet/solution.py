"""853. Car Fleet

https://leetcode.com/problems/car-fleet/
"""


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        timeToReachStack = []

        zipped = sorted(zip(position, speed))

        for position, speed in zipped:
            # calculate each time to reach target of each car
            timeToReach = (target - position) / speed

            timeToReachStack.append(timeToReach)

        ans = 0
        lastMax = 0

        while timeToReachStack:
            time = timeToReachStack.pop()

            if lastMax < time:
                ans += 1
                lastMax = time

        return ans
