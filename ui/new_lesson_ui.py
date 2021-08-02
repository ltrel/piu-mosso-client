# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_lesson.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_NewLessonForm(object):
    def setupUi(self, NewLessonForm):
        if not NewLessonForm.objectName():
            NewLessonForm.setObjectName(u"NewLessonForm")
        NewLessonForm.resize(1000, 600)
        self.horizontalLayout = QHBoxLayout(NewLessonForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar_frame = QWidget(NewLessonForm)
        self.sidebar_frame.setObjectName(u"sidebar_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_frame.sizePolicy().hasHeightForWidth())
        self.sidebar_frame.setSizePolicy(sizePolicy)
        self.sidebar_layout = QVBoxLayout(self.sidebar_frame)
        self.sidebar_layout.setObjectName(u"sidebar_layout")

        self.horizontalLayout.addWidget(self.sidebar_frame)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(160, 20, 160, 20)
        self.label = QLabel(NewLessonForm)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(NewLessonForm)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.label_2 = QLabel(NewLessonForm)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(NewLessonForm)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.label_3 = QLabel(NewLessonForm)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.comboBox_3 = QComboBox(NewLessonForm)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout.addWidget(self.comboBox_3)

        self.label_4 = QLabel(NewLessonForm)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.timeEdit = QTimeEdit(NewLessonForm)
        self.timeEdit.setObjectName(u"timeEdit")

        self.verticalLayout.addWidget(self.timeEdit)

        self.calendarWidget = QCalendarWidget(NewLessonForm)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGridVisible(True)

        self.verticalLayout.addWidget(self.calendarWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(NewLessonForm)

        QMetaObject.connectSlotsByName(NewLessonForm)
    # setupUi

    def retranslateUi(self, NewLessonForm):
        NewLessonForm.setWindowTitle(QCoreApplication.translate("NewLessonForm", u"New Lesson", None))
        self.label.setText(QCoreApplication.translate("NewLessonForm", u"Student:", None))
        self.label_2.setText(QCoreApplication.translate("NewLessonForm", u"Location:", None))
        self.label_3.setText(QCoreApplication.translate("NewLessonForm", u"Instrument:", None))
        self.label_4.setText(QCoreApplication.translate("NewLessonForm", u"Date:", None))
    # retranslateUi

