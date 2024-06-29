def main():
    result = []
    
    while True:
        start = input('Enter the starting letter: ').strip().lower()
        end = input('Enter the starting letter: ').strip().lower()

        if len(start) != 1 or len(end) != 1 or not start.isalpha() or not end.isalpha():
            print("Error: Enter only alphabetic char")
            continue
        
        if start >= end:
            print("Error: Starting letter needs to be less than ending")
            continue
        
        letter = start
        while letter <= end:
            result.append(letter)
            letter = chr(ord(letter) + 1)
            
        break
    
    print('Consecutive letters:', ' '.join(result))
        

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
