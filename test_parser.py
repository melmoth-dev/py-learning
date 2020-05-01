import re

number_regex = re.compile(r"(-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*(.*)", re.DOTALL)
def parse_number(src):
    match = number_regex.match(src)
    if match is not None:
        number, src = match.groups()
        return eval(number), src

string_regex = re.compile(r"('(?:[^\\']|\\['\\/bfnrt]|\\u[0-9a-fA-F]{4})*?')\s*(.*)", re.DOTALL)
def parse_string(src):
    match = string_regex.match(src)
    if match is not None:
        string, src = match.groups()
        return eval(string), src

def parse_word(word, value=None):
    l = len(word)
    def result(src):
        if src.startswith(word):
            return value, src[l:].lstrip()
    result.__name__ = "parse_%s" % word
    return result

parse_true = parse_word("true", True)
parse_false = parse_word("false", False)
parse_null = parse_word("null", None)

in_file = open('input.txt', 'r')

src = in_file.read()

n = parse_number(src)

print(str(n))
print(src)

in_file.close()