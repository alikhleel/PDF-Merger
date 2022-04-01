from PySide2.QtCore import QUrl

from lib.merge_core import EmptyFolderException, PDFCore


class GeneralFiles:
    def __init__(self, pdf_files: list, output_file_name: str, output_path: str):
        self.files = pdf_files
        self.output_path = output_path
        self.output_file_name = output_file_name

    def merge(self):
        done_files = 0
        if not len(self.files):
            raise EmptyFolderException("Empty Folder")
        for sub_file in PDFCore.merge(self.output_path, self.files, self.output_file_name, remove=False,
                                      get_result_in_each_file=True):
            try:
                done_files += 1
                sub_file = QUrl.fromLocalFile(sub_file).fileName()
                yield [True, "تم دمج ملف " + sub_file]
                yield done_files
            except Exception:
                yield ([
                    False, f'There are some errors when Combined {sub_file} files'])
                print(f'There are some errors when Combined {sub_file} files')


if __name__ == '__main__':
    # sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')
    input_files = [
        'D:\\ali-kh\\Desktop\\aaaa\\1440\\الجشة-1440.pdf',
        'D:\\ali-kh\\Desktop\\aaaa\\1440\\الجفر-1440.pdf',
        'D:\\ali-kh\\Desktop\\aaaa\\1440\\الحقل-1440.pdf'
    ]
    output_path = 'D:\\ali-kh\\Desktop\\aaaa\\output'
    app = GeneralFiles(input_files, 'zz', output_path)
    app.merge()
    print('The mission is done')
    input()
