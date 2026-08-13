class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result = []
        output = []
        
        def heap_insert(num):
            if len(result) == 0:
                result.append(num)
            else:
                result.append(num)
                child_index = len(result) - 1
                while child_index > 0:
                    parent_index = (child_index - 1) // 2
                    if result[parent_index] > result[child_index]:
                        result[parent_index], result[child_index] = result[child_index], result[parent_index] 

                        child_index = parent_index
                    else:
                        break
                    

        def sink_down(index):
            
            while True:
                min_index = index

                left_index = (index * 2) + 1
                right_index = (index * 2) + 2

                if left_index < len(result) and result[left_index] < result[min_index]:
                    min_index = left_index
                if right_index < len(result) and result[right_index] < result[min_index]:
                    min_index = right_index
                if min_index != index:
                    result[index], result[min_index] = result[min_index], result[index]
                    index = min_index
                else:
                    return 


        def heap_remove():
            if len(result) == 0:
                return
            if len(result) == 1:
                return result.pop()
            temp = result[0]
            result[0] = result.pop()
            sink_down(0)
            return temp

        for i in range(len(nums)):
            heap_insert(nums[i])
            
        for i in range(len(result)):
            output.append(heap_remove())

        return output