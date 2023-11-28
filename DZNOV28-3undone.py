from gensim import corpora
def create_token_dictionary(text):
    tokens = text.split()
    dictionary = corpora.Dictionary
    return dictionary

text_to_check = "This is a test sentence to create a token dictionary."
token_dictionary = create_token_dictionary(text_to_check)

print("Уникальные токены:", token?????
