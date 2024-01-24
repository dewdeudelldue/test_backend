def find_trailing_zeros(n):
    count = 0
    i = 5
    while n / i >= 1:
        count += int(n / i)
        i *= 5
    return count


def main():
    try:
        user_input = input("ป้อนตัวเลข: ")
        user_number = int(user_input)
        result = find_trailing_zeros(user_number)
        print(f"ผลลัพธ์: {result}")
    except ValueError:
        print("กรุณาป้อนตัวเลขที่ถูกต้อง")


if __name__ == "__main__":
    main()

