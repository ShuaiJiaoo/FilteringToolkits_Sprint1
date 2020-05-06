import sys
import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from process_miner import visualizer
from .centralWidget import Ui_centralWidget
import global_util


class ProMWidget(QWidget, Ui_centralWidget):
    def __init__(self):
        super().__init__()
        # loadUi("./centralWidget.ui", self)  # 加载UI文件
        self.setupUi(self)
        self.pushButtonOpen.clicked.connect(self.slot_btn_open_file)
        self.pushButtonRun.clicked.connect(self.slot_btn_show_result)
        self.file = ""

    @pyqtSlot()
    def slot_btn_open_file(self):
        print("1111111111111")
        self.file, file_type = QFileDialog.getOpenFileName(self, 'open file', './input_file', '*.xes;;*.csv;;')
        print(file_type)
        print(self.file)

    @pyqtSlot()
    def slot_btn_show_result(self):
        print("222222222222222222")
        output = visualizer.import_xes_data(self.file)
        output_full_name = global_util.get_full_path_output_file(output)
        png = QPixmap(output_full_name).scaled(self.labelImage.width(), self.labelImage.height())
        self.labelImage.setPixmap(png)
