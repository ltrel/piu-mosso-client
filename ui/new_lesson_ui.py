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
        self.verticalLayout.setContentsMargins(165, 20, 165, 20)
        self.label = QLabel(NewLessonForm)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.student_combo = QComboBox(NewLessonForm)
        self.student_combo.setObjectName(u"student_combo")

        self.verticalLayout.addWidget(self.student_combo)

        self.label_2 = QLabel(NewLessonForm)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.location_combo = QComboBox(NewLessonForm)
        self.location_combo.setObjectName(u"location_combo")
        self.location_combo.setEditable(True)

        self.verticalLayout.addWidget(self.location_combo)

        self.label_3 = QLabel(NewLessonForm)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.instrument_combo = QComboBox(NewLessonForm)
        self.instrument_combo.setObjectName(u"instrument_combo")
        self.instrument_combo.setEditable(True)

        self.verticalLayout.addWidget(self.instrument_combo)

        self.label_5 = QLabel(NewLessonForm)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.minutes_spinbox = QSpinBox(NewLessonForm)
        self.minutes_spinbox.setObjectName(u"minutes_spinbox")
        self.minutes_spinbox.setMaximum(120)
        self.minutes_spinbox.setValue(30)

        self.verticalLayout.addWidget(self.minutes_spinbox)

        self.label_4 = QLabel(NewLessonForm)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.time_edit = QTimeEdit(NewLessonForm)
        self.time_edit.setObjectName(u"time_edit")

        self.verticalLayout.addWidget(self.time_edit)

        self.date_calendar = QCalendarWidget(NewLessonForm)
        self.date_calendar.setObjectName(u"date_calendar")
        self.date_calendar.setGridVisible(True)

        self.verticalLayout.addWidget(self.date_calendar)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(14)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.create_button = QPushButton(NewLessonForm)
        self.create_button.setObjectName(u"create_button")

        self.horizontalLayout_2.addWidget(self.create_button)

        self.cancel_button = QPushButton(NewLessonForm)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_2.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.retranslateUi(NewLessonForm)

        QMetaObject.connectSlotsByName(NewLessonForm)
    # setupUi

    def retranslateUi(self, NewLessonForm):
        NewLessonForm.setWindowTitle(QCoreApplication.translate("NewLessonForm", u"New Lesson", None))
        self.label.setText(QCoreApplication.translate("NewLessonForm", u"Student:", None))
        self.label_2.setText(QCoreApplication.translate("NewLessonForm", u"Location:", None))
        self.label_3.setText(QCoreApplication.translate("NewLessonForm", u"Instrument:", None))
        self.label_5.setText(QCoreApplication.translate("NewLessonForm", u"Duration (minutes):", None))
        self.label_4.setText(QCoreApplication.translate("NewLessonForm", u"Date:", None))
        self.create_button.setText(QCoreApplication.translate("NewLessonForm", u"Create Lesson", None))
        self.cancel_button.setText(QCoreApplication.translate("NewLessonForm", u"Cancel", None))
    # retranslateUi

