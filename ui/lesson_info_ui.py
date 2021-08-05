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
        self.horizontalLayout = QHBoxLayout(LessonInfoForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(LessonInfoForm)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.student_label = QLabel(LessonInfoForm)
        self.student_label.setObjectName(u"student_label")

        self.verticalLayout.addWidget(self.student_label)

        self.date_label = QLabel(LessonInfoForm)
        self.date_label.setObjectName(u"date_label")

        self.verticalLayout.addWidget(self.date_label)

        self.duration_label = QLabel(LessonInfoForm)
        self.duration_label.setObjectName(u"duration_label")

        self.verticalLayout.addWidget(self.duration_label)

        self.location_label = QLabel(LessonInfoForm)
        self.location_label.setObjectName(u"location_label")

        self.verticalLayout.addWidget(self.location_label)

        self.instrument_label = QLabel(LessonInfoForm)
        self.instrument_label.setObjectName(u"instrument_label")
        self.instrument_label.setWordWrap(False)

        self.verticalLayout.addWidget(self.instrument_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(LessonInfoForm)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(False)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)

        self.notes_textbox = QPlainTextEdit(LessonInfoForm)
        self.notes_textbox.setObjectName(u"notes_textbox")

        self.verticalLayout_2.addWidget(self.notes_textbox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.save_button = QPushButton(LessonInfoForm)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_2.addWidget(self.save_button)

        self.discard_button = QPushButton(LessonInfoForm)
        self.discard_button.setObjectName(u"discard_button")

        self.horizontalLayout_2.addWidget(self.discard_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(LessonInfoForm)

        QMetaObject.connectSlotsByName(LessonInfoForm)
    # setupUi

    def retranslateUi(self, LessonInfoForm):
        LessonInfoForm.setWindowTitle(QCoreApplication.translate("LessonInfoForm", u"Lesson Info", None))
        self.label_3.setText(QCoreApplication.translate("LessonInfoForm", u"Lesson Details:", None))
        self.student_label.setText(QCoreApplication.translate("LessonInfoForm", u"Student:", None))
        self.date_label.setText(QCoreApplication.translate("LessonInfoForm", u"Date:", None))
        self.duration_label.setText(QCoreApplication.translate("LessonInfoForm", u"Duration:", None))
        self.location_label.setText(QCoreApplication.translate("LessonInfoForm", u"Location:", None))
        self.instrument_label.setText(QCoreApplication.translate("LessonInfoForm", u"Instrument:", None))
        self.label.setText(QCoreApplication.translate("LessonInfoForm", u"Lesson Notes:", None))
        self.save_button.setText(QCoreApplication.translate("LessonInfoForm", u"Save Changes", None))
        self.discard_button.setText(QCoreApplication.translate("LessonInfoForm", u"Discard Changes", None))
    # retranslateUi

