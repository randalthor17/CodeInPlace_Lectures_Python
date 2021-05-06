SENTINEL_VALUE = -1


def main():
    sum = 0
    entered_value = 0
    while entered_value != -1:
        entered_value = float(input("Type a number: "))
        if entered_value != -1:
            sum += entered_value
    print("total is", sum)


if __name__ == "__main__":
    main()