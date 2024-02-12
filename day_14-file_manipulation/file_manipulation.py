from collections import Counter

def count_words(filename, n=5):
    with open(filename, 'r') as file:
        words = file.read().split()
        word_counts = Counter(words)
        top_words = word_counts.most_common(n)
        for word, count in top_words:
            print(word, ":", count)

# Example usage
file_path = 'day_14-file_manipulation/file.txt'
count_words(file_path, 20)
