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
        self.pushButton_2 = QPushButton(TeacherSidebar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(TeacherSidebar)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(TeacherSidebar)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(TeacherSidebar)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(TeacherSidebar)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_5)

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


        self.retranslateUi(TeacherSidebar)

        QMetaObject.connectSlotsByName(TeacherSidebar)
    # setupUi

    def retranslateUi(self, TeacherSidebar):
        TeacherSidebar.setWindowTitle(QCoreApplication.translate("TeacherSidebar", u"Teacher Sidebar", None))
        self.pushButton_2.setText(QCoreApplication.translate("TeacherSidebar", u"New Lesson", None))
        self.pushButton.setText(QCoreApplication.translate("TeacherSidebar", u"Last Lesson", None))
        self.pushButton_3.setText(QCoreApplication.translate("TeacherSidebar", u"Calendar", None))
        self.pushButton_4.setText(QCoreApplication.translate("TeacherSidebar", u"Manage Students", None))
        self.pushButton_5.setText(QCoreApplication.translate("TeacherSidebar", u"Shared Files", None))
        self.user_label.setText(QCoreApplication.translate("TeacherSidebar", u"You are signed in as:", None))
    # retranslateUi

