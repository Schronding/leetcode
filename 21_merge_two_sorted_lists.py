# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
head_0 = ListNode(1)
head_0.next = ListNode(2)
head_0.next.next = ListNode(4)
# list1 = [1,2,4]

head_1 = ListNode(1)
head_1.next = ListNode(3)
head_1.next.next = ListNode(4)
# list2 = [1,3,4]

# Expected output: [1,1,2,3,4,4]

# **Input:** 
head_2 = None
head_3 = None

# Expected Output: []

head_4 = None
head_5 = ListNode()

def printNodes(head):
    i = 0
    while head != None:
        print(f"{i} node: {head.val}")
        head = head.next
        i += 1
    print("\n")

def mergeTwoLists(list1, list2):
    if list1 == None:
        if list2 == None:
            return None
        else:
            return list2
    if list2 == None:
        if list1 == None:
            return None
        else:
            return list1
    option_one = True
    if list1.val <= list2.val:
        main = list1
        auxiliar = list2
    else:
        main = list2
        auxiliar = list1
        option_one = False
    bucket = 0
    while auxiliar != None:
        if main.next == None:
            diff_main = 100000
        else:
            diff_main = main.next.val - main.val
        diff_aux = auxiliar.val - main.val
        if diff_aux < diff_main:
            bucket = main.next
            main.next = auxiliar
            auxiliar = bucket
            main = main.next
        elif diff_aux >= diff_main:
            main = main.next
    if option_one:
        return list1
    else:
        return list2


printNodes(mergeTwoLists(head_0, head_1))
printNodes(mergeTwoLists(head_2, head_3))
printNodes(mergeTwoLists(head_4, head_5))