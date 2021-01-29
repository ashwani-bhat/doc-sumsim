from doc import DocumentFeature
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('--threshold', help=" should be between 0 (same) and 2 (totally different)", required=True)
    requiredNamed.add_argument('--source', required=True)
    requiredNamed.add_argument('--dir', required=True)
    requiredNamed.add_argument('--clean', action='store_true', default=False, help='clean the dataset')
    args = parser.parse_args()

    threshold = float(args.threshold)  # should be between 0 (same) and 2 (totally different)
    student_roll_no = str(args.source)
    clean = args.clean

    doc = DocumentFeature(args.dir, clean)
    df = doc.get_features()
    print(df.head())
    doc.view_corpus()
    doc.get_similar_docs(df, student_roll_no, threshold)
