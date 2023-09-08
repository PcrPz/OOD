# พี่อยากให้น้องๆ หา string ทุกตัวที่เป็นไปได้จาก string ที่พี่ให้หน่อย ว่าง่ายๆ คือการประกอบคำนั่นเอง หรือที่เขาเรียกกันว่า String Permutation เป็นการเอาตัวอักษรแต่ละตัวจาก string ที่ให้ไปนำไปสร้าง string ที่มีความเป็นไปได้ทั้งหมด จากตัวอักษรของ string ที่ได้รับมา

# Input มี 2 ค่า

# string ที่จะนำมาหา Permutation
# k = ขนาดของ string ที่จะสร้างขึ้นมาใหม่
# โดยหลักการมีดังนี้

# ฟังก์ชัน `permute_string` รับพารามิเตอร์ 2 ตัวคือ string `s` และ integer `k` ที่แทนจำนวนตัวอักษรที่จะถูกสับเปลี่ยนตำแหน่ง
# ฟังก์ชันตรวจสอบว่า `k` มีค่าน้อยกว่า 0 หรือไม่ ถ้าใช่ จะเกิด `ValueError` ที่ระบุว่าไม่อนุญาตให้ใช้ค่า `k` ที่เป็นลบ โดยให้ return "Invalid value of k. k must be a non-negative integer."
# ภายในฟังก์ชัน `generate_permutations` มีการใช้ recursive เพื่อสร้างทุกความเป็นไปได้ของการสับเปลี่ยนตำแหน่งของความยาว `k` จาก string `s` ที่กำหนด. ถ้า `k` เป็น 0 จะ return เป็น string ว่าง
# ในส่วน recursion ฟังก์ชันวนลูปผ่านแต่ละตัวอักษรใน string `s` โดยนำตัวอักษรปัจจุบันมาเป็น "prefix" และสร้างการสับเปลี่ยนตำแหน่งของตัวอักษรที่เหลือโดยใช้ recursive ด้วยความยาวที่ลดลงเป็น `k - 1`
# ส่วนหลักการในการทำการสร้างการสับเปลี่ยนตำแหน่งทั้งหมดของความยาว `k` โดยใช้ฟังก์ชัน `generate_permutations` และในผลลัพธ์อาจมี string ที่สับเปลี่ยนแล้วซ้ำกัน ให้เปลี่ยนผลลัพธ์เป็น string ที่มีความ unique เท่านั้น เช่น ['abb', 'bab', 'bba', 'abb'] -> ['abb', 'bab', 'bba']
# สุดท้าย แต่ละ string ที่เป็นไปได้หลังจากหา unique และทำการ sorted
# หมายเหตุ : ใครไม่รู้อะไร หรือ สงสัย สามารถสอบถาม TA ได้เลยครับ
def permute_string(string,k):

    if int(k) < 0:
        return "Invalid value of k. k must be a non-negative integer."
    elif int(k) > len(string):
        return "Invalid value of k. k must be less than or equal to the length of the string."
    elif int(k) == 0:
        return ['']
    else:
        result = generate_permutations(list(strings), int(k))
        return sorted(set(result))

def generate_permutations(s, k, index=0, prefix=''):
    #last condition
    if k == 0:
        return [prefix]

    permutations = []
   #loop เช็คทุกตัวเลย
    if index < len(s):
        new_prefix = prefix + s[index]
        remaining_chars = s[:index] + s[index+1:]
        smaller_permutations = generate_permutations(remaining_chars, k - 1, 0, new_prefix)
        permutations.extend(smaller_permutations)

        next_index = index + 1
        permutations_from_next_index = generate_permutations(s, k, next_index, prefix)
        permutations.extend(permutations_from_next_index)

    return permutations


strings, k = input("Enter a string and k: ").split("/")
print(permute_string(strings,k))
