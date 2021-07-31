# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teacher_sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_TeacherSidebar(object):
    def setupUi(self, TeacherSidebar):
        if not TeacherSidebar.objectName():
            TeacherSidebar.setObjectName(u"TeacherSidebar")
        TeacherSidebar.resize(280, 640)
        self.verticalLayout = QVBoxLayout(TeacherSidebar)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_button = QPushButton(TeacherSidebar)
        self.new_button.setObjectName(u"new_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_button.sizePolicy().hasHeightForWidth())
        self.new_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.new_button)

        self.last_button = QPushButton(TeacherSidebar)
        self.last_button.setObjectName(u"last_button")
        sizePolicy.setHeightForWidth(self.last_button.sizePolicy().hasHeightForWidth())
        self.last_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.last_button)

        self.calendar_button = QPushButton(TeacherSidebar)
        self.calendar_button.setObjectName(u"calendar_button")
        sizePolicy.setHeightForWidth(self.calendar_button.sizePolicy().hasHeightForWidth())
        self.calendar_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.calendar_button)

        self.students_button = QPushButton(TeacherSidebar)
        self.students_button.setObjectName(u"students_button")
        sizePolicy.setHeightForWidth(self.students_button.sizePolicy().hasHeightForWidth())
        self.students_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.students_button)

        self.files_button = QPushButton(TeacherSidebar)
        self.files_button.setObjectName(u"files_button")
        sizePolicy.setHeightForWidth(self.files_button.sizePolicy().hasHeightForWidth())
        self.files_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.files_button)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.user_label = QLabel(TeacherSidebar)
        self.user_label.setObjectName(u"user_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.user_label.sizePolicy().hasHeightForWidth())
        self.user_label.setSizePolicy(sizePolicy1)
        self.user_label.setAlignment(Qt.AlignCenter)
        self.user_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.user_label)

        self.sign_out_button = QPushButton(TeacherSidebar)
        self.sign_out_button.setObjectName(u"sign_out_button")

        self.verticalLayout.addWidget(self.sign_out_button)


        self.retranslateUi(TeacherSidebar)

        QMetaObject.connectSlotsByName(TeacherSidebar)
    # setupUi

    def retranslateUi(self, TeacherSidebar):
        TeacherSidebar.setWindowTitle(QCoreApplication.translate("TeacherSidebar", u"Teacher Sidebar", None))
        self.new_button.setText(QCoreApplication.translate("TeacherSidebar", u"New Lesson", None))
        self.last_button.setText(QCoreApplication.translate("TeacherSidebar", u"Last Lesson", None))
        self.calendar_button.setText(QCoreApplication.translate("TeacherSidebar", u"Calendar", None))
        self.students_button.setText(QCoreApplication.translate("TeacherSidebar", u"Manage Students", None))
        self.files_button.setText(QCoreApplication.translate("TeacherSidebar", u"Shared Files", None))
        self.user_label.setText(QCoreApplication.translate("TeacherSidebar", u"You are signed in as:", None))
        self.sign_out_button.setText(QCoreApplication.translate("TeacherSidebar", u"Sign Out", None))
    # retranslateUi

