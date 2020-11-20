import difflib
import argparse
import os


def load_file(file_path):
    with open(file_path) as f:
        return f.readlines()


def diff_file(file_standard, file_compare):
    content_standard = load_file(file_standard)
    content_compare = load_file(file_compare)
    diff = difflib.HtmlDiff()
    result = diff.make_file(content_standard, content_compare, file_standard, file_compare, context=True)
    with open('./result.html', 'w') as rf:
        rf.write(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="require two file parameters")
    parser.add_argument("-f1", "--file_standard", action='store', dest='file_standard',
                        help="file path which has content to be standard")
    parser.add_argument("-f2", "--file_compare", action='store', dest='file_compare',
                        help="file path which has content to compare")
    args = parser.parse_args()
    diff_file(args.file_standard, args.file_compare)
    # result_file_path = os.path.join(os.getcwd(),"result.html")
    os.system("python qresult.py")
    print("Done")
