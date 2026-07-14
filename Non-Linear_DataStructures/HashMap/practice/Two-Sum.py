'''
Start
    input รับค่าเป็น list ของ number

'''

class Solution:
    def two_sum(self, list_number, target):
        storage = {}
        for index,number in enumerate(list_number):
            if target - number in storage:
                return [index, storage[target - number]]

            storage[number] = index

newSolution = Solution()
print(newSolution.two_sum([2, 4, 10, 5], 4))