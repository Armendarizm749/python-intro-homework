numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("\n--- Number Cruncher Menu ---")
    print("1. Find Minimum")
    print("2. Find Maximum")
    print("3. Search for a Number")
    print("4. Sort Numbers")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        smallest = numbers[0]

        for number in numbers:
            if number < smallest:
                smallest = number

        print(f"The smallest number is: {smallest}")
    elif choice == "2":
        largest = numbers[0]

        for number in numbers:
            if number > largest:
                largest = number

        print(f"The largest number is: {largest}")

    elif choice == "3":
        search_number = int(input("Enter a number to search for: "))
        found_index = -1

        for i in range(len(numbers)):
            if numbers[i] == search_number:
                found_index = i
                break

        if found_index != -1:
            print(f"{search_number} was found at index {found_index}.")
        else:
            print(f"{search_number} was not found in the list.")

    elif choice == "4":
        swapped = True
        
        while swapped:
            swapped = False

            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True

        print(f"Sorted numbers: {numbers}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")



