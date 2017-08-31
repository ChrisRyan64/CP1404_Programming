"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
COLOUR_HEXADECIMALS = {"siena": "#a0522d", "rebeccapurple": "#663399", "PapayaWhip": "#ffefdy", "orchid1": "#ff83fa",
                       "OldLace": "#fdf5e6", "MintCream": "#f5fffa", "linen": "#faf0e6", "light": "#eedd82",
                       "LawnGreen": "#7cfc00", "gray49": "#7d7d7d"}
# print(STATE_NAMES)


def main():
    """
    (Walk-Through)
    state = input("Enter short state: ").upper()
    while state != "":
        if state in STATE_NAMES:
            print(state, "is", STATE_NAMES[state])
        else:
            print("Invalid short state")
    state = input("Enter short state: ").upper()
    for key, value in STATE_NAMES.items():
        print("{:3} is {}".format(key, value))
    (Intermediate Exercise)
    colour = input("Colour: ")
    while colour != "":
        if colour in COLOUR_HEXADECIMALS:
            print(COLOUR_HEXADECIMALS[colour])
        colour = input("Colour: ")"""
    text = input("Enter text: ")
    words = []
    words_count_dict = {}
    largest_word = 0
    user_words = text.split(" ")
    for word in user_words:
        if len(word) > largest_word:
            largest_word = len(word)
        if word in words_count_dict.keys():
            words_count_dict[word] += 1
        else:
            words_count_dict[word] = 1
    words_keys = list(words_count_dict.keys())
    words_keys.sort()
    for word in words_keys:
        print("{0:{2}} : {1}".format(word, words_count_dict[word], largest_word))

main()
