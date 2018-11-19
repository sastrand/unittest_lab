def first_letter_cap(word):
	if len(word) == 0:
		return word
	if word[0].isdigit(): 
		return word
	elif word[0].isalpha():
		return list(word[0].capitalize()) + word[1:]
	else:
		return list(word[0]) + first_letter_cap(word[1:])

def first_letter_cap_helper(word):
	return "".join(first_letter_cap(list(word)))

def capitalizer(text):
    """Capitalizes the first letter of each word in a string."""
    return " ".join([first_letter_cap_helper(w) for w in text.split(" ")])
