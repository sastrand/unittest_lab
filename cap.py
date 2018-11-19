def first_letter_cap(word):
	if len(word) == 0:
		return word
	if word[0].isdigit(): 
		return word
	elif word[0].isalpha():
		return word[0].capitalize() + word[1:]
	else:
		return word[0] + first_letter_cap(word[1:])

def capitalizer(text):
    """Capitalizes the first letter of each word in a string."""
    return " ".join([first_letter_cap(w) for w in text.split(" ")])
