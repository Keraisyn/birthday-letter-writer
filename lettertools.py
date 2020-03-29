import random


def create_model():
    # Load in text
    text = open("text.txt", encoding="utf8").read()

    # Split into single words
    corpus = text.split()

    def make_pairs(corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])


    pairs = make_pairs(corpus)

    # Create a dictionary that lists the words that follow another word
    word_dict = {}

    for word1, word2 in pairs:
        if word1 in word_dict.keys():
            word_dict[word1].append(word2)
        else:
            word_dict[word1] = [word2]

    return corpus, word_dict


def create_chain(corpus, word_dict, n_words):
    # Random starting word that must be capitalized
    first_word = random.choice(corpus)

    while first_word.islower():
        first_word = random.choice(corpus)

    chain = [random.choice(["I", "You"])]

    # Randomly choose a word following the previous one
    for i in range(n_words):
        chain.append(random.choice(word_dict[chain[-1]]))

    if chain[-1][-1] not in [".", "!", "?"]:
        chain[-1] = chain[-1] + random.choice([".", ".", ".", ".", ".", "!", "!", "!", "?"])

    generated_text = " ".join(chain)

    return generated_text
