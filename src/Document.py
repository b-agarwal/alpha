import uuid

class Document(object):
    def __init__(self, name, date, text):
        self.document_id = uuid.uuid4()
        self.document_name = name
        self.publishing_date = date
        self.raw_text = text
        self.sentences = []

class Sentence(object):
    def __init__(self, text, index, parentId):
        self.words = {}
        self.relations = []
        self.sentence_id = uuid.uuid4
        self.raw_sentence = text
        self.document_id = parentId
        index = 0
        for w in text.split():
            #if w.lower() in self.words:
            self.words[w.lower() + '_' + str(index)] = Word(index, self.sentence_id, w.lower())
            #else:
            #    self.words[w.lower()] = Word(index, self.sentence_id, w.lower())
            index = index + 1

class Word(object):
    def __init__(self, index, parentId, text):
        self.tags = {}
        self.ne_tag = ''
        self.pos_tag = ''
        self.index = index
        self.text = text
        self.sentence_id = parentId
