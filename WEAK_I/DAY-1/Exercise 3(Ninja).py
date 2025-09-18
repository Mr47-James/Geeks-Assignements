PAR = """Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation. 
Python is dynamically type-checked and garbage-collected."""

# Split into words and sentences
WLIST = PAR.split()
SLIST = PAR.split(". ")

# Count total words
words = len(WLIST)

# Count unique words
unique_words = len(set([w.strip(".,").lower() for w in WLIST]))

# Count word frequencies
word_freq = {}
for word in WLIST:
    word = word.strip(".,").lower()  # normalize
    word_freq[word] = word_freq.get(word, 0) + 1

repeating_words = {w: c for w, c in word_freq.items() if c > 1}

non_whitespace_chars = len(PAR.replace(" ", "").replace("\n", ""))
avg_words_per_sentence = words / len(SLIST)
non_unique_count = words - unique_words

print(f"Your paragraph length: {len(PAR)} characters (including spaces)")
print(f"The number of words it contains: {words}")
print(f"The number of unique words it contains: {unique_words}")
print(f"The number of sentences it contains: {len(SLIST)}")
print(f"Repeating words and their counts: {repeating_words}")
print(f"Non-whitespace characters: {non_whitespace_chars}")
print(f"Average words per sentence: {avg_words_per_sentence:.2f}")
print(f"Number of non-unique words: {non_unique_count}")
