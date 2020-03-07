from random import randrange

#Set up the rules via a dict.
dict =  {1:"Information is everything - Go around the circle. Everybody has the choice: Reading the last message you received or drink three zips.",
		 2:"Two for you - Nominate two players that must drink. (One for each player)",
		 3:"Me - If it is your turn, you must drink.",
		 4:"Hug - Give a person of your choice a hug.",
		 5:"Boys - All boys drink.",
		 6:"Girls - All girls drink.",
		 7:"Heaven - Put your hands up. The last person to do so must drink.",
		 8:"Never have I ever - Ask all players a question starting with ""I've Never…"". Players who have done this thing respond by taking a drink.",
		 9:"Rhyme - Go around the circle rhyming one word. The person who drew chooses the word. No silver, orange, purple, or other stupid junk. First long hesitation or failure is the loser and must drink.",
		 10:"Category - The person who drew chooses a category (e. g. car brands), and then everyone must name something in it.",
		 11:"Make up a new rule — Your rule cancel an existing rule.",
		 12:"Waterfall — The person who drew the Ace begins to drink, then the person after them, then the next person, etc. until everyone in the circle is drinking. Then the first person stops, then the second, third, and so on. The point being that you cannot stop drinking before the person ahead of you.",
		 13:"Who smells good? - If it is your turn, close your eyes and try to guess ",
		 14:"Live Insta -  If it is your turn, show everyone the last five photos from your phone or drink three zips.",
		 15:"Catch up - The one with the fullest cup takes three zips.",
		 16:"Finish line - The person with the emptiest cup must finish their drink.",
		 17:"Zodiac mania - If there is another player with the same zodiac sign, you must drink.",
		 18:"Good neighborhood - The players next to you have to drink one zip each.",
		 19:"Creative bingo - Go around the circle and count from 1. Choose a number between 2 and 9. Everytime the countet number contains X, or can be devided by X you have to say a word of your choice (e.g. ""bingo""). If someone fails he has to drink two zips.",
		 20:"Single but drunk - All singles drink.",
		 21:"Couples are great - Everyone who is in a relationship drinks."}

#Get a random number between 0 and the length of the dict (number of key/value pairs). +1 is for including the last item.
randomNo = randrange(1, len(dict) + 1)
print(randomNo)

#Get the description at dict[index] where index = randomNo
resultStr = dict[randomNo]
print(resultStr)
