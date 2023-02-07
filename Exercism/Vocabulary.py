def make_word_groups(*vocab_words) -> str:
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    """ list_word = []

    for i, word in enumerate(vocab_words):
        if i == 0:
            list_word.append(vocab_words[0])
        else:
            list_word.append(vocab_words[0] + vocab_words[i])
    
    return str(" :: ".join(word for word in list_word)) """

    return f' :: {vocab_words[0]}'.join(vocab_words)

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    if word[-5:] == 'iness':
        return word[0:(len(word)-5)] + "y"
    elif word[-4:] == 'ness':
        return word[0:(len(word)-4)]
    return word

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """

    return sentence.split()[index] + "en" if "." not in sentence.split()[index] else sentence.split()[index][:-1] + "en"


#print(make_word_groups('en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture'))
print(make_word_groups('en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture'))
#print(remove_suffix_ness('happy'))
#print(adjective_to_verb('It got dark as the sun set.', 2))