Run the following python command
- dir: directory for all the summaries in txt
- threshold for cosine threshold (cosine similarity -> [0 (same), 2 (exactly opposite)])
- source: name of the file without extension

`python main.py --threshold thres_number --source file_name --dir dir_name`

Example code:
`python main.py --threshold 0.5 --source sum1 --dir ./summaries`

In order to clean the document (i.e, remove stopwords, punctuation, digits):
`python main.py --threshold 0.5 --source sum1 --dir ./summaries --clean`