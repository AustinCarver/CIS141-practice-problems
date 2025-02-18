#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
numbers = [3,1,4,1,5,9,2,6,5]
total_evens = 0
for number in numbers:
    if number % 2 == 0:
        total_evens += number
print(total_evens)
#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
words_list = ["Olympic","Gonzaga","Seattle","Washington","Olympic","Olympic"]
olympic_count = 0
for word in words_list:
    if word == "Olympic":
        olympic_count += 1
print(olympic_count)
#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.
more_words = ["Axe","Shield","Sword","Bow","Hammer","Gun"]
new_list = []
for weapon in more_words:
    if len(weapon) >= 4:
        new_list.append(weapon)
print(new_list)
#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.
more_numbers = [3,-1,4,1,-5,9,2,6,-5]
pos_num = 0
neg_num = 0
for num in more_numbers:
    if num > 0:
        pos_num += 1
    else:
        neg_num += 1
print("Number of Positives:",pos_num)
print("Number of Negatives:",neg_num)
#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.
even_more_numbers = [3,1,4,1,5,9,2,6,5]
sqr_num = []
for int in even_more_numbers:
    sqr_num.append(int * int)
print(sqr_num)
