from collections import Counter
fh = open("war_and_peace.txt", 'r')
# Find the most common 5 words in War and Peace

words = Counter()
for line in fh:
    words.update(
        [word.strip("., \n") for word in line.lower().split()]    )

print (words.cost_common(5))