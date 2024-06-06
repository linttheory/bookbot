import re

BOOK_PATH = "books/frankenstein.txt"


def main():
    try:
        book_text = get_book_text(BOOK_PATH)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(e)

    cleaned_book_text = clean_book(book_text)
    total_words, unique_words = count_words(cleaned_book_text)
    print(
        f"This book has {total_words} total words and {unique_words} total unique words. Numbers have been excluded from the count.")
    letter_stats = count_letters(cleaned_book_text)
    for letter, count in letter_stats:
        print(f"The letter '{letter}' is used {count} times.")


def get_book_text(path):
    with open(path) as book:
        return book.read()


def clean_book(book_text):
    """Removes numbers and special characters from book text."""
    cleaned_book_text = re.sub(r'[^A-Za-z\s]', '', book_text.lower())
    return cleaned_book_text


def count_words(words):
    """Counts the number of total words and unique words in the book."""
    split_words = words.split()
    total_words = len(split_words)
    unique_words = len(set(split_words))
    return total_words, unique_words


def count_letters(string):
    """Removes spaces and linebreaks from the book text."""
    cleaned_string = string.replace(" ", "").replace("\n", "")
    stat_dict = {}
    for letter in cleaned_string:
        if len(stat_dict) < 26 and letter not in stat_dict:
            stat_dict[letter] = 1
        else:
            stat_dict[letter] += 1
    print(len(stat_dict))
    sorted_stats = sorted(stat_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_stats


main()
