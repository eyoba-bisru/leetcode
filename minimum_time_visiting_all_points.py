from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(1, len(points)):
            p11 = points[i-1][0]
            p12 = points[i-1][1]
            p21 = points[i][0]
            p22 = points[i][1]

            d1 = abs(p11 - p21)
            d2 = abs(p12 - p22)

            if d1 > d2:
                count += d1
            else:
                count += d2
            
        
        return count
                

                    
                
        