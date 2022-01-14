def sothuannghich(n):
    str1 = str(n);
    str2 = str1[::-1];
    if (str1 == str2):
        return True;
    else:
        return False;

m = input("nhập họ và tên của bạn ")
n = int(input("Nhập số nguyên dương n = "));
print(m)
print("số", n, "là số thuật nghịch là ", sothuannghich(n));
