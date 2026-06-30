# Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
# Answers within 10-5 of the actual value will be accepted as correct.
# 12pm 0618-2026 issues with 6hour 5minute expected 152.50
# https://leetcode.com/problems/angle-between-hands-of-a-clock/?envType=daily-question&envId=2026-06-18

#0619-2026 FIGHTING!
#          105/105 test passed per leetcode.com ; 
#          Memory beats 45.34%
#          Runtime beats 100.00% 

class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        minute_hand_number = minutes/5
        minute_hand_arc= float(abs(hour-minute_hand_number)*30)
        hour_hand_arc = (float(minutes)/2) 
        if hour > minute_hand_number and hour != 12:
            angle = (minute_hand_arc) + hour_hand_arc
        else: 
            if hour ==12:
                angle = (minute_hand_arc) + hour_hand_arc
            else:
                angle = (minute_hand_arc) - hour_hand_arc
        if angle == 360:
            angle=0
        if angle > 180:
            angle -=360
        return abs(angle)
       
        
        
       

my_object = Solution()
print(my_object.angleClock(6,5))
print(my_object.angleClock(12,30))
print(my_object.angleClock(3,30))
print(my_object.angleClock(3,15))
print(my_object.angleClock(1,57))
print(my_object.angleClock(12,1)) #5.5
print(my_object.angleClock(12,36)) # ❌ 12:36 should return 162 not 126