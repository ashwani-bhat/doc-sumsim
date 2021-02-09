## Usage
```bash
$ python main.py --pdf-dir directory-containing-all-pdfs --threshold threshold-value \
[--clean] [--one] [--verbose]
```
- `pdf-dir`: directory containing all the summaries in pdf format (filenames should be roll_no.pdf). 
- `threshold`: cosine threshold (cosine similarity -> [0 (same), 2 (exactly opposite)]).
- `clean`: remove punctuations and stopwords from the corpus.
- `one`: run this script for only one student roll number. You will be prompted to enter the roll number.
- `verbose`: print the cosine similarity of every similar summaries

### Example scripts
```bash
$ python main.py --threshold 0.7 --pdf-dir ./pdfs 
```
```bash
$ python main.py --threshold 0.8 --pdf-dir ./pdfs --verbose --one

Enter the roll number:   
```
