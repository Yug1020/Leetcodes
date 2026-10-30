# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
    
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
    
        mid = count // 2
    
        first_tail = head
        for _ in range(mid - 1):
            first_tail = first_tail.next
            
        second_head = first_tail.next
        
        first_tail.next = None
    
        prev = None
        curr = second_head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        reversed_second_head = prev
    
        temp1 = head
        temp2 = reversed_second_head
    
        while temp1:
            if temp1.val != temp2.val:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
    
        return True

# class Solution:
#     def isPalindrome(self, head: ListNode | None) -> bool:
#         if head is None or head.next is None:
#             return True

#         stack = []
#         odd = False

#         temp = head
#         count = 0

#         while temp:
#             count += 1
#             temp = temp.next
        
#         if count % 2 != 0:
#             odd = True
        
#         mid = count // 2

#         temp = head
#         count = 0
#         while temp:
#             if count < mid:
#                 stack.append(temp.val)

#             if count == mid:
#                 if odd == True:
#                     temp = temp.next


#             if count >= mid:
#                 if len(stack) > 0 and temp.val == stack[len(stack) - 1]:
#                     stack.pop()
#                 else:
#                     return False

#             temp = temp.next
#             count += 1

#         return True