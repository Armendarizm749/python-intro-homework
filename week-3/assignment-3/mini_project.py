day = input("What day is it?").lower()
time = input("What time of the day?").lower()

if day == "monday" and time == "morning":
    print("Suggestionn: Start the day with a glass of water!")

elif day == "monday" and time == "afternoon":
    print("Suggestion: Take a walk outside!")

elif day == "monday" and time == "evening":
    print("Suggestion: Take a break for meditation!")


elif day == "tuesday" and time == "morning":
    print("Suggestion: Eat a breakfast with protein!")

elif day == "tuesday" and time == "afternoon":
    print("Suggestion: Go to the gym!")

elif day == "tuesday" and time == "evening":
    print("Suggestion: Pay the pendinng payments!")

elif day == "wednesday" and time == "morning":
    print("Suggestion: Start the day with a shower!")

elif day == "wednesday" and time == "afternoon":
    print("Suggestion: Drink a cup of tea!")

elif day == "wednesday" and time == "evening":
    print("Suggestion: Take a nap!")

# else - to use it when we don't have a recommendation
else:
    print("Sorry, I don't have a suggestion for that day or time.")






          
