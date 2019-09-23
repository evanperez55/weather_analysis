
def palinedrome(word):
	for x in word[::-1]:
		result += x
	if result == word:
		print('That is a palindrome')
	else:
		print('Not a palindrome ya dumbass')
    

