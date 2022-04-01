import math
import traceback

from PySide2 import QtCore
from PySide2.QtCore import QThread, Signal

from lib.general_files import GeneralFiles
from lib.merge_core import EmptyFolderException, PDFCore
from lib.special_files import SpecialFiles


class OptionOneThread(QThread):
    def __init__(self, input_path, output_path):
        QThread.__init__(self)
        self.app = SpecialFiles(input_path, output_path)
        self.number_of_files = self.app.get_number_of_files()
        self.signals = WorkerSignals()

    def __del__(self):
        self.wait()

    def generate_output_processes(self):
        nfiles_done = 0
        self.signals.start.emit()
        for message in self.app.merge():
            if type(message) == int:
                nfiles_done = message
            else:
                self.signals.message.emit(message)
            percent = (100 * nfiles_done / self.number_of_files)
            self.signals.progress.emit(math.floor(percent))

    def run(self):
        try:
            self.generate_output_processes()
        except EmptyFolderException:
            print("error")
            self.signals.error.emit(
                "لا توجد مستندات تحتاج إلى دمج في هذا المجلد \n تأكد من تسميات المستندات أو مسار المستندات"
            )
        except Exception:
            traceback.print_exc()
            self.signals.error.emit("حدد أماكن المدخلات و المخرجات")
        else:
            self.signals.done.emit(int(self.number_of_files))


class OptionTwoThread(QThread):
    def __init__(self, pdf_files: list, output_file_name: str, output_path: str, get_number_of_files):
        QThread.__init__(self)
        self.app = GeneralFiles(pdf_files, output_file_name, output_path)
        self.number_of_files = get_number_of_files
        self.signals = WorkerSignals()

    def __del__(self):
        self.wait()

    def generate_output_processes(self):
        nfiles_done = 0
        self.signals.start.emit()
        for message in self.app.merge():
            if type(message) == int:
                nfiles_done = message
            else:
                self.signals.message.emit(message)
            percent = (100 * nfiles_done / self.number_of_files)
            self.signals.progress.emit(math.floor(percent))

    def run(self):
        try:
            self.generate_output_processes()
        except EmptyFolderException:
            print("error")
            self.signals.error.emit(
                "لا توجد مستندات تحتاج إلى دمج في هذا المجلد \n تأكد من تسميات المستندات أو مسار المستندات"
            )
        except Exception:
            traceback.print_exc()
            self.signals.error.emit("حدد أماكن المدخلات و المخرجات")
        else:
            self.signals.done.emit(int(self.number_of_files))


class CardsThread(QThread):
    card = Signal(object)

    def __init__(self):
        QThread.__init__(self)

    def add_card(self, card: object):
        self.card.emit(card)


class WorkerSignals(QtCore.QObject):
    # finished = Signal()  # QtCore.Signal
    start = Signal()
    done = Signal(int)
    error = Signal(str)
    progress = Signal(int)
    message = Signal(list)
