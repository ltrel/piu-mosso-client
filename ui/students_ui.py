# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'students.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_StudentsForm(object):
    def setupUi(self, StudentsForm):
        if not StudentsForm.objectName():
            StudentsForm.setObjectName(u"StudentsForm")
        StudentsForm.resize(1000, 600)
        self.horizontalLayout = QHBoxLayout(StudentsForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar_frame = QFrame(StudentsForm)
        self.sidebar_frame.setObjectName(u"sidebar_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_frame.sizePolicy().hasHeightForWidth())
        self.sidebar_frame.setSizePolicy(sizePolicy)
        self.sidebar_frame.setFrameShape(QFrame.StyledPanel)
        self.sidebar_frame.setFrameShadow(QFrame.Raised)
        self.sidebar_layout = QVBoxLayout(self.sidebar_frame)
        self.sidebar_layout.setObjectName(u"sidebar_layout")

        self.horizontalLayout.addWidget(self.sidebar_frame)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.students_listwidget = QListWidget(StudentsForm)
        self.students_listwidget.setObjectName(u"students_listwidget")

        self.gridLayout.addWidget(self.students_listwidget, 1, 0, 1, 1)

        self.label = QLabel(StudentsForm)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(StudentsForm)

        QMetaObject.connectSlotsByName(StudentsForm)
    # setupUi

    def retranslateUi(self, StudentsForm):
        StudentsForm.setWindowTitle(QCoreApplication.translate("StudentsForm", u"Students", None))
        self.label.setText(QCoreApplication.translate("StudentsForm", u"All Students:", None))
    # retranslateUi

