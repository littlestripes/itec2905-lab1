import datetime as dt

if __name__ == "__main__":
    # Get full name of current month as a lowercase string
    current_month_str = dt.date.today().strftime("%B").lower()
    current_month_num = dt.date.today().month

    name = str(input("What is your name? "))
    birth_month = str(input("What month were you born in? "))

    print("Hi {}!".format(name))
    if (
        birth_month.lower() in current_month_str
        or int(birth_month.strip()) == current_month_num
    ):
        print("Happy birth month!")

    name_length = len(name)
    print("Your name has {} characters in it.".format(name_length))
