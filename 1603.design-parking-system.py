#
# @lc app=leetcode id=1603 lang=python3
#
# [1603] Design Parking System
#

# @lc code=start
BIG = 1
MEDIUM = 2
SMALL = 3

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = {
            BIG: [],
            MEDIUM: [],
            SMALL: []
        }
        self.limit = {
            BIG: big,
            MEDIUM: medium,
            SMALL: small
        }

    def addCar(self, carType: int) -> bool:
        if carType == BIG and len(self.slots[BIG])>=self.limit[BIG]:
            return False
        if carType == MEDIUM and len(self.slots[MEDIUM])>=self.limit[MEDIUM]:
            return False
        if carType == SMALL and len(self.slots[SMALL])>=self.limit[SMALL]:
            return False
        # add car
        self.slots[carType].append(1)
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end

