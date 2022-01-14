def KiemTraSoThuanNghich(n):
    str1 = str(n)
    str2 = str1[::-1]
    if (str1 == str2):
        return True
    else:
        return False
n = int(input("Nhập số nguyên dương n = "))
print("Số bạn vừa nhập là", n, "là", KiemTraSoThuanNghich(n))

ho = str ( input ( "nhập họ:" ))
Tendem = str ( input ( "nhập tên đệm:" ))
Ten = str ( input ( "nhập tên:" ))


print("Họ và tên:", ho+" "+Tendem+" "+Ten)
print(ho+" "+Tendem+" "+Ten,"=",len(ho),len(Tendem),len(Ten),sep='')



