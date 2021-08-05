# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'last_lesson.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_LastLessonForm(object):
    def setupUi(self, LastLessonForm):
        if not LastLessonForm.objectName():
            LastLessonForm.setObjectName(u"LastLessonForm")
        LastLessonForm.resize(1000, 600)
        self.horizontalLayout = QHBoxLayout(LastLessonForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar_frame = QWidget(LastLessonForm)
        self.sidebar_frame.setObjectName(u"sidebar_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_frame.sizePolicy().hasHeightForWidth())
        self.sidebar_frame.setSizePolicy(sizePolicy)
        self.sidebar_layout = QVBoxLayout(self.sidebar_frame)
        self.sidebar_layout.setObjectName(u"sidebar_layout")

        self.horizontalLayout.addWidget(self.sidebar_frame)

        self.lesson_info_frame = QWidget(LastLessonForm)
        self.lesson_info_frame.setObjectName(u"lesson_info_frame")
        self.lesson_info_layout = QVBoxLayout(self.lesson_info_frame)
        self.lesson_info_layout.setObjectName(u"lesson_info_layout")

        self.horizontalLayout.addWidget(self.lesson_info_frame)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(LastLessonForm)

        QMetaObject.connectSlotsByName(LastLessonForm)
    # setupUi

    def retranslateUi(self, LastLessonForm):
        LastLessonForm.setWindowTitle(QCoreApplication.translate("LastLessonForm", u"Last Lesson", None))
    # retranslateUi

