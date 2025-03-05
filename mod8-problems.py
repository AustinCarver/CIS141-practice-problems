'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
it.
Write a Python script that reads a file gardening_tips.txt and prints
out each tip one by one.
'''
with open("gardening_tips.txt", "r") as garden_tips:
    for tip in garden_tips:
        print(tip)
'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
hikes = open("hiking_log.txt","w")
hikes.write("")
hikes.close()

hikes = open("hiking_log.txt","a")
while True:
    hike_name = input("What is your hike's name? Press 0 to exit.")
    if hike_name == str(0):
        break
    hike_distance = input(f"What was {hike_name}'s distance? Press 0 to exit.")
    if hike_distance == str(0):
        break
    hikes.write(hike_name+": "+hike_distance + "\n")
hikes.close()
with open("hiking_log.txt", "r") as hikes:
    for hike in hikes:
        print(hike)
'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the
frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''
word_count = {}
with open("song_lyrics.txt", "r") as song:
    lyrics = song.read().lower()
    words = input("Give me a word to look for."), input("Give me a second word to look for."), input("Give me a third word to look for."), input("Give me a fourth word to look for."), input("Give me a fifth word to look for.")
    for word in words:
        word_count[f"{word}"] = lyrics.count(word)
print(word_count)
'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas.
Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''
with open("poll.txt", "r") as votes:
    vote_count = votes.read().lower()
    vote_list = vote_count.strip()
    yea_votes = vote_list.count("yea")
    nay_votes = vote_list.count("nay")
    print(f"There are {yea_votes} votes for yea and {nay_votes} for nay.")
