#Clear Text
#should be encrypted into certain values
#ceasar Cypher
#shift 13
alphapets = "abcdefghijklmnopqrstuvwxyz"
def encrypt(clear_text):
	cypher_text = ""
	for char in clear_text:
		if char in alphapets:
			newpos = (alphapets.find(char) + 13) % 26
			cypher_text += alphapets[newpos]
		else:
			cypher_text += char
	return cypher_text
		
clear_text = input("Clear text: ")
clear_text = clear_text.lower()
print(encrypt(clear_text))
