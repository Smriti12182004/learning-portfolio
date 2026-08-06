import string
from collections import Counter

# Counts the frequency of each word using a dictionary.
# Converts text to lowercase and removes punctuation.
def word_count(text):
    text=text.lower()

    for ch in string.punctuation:
        text=text.replace(ch, "")

    words = text.split()
    count = {}
    for word in words:
        count[word]=count.get(word,0)+1

    return count

# Counts the frequency of each work using collections.Counter.
# Produces the same result as word_count() with less code.
def word_count_counter(text):
    text=text.lower()
    for ch in string.punctuation:
        text=text.replace(ch,"")
    words= text.split()

    return dict(Counter(words))

# test code for testing all functions and print the outputs
if __name__ == "__main__":
    text="Hello hello world, welcome to Python World!"
    print("Manual Count: ")
    print(word_count(text))

    print("\n Counter Count: ")
    print(word_count_counter(text))