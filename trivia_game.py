import random


def play_game():
	print "Welcome to the game!"
	pick_category = raw_input("Please pick from the following categories:\nPress 1 for Animals\nPress 2 for US History\nPress 3 for Coding\n").lower()
	if pick_category == '1':
		animals()



def animals():
	correct_answers = []
	question1 = raw_input("A sea pig is a type of sea cucumber. ").lower()
	question2 = raw_input("Sharks have bones. ").lower()
	question3 = raw_input("The cuddlefish has a poisonous beak. ").lower()
	question_list =[question1, question2, question3]

	random.shuffle(question_list)

	if question1 == 't':
		print "That's correct!"
		correct_answers.append(question1)
	elif question1 == 'f':
		print "Oh no! That's not right!"
	else:
		print "You didn't enter 'T' or 'F'!"

	if question2 == 't':
		print "I'm sorry, that is not correct."
	elif question2 == 'f':
		print "Yes, that's correct!"
		correct_answers.append(question2)
	else:
		print "You didn't enter 'T' or 'F'!"

	if question3 == 't':
		print "Correct!"
		correct_answers.append(question3)
	elif question3 == 'f':
		print "Nope! Incorrect!"


	if len(correct_answers) >= 4:
		print "You're a genius!"
	if len(correct_answers) == 3:
		print "Try harder next time!"
	if len(correct_answers) <= 2:
		print "Wow, you're not very bright are you?"



def main():
	print "Welcome to Trivia!\nThis is a game to test your knowledge from various categories!"
	while True:
		menu_options = raw_input("Please select from the following menu:\nPress 'I' for instructions\nPress 'P' to play\nPress 'Q' at anytime to quit.\n").lower()
		if menu_options == 'i':
			help_options = raw_input("You will be asked to answer 5 True/False questions from a category of your choosing.\nPress 'T' for True, and 'F' for False\nPlease press Enter to go back.").lower()
		if menu_options == 'p':
			play_game()
			break

		

if __name__ == '__main__':
	main()