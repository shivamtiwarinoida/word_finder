import os


def get_path(extension='.txt'):
    files_path = os.path.join(os.curdir,'words')
    files_full_path = [os.path.join(files_path,f) for f in os.listdir(files_path) if f.endswith(extension)]

    # for path in files_full_path:
    #     print(path)

    return  files_full_path

colour = {
    'red': '\033[93m',
    'base': '\033[0m'
}

def find_word(str):
    all_files = get_path()

    for file in all_files:
        with open(file,'r') as f:
            lines = f.readlines()
            # print(len(lines))
            for line in lines:
                if str in line:
                    matched_line=line.replace(str,f"{colour['red']}{str}{colour['base']}")
                    print(matched_line)
