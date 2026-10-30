# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None or head.next is None:
            return True

        stack = []
        odd = False

        temp = head
        count = 0

        while temp:
            count += 1
            temp = temp.next
        
        if count % 2 != 0:
            odd = True
        
        mid = count // 2

        temp = head
        count = 0
        while temp:
            if count < mid:
                stack.append(temp.val)

            if count == mid:
                if odd == True:
                    temp = temp.next


            if count >= mid:
                if len(stack) > 0 and temp.val == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False

            temp = temp.next
            count += 1

        return True