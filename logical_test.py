def thai_number_to_text(number):
    if 0 <= number < 10000000:

        thai_digits = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        thai_places = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        thai_text = ""
        digits = [int(digit) for digit in str(number)[::-1]]

        for i, digit in enumerate(digits):
            if digit != 0 or (i == 0 and digit == 0):
                thai_text = thai_digits[digit] + thai_places[i] + thai_text

        thai_text = thai_text.replace("หนึ่งสิบ", "สิบ")
        thai_text = thai_text.replace("สองสิบ", "ยี่สิบ")
        thai_text = thai_text.replace("สิบหนึ่ง", "สิบเอ็ด")

        if number > 1 and str(number)[-1] == "1" and str(number)[-2] == "0":
            thai_text = thai_text[:-5] + "เอ็ด"
        return thai_text
    else:
        return "กรุณาป้อนตัวเลขในช่วง 0 ถึง 10 ล้าน"
    
def main():
    try:
        user_input = input("ป้อนตัวเลข: ")
        user_number = int(user_input)
        result = thai_number_to_text(user_number)
        print(f"ผลลัพธ์: {result}")
    except ValueError:
        print("กรุณาป้อนตัวเลขที่ถูกต้อง")


if __name__ == "__main__":
    main()