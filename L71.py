#Emily Rusch and Kaylen Nyhuis
import unicodedata
def too_long(x):
    if len(x) >= 140:
        print("The text is too long.")
    else:
        print(x)

too_long("Today is Thursday, October 6th, 2022. We are in class writing code in python that is longer than 140 characters. dfsdfsdsdfdsdfsdfdsfsdfsdfdsdssdfsdfsdfsfwfuhfiwekhfiuwefbkebfefwb")
too_long("It was a hot 🌞 day. We went to get 🍓 after playing with our 🐕 .")

print("It was a hot", unicodedata.lookup("sun with face"), "day. We went to get", unicodedata.lookup("strawberry"), "after playing with our", unicodedata.lookup("dog"), ".")
