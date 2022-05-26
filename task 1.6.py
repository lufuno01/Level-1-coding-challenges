longest_words = ["the", "quick", "brown", "fox", "ate", "my", "chickens", "abashedly"]


def longest_string(longest_words, longest_array):
    word = len(longest_words)
    string = []
    for x in range(word):
        if longest_array == len(longest_words[x]):
            string.append(longest_words[x])
            for x in range(len(string)):
                print(string[x], end="\n")


print(longest_string(longest_words, longest_array))
