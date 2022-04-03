# import pretty_errors
import sys
import re
import random
import yaml


def get_words(string:str) -> str:
    """
    Extract words from a string, stripping out punctuation, spaces
    """
    return re.compile("\w+").findall(string)


def redact_bad_words(string: str, bad_words: list, redaction_chars: list) -> str:
    redacted_str = string
    all_words = get_words(string)
    for word in all_words:
        if word in bad_words:
            try:
                replacement_char = random.choice(redaction_chars)
                redacted_str = re.sub(
                    word,
                    replacement_char * len(word),
                    redacted_str,
                    flags=re.IGNORECASE,
                    count=1, # only replace first instance with THIS redactment_char
                )
            except:
                redacted_str = redacted_str
        else:
            pass

    return redacted_str


with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

with open(config["bad_word_file"], "r") as file:
    bad_words = file.readlines()
    bad_words = [word.strip() for word in bad_words]

redaction_chars = config["replacements"]

# handle stream input
if not sys.stdin.isatty():
    input_stream = sys.stdin

# otherwise, read the given filename
else:
    try:
        input_filename = sys.argv[1]
    except IndexError:
        message = "need filename as first argument if stdin is not full"
        raise IndexError(message)
    else:
        input_stream = open(input_filename, "r")

input_stream = input_stream.read()

# replace bad words with redaction_chars
redacted = redact_bad_words(input_stream, bad_words, redaction_chars)

# print to stdout
print(redacted)
