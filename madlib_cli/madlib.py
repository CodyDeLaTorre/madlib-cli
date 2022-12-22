print("Welcome to a MadLib game. I will ask for adjectives or nouns and you will type in whatever you want")


def read_template(string):
    with open(string, 'r') as reader:
        return reader.read()


def parse_template(template):
    words = []
    stripped_sent = ""

    capturing = False
    captured_words = ""

    for char in template:
        if capturing:
            if char == "}":
                words.append(captured_words)
                stripped_sent += char
                captured_words = ""
                capturing = False
            else:
                captured_words += char
        else:
            stripped_sent += char
            if char == "{":
                capturing = True
    return stripped_sent, tuple(words)


def merge(string, tup):
    txt = string.format(tup[0], tup[1], tup[2])
    return txt


