# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(1200, 720)
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(380, 160, 380, 120)
        self.label_13 = QLabel(Login)
        self.label_13.setObjectName(u"label_13")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.label_13)

        self.username_txt = QLineEdit(Login)
        self.username_txt.setObjectName(u"username_txt")

        self.verticalLayout_5.addWidget(self.username_txt)

        self.label_14 = QLabel(Login)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.label_14)

        self.password_txt = QLineEdit(Login)
        self.password_txt.setObjectName(u"password_txt")
        self.password_txt.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.password_txt)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(7)
        self.gridLayout_4.setVerticalSpacing(20)
        self.address_txt = QLineEdit(Login)
        self.address_txt.setObjectName(u"address_txt")

        self.gridLayout_4.addWidget(self.address_txt, 1, 0, 1, 1)

        self.label_15 = QLabel(Login)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_15, 0, 1, 1, 1)

        self.port_txt = QLineEdit(Login)
        self.port_txt.setObjectName(u"port_txt")

        self.gridLayout_4.addWidget(self.port_txt, 1, 1, 1, 1)

        self.label_16 = QLabel(Login)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)

        self.login_button = QPushButton(Login)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout_5.addWidget(self.login_button)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.goto_register_button = QPushButton(Login)
        self.goto_register_button.setObjectName(u"goto_register_button")

        self.gridLayout.addWidget(self.goto_register_button, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label_13.setText(QCoreApplication.translate("Login", u"Username:", None))
        self.label_14.setText(QCoreApplication.translate("Login", u"Password:", None))
        self.label_15.setText(QCoreApplication.translate("Login", u"Port:", None))
        self.label_16.setText(QCoreApplication.translate("Login", u"Server Address:", None))
        self.login_button.setText(QCoreApplication.translate("Login", u"Login", None))
        self.goto_register_button.setText(QCoreApplication.translate("Login", u"Create New Account", None))
    # retranslateUi

