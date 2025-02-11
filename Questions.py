#Question 1 ----------

punctuation_remove = (".,!?")
punctuation_space = ("'")

def find_3_letter_words(filename):
    with open(filename) as f:
        for line in f:
            for p in punctuation_remove:
                line = line.replace(p,"")
            for p in punctuation_space:
                line = line.replace(p, " ")
            words = line.split()

            for word in words:
                if len(word) == 3 and word[0].lower() == "b":
                    print(word)

find_3_letter_words("input.txt")


