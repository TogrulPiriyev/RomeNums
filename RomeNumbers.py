one = "I"
five = "V"
ten = "X"
fifty = "L"
hundred = "C"
five_hundred = "D"
thousand = "M"
ful_num = []


def rim_nums(num):
    thousandc = 0
    fivehundred = 0
    hundredc = 0
    fiftyc = 0
    tenc = 0
    four = 0
    nine = 0
    count_under = 0
    count_upper = 0
    fivec = 0
    nine_hundred = 0
    ninety = 0
    four_hundred = 0
    fourty = 0
    while num > 0:
        if num >= 1000:
            thousandc += num // 1000
            num = num % 1000
        if num >= 500 and num < 600:
            fivehundred += num // 500
            num = num % 500

        if num >= 600 and num < 900:
            fivehundred += 1
            hundredc += (num - 500) // 100
            num = num % 100
        if num >= 900 and num < 1000:
            nine_hundred += 1
            num = num % 100
        if num < 400 and num >= 100:
            hundredc += num // 100
            num = num % 100
        if num >= 400 and num < 500:
            four_hundred += 1
            num = num % 100
        if num >= 90 and num < 100:
            ninety += 1
            num = num % 10
        if num > 50 and num < 90:
            fiftyc += 1
            tenc += (num - 50) // 10
            num = num % 10
        if num == 50:
            fiftyc += 1
            num = num % 50
        if num < 50 and num >= 40:
            fourty += 1
            num = num % 10
        if num < 40 and num >= 10:
            tenc += num // 10
            num = num % 10

        if num == 9:
            nine += 1
            break
        elif num == 4:
            four += 1
            break
        if num % 10 != 4 and num % 10 != 9:
            if num % 10 < 4:
                count_under += num % 10
                break
            if num % 10 > 5 and num % 10 < 9:
                count_upper += num % 10 - 5
                break
        if num % 10 == 5:
            fivec += 1
            break

    if thousandc > 0:
        for i in range(thousandc):
            ful_num.append(thousand)
    if nine_hundred > 0:
        ful_num.append(hundred)
        ful_num.append(thousand)
    if fivehundred > 0:
        ful_num.append(five_hundred)
    if four_hundred > 0:
        ful_num.append(hundred)
        ful_num.append(five_hundred)
    if hundredc > 0:
        for i in range(hundredc):
            ful_num.append(hundred)
    if ninety > 0:
        ful_num.append(ten)
        ful_num.append(hundred)
    if fiftyc > 0:
        ful_num.append(fifty)
    if fourty > 0:
        ful_num.append(ten)

        ful_num.append(fifty)
    if tenc > 0:
        for i in range(tenc):
            ful_num.append(ten)
    if count_under > 0:
        for i in range(count_under):
            ful_num.append(one)
    if count_upper > 0:
        ful_num.append(five)
        for i in range(count_upper):
            ful_num.append(one)
    if fivec > 0:
        ful_num.append(five)
    if nine > 0:
        ful_num.append(one)
        ful_num.append(ten)
    if four > 0:
        ful_num.append(one)
        ful_num.append(five)
    for i in ful_num:
        print(i, end="")


rim_nums(int(input()))
o = "I"
fi = "V"
t = "X"
fif = "L"
hundr = "C"
five_hundr = "D"
thousa = "M"
print()
rom_num = input("rom num: ")
number_from_num = []
thous = 0
hundre = 0
te = 0
fiv = 0
count = 0
for i in rom_num:
    hello = rom_num.index(i) + 1
    lenny = len(rom_num)
    if i == "M":
        thous += 1
    if i == "D":
        hundre += 5
    if i == "C":
        if hello == lenny:
            hundre += 1
            break
        if rom_num[rom_num.index(i) + 1] == "M":
            hundre += 9
            thous -= 1
        elif rom_num[rom_num.index(i) + 1] == "D":
            hundre -= 1
        else:
            hundre += 1

    if i == "L":
        te += 5
    if i == "X":

        if lenny == hello:
            te += 1
            break
        if rom_num[rom_num.index(i) + 1] == "L":
            te -= 1
        else:
            te += 1
    if i == "V":
        count += 5
    if i == "I":
        if lenny == hello:
            count += 1
            break
        if rom_num[rom_num.index(i) + 1] == "X":
            count += 9
            te -= 1
        elif rom_num[rom_num.index(i) + 1] == "V":
            count -= 1
        else:
            count += 1
ful_nu = thous * 1000 + hundre * 100 + te * 10 + count
print(ful_nu)
