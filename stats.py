def get_words_num(content=str):
	str_split = content.split()
	words_count = len(str_split)
	return f"Found {words_count} total words"

def count_char(content=str):
	chars_dictionary = {}
	for character in content.lower():
		if character in chars_dictionary:
			chars_dictionary[character] += 1
		else:
			chars_dictionary[character] = 1
	return chars_dictionary

def sort_on(dict):
	return dict["num"]

def sort_dictionary(dictionary):
	new_list = []
	for k,v in dictionary.items():
		if k.isalpha():
			new_list.append({"char":f"{k}","num":v})
	new_list.sort(reverse=True, key= lambda x: x["num"])
	return new_list
