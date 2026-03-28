def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                m, d, y = map(int, date.split("/"))
            elif "," in date:
                parts = date.replace(",", "").split()
                m_name = parts[0].title()
                if m_name not in months:
                    continue
                m, d, y = months.index(m_name) + 1, int(parts[1]), int(parts[2])
            else:
                continue

            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f"{y}-{m:02}-{d:02}")
                break
        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
