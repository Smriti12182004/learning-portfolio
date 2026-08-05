import string
from collections import Counter

def word_count(text):
    text=text.lower()

    for ch in string.punctuation:
        text=text.replace(ch, "")

    words = text.split()
    count = {}
    for word in words:
        count[word]=count.get(word,0)+1

    return count

def word_count_counter(text):
    text=text.lower()
    for ch in string.punctuation:
        text=text.replace(ch,"")
    words= text.split()

    return dict(Counter(words))

def flatten_loop(list_of_lists):
    flat_list = []
    for sublist in list_of_lists:
        for item in  sublist:
            flat_list.append(item)
    return flat_list

def flatten_comprehension(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

# 5. Mean of numbers in a file
def mean_of_file(path):
    numbers = []

    try:
        with open(path, "r") as file:
            for line in file:
             try:
                numbers.append(float(line.strip()))
             except ValueError:
                continue

        if not numbers:
            return "No valid numbbers found."
        return sum(numbers)/len(numbers)

    except FileNotFoundError:
        return f"Error: File '{path}' not found"

#test code
if __name__ == "__main__":
    text="Hello hello world, welcome to Python World!"
    print("Manual Count: ")
    print(word_count(text))

    print("\n Counter Count: ")
    print(word_count_counter(text))

    print("\n Do both methods give same output? ")
    print(word_count(text)==word_count_counter(text))

    nested = [[1,2], [3,4], [5,6]]

    print("\n Flatten using loop: ")
    print(flatten_loop(nested))

    print("\n Flatten using List Comprehension: ")
    print(flatten_comprehension(nested))

    print("\n Mean of numbers.txt: ")
    print(mean_of_file("numbers.txt"))

    print("\n Testing the missing file: ")
    print(mean_of_file("missing.txt"))