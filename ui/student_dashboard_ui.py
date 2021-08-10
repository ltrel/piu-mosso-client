# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student_dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_StudentDashboard(object):
    def setupUi(self, StudentDashboard):
        if not StudentDashboard.objectName():
            StudentDashboard.setObjectName(u"StudentDashboard")
        StudentDashboard.resize(1200, 720)
        self.horizontalLayout = QHBoxLayout(StudentDashboard)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(120, -1, 120, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(StudentDashboard)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_8 = QLabel(StudentDashboard)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_4 = QLabel(StudentDashboard)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(StudentDashboard)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_7 = QLabel(StudentDashboard)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)

        self.label_6 = QLabel(StudentDashboard)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 16, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_10 = QLabel(StudentDashboard)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_2.addWidget(self.label_10)

        self.label_2 = QLabel(StudentDashboard)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.student_combo = QComboBox(StudentDashboard)
        self.student_combo.setObjectName(u"student_combo")

        self.verticalLayout_2.addWidget(self.student_combo)

        self.download_button = QPushButton(StudentDashboard)
        self.download_button.setObjectName(u"download_button")

        self.verticalLayout_2.addWidget(self.download_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_9 = QLabel(StudentDashboard)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_9)

        self.pushButton = QPushButton(StudentDashboard)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(StudentDashboard)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.files_listwidget = QListWidget(StudentDashboard)
        self.files_listwidget.setObjectName(u"files_listwidget")
        self.files_listwidget.setAlternatingRowColors(True)
        self.files_listwidget.setWordWrap(True)

        self.verticalLayout.addWidget(self.files_listwidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout.setStretch(0, 4)

        self.retranslateUi(StudentDashboard)

        QMetaObject.connectSlotsByName(StudentDashboard)
    # setupUi

    def retranslateUi(self, StudentDashboard):
        StudentDashboard.setWindowTitle(QCoreApplication.translate("StudentDashboard", u"Student Dashboard", None))
        self.label_3.setText(QCoreApplication.translate("StudentDashboard", u"Next Lesson:", None))
        self.label_8.setText(QCoreApplication.translate("StudentDashboard", u"Duration:", None))
        self.label_4.setText(QCoreApplication.translate("StudentDashboard", u"Date:", None))
        self.label_5.setText(QCoreApplication.translate("StudentDashboard", u"Location:", None))
        self.label_7.setText(QCoreApplication.translate("StudentDashboard", u"Instrument:", None))
        self.label_6.setText(QCoreApplication.translate("StudentDashboard", u"Teacher:", None))
        self.label_10.setText(QCoreApplication.translate("StudentDashboard", u"Files:", None))
        self.label_2.setText(QCoreApplication.translate("StudentDashboard", u"Show files shared with you by:", None))
        self.download_button.setText(QCoreApplication.translate("StudentDashboard", u"Download Selected File", None))
        self.label_9.setText(QCoreApplication.translate("StudentDashboard", u"You are signed in as:", None))
        self.pushButton.setText(QCoreApplication.translate("StudentDashboard", u"Sign Out", None))
        self.label.setText(QCoreApplication.translate("StudentDashboard", u"Showing files shared by:", None))
    # retranslateUi

