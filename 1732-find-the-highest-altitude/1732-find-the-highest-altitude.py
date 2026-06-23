class Solution(object):
    def largestAltitude(self, gain):
        size=len(gain)
        current=0
        highest=0
        for i in range(size):
            current+=gain[i]
            highest=max(highest,current)
        return highest
            
        

        