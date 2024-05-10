from datetime import *

current_date = datetime.now().date()

d, m, y = [int(x) for x in input("Enter date of birth (DD/MM/YYYY): ").split("/")]
b1 = date(y, m, d)


def minutes_lived():
    d = (current_date - b1).total_seconds()
    ml = int(round(d // 60))
    print(f"You have lived for {ml} minutes")


minutes_lived()
