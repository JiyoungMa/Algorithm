class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        answer = (end-start) * min(height[end], height[start])

        while(start + 1 < end):
            tempResultStart = (end - start - 1) * min(height[end], height[start+1])
            tempResultEnd = (end - start - 1) * min(height[end-1], height[start])

            if tempResultEnd>=answer and tempResultStart>=answer:
                if tempResultEnd>tempResultStart:
                    end -= 1
                    answer = tempResultEnd
                else:
                    start += 1
                    answer = tempResultStart
                continue
                
            elif tempResultEnd>=answer:
                end -= 1
                answer = tempResultEnd
                continue
                
            elif tempResultStart>=answer:
                start += 1
                answer = tempResultStart
                continue

            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return answer
