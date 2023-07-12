# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_fn_plotter_window(object):
    def setupUi(self, fn_plotter_window):
        if not fn_plotter_window.objectName():
            fn_plotter_window.setObjectName(u"fn_plotter_window")
        fn_plotter_window.resize(640, 530)
        self.control_group = QGroupBox(fn_plotter_window)
        self.control_group.setObjectName(u"control_group")
        self.control_group.setGeometry(QRect(20, 290, 600, 131))
        self.fx_label = QLabel(self.control_group)
        self.fx_label.setObjectName(u"fx_label")
        self.fx_label.setGeometry(QRect(10, 40, 29, 25))
        self.fx_input = QLineEdit(self.control_group)
        self.fx_input.setObjectName(u"fx_input")
        self.fx_input.setGeometry(QRect(40, 40, 200, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fx_input.sizePolicy().hasHeightForWidth())
        self.fx_input.setSizePolicy(sizePolicy)
        self.fx_input.setMinimumSize(QSize(200, 0))
        self.min_input = QLineEdit(self.control_group)
        self.min_input.setObjectName(u"min_input")
        self.min_input.setGeometry(QRect(470, 40, 93, 25))
        self.max_input = QLineEdit(self.control_group)
        self.max_input.setObjectName(u"max_input")
        self.max_input.setGeometry(QRect(470, 80, 93, 25))
        self.plot_button = QPushButton(self.control_group)
        self.plot_button.setObjectName(u"plot_button")
        self.plot_button.setGeometry(QRect(250, 100, 100, 25))
        self.label = QLabel(self.control_group)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 40, 31, 17))
        self.label_2 = QLabel(self.control_group)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 80, 41, 17))
        self.plot = QGroupBox(fn_plotter_window)
        self.plot.setObjectName(u"plot")
        self.plot.setGeometry(QRect(10, 10, 620, 280))
        self.groupBox = QGroupBox(fn_plotter_window)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 440, 620, 75))
        self.status_output = QTextEdit(self.groupBox)
        self.status_output.setObjectName(u"status_output")
        self.status_output.setEnabled(True)
        self.status_output.setGeometry(QRect(10, 35, 600, 25))
        self.status_output.setMouseTracking(False)
        self.status_output.setAcceptDrops(False)
        self.status_output.setUndoRedoEnabled(False)
        self.status_output.setReadOnly(True)

        self.retranslateUi(fn_plotter_window)

        QMetaObject.connectSlotsByName(fn_plotter_window)
    # setupUi

    def retranslateUi(self, fn_plotter_window):
        fn_plotter_window.setWindowTitle(QCoreApplication.translate("fn_plotter_window", u"Dialog", None))
        self.control_group.setTitle(QCoreApplication.translate("fn_plotter_window", u"Control", None))
        self.fx_label.setText(QCoreApplication.translate("fn_plotter_window", u"F(x):", None))
        self.plot_button.setText(QCoreApplication.translate("fn_plotter_window", u"Plot", None))
        self.label.setText(QCoreApplication.translate("fn_plotter_window", u"Min:", None))
        self.label_2.setText(QCoreApplication.translate("fn_plotter_window", u"Max:", None))
        self.plot.setTitle(QCoreApplication.translate("fn_plotter_window", u"Plot", None))
        self.groupBox.setTitle(QCoreApplication.translate("fn_plotter_window", u"Output", None))
    # retranslateUi

