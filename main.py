def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

try:
    year_input = input("请输入一个年份：")
    year = int(year_input)
    if is_leap_year(year):
        print(f"{year} 是闰年")
    else:
        print(f"{year} 不是闰年")
except ValueError:
    print("输入错误，请输入一个有效的年份数字。")
