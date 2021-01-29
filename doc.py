import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from utils import cosine_similarity, clean_document

import scipy.sparse
import glob, os


class DocumentFeature():
    def __init__(self, dir, clean):

        corpus = []
        corpus_dict = {}
        os.chdir(dir)
        for file in glob.glob("*.txt"):
            f = open(file, 'r', encoding='utf-8')
            document = f.read()
            roll_no = file.split('.')[0]
            
            clean_text = document
            if clean:
                clean_text = clean_document(document)
            corpus.append(clean_text)
            corpus_dict[roll_no] = document
            f.close()
        
        self.corpus = corpus
        self.corpus_dict = corpus_dict
    


    def get_features(self):

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(self.corpus)
        feature_names = vectorizer.get_feature_names()

        vectorizer_cv = CountVectorizer(ngram_range=(2, 4))
        X_cv = vectorizer_cv.fit_transform(self.corpus)
        feature_names.extend(vectorizer_cv.get_feature_names())
        X = scipy.sparse.hstack([X, X_cv])

        dense = X.todense()
        denselist = dense.tolist()
        df = pd.DataFrame(denselist, columns=feature_names)
        
        df["Roll Number"] = self.corpus_dict.keys()
        df.set_index("Roll Number",inplace=True)

        return df


    def view_corpus(self):
        print("#################  Corpus #####################\n")
        print(self.corpus_dict)
        print("\n#############################################")

    def get_similar_docs(self, df, roll_no, threshold):
        current = df.loc[roll_no]
        for idx, row in df.iterrows():
            if idx != roll_no:
                two = row
                cs = cosine_similarity(current, two)
                if cs < threshold:
                    print(f"{roll_no} and {idx} has a cosine similarity of {cs}")