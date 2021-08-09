# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendar.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_CalendarForm(object):
    def setupUi(self, CalendarForm):
        if not CalendarForm.objectName():
            CalendarForm.setObjectName(u"CalendarForm")
        CalendarForm.resize(1000, 600)
        self.horizontalLayout = QHBoxLayout(CalendarForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar_frame = QWidget(CalendarForm)
        self.sidebar_frame.setObjectName(u"sidebar_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_frame.sizePolicy().hasHeightForWidth())
        self.sidebar_frame.setSizePolicy(sizePolicy)
        self.sidebar_layout = QVBoxLayout(self.sidebar_frame)
        self.sidebar_layout.setObjectName(u"sidebar_layout")

        self.horizontalLayout.addWidget(self.sidebar_frame)

        self.stacked_widget = QStackedWidget(CalendarForm)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.calendar_page = QWidget()
        self.calendar_page.setObjectName(u"calendar_page")
        self.horizontalLayout_3 = QHBoxLayout(self.calendar_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.previous_button = QPushButton(self.calendar_page)
        self.previous_button.setObjectName(u"previous_button")

        self.horizontalLayout_2.addWidget(self.previous_button)

        self.next_button = QPushButton(self.calendar_page)
        self.next_button.setObjectName(u"next_button")

        self.horizontalLayout_2.addWidget(self.next_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(1)
        self.wednesday_list = QListWidget(self.calendar_page)
        self.wednesday_list.setObjectName(u"wednesday_list")
        self.wednesday_list.setAlternatingRowColors(True)
        self.wednesday_list.setWordWrap(True)

        self.gridLayout.addWidget(self.wednesday_list, 2, 2, 1, 1)

        self.sunday_list = QListWidget(self.calendar_page)
        self.sunday_list.setObjectName(u"sunday_list")
        self.sunday_list.setAlternatingRowColors(True)
        self.sunday_list.setWordWrap(True)

        self.gridLayout.addWidget(self.sunday_list, 2, 6, 1, 1)

        self.friday_list = QListWidget(self.calendar_page)
        self.friday_list.setObjectName(u"friday_list")
        self.friday_list.setAlternatingRowColors(True)
        self.friday_list.setWordWrap(True)

        self.gridLayout.addWidget(self.friday_list, 2, 4, 1, 1)

        self.thursday_list = QListWidget(self.calendar_page)
        self.thursday_list.setObjectName(u"thursday_list")
        self.thursday_list.setAlternatingRowColors(True)
        self.thursday_list.setWordWrap(True)

        self.gridLayout.addWidget(self.thursday_list, 2, 3, 1, 1)

        self.tuesday_list = QListWidget(self.calendar_page)
        self.tuesday_list.setObjectName(u"tuesday_list")
        self.tuesday_list.setAlternatingRowColors(True)
        self.tuesday_list.setWordWrap(True)

        self.gridLayout.addWidget(self.tuesday_list, 2, 1, 1, 1)

        self.monday_list = QListWidget(self.calendar_page)
        self.monday_list.setObjectName(u"monday_list")
        self.monday_list.setAlternatingRowColors(True)
        self.monday_list.setWordWrap(True)

        self.gridLayout.addWidget(self.monday_list, 2, 0, 1, 1)

        self.saturday_list = QListWidget(self.calendar_page)
        self.saturday_list.setObjectName(u"saturday_list")
        self.saturday_list.setAlternatingRowColors(True)
        self.saturday_list.setWordWrap(True)

        self.gridLayout.addWidget(self.saturday_list, 2, 5, 1, 1)

        self.monday_label = QLabel(self.calendar_page)
        self.monday_label.setObjectName(u"monday_label")
        self.monday_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.monday_label, 1, 0, 1, 1)

        self.tuesday_label = QLabel(self.calendar_page)
        self.tuesday_label.setObjectName(u"tuesday_label")
        self.tuesday_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.tuesday_label, 1, 1, 1, 1)

        self.saturday_label = QLabel(self.calendar_page)
        self.saturday_label.setObjectName(u"saturday_label")
        self.saturday_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.saturday_label, 1, 5, 1, 1)

        self.friday_label = QLabel(self.calendar_page)
        self.friday_label.setObjectName(u"friday_label")
        self.friday_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.friday_label, 1, 4, 1, 1)

        self.thursday_label = QLabel(self.calendar_page)
        self.thursday_label.setObjectName(u"thursday_label")
        self.thursday_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.thursday_label, 1, 3, 1, 1)

        self.wednesday_label = QLabel(self.calendar_page)
        self.wednesday_label.setObjectName(u"wednesday_label")
        self.wednesday_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.wednesday_label, 1, 2, 1, 1)

        self.sunday_label = QLabel(self.calendar_page)
        self.sunday_label.setObjectName(u"sunday_label")
        self.sunday_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.sunday_label, 1, 6, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.stacked_widget.addWidget(self.calendar_page)

        self.horizontalLayout.addWidget(self.stacked_widget)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.retranslateUi(CalendarForm)

        QMetaObject.connectSlotsByName(CalendarForm)
    # setupUi

    def retranslateUi(self, CalendarForm):
        CalendarForm.setWindowTitle(QCoreApplication.translate("CalendarForm", u"Calendar", None))
        self.previous_button.setText(QCoreApplication.translate("CalendarForm", u"Show Previous Week", None))
        self.next_button.setText(QCoreApplication.translate("CalendarForm", u"Show Next Week", None))
        self.monday_label.setText(QCoreApplication.translate("CalendarForm", u"Monday", None))
        self.tuesday_label.setText(QCoreApplication.translate("CalendarForm", u"Tuesday", None))
        self.saturday_label.setText(QCoreApplication.translate("CalendarForm", u"Saturday", None))
        self.friday_label.setText(QCoreApplication.translate("CalendarForm", u"Friday", None))
        self.thursday_label.setText(QCoreApplication.translate("CalendarForm", u"Thursday", None))
        self.wednesday_label.setText(QCoreApplication.translate("CalendarForm", u"Wednesday", None))
        self.sunday_label.setText(QCoreApplication.translate("CalendarForm", u"Sunday", None))
    # retranslateUi

