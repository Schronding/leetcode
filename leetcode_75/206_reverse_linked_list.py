# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Test cases
head_0 = [1,2,3,4,5]
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)

# Expected output: [5,4,3,2,1]

class Solution:
    def reverseList(head: ListNode) -> ListNode:
        previous_pointer, current_pointer = None, head
        # As my linked list "flows" in only one direction, I need to make use of TWO, not one pointer, as when I break the link of one node in order to ...
        # ... reverse it I could potentially be losing the location that references the rest of the list. 
        # 'current_pointer' could be thought as the pivot that I will use to reverse the direction of the pointers. 
        # You could also think of it as a "center". By default, the center is pointing to only one direction, lets say it is either right or left (even ...
        # ... as this doesn't make sense inside the actual memory, as the values could be allocated anywhere; up, down, before or after; any 2D ...
        # ... combination of coordinates). When it is pointing to the right, he can't "see" what is on his left, so when we shift his attention to the ...
        # ... left, we lose sight of what was in the right. >>

        while current_pointer != None: 
            landmark = current_pointer.next
            # >> That is why we create a "landmark" of where the rest of the list is. 
            current_pointer.next = previous_pointer
            ## This step is the one that actually changes the attention (or the direction in which the arrow is pointing) from right to left. 
            ## This could be visualized as a rotation of 180 degrees from the center. 
            previous_pointer = current_pointer
            ### As the move has already been made, we shift our pointers one position to the right, as to continue reversing the direction of the pointers.
            ### 'previous_pointer' will always be behind of 'current_pointer' so to move, previous only has to move to the position of current. 
            current_pointer = landmark 
            ### But where does current move? To the position we saved; the one that included where is the rest of the list. 
            ### It would sound strange, but it is as if current walked backwards until he reached 'landmark'. 
            ### As 'landmark' is still pointing to the right, when we moved to that position 'current_pointer' stopped looking at the left and rather ...
            ### ... shifted to look at its right, why? Because current is just a pointer, not a value. When he moved to point at 'landmark' the behavior ...
            ### ... we get of 'landmark' is not the pointer, but 'landmark' itself. 
            ### That is why in subsequent iterations of the loop we are able to access the property '.next'. 

        return previous_pointer
        ## When there finally comes the moment in which we arrived at the "non-starting None", our while loop has ended, so current it is pointing at None. 
        ## We return 'previous_pointer' because that is the last element before the "non-starting None", therefore, as everything is reversed, that means ...
        ## ... that is our new beginning; 'previous_pointer' is the head of the new linked list. 
        

        