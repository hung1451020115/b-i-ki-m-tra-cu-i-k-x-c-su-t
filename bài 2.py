def tinhtong(n):
    i = 0;
    while (n > 0):
        i = i + n % 10;
        n = int(n / 10);
    return i;
m = input("nhập tên đệp")
n = len(m)
print(m)
print("tổng số ký tự có trong tên là",n)
print("Tổng các chữ số của", n , "là", tinhtong(n));