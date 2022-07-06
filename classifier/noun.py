import spacy


class Noun:
    """"
    Noun is a classifier to retrieves all nouns in a text
    """
    def __init__(self, spacy_model):
        self.__spacy_model = spacy_model
        self.__nlp = spacy.load(self.__spacy_model)

    def classify(self, text) -> []:
        """
        :param text: it's a string with sentences.
        :return: a list of the nouns found
        """
        doc = self.__nlp(text)
        sentences = list(doc.sents)
        nouns = []

        for sentence in sentences:
            for token in sentence:
                if token.pos_ == "NOUN":
                    nouns.append(token)

        return nouns
