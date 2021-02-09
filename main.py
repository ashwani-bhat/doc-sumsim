from doc import DocumentFeature
import argparse
from pdftotext import PdfConverter

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('--threshold', help=" should be between 0 (same) and 2 (totally different)", required=True)
    requiredNamed.add_argument('--pdf-dir', required=True)
    
    optionalNamed = parser.add_argument_group('optional arguments')
    optionalNamed.add_argument('--clean', action='store_true', default=False, help='clean the dataset')
    optionalNamed.add_argument('--verbose', action='store_true', default=False, help='clean the dataset')
    optionalNamed.add_argument('--one', action='store_true', default=False, help='clean the dataset')
    
    args = parser.parse_args()

    threshold = float(args.threshold)  # should be between 0 (same) and 2 (totally different)
    clean = args.clean
    pdf_dir = args.pdf_dir
    verbose = args.verbose
    one = args.one

    # Convert all pdfs and store it in json
    pdfConverter = PdfConverter(pdf_dir)
    pdfConverter.convertall()

    doc = DocumentFeature(pdf_dir, clean)
    doc.create_features()

    if one:
        roll_no = str(input("Enter the roll number: \t"))
        print(doc.compare_one(roll_no, threshold, verbose))
    else:
        print(doc.compare_all(threshold, verbose))
    
