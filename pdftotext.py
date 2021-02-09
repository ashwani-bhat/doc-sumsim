from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re
import glob, os
import json

class PdfConverter:
    def __init__(self, path):
        self.path = path

    def convert_pdf_to_txt(self, file_path):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        fp = open(file_path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
            interpreter.process_page(page)
        
        fp.close()
        device.close()
        string = retstr.getvalue()
        string = " ".join(string.split('\n')[2:]) # dont add name and roll number
        string = " ".join(string.split()) # split by all the whitespaces and join by one space
        swo_i = re.sub(r"\(\d+\)", '', string) # remove equation numbers
        retstr.close()
        return swo_i

    def convertall(self):
        corpus = {}
        os.chdir(self.path)
        for file in glob.glob("*.pdf"):
            content = self.convert_pdf_to_txt(file)
            corpus[file.split('.')[0]] = [content]
        
        # print(corpus)
        os.chdir("../")
        with open("corpus.json", "w", encoding='utf-8') as out:  
            json.dump(corpus, out, indent=2)  
