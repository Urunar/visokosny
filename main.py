def is_leap_year(year):
    """comment test git_version_2"""
    """Определяет, является ли год високосным."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    while 1 == 1:
        val = input("Введите год: ")
        if val == "exit":
            exit(0)
        year = int(val)
        if is_leap_year(year):
            print(f"{year} является високосным годом.")
        else:
            print(f"{year} не является високосным годом.")

if __name__ == "__main__":
    main()