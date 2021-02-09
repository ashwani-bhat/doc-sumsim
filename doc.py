import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from utils import cosine_similarity, clean_document

import scipy.sparse
import glob, os
import json

class DocumentFeature:
    def __init__(self, dir, clean):
        f = open('corpus.json', encoding='utf-8')
        self.corpus = json.load(f)

        if clean:
            self.corpus = {k: clean_document(str(v)) for k, v in self.corpus.items()}
        
        self.df = pd.DataFrame.from_dict(self.corpus, orient='index', columns=['Summary']).reset_index()
        self.df.columns = ['Roll Number', 'Summary']


    def create_features(self):
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(self.df['Summary'])
        feature_names = vectorizer.get_feature_names()

        vectorizer_cv = CountVectorizer(ngram_range=(2, 4))
        X_cv = vectorizer_cv.fit_transform(self.df['Summary'])
        feature_names.extend(vectorizer_cv.get_feature_names())
        X = scipy.sparse.hstack([X, X_cv])

        dense = X.todense()
        denselist = dense.tolist()
        df_x = pd.DataFrame(denselist, columns=feature_names)
        self.df = pd.concat([self.df, df_x], axis=1).drop('Summary', axis=1).set_index('Roll Number')

    def _find_similar(self, roll_no, x, threshold, verbose):
        if roll_no != x:
            cs = cosine_similarity(self.df.loc[roll_no], self.df.loc[x])
            if cs < threshold:
                if verbose:
                    print(f"{roll_no} and {x} has a cosine similarity of {cs}")
                return True

    def compare_one(self, roll_no, threshold, verbose=False):
        return list(filter(lambda x: self._find_similar(roll_no, x, threshold, verbose), \
            self.corpus.keys()))
    
    def compare_all(self, threshold, verbose=False):
        return {roll_no: list(filter(lambda x: self._find_similar(roll_no, x, threshold, verbose), \
            self.corpus.keys())) for roll_no in self.corpus.keys()}
