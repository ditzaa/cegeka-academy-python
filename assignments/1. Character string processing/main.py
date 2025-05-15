print("Please introduce a sentence: ")
sentence = input()

nb_of_chars = len(sentence.replace(" ", ""))
print("Nb. of characters: " + str(nb_of_chars))

lower_sentence = sentence.lower()
print("Sentence in lowercase: " + lower_sentence)

upper_sentence = sentence.upper()
print("Sentence in uppercase: " + upper_sentence)

replaced_a_sentence = sentence.replace("a", "e")
print("Replaced 'a' with 'e': " + str(replaced_a_sentence))

reversed_sentence = ' '.join(sentence.split()[::-1])
print("Sentence with words in reverse order: " + reversed_sentence)

print("Please introduce a new word: ")
word = input()
word = word.replace(" ", "")
count_word = lower_sentence.split().count(word.lower())
print("Word '" + word + "' appeared " + str(count_word) + " times in the sentence")
