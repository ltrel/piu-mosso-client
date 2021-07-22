# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(1000, 600)
        self.horizontalLayout = QHBoxLayout(Register)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(320, 50, 320, 50)
        self.label = QLabel(Register)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label)

        self.username_txt = QLineEdit(Register)
        self.username_txt.setObjectName(u"username_txt")

        self.verticalLayout_2.addWidget(self.username_txt)

        self.label_5 = QLabel(Register)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_5)

        self.fullname_txt = QLineEdit(Register)
        self.fullname_txt.setObjectName(u"fullname_txt")

        self.verticalLayout_2.addWidget(self.fullname_txt)

        self.label_2 = QLabel(Register)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_2)

        self.password_txt = QLineEdit(Register)
        self.password_txt.setObjectName(u"password_txt")
        self.password_txt.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password_txt)

        self.label_6 = QLabel(Register)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_6)

        self.verify_password_txt = QLineEdit(Register)
        self.verify_password_txt.setObjectName(u"verify_password_txt")
        self.verify_password_txt.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.verify_password_txt)

        self.groupBox = QGroupBox(Register)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 20, 321, 61))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.student_button = QRadioButton(self.gridLayoutWidget)
        self.student_button.setObjectName(u"student_button")
        self.student_button.setChecked(True)

        self.gridLayout_2.addWidget(self.student_button, 0, 0, 1, 1)

        self.teacher_button = QRadioButton(self.gridLayoutWidget)
        self.teacher_button.setObjectName(u"teacher_button")
        self.teacher_button.setChecked(False)

        self.gridLayout_2.addWidget(self.teacher_button, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.address_txt = QLineEdit(Register)
        self.address_txt.setObjectName(u"address_txt")

        self.gridLayout.addWidget(self.address_txt, 1, 0, 1, 1)

        self.label_4 = QLabel(Register)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.port_txt = QLineEdit(Register)
        self.port_txt.setObjectName(u"port_txt")

        self.gridLayout.addWidget(self.port_txt, 1, 1, 1, 1)

        self.label_3 = QLabel(Register)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.register_button = QPushButton(Register)
        self.register_button.setObjectName(u"register_button")

        self.verticalLayout_2.addWidget(self.register_button)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Register", None))
        self.label.setText(QCoreApplication.translate("Register", u"Username:", None))
        self.label_5.setText(QCoreApplication.translate("Register", u"Full Name:", None))
        self.label_2.setText(QCoreApplication.translate("Register", u"Password:", None))
        self.label_6.setText(QCoreApplication.translate("Register", u"Verify Password:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Register", u"Account Type", None))
        self.student_button.setText(QCoreApplication.translate("Register", u"Student", None))
        self.teacher_button.setText(QCoreApplication.translate("Register", u"Teacher", None))
        self.label_4.setText(QCoreApplication.translate("Register", u"Port:", None))
        self.label_3.setText(QCoreApplication.translate("Register", u"Server Address:", None))
        self.register_button.setText(QCoreApplication.translate("Register", u"Register", None))
    # retranslateUi

