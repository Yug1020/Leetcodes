# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head.next is None:
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

        # print("odd =", odd, "mid =", mid, "count =", count)

        temp = head
        count = 0
        while temp:
            if count < mid:
                stack.append(temp.val)
            # print("stack", stack)

            if count == mid:
                if odd == True:
                    # print("worked")
                    temp = temp.next

            # print("count =", count)
            # print("temp =", temp.val)

            if count >= mid:
                if len(stack) > 0 and temp.val == stack[len(stack) - 1]:
                    # 
                    ("temp =", temp.val, "stack[len] =", stack[len(stack) - 1])
                    stack.pop()
                else:
                    # print("temp =", temp.val, "stack[len] =", stack[len(stack) - 1])
                    return False

            temp = temp.next
            count += 1
            # print("")

        return True