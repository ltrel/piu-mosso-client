# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lesson_info.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_LessonInfoForm(object):
    def setupUi(self, LessonInfoForm):
        if not LessonInfoForm.objectName():
            LessonInfoForm.setObjectName(u"LessonInfoForm")
        LessonInfoForm.resize(869, 555)
        self.verticalLayout = QVBoxLayout(LessonInfoForm)
        self.verticalLayout.setSpacing(26)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(12)
        self.date_label = QLabel(LessonInfoForm)
        self.date_label.setObjectName(u"date_label")

        self.gridLayout.addWidget(self.date_label, 1, 0, 1, 1)

        self.student_label = QLabel(LessonInfoForm)
        self.student_label.setObjectName(u"student_label")

        self.gridLayout.addWidget(self.student_label, 0, 0, 1, 1)

        self.location_label = QLabel(LessonInfoForm)
        self.location_label.setObjectName(u"location_label")

        self.gridLayout.addWidget(self.location_label, 0, 1, 1, 1)

        self.duration_label = QLabel(LessonInfoForm)
        self.duration_label.setObjectName(u"duration_label")

        self.gridLayout.addWidget(self.duration_label, 2, 0, 1, 1)

        self.instrument_label = QLabel(LessonInfoForm)
        self.instrument_label.setObjectName(u"instrument_label")
        self.instrument_label.setWordWrap(False)

        self.gridLayout.addWidget(self.instrument_label, 1, 1, 1, 1)

        self.attendance_checkbox = QCheckBox(LessonInfoForm)
        self.attendance_checkbox.setObjectName(u"attendance_checkbox")

        self.gridLayout.addWidget(self.attendance_checkbox, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(LessonInfoForm)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.notes_textbox = QPlainTextEdit(LessonInfoForm)
        self.notes_textbox.setObjectName(u"notes_textbox")

        self.verticalLayout_2.addWidget(self.notes_textbox)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.save_button = QPushButton(LessonInfoForm)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_2.addWidget(self.save_button)

        self.discard_button = QPushButton(LessonInfoForm)
        self.discard_button.setObjectName(u"discard_button")

        self.horizontalLayout_2.addWidget(self.discard_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(LessonInfoForm)

        QMetaObject.connectSlotsByName(LessonInfoForm)
    # setupUi

    def retranslateUi(self, LessonInfoForm):
        LessonInfoForm.setWindowTitle(QCoreApplication.translate("LessonInfoForm", u"Lesson Info", None))
        self.date_label.setText(QCoreApplication.translate("LessonInfoForm", u"Date:", None))
        self.student_label.setText(QCoreApplication.translate("LessonInfoForm", u"Student:", None))
        self.location_label.setText(QCoreApplication.translate("LessonInfoForm", u"Location:", None))
        self.duration_label.setText(QCoreApplication.translate("LessonInfoForm", u"Duration:", None))
        self.instrument_label.setText(QCoreApplication.translate("LessonInfoForm", u"Instrument:", None))
        self.attendance_checkbox.setText(QCoreApplication.translate("LessonInfoForm", u"Attendance", None))
        self.label_2.setText(QCoreApplication.translate("LessonInfoForm", u"Lesson Notes:", None))
        self.save_button.setText(QCoreApplication.translate("LessonInfoForm", u"Save Changes", None))
        self.discard_button.setText(QCoreApplication.translate("LessonInfoForm", u"Discard Changes", None))
    # retranslateUi

