def totalDigitsOfNumber(n):
    total = 0
    while (n > 0):
        total = total + n % 10
        n = int(n / 10)
    return total
n = int(input("Nhập số nguyên dương n = "))
print("Tổng các chữ số của", n, "là", totalDigitsOfNumber(n))

# nhập in ra màn hình tên của mình
tongkitu = str ( input ( "nhập tên:"))
print ( "Tên tôi là:",tongkitu)

res = sum(map(len, tongkitu.split()))
# độ dài tên của mình
print("Ten co do dai la:"+ str(res))

