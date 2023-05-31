#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
from collections import defaultdict
class Records:
    def __init__(self):
        self.recordCount = 0
        self.totalTime = 0
    def addRecord(self, t):
        self.totalTime += t
        self.recordCount += 1
    def getAvg(self):
        if self.recordCount==0: return 0
        return self.totalTime/self.recordCount

class UndergroundSystem:

    def __init__(self):
        # create a database (dictionary), indexed by id, the value is (startStation, startAt)
        self.checkins = {}
        # create a history record database, indexed by startStation, the value is another default dict
        # the value of inside dict is (total time, record count)
        self.records = defaultdict(lambda: defaultdict(Records))
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # if (self.checkins.get(id)){}
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # push a record into history db
        # get startStation
        startStation, startAt = self.checkins[id]
        self.records[startStation][stationName].addRecord(t-startAt)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.records[startStation][endStation].getAvg()
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

