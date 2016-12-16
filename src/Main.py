import nltk
from nltk.tag import StanfordNERTagger
from nltk.tag import StanfordPOSTagger
import uuid
import Document
import json
from Helper import GetASCIIString, MergeEntities
from CustomSerializer import CustomSerializer

NERTagger1 = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
NERTagger2 = StanfordNERTagger('english.muc.7class.distsim.crf.ser.gz')
POSTagger = StanfordPOSTagger('.\\stanford-postagger-full-2015-12-09\\models\\english-bidirectional-distsim.tagger', '.\\stanford-postagger-full-2015-12-09\\stanford-postagger.jar')


raw_document_text = 'Federer is married to former Women\'s Tennis Association '\
'player Mirka Vavrinec. He met her while both were competing for Switzerland in'\
'the 2000 Sydney Olympics. Couple of years later Vavrinec retired from the tour because of a'\
'foot injury.[35] They were married at Wenkenhof Villa in Riehen near Basel on'\
 '11 April 2009, surrounded by a small group of close friends and family.[36]'\
 'In July 2009, Mirka gave birth to identical twin girls, Myla Rose and Charlene'\
 ' Riva.[37] The Federers had another set of twins in 2014, this time boys whom'\
 '  they named Leo and Lennart,[38] called Lenny.[39]'

doc = Document.Document('RFWiki', '2016\/11\/22', raw_document_text);

json_str = json.dumps(doc, default=lambda o: o.__dict__)

tokens = nltk.sent_tokenize(doc.raw_text)

sentences = []

classes = ['money', 'percent', 'date', 'time']

index = 0
for sent in tokens:
    sent_object = Document.Sentence(sent, index, doc.document_id)
    index = index + 1
    tags1 = NERTagger1.tag(sent_object.raw_sentence.split())
    for i, t in enumerate(tags1):
        sent_object.words[GetASCIIString(t[0])+'_'+str(i)].ne_tag = GetASCIIString(t[1])
    tags2 = NERTagger2.tag(sent_object.raw_sentence.split())
    for i, t in enumerate(tags2):
        if GetASCIIString(t[1]) in classes:
            sent_object.words[GetASCIIString(t[0])+'_'+str(i)].ne_tag = GetASCIIString(t[1])

    tags3 = POSTagger.tag(sent_object.raw_sentence.split())
    for i, t in enumerate(tags3):
        sent_object.words[GetASCIIString(t[0])+'_'+str(i)].pos_tag = GetASCIIString(t[1])

    doc.sentences.append(sent_object)



json_str = json.dumps(doc, default=lambda o: o.__dict__)

target = open('debug.json','w')
try:
    target.write(json_str)
finally:
    target.close()
#Merge all the entities
MergeEntities(doc)
json_str = json.dumps(doc, default=lambda o: o.__dict__)

json_str = json.dumps(doc, default=lambda o: o.__dict__)

target = open('debug2.json','w')
try:
    target.write(json_str)
finally:
    target.close()
