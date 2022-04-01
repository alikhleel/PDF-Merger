import os
import re
import time

from lib.merge_core import EmptyFolderException, PDFCore


class SpecialFiles:
    def __init__(self, in_path, out_path):
        self.type = ".pdf"  # type of file
        self.input_path = in_path  # path of input files
        self.output_path = out_path  # path of output files
        self.name = ""  # a temp name of file that will change inside loop
        self.files = self._search()

    def _search(self):
        regex = re.compile(r'.*?\d{4}\.(pdf$)')
        names = []
        for root, dirs, files in os.walk(self.input_path):
            for file in files:
                if regex.match(file):
                    names.append(file)
        return names

    def _get_names(self, name: str) -> list:
        sub_files = [self.input_path + '\\' + name]
        exist = True
        num = 1
        while exist:
            sub_file_name = name[0:-4] + str(num) + self.type
            if os.path.exists(self.input_path + '\\' + sub_file_name):
                sub_files.append(self.input_path + '\\' + sub_file_name)
                name = sub_file_name
            else:
                exist = False
            num += 1
        return sub_files

    def get_number_of_files(self):
        number_of_files = 0
        for file in self.files:
            if str(file).endswith(self.type):
                name = file
            else:
                name = file + self.type
            number_of_files += len(self._get_names(name))
        return number_of_files

    def merge(self):
        print('login')
        done_files = 0
        if len(self.files) == 0:
            raise EmptyFolderException("")
        for file in self.files:
            if str(file).endswith(self.type):
                name = file
            else:
                name = file + self.type
            sub_files = self._get_names(name)
            year = re.findall(r'\d+', name)[0]
            try:
                for _ in PDFCore.merge(self.output_path, sub_files, name, year, remove=False,
                                       get_result_in_each_file=False):
                    pass
                done_files += len(sub_files)
                yield [True, "تم دمج مجموعة " + file]
                yield done_files
            except Exception:
                yield ([
                    False, f'There are some errors when Combined {name} files'])
                print(f'There are some errors when Combined {name} files')


if __name__ == '__main__':
    # sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')
    print('''
    This Program is used to combine PDFs which named with a specific structure.\
    The structure is like [name-YYYY.pdf] and in which the 'YYYY' is the year of that file.\
    And the files that will combine with it should be [name-YYYY.pdf], [name-YYYY1.pdf], [name-YYYY12.pdf] ...
    
    
            ''')
    input_path = input(
        "Enter path of the folder that contains files you want to combine:\n")
    output_path = input(
        "Enter the path of the output folder (the program will organize them): \n"
    )
    app = SpecialFiles(input_path, output_path)
    app.merge()
    print('The mission is done')
    input()
