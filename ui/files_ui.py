# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'files.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_FilesForm(object):
    def setupUi(self, FilesForm):
        if not FilesForm.objectName():
            FilesForm.setObjectName(u"FilesForm")
        FilesForm.resize(1200, 720)
        self.horizontalLayout = QHBoxLayout(FilesForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar_frame = QWidget(FilesForm)
        self.sidebar_frame.setObjectName(u"sidebar_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_frame.sizePolicy().hasHeightForWidth())
        self.sidebar_frame.setSizePolicy(sizePolicy)
        self.sidebar_layout = QVBoxLayout(self.sidebar_frame)
        self.sidebar_layout.setObjectName(u"sidebar_layout")

        self.horizontalLayout.addWidget(self.sidebar_frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(FilesForm)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.student_combo = QComboBox(FilesForm)
        self.student_combo.setObjectName(u"student_combo")

        self.verticalLayout_2.addWidget(self.student_combo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.upload_button = QPushButton(FilesForm)
        self.upload_button.setObjectName(u"upload_button")

        self.verticalLayout_3.addWidget(self.upload_button)

        self.download_button = QPushButton(FilesForm)
        self.download_button.setObjectName(u"download_button")

        self.verticalLayout_3.addWidget(self.download_button)

        self.delete_button = QPushButton(FilesForm)
        self.delete_button.setObjectName(u"delete_button")

        self.verticalLayout_3.addWidget(self.delete_button)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.student_label = QLabel(FilesForm)
        self.student_label.setObjectName(u"student_label")

        self.verticalLayout.addWidget(self.student_label)

        self.files_listwidget = QListWidget(FilesForm)
        self.files_listwidget.setObjectName(u"files_listwidget")
        self.files_listwidget.setAlternatingRowColors(True)
        self.files_listwidget.setWordWrap(True)

        self.verticalLayout.addWidget(self.files_listwidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.retranslateUi(FilesForm)

        QMetaObject.connectSlotsByName(FilesForm)
    # setupUi

    def retranslateUi(self, FilesForm):
        FilesForm.setWindowTitle(QCoreApplication.translate("FilesForm", u"Files", None))
        self.label_2.setText(QCoreApplication.translate("FilesForm", u"Select Student:", None))
        self.upload_button.setText(QCoreApplication.translate("FilesForm", u"Upload New File", None))
        self.download_button.setText(QCoreApplication.translate("FilesForm", u"Download Selected File", None))
        self.delete_button.setText(QCoreApplication.translate("FilesForm", u"Delete Selected File", None))
        self.student_label.setText(QCoreApplication.translate("FilesForm", u"Showing files for student:", None))
    # retranslateUi

