"""981. Time Based Key-Value Store

https://leetcode.com/problems/time-based-key-value-store/
"""


class TimeMap:

    def __init__(self):
        self.timeHistoryMap = {}
        self.keyMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyMap:
            keyTimeMap = {}
            keyTimeMap[timestamp] = value
            self.keyMap[key] = keyTimeMap
        else:
            keyTimeMap = self.keyMap[key]
            keyTimeMap[timestamp] = value

        if key not in self.timeHistoryMap:
            self.timeHistoryMap[key] = [timestamp]
        else:
            self.timeHistoryMap[key].append(timestamp)
            self.timeHistoryMap[key].sort()

    def get(self, key: str, timestamp: int) -> str:
        timeHistory = self.timeHistoryMap.get(key, -1)

        if timeHistory == -1: return ""

        targetTime = None
        l, r = 0, len(timeHistory) - 1
        while l <= r:
            m = l + (r - l) // 2
            if timeHistory[m] == timestamp:
                targetTime = timestamp
                break
            elif timeHistory[m] < timestamp:
                # move on to the right half
                targetTime = timeHistory[m]
                l = m + 1
            else:
                # move on to the left half
                r = m - 1

        if targetTime is None: return ""

        keyTimeMap = self.keyMap[key]
        return keyTimeMap[targetTime]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
