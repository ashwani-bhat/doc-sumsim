from scipy.spatial import distance
from nltk.corpus import stopwords
import string

def cosine_similarity(one, two):
    '''
    cosine similarity -> [0 (same), 2 (exactly opposite)]
    '''

    return distance.cosine(one, two)


def clean_document(text):
    '''
    Removes punctuation and stop words from the document 
    '''

    text = ''.join(c for c in text if c not in string.punctuation)
    text = ''.join([c for c in text if not c.isdigit()])
    st = stopwords.words('english')
    text = ' '.join([c.lower() for c in text.split() if c.lower() not in st])

    return text
