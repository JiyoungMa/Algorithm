# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(-1)
        nowNode = answer
        prev = 0
        nowNode1 = l1
        nowNode2 = l2
        
        
        while True:
            if nowNode1 != None and nowNode2 != None:
                nowResult = nowNode1.val + nowNode2.val + prev
                prev = nowResult // 10
                
                nowNode.next = ListNode(nowResult%10)    
                nowNode = nowNode.next
                
                nowNode1 = nowNode1.next
                nowNode2 = nowNode2.next
            elif nowNode1 != None :
                nowResult = prev + nowNode1.val
                prev = nowResult // 10
                
                nowNode.next = ListNode(nowResult%10)    
                nowNode = nowNode.next
                
                nowNode1 = nowNode1.next
            elif nowNode2 != None:
                nowResult = prev + nowNode2.val
                prev = nowResult // 10
                
                nowNode.next = ListNode(nowResult%10)    
                nowNode = nowNode.next
                
                nowNode2 = nowNode2.next
            else:
                if prev > 0:
                    nowNode.next = ListNode(prev)    
                    nowNode = nowNode.next
                break
                
        return answer.next
