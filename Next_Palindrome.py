print("Welcome TO Next Palindrome Finder")
a = int(input("\nEnter The Number Of Test Cases : "))
restart = ('y')
while restart == 'y':
    for i in range(a):
        number = int(input("\nEnter a Number : "))
        original_number = number
        while True:
            if str(number) == str(number)[::-1]:
                print(f"Next Palindrome Number Of {original_number} is {number}")
                break

            else:
                number += 1

    restart = input("\nPress y to restart : ").lower()
    if restart != 'y':
        print("Thank You")
        break