from Document import Document, Sentence, Word

def GetASCIIString(str):
    return str.encode('ascii', 'ignore').lower()

def GetSortingKey(element):
    return element.index

def MergeEntities(doc):
    lines = doc.sentences

    for line in lines:
        elements = list(line.words.values())
        sorted_elements = sorted(elements, key=GetSortingKey)
        count = 0
        for i, elem in enumerate(sorted_elements):
            if(0 == i):
                continue
            if(sorted_elements[i-1].ne_tag == sorted_elements[i].ne_tag):
                count = count + 1
            else:
                entity = line.words[sorted_elements[i-count-1].text + '_' + str(sorted_elements[i-count-1].index)]
                while(count > 0):
                    e = sorted_elements[i - count].text
                    entity.text = entity.text + ' ' + e

                    #To be removed
                    elements.remove(sorted_elements[i - count])

                    del line.words[e + '_' + str(sorted_elements[i - count].index)]
                    count = count - 1

        print elements
