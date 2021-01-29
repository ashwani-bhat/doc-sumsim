from doc import DocumentFeature
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--threshold', default=, help=" should be between 0 (same) and 2 (totally different)")
    parser.add_argument('--source', default=)
    parser.add_argument('--dir', action='store_true')
    parser.add_argument('--dir', default=)
    args = parser.parse_args()

    threshold = args.threshold  # should be between 0 (same) and 2 (totally different)
    student_roll_no = args.source

    doc = DocumentFeature(args.dir)
    df = doc.get_features()
    print(df.head())
    doc.view_corpus()
    doc.get_similar_docs(df, student_roll_no, threshold)
