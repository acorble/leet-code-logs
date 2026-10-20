"""853. Car Fleet

https://leetcode.com/problems/car-fleet/
"""


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        timeToReachStack = []

        ans = 0

        for i in range(len(position)):
            # calculate each time to reach target of each car
            timeToReach = 0
            if (target - position[i]) % speed[i] == 0:
                timeToReach = (target - position[i]) // speed[i]
            else:
                timeToReach = (target - position[i]) // speed[i] + 1

            timeToReachStack.append(timeToReach)

        lastMax = 0

        while timeToReachStack:
            time = timeToReachStack.pop()

            if lastMax < time:
                ans += 1
                lastMax = time

        return ans
