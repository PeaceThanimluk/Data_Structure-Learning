'''
Start
    รับค่าเป็น list
    สร้าง dictionary เอาไว้เก็บคำที่พบแล้ว เช่น orange: 1
    ถ้ายังไม่มีคำนี้ใน dict ให้เพิ่มเข้าไป value เป็น 1
    ถ้าเจอแล้ว ให้หาคำที่เหมือนกันแล้วเพิ่ม value คำนั้น + 1
    output ออก มาเป็น dictionary

'''

class Solution():
    def count_words(self, word_list):
        word_Storage = {}

        for index in range(len(word_list)):
            word = word_list[index]

            if word in word_Storage:
                word_Storage[word] += 1
            else:
                word_Storage[word] = 1

        return word_Storage

Solution1 = Solution()
print(Solution1.count_words(["apple", "banana", "apple", "orange", "banana", "apple"]))

print(Solution1.count_words(["cat", "dog", "cat", "cat"]))