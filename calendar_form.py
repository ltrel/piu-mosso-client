import json
from PySide6.QtWidgets import QWidget
from ui.calendar_ui import Ui_CalendarForm
from teacher_sidebar import TeacherSidebar
from lesson_info_form import LessonInfoForm
from datetime import datetime, date, timedelta
from utils import app_state_ref


class CalendarForm(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_CalendarForm()
        self.ui.setupUi(self)

        self.ui.sidebar = TeacherSidebar(self, 'calendar_button')
        self.ui.sidebar_layout.addWidget(self.ui.sidebar)

        self.ui.next_button.clicked.connect(self.next_week)
        self.ui.previous_button.clicked.connect(self.previous_week)

        # Organize all the list widgets into a list so they can be accessed
        # by weekday number
        self.ui.list_widgets = [
            self.ui.monday_list,
            self.ui.tuesday_list,
            self.ui.wednesday_list,
            self.ui.thursday_list,
            self.ui.friday_list,
            self.ui.saturday_list,
            self.ui.sunday_list,
        ]
        for list_widget in self.ui.list_widgets:
            list_widget.itemDoubleClicked.connect(self.show_details)

        self.all_lessons = []
        # List of 7 lists where each list corresponds to a weekday
        self.shown_lessons = [[] for i in range(7)]

        self.week_monday = None

    def setup(self):
        # Use most recent monday as the start of the currently shown week
        today = datetime.combine(date.today(), datetime.min.time())
        self.week_monday = today - timedelta(days=today.weekday())

        # Label the date of each column
        self.label_columns()

        # Fetch and draw the lessons
        self.refresh_lessons()

        # Make sure the calendar page of the stacked widget is showing
        self.ui.stacked_widget.setCurrentWidget(self.ui.calendar_page)

    def populate(self):
        # Clear the list widgets
        for list_widget in self.ui.list_widgets:
            list_widget.clear()
        # Clear the internal representation of the currently shown lessons
        self.shown_lessons = [[] for i in range(7)]

        next_week_start = self.week_monday + timedelta(weeks=1)

        # Iterate over all the lessons
        for lesson in self.all_lessons:
            # Skip this lesson if it isn't part of the currently shown week
            dt = datetime.fromtimestamp(lesson['dateTime'] // 1000)
            if not self.week_monday <= dt <= next_week_start:
                continue

            # Calculate the end time of the lesson
            end_dt = dt + timedelta(minutes=lesson["minutes"])

            # Add the lesson to the list widget for the lesson's weekday
            list_widget = self.ui.list_widgets[dt.weekday()]
            list_widget.addItem(
                f'{lesson["studentName"]}\n'
                f'{dt:%I:%M %p} - {end_dt:%I:%M %p}\n'\
                f'{lesson["location"]}'
            )
            # Add the lesson to the relevant internal list
            self.shown_lessons[dt.weekday()].append(lesson)


    def next_week(self):
        self.week_monday += timedelta(weeks=1)
        self.label_columns()
        self.populate()

    def previous_week(self):
        self.week_monday -= timedelta(weeks=1)
        self.label_columns()
        self.populate()

    def refresh_lessons(self):
        # Get lessons from the server and sort them by date
        app_state = app_state_ref(self)
        self.all_lessons = json.loads(app_state.api_get('/lessons').content)
        self.all_lessons.sort(key=lambda x: x['dateTime'])
        # Draw the lessons to the list widgets
        self.populate()

    def label_columns(self):
        day = self.week_monday
        self.ui.monday_label.setText(f'Monday\n{day:%B} {day.day}')
        day += timedelta(days=1)
        self.ui.tuesday_label.setText(f'Tuesday\n{day:%B} {day.day}')
        day += timedelta(days=1)
        self.ui.wednesday_label.setText(f'Wednesday\n{day:%B} {day.day}')
        day += timedelta(days=1)
        self.ui.thursday_label.setText(f'Thursday\n{day:%B} {day.day}')
        day += timedelta(days=1)
        self.ui.friday_label.setText(f'Friday\n{day:%B} {day.day}')
        day += timedelta(days=1)
        self.ui.saturday_label.setText(f'Saturday\n{day:%B} {day.day}')
        day += timedelta(days=1)
        self.ui.sunday_label.setText(f'Sunday\n{day:%B} {day.day}')

    def show_details(self):
        # Find the lesson's JSON in the internal list
        sender = self.sender()
        weekday = self.ui.list_widgets.index(sender)
        index = sender.currentRow()
        lesson = self.shown_lessons[weekday][index]

        # Create and display a lesson info page for the selected lesson
        self.ui.details_page = LessonInfoForm(self.ui.stacked_widget, lesson)
        self.ui.stacked_widget.addWidget(self.ui.details_page)
        self.ui.stacked_widget.setCurrentWidget(self.ui.details_page)
