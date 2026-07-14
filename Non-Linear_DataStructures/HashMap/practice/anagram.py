'''
Start
    input รับ string มา2ค่่า string1 string2
    สร้าง dictionary ขึ้นมา string_storage
    loop ด้วย string len
    เพิ่มตัวอักษรแต่ละตัวเข้าไปใน string_storage value = 1
    เพิ่ม letter เช้า string2
    เช็คว่าทั้งสอง dict เท่ากันไหม
'''

class Solution:
    def anagram(self, string1, string2):
        string1_storage = {}
        string2_storage = {}

        if len(string1) != len(string2):
            return False

        #add letter to dictionary
        for word in string1:
            if not word in string1_storage:
                string1_storage[word] = 1
            else:
                string1_storage[word] += 1

        for word in string2:
            if not word in string2_storage:
                string2_storage[word] = 1
            else:
                string2_storage[word] += 1

        return string1_storage == string2_storage


newSolution = Solution()
print(newSolution.anagram("anagram", "nagaram"))