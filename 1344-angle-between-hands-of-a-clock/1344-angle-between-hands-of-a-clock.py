class Solution(object):
    def angleClock(self, hour, minutes):
        minuteangle=6*minutes
        hourangle=30*(hour%12)+0.5*minutes
        diff=abs(hourangle-minuteangle)
        return min(diff,360-diff)

        
        