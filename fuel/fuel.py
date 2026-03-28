def main():
    while True:
        s = input("Fraction: ").strip()
        try:
            a, b = s.split("/")
            num = int(a)
            den = int(b)

            if num > den or num < 0:
                continue
          
            val = round((num / den) * 100)

            if val >= 99:
                print("F")
            elif val <= 1:
                print("E")
            else:
                print(f"{val}%")

            break
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()