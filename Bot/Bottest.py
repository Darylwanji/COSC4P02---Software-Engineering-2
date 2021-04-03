import unittest
import chatbot
import json

with open("sample2.json") as file:
    data = json.load(file)

class Bottest(unittest.TestCase):

	def test_Greetings(self):
		result1 = chatbot.Test("Hello")
		result2 = chatbot.Test("Hi")
		result3 = chatbot.Test("How are you?")
		result4 = chatbot.Test("Is anyone there?")
		result5 = chatbot.Test("Good day")
		result6 = chatbot.Test("I need help")
		result7 = chatbot.Test("Morning")

		R = [result1,result2,result3,result4,result5,result6,result6]

		for results in R:
			if results in data['intents'][0]['responses']:
				self.assertEqual(1,1)

	def test_Goodbye(self):
		result1 = chatbot.Test("bye")
		result2 = chatbot.Test("See you later")
		result3 = chatbot.Test("Goodbye")

		R = [result1,result2,result3]
		for results in R:
			if results in data['intents'][1]['responses']:
				self.assertEqual(1,1)


	def test_thanks(self):
		result1 = chatbot.Test("Thanks")
		result2 = chatbot.Test("Thank you")
		result3 = chatbot.Test("That's helpful")
		result4 = chatbot.Test("Thanks a lot")

		R = [result1,result2,result3,result4]
		for results in R:
			if results in data['intents'][2]['responses']:
				self.assertEqual(1,1)

	def test_payments(self):
		result1 = chatbot.Test("Do you take credit cards?")
		result2 = chatbot.Test("Do you accept Mastercard?")
		result3 = chatbot.Test("Are you cash only?")

		R = [result1,result2,result3]
		for results in R:
			if results in data['intents'][3]['responses']:
				self.assertEqual(1,1)

	def test_offerings(self):
		result1 = chatbot.Test("Do you offer ?")
		result2 = chatbot.Test("Will I be able to do ?")
		result3 = chatbot.Test("is it offered ?")

		R = [result1,result2,result3]
		for results in R:
			if results in data['intents'][4]['responses']:
				self.assertEqual(1,1)




if __name__ == '__main__': 
	unittest.main()