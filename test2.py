def find_max_index(arr):
    max = arr[0]
    max_index = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            max_index = i
    return max_index


def main():
    try:
        user_input = input("ป้อนตัวเลขที่ต้องการหาค่าสูงสุด: ")
        user_input = user_input.split()
        user_input = [int(i) for i in user_input]
        result = find_max_index(user_input)
        print(f"ผลลัพธ์: {result}")
    except ValueError:
        print("กรุณาป้อนตัวเลขที่ถูกต้อง")


if __name__ == "__main__":
    main()
