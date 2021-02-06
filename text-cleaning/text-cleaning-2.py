import re
from transliterate import translit, get_available_language_codes

text = ['This is dirty TEXT: A phone number +001234561234, moNey 3.333, some date like 09.08.2016 and weird Čárákterš.']

for line in text:
    # line = line.decode('utf8')
    APPOSTOPHES = {
        "+": " ",
        ".": " ",
        ",": " ",
        ":": " "
    }
    # remove punctuations
    reformed = ''.join([APPOSTOPHES[w] if w in APPOSTOPHES else w for w in line])
    print(reformed)

    # remove numbers
    print(re.sub("(^|\W*)\d+($|W*)", "", line))

    # filter number via function
    def is_digit(word):
        try:
            int(word)
            return True
        except ValueError:
            return False

    #num_removed = ''.join('' if is_digit(w) else w for w in reformed)
    new_line = []
    for w in reformed.split():
        if not is_digit(w):
            new_line.append(w)
    num_removed = " ".join(new_line)
    print(num_removed)

    # retain lowercase and special characters
    # using transliterate
    print(get_available_language_codes())
    line = translit(line, reversed=True)
    line = line.lower()
    print(line)
    # using user-defined dict
    cedilla2latin = [[u'Á', u'A'], [u'á', u'a'], [u'Č', u'C'], [u'č', u'c'], [u'Š', u'S'], [u'š', u's']]
    tr = dict([(a[0], a[1]) for (a) in cedilla2latin])
    print(tr)

    def transliterate(line):
        translated = ""
        for letter in line:
            if letter in tr:
                translated += tr[letter]
            else:
                translated += letter
        return translated

    print(transliterate(line).lower())
