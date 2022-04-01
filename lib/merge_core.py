from PyPDF2.pdf import PdfFileReader, PdfFileWriter
import os

from PySide2.QtCore import Signal


class EmptyFolderException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class PDFCore:
    type = '.pdf'

    @staticmethod
    def remove(sub_files):
        for file in sub_files:
            os.remove(file)

    @staticmethod
    def is_fill(text):
        if text and text.strip():
            return True
        else:
            return False

    @staticmethod
    def merge(output_path: str, sub_files: list, final_name: str, sub_folder: str = '',
              remove: bool = True, get_result_in_each_file: bool = False):
        if final_name.endswith(PDFCore.type):
            final_name = final_name[0:-4]
        if not (sub_folder and sub_folder.strip()):
            sub_folder = final_name
        pdf_writer = PdfFileWriter()
        for sub_file in sub_files:
            pdf_reader = PdfFileReader(sub_file)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))
            if get_result_in_each_file:
                yield sub_file
        path = output_path + "\\" + sub_folder + "\\" + final_name + PDFCore.type

        try:
            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            with open(path, 'wb') as out:
                pdf_writer.write(out)
                if remove:
                    PDFCore.remove(sub_files)
                    return
        except OSError as exc:  # Guard against race condition
            raise Exception
