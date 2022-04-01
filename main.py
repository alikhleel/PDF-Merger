import os
import sys
import time
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QSize, QUrl, Signal
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolButton


from lib.general_files import GeneralFiles
from lib.merge_core import PDFCore
from lib.threads import OptionOneThread, WorkerSignals, CardsThread, OptionTwoThread
from ui.card import Ui_Form
from ui.main_page import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.path = ""
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("دامج المستندات - نسخة تجريبية")
        # myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.set_icon()
        self.option = 1
        self.ui.generate_btn.clicked.connect(self.generate_btn)
        self.ui.output_btn.clicked.connect(self.get_output_folder_url)
        self.ui.radioButton_op_1.toggled.connect(
            lambda: self.change_option(self.ui.radioButton_op_1, 1))
        self.ui.radioButton_op_2.toggled.connect(
            lambda: self.change_option(self.ui.radioButton_op_2, 2))
        self.input_path = ""
        self.output_path = ""
        self.start_time = 0
        self.ui.progressBar.setValue(0)
        self.log_is_running = False
        self.ui.radioButton_op_1.setChecked(True)
        self.card_thread = CardsThread()
        self.card_thread.card.connect(self.manage_card)
        self.cards = []

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def set_icon(self):
        app_icon = QtGui.QIcon()
        # application/ui/img/
        # self.resource_path('img\pdf_32.png')
        app_icon.addFile(self.resource_path('img\pdf_32.png'),
                         QtCore.QSize(32, 32))
        app_icon.addFile(self.resource_path('img\pdf_64.png'),
                         QtCore.QSize(64, 64))
        app_icon.addFile(self.resource_path('img\pdf_128.png'),
                         QtCore.QSize(128, 128))
        app_icon.addFile(self.resource_path('img\pdf_256.png'),
                         QtCore.QSize(256, 256))
        app_icon.addFile(self.resource_path('img\pdf_512.png'),
                         QtCore.QSize(512, 512))
        self.setWindowIcon(app_icon)

    def reset(self):
        self.cards = []
        self.path = ""
        self.input_path = ""
        self.output_path = ""
        self.start_time = 0
        self.ui.progressBar.setValue(0)
        self.log_is_running = False
        self.ui.input_text.setText('')
        self.ui.input_btn.clicked.connect(self.get_input_folder_url)
        self.ui.input_btn.clicked.disconnect()

    def change_option(self, radio_btn, opt):
        if not self.log_is_running:
            self.reset()
            if radio_btn.isChecked():
                self.option = opt
                if opt == 1:
                    self.ui.input_btn.setText("اختيار مجلد الأدخال")
                    self.ui.input_btn.clicked.connect(
                        self.get_input_folder_url)
                    self.ui.scrollArea.setVisible(False)
                    self.ui.input_text.setVisible(True)
                elif opt == 2:
                    self.ui.input_btn.setText("إضافة ملفات جديدة")
                    self.ui.input_btn.clicked.connect(
                        self.get_input_files_urls)
                    self.ui.scrollArea.setVisible(True)
                    self.ui.input_text.setVisible(False)

    def get_input_files_urls(self):
        if not PDFCore.is_fill(self.path):
            self.path = os.environ['USERPROFILE'] + '\\Desktop'

        files = QtWidgets.QFileDialog.getOpenFileUrls(self,
                                                      'مكان مجلد الإدخال',
                                                      QUrl(self.path),
                                                      "PDF Files (*.pdf)")
        for file in files[0]:
            widget = QWidget()
            self.card_thread.add_card((widget, file))

    def manage_card(self, card):
        scroll_area = self.ui.scroll_list_input_files
        self.cards.append(card)
        Ui_Form().setupUi(card[0])
        card[0].findChild(QLabel, 'name_file_card').setText(card[1].fileName())
        card[0].findChild(
            QToolButton,
            'delete__btn_card').clicked.connect(lambda: self.delete_card(card))
        scroll_area.layout().addWidget(card[0])

    def delete_card(self, card):
        print(self.cards)
        self.cards.remove(card)
        card[0].deleteLater()
        self.ui.scroll_list_input_files.update()

    def get_input_folder_url(self):
        input_text = self.ui.input_text
        output_text = self.ui.output_text
        desktop = os.environ['USERPROFILE'] + '\\Desktop'
        if not (PDFCore.is_fill(input_text.text())):
            name = QtWidgets.QFileDialog.getExistingDirectory(
                self, 'مكان مجلد الإدخال', desktop)
        else:
            name = QtWidgets.QFileDialog.getExistingDirectory(
                self, 'مكان مجلد الإدخال', input_text.text())
        if PDFCore.is_fill(name):
            input_text.setText(name)

        if not (PDFCore.is_fill(output_text.text())):
            output_text.setText('/'.join(name.split('/')[0:-1]))

    def get_output_folder_url(self):
        output_text = self.ui.output_text
        desktop = os.environ['USERPROFILE'] + '\\Desktop'
        if not (PDFCore.is_fill(output_text.text())):
            name = QtWidgets.QFileDialog.getExistingDirectory(
                self, 'مكان مجلد الإخراج', desktop)
        else:
            name = QtWidgets.QFileDialog.getExistingDirectory(
                self, 'مكان مجلد الإخراج', output_text.text())
        if PDFCore.is_fill(name):
            output_text.setText(name)

    def generate_btn(self):
        if self.option == 1:
            self.generate_special_output()
        elif self.option == 2:
            self.generate_general_output()

    def generate_general_output(self):
        self.output_path = self.ui.output_text.text()
        files = []
        for file in self.cards:
            files.append(QUrl(file[1]).path()[1::].replace('/', '\\'))
        if not self.log_is_running:
            self.log_rest()
            self.input_path = self.ui.input_text.text()
            self.output_path = self.ui.output_text.text()
            self.myThread = OptionTwoThread(files, 'output', self.output_path,
                                            len(self.cards))
            self.myThread.signals.start.connect(self.start_log)
            self.myThread.signals.message.connect(self.handle_output)
            self.myThread.signals.done.connect(self.done_log)
            self.myThread.signals.error.connect(self.terminate_log)
            self.myThread.signals.progress.connect(self.update_progressbar)
            self.myThread.start()

    def log_rest(self):
        log_text = self.ui.log_text
        log_text.clear()
        log_text.setAlignment(QtCore.Qt.AlignRight)
        log_text.setTextColor('black')
        log_text.setFontPointSize(12)

    def handle_output(self, message):
        log_text = self.ui.log_text
        if message[0]:
            log_text.setTextColor('green')
            log_text.append("\n" + message[1])
            if len(self.cards) != 0:
                self.delete_card(self.cards[0])
        else:
            log_text.setTextColor('red')
            log_text.append("\n" + message[0])
        log_text.moveCursor(QtGui.QTextCursor.End)
        log_text.ensureCursorVisible()

    def generate_special_output(self):
        if not self.log_is_running:
            self.log_rest()
            self.input_path = self.ui.input_text.text()
            self.output_path = self.ui.output_text.text()
            self.myThread = OptionOneThread(self.input_path, self.output_path)
            self.myThread.signals.start.connect(self.start_log)
            self.myThread.signals.message.connect(self.handle_output)
            self.myThread.signals.done.connect(self.done_log)
            self.myThread.signals.error.connect(self.terminate_log)
            self.myThread.signals.progress.connect(self.update_progressbar)
            self.myThread.start()

    def start_log(self):
        self.log_is_running = True
        log_text = self.ui.log_text
        log_text.setText("بدأ المعالجة ...")
        self.set_radio_enabled(False)
        self.start_time = time.perf_counter()

    def set_radio_enabled(self, checkable):
        if checkable:
            self.ui.radioButton_op_1.setEnabled(True)
            self.ui.radioButton_op_2.setEnabled(True)
        else:
            self.ui.radioButton_op_1.setEnabled(False)
            self.ui.radioButton_op_2.setEnabled(False)

    def done_log(self, total_number_files=0):
        log_text = self.ui.log_text
        seconds = time.perf_counter() - self.start_time
        log_text.append("\n")
        log_text.append("\n")
        log_text.setAlignment(QtCore.Qt.AlignCenter)
        log_text.setTextColor('black')
        log_text.setFontWeight(2)
        log_text.append(" تمت العملية بنجاح\n")
        log_text.setAlignment(QtCore.Qt.AlignLeft)
        log_text.append(f'الوقت : {seconds:0.2f} ثانية')
        log_text.append(
            f'عدد المستندات التي تم دمجها : {total_number_files} مستند')

        self.log_is_running = False
        self.set_radio_enabled(True)

    def terminate_log(self, message):
        log_text = self.ui.log_text
        log_text.setTextColor('red')
        log_text.setText(message)
        self.log_is_running = False
        self.set_radio_enabled(True)

    def update_progressbar(self, value):
        self.ui.progressBar.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
