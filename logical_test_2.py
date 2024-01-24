
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

def decimal_to_roman(decimal):
    if not 0 < decimal < 1000:
        print("โปรดป้อนค่าที่มีค่ามากกว่า 0 และน้อยกว่า 1000")
        return

    roman_numerals = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    ]

    result = ''
    for numeral, value in roman_numerals:
        while decimal >= value:
            result += numeral
            decimal -= value

    return result

def main():
    try:
        decimal_input = int(input("กรุณาป้อนตัวเลขที่ต้องการแปลง (1-1000): "))
        if 0 < decimal_input < 1000:
            roman_output = decimal_to_roman(decimal_input)
            print(f"ตัวเลขโรมันที่แปลงจาก {decimal_input} คือ {roman_output}")
        else:
            print("กรุณาป้อนค่าที่มีค่ามากกว่า 0 และน้อยกว่า 1000")
    except ValueError:
        print("กรุณาป้อนตัวเลขที่ถูกต้อง")

if __name__ == "__main__":
    main()

