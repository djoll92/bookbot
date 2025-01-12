def main():
	book_path = "books/frankenstein.txt"
	print_book_report(book_path)

def get_book_text(book_path):
	with open(book_path) as book_file:
		book_text = book_file.read()
		return book_text

def get_book_words_count(book_text):
	words = book_text.split()
	return len(words)

def get_book_characters_dict(book_text, only_alphabet=False):
	characters = {}
	for char in book_text:
		if only_alphabet and not char.isalpha():
			continue
		char = char.lower()
		if char in characters:
			characters[char] += 1
		else:
			characters[char] = 1
	return characters

def get_book_letters_dict(book_text):
	return get_book_characters_dict(book_text, True)

def print_book_report(book_path):
	book_text = get_book_text(book_path)
	letters_dict = get_book_letters_dict(book_text)
	words_count = get_book_words_count(book_text)

	print(f"--- Begin report of {book_path} ---")
	print(f"{words_count} words fond in the document")
	print()
	for letter in letters_dict:
		print(f"The '{letter}' character was found {letters_dict[letter]} times")

main()