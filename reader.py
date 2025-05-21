import re

# Import file


# Token count
def token_count(text):
    # Split the text into words using regex to handle punctuation
    words = re.findall(r'\b\w+\b', text)
    return len(words)


