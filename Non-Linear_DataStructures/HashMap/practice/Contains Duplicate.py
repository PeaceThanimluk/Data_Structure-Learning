'''
Start
    รับค่าเป็นlist ที่เก็บตัวเลข
    สร้าง dictionary ไว้เก็บเลขที่มีแล้ว value เป็น True
    ถ้าเลขนั้นมีอยู่แล้ว return true
'''

class Solution:
    def contains_duplicate(self,nums):
        nums_storage = {}

        for number in nums:
            number_str = str(number)

            if number_str in nums_storage:
                return True
            else:
                nums_storage[number_str] = True
            
        return False




Solution1 = Solution()
print(Solution1.contains_duplicate([1, 2, 3, 1]))
print(Solution1.contains_duplicate([1, 2, 3, 4]))