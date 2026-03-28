# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# case 1
# head = [2,1,5]

# case 2
# head = [2,7,4,3,5]

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        current_number = head.val
        next_number = head.next
        array_of_larger = [0]
        if next_number == None:
            return array_of_larger
        def loopOnDemand(value, next_value):
            if next_number > current_number:
                array_of_larger.append(next_number)
            else:
                next_number = next_number.next
                loopOnDemand(current_number, next_number)
        while next_number != None:
            loopOnDemand(current_number, next_number)
            current_number = next_number
            next_number = next_number.next
        array_of_larger.append(0)
        return array_of_larger
        
