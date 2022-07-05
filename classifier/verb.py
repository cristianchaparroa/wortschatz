import spacy
import textacy.extract


class Verb:
    """"
    Verb is a classifier to retrieves all verbs in a text
    """

    def __init__(self, spacy_model):
        self.__spacy_model = spacy_model
        self.__nlp = spacy.load(self.__spacy_model)

    def classify(self, text) -> []:
        doc = self.__nlp(text)
        patterns = [{"POS": "VERB"}]
        verb_phrases = textacy.extract.token_matches(doc, patterns=patterns)

        verbs = []

        for verb in verb_phrases:
            verbs.append(verb)

        return verbs
