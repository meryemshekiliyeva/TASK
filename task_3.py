def word_frequency(text):
    words = text.split()
    count = {}
    for word in words:
        word = word.strip(".,!?()[]{}\"'").lower()
        if word:
            count[word] = count.get(word, 0) + 1
    return count
text = input()
word_dict = word_frequency(text)
print(word_dict)
