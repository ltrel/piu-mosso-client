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
        Register.resize(1200, 720)
        self.verticalLayout = QVBoxLayout(Register)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(380, 80, 380, 0)
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
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.student_button = QRadioButton(self.groupBox)
        self.student_button.setObjectName(u"student_button")
        self.student_button.setChecked(True)

        self.gridLayout_2.addWidget(self.student_button, 0, 0, 1, 1)

        self.teacher_button = QRadioButton(self.groupBox)
        self.teacher_button.setObjectName(u"teacher_button")
        self.teacher_button.setChecked(False)

        self.gridLayout_2.addWidget(self.teacher_button, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)


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


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.goto_login_button = QPushButton(Register)
        self.goto_login_button.setObjectName(u"goto_login_button")

        self.gridLayout_3.addWidget(self.goto_login_button, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalLayout.setStretch(0, 1)

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
        self.goto_login_button.setText(QCoreApplication.translate("Register", u"Sign in to Existing Account", None))
    # retranslateUi

