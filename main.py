def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')

        if len(start) != 1 or len(end) != 1 or not start.isalpha() or not end.isalpha():
            print("Error: Enter only alphabetic char")
            continue
        

    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
