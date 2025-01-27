# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
word = input("Choose a word. ")
repeat = input("Repeat it how many times? ")
print(word*int(repeat))

#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name, age1 = input("What is your name? "), input("What is your age? ")
age2 = int(age1) + 1
print("Hello, " + name + "! You are " + age1 + " years old. Next year, you will be " + str(age2) + " years old.")

#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence = input("Write a sentence. ")
word = input("Give me a word to find in that sentence. ")
print(word in sentence)

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word = input("Give me a word. ")
index1 = input("Where will the first slice be? ")
index2 = input("Where will the second slice be? ")
print(word[int(index1):int(index2)])

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
words = "Lets freaking goooooo"
words2 = words.split(" ")
split_words = "|".join(words2)
print(split_words)
