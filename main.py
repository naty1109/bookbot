import sys
from stats import get_words_num, count_char, sort_dictionary

def get_books_text(filepath):
	with open(filepath,"r") as f:
		content = f.read()
	return content


def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n")
	book_content = get_books_text(filepath=f"{sys.argv[1]}")
	print(f"----------- Word Count ----------\n{get_words_num(book_content)}\n")
	chars_count_list = count_char(book_content)
	print("--------- Character Count -------")
	for item in sort_dictionary(chars_count_list):
		print(f"{item['char']}:",item['num'])


main()
