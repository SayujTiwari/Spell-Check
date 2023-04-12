# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])

    while True:
        print("1. Spell Check a Word (Linear Search)")
        print("2. Spell Check a Word (Binary Search)")
        print("3. Spell Check Alice In Wonderland (Linear Search)")
        print("4. Spell Check Alice In Wonderland (Binary Search)")
        print("5. Exit")
        choice = input("Enter menu selection (1-5): ")
        # Choice 1
        if choice == "1":
            word = input("Please enter a word: ").lower()
            print("Linear Search starting...")
            timeStart = time.time()
            found = (linearSearch(dictionary, word))
            endtimer = time.time()
            if found != -1:
                print(f"{word} is IN the dictionary at position {found}")
            elif found == -1:
                print(f"{word} is NOT in the dictionary")

            print(f"Time Elapsed {(endtimer - timeStart)} seconds")
        # Choice 2
        elif choice == "2":
            word = input("Please enter a word: ").lower()
            print("Binary Search starting...")
            timeStart = time.time()
            found = (binarySearch(dictionary, word))
            endtimer = time.time()
            if found != -1:
                print(f"{word} is IN the dictionary at position {found}")
            elif found == -1:
                print(f"{word} is NOT in the dictionary")
            print(f"Time Elapsed {(endtimer - timeStart)} seconds")
        # Choice 3
        elif choice == "3":
            count = 0
            print("Linear search is starting...")
            timeStart = time.time()
            for i in range(len(aliceWords)):
                found = linearSearch(dictionary, aliceWords[i])
                endtimer = time.time()
                if found == -1:
                    count += 1
            print(f"Total words not found: {(count)}")
            print(f"Time Elapsed {(endtimer - timeStart)} seconds")
        # Choice 4
        elif choice == "4":
            count = 0
            timeStart = time.time()
            for i in range(len(aliceWords)):
                found = binarySearch(dictionary, aliceWords[i])
                endtimer = time.time()
                if found == -1:
                    count += 1
            print(f"Total words not found: {(count)}")
            print(f"Time Elapsed {(endtimer - timeStart)} seconds")
        elif choice == "5":
            break
        else:
            print("Invalid input, try again")

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)

def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return f"{item} is in the dictionary"
    return -1

def binarySearch(anArray, item):
    lowerIndex = 0
    upperIndex = (len(anArray) - 1)

    while lowerIndex <= upperIndex:
        middleIndex = (lowerIndex + upperIndex) // 2
        if (item == anArray[middleIndex]):
            return f"{item} is in the dictionary"
        elif (item < anArray[middleIndex]):
            upperIndex = middleIndex - 1
        else:
            lowerIndex = middleIndex + 1
    return -1


# Call main() to begin program
main()
