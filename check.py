import os
import filetype
import argparse

def parse_args():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder_path", type=str,
                        help='Path to folder need guess')
    parser.add_argument('--file_path', type=str,
                        help='Path to file need guess')
    return parser.parse_args()


def guess_type(file_path):
    '''
    args:
        file_path(str): path to folder contain all file need guess type 
    '''
    kind = filetype.guess(file_path)
    if kind is None:
        print('Cannot guess file type!')
    else:
        if kind.extension == "pdf":
            print('File extension: %s' % kind.extension)
            print('File MIME type: %s' % kind.mime)

if __name__ == '__main__':
    args = parse_args()
    if args.folder_path == None:
        guess_type(args.file_path)
    else:
        for file_path in os.listdir(args.folder_path):
            file_path = os.path.join(file_path, args.folder_path)
            guess_type(file_path)