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
        self.horizontalLayout.setContentsMargins(140, -1, 140, -1)
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
        self.duration_label = QLabel(StudentDashboard)
        self.duration_label.setObjectName(u"duration_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.duration_label.sizePolicy().hasHeightForWidth())
        self.duration_label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.duration_label, 2, 0, 1, 1)

        self.date_label = QLabel(StudentDashboard)
        self.date_label.setObjectName(u"date_label")
        sizePolicy1.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.date_label, 0, 0, 1, 1)

        self.location_label = QLabel(StudentDashboard)
        self.location_label.setObjectName(u"location_label")
        sizePolicy1.setHeightForWidth(self.location_label.sizePolicy().hasHeightForWidth())
        self.location_label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.location_label, 0, 1, 1, 1)

        self.instrument_label = QLabel(StudentDashboard)
        self.instrument_label.setObjectName(u"instrument_label")
        sizePolicy1.setHeightForWidth(self.instrument_label.sizePolicy().hasHeightForWidth())
        self.instrument_label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.instrument_label, 1, 1, 1, 1)

        self.lesson_teacher_label = QLabel(StudentDashboard)
        self.lesson_teacher_label.setObjectName(u"lesson_teacher_label")
        sizePolicy1.setHeightForWidth(self.lesson_teacher_label.sizePolicy().hasHeightForWidth())
        self.lesson_teacher_label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lesson_teacher_label, 1, 0, 1, 1)


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

        self.teacher_combo = QComboBox(StudentDashboard)
        self.teacher_combo.setObjectName(u"teacher_combo")

        self.verticalLayout_2.addWidget(self.teacher_combo)

        self.download_button = QPushButton(StudentDashboard)
        self.download_button.setObjectName(u"download_button")

        self.verticalLayout_2.addWidget(self.download_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.user_label = QLabel(StudentDashboard)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setAlignment(Qt.AlignCenter)
        self.user_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.user_label)

        self.sign_out_button = QPushButton(StudentDashboard)
        self.sign_out_button.setObjectName(u"sign_out_button")

        self.verticalLayout_2.addWidget(self.sign_out_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.files_teacher_label = QLabel(StudentDashboard)
        self.files_teacher_label.setObjectName(u"files_teacher_label")

        self.verticalLayout.addWidget(self.files_teacher_label)

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
        self.duration_label.setText(QCoreApplication.translate("StudentDashboard", u"Duration:", None))
        self.date_label.setText(QCoreApplication.translate("StudentDashboard", u"Date:", None))
        self.location_label.setText(QCoreApplication.translate("StudentDashboard", u"Location:", None))
        self.instrument_label.setText(QCoreApplication.translate("StudentDashboard", u"Instrument:", None))
        self.lesson_teacher_label.setText(QCoreApplication.translate("StudentDashboard", u"Teacher:", None))
        self.label_10.setText(QCoreApplication.translate("StudentDashboard", u"Files:", None))
        self.label_2.setText(QCoreApplication.translate("StudentDashboard", u"Teacher:", None))
        self.download_button.setText(QCoreApplication.translate("StudentDashboard", u"Download Selected File", None))
        self.user_label.setText(QCoreApplication.translate("StudentDashboard", u"You are signed in as:", None))
        self.sign_out_button.setText(QCoreApplication.translate("StudentDashboard", u"Sign Out", None))
        self.files_teacher_label.setText(QCoreApplication.translate("StudentDashboard", u"Showing files shared with you by:", None))
    # retranslateUi

