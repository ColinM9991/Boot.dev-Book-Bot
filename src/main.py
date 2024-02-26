BOOK = "books/Frankenstein.txt"

def main():
    with open(BOOK) as f:
        file_contents = f.read()
        print(f"--- Begin report of {BOOK} ---")
        print(count_words(file_contents))

        letter_counts = count_letters(file_contents)
        letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

        for letter, count in letter_counts:
            print(f"The '{letter}' character was found {count} times")

def count_words(text):
    words = text.split()

    return len(words)

def count_letters(text):
    text = list(text.lower())
    letters = filter(lambda x: x.isalpha(), text)
    letters = list(set(letters))
    
    counts = {}

    for letter in letters:
        counts[letter] = text.count(letter)

    return counts

if __name__ == '__main__':
    main()
