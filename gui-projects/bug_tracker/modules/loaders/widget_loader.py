from PyQt5 import QtCore
from PyQt5.QtWidgets import QHeaderView, QLineEdit, QTableView, QTableWidgetItem

from modules.loaders import account_loader


def load_all_widgets(window):
    load_tabs(window)
    load_text_lines(window)
    load_buttons(window)
    load_labels(window)
    load_tables(window)
    load_text_browsers(window)
    load_text_boxes(window)
    load_combo_boxes(window)
    load_graphics_view(window)
    window.setCentralWidget(window.central_widget)


def load_tabs(window):
    window.tab_widget.setGeometry(QtCore.QRect(0, 0, 921, 641))
    window.tab_widget.setCurrentIndex(1)
    window.tab_widget.addTab(window.accounts_tab, "Accounts")
    window.tab_widget.addTab(window.reports_tab, "Reports")


def load_text_lines(window):
    window.email_line.setPlaceholderText("Email Address")
    window.email_line.setGeometry(QtCore.QRect(400, 140, 181, 24))

    window.account_name_line.setPlaceholderText("Account Name")
    window.account_name_line.setGeometry(QtCore.QRect(400, 80, 181, 24))

    window.password_line.setPlaceholderText("Password")
    window.password_line.setEchoMode(QLineEdit.Password)
    window.password_line.setGeometry(QtCore.QRect(400, 110, 181, 24))

    window.find_account_line.setPlaceholderText("Find Account...")
    window.find_account_line.setGeometry(QtCore.QRect(10, 410, 381, 24))
    window.find_account_line.setAlignment(QtCore.Qt.AlignCenter)

    window.found_account_line.setText("Account Name")
    window.found_account_line.setGeometry(QtCore.QRect(10, 440, 291, 24))
    window.found_account_line.setAlignment(QtCore.Qt.AlignCenter)
    window.found_account_line.setReadOnly(True)

    window.found_email_line.setText("Email Address")
    window.found_email_line.setGeometry(QtCore.QRect(10, 470, 291, 24))
    window.found_email_line.setAlignment(QtCore.Qt.AlignCenter)
    window.found_email_line.setReadOnly(True)

    window.reports_filed_line.setText("")
    window.reports_filed_line.setGeometry(QtCore.QRect(100, 500, 51, 24))
    window.reports_filed_line.setReadOnly(True)

    window.last_login_line.setText("")
    window.last_login_line.setGeometry(QtCore.QRect(230, 500, 161, 24))
    window.last_login_line.setAlignment(QtCore.Qt.AlignCenter)
    window.last_login_line.setReadOnly(True)

    window.new_pass_id_line.setPlaceholderText("Account Name/Email Address")
    window.new_pass_id_line.setGeometry(QtCore.QRect(401, 310, 181, 24))

    window.new_password_line.setPlaceholderText("New Password")
    window.new_password_line.setEchoMode(QLineEdit.Password)
    window.new_password_line.setGeometry(QtCore.QRect(401, 340, 181, 24))

    window.search_reports_line.setPlaceholderText("Search reports for...")
    window.search_reports_line.setGeometry(QtCore.QRect(340, 190, 241, 24))
    window.search_reports_line.setAlignment(QtCore.Qt.AlignCenter)


def load_buttons(window):
    window.change_account_button.setText("Change")
    window.change_account_button.setGeometry(QtCore.QRect(310, 440, 80, 24))

    window.change_email_button.setText("Change")
    window.change_email_button.setGeometry(QtCore.QRect(310, 470, 80, 24))

    window.create_account_button.setText("Create")
    window.create_account_button.setGeometry(QtCore.QRect(529, 200, 51, 24))
    window.create_account_button.pressed.connect(window.create_new_account)

    window.reset_password_button.setText("Reset")
    window.reset_password_button.setGeometry(QtCore.QRect(530, 370, 51, 24))
    window.reset_password_button.pressed.connect(window.reset_account_password)

    window.delete_account_button.setText("Delete Selected Account")
    window.delete_account_button.setGeometry(QtCore.QRect(430, 500, 150, 24))
    window.delete_account_button.pressed.connect(window.delete_selected_account)

    window.update_report_button.setText("Update")
    window.update_report_button.setGeometry(QtCore.QRect(500, 500, 80, 24))


def load_labels(window):
    window.create_account_label.setText("Create Account")
    window.create_account_label.setGeometry(QtCore.QRect(400, 60, 100, 16))

    window.last_login_label.setText("Last Login:")
    window.last_login_label.setGeometry(QtCore.QRect(160, 500, 71, 16))

    window.reports_filed_label.setText("Reports Filed:")
    window.reports_filed_label.setGeometry(QtCore.QRect(10, 500, 91, 16))

    window.reset_password_label.setText("Reset Password")
    window.reset_password_label.setGeometry(QtCore.QRect(401, 290, 91, 16))


def load_tables(window):
    window.accounts_table.setGeometry(QtCore.QRect(10, 10, 381, 391))
    window.accounts_table.setRowCount(0)
    window.accounts_table.setColumnCount(3)

    # Columns
    item = QTableWidgetItem()
    window.accounts_table.setHorizontalHeaderItem(0, item)
    item = QTableWidgetItem()
    window.accounts_table.setHorizontalHeaderItem(1, item)
    item = QTableWidgetItem()
    window.accounts_table.setHorizontalHeaderItem(2, item)

    # Column Settings
    window.accounts_table.setSelectionBehavior(QTableView.SelectRows)
    item = window.accounts_table.horizontalHeaderItem(0)
    header = window.accounts_table.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeToContents)
    item.setText("Account Name")
    item = window.accounts_table.horizontalHeaderItem(1)
    header.setSectionResizeMode(1, QHeaderView.Stretch)
    item.setText("Email")
    item = window.accounts_table.horizontalHeaderItem(2)
    item.setText("Reports")

    # Row Settings
    account_loader.load_accounts(window)

    window.accounts_table.setSortingEnabled(True)

    # Reports Table
    window.reports_table.setGeometry(QtCore.QRect(10, 10, 571, 171))
    window.reports_table.setColumnCount(4)
    window.reports_table.setRowCount(0)
    item = QTableWidgetItem()
    header = window.reports_table.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeToContents)
    header.setSectionResizeMode(0, QHeaderView.Stretch)
    window.reports_table.setHorizontalHeaderItem(0, item)
    item = QTableWidgetItem()
    window.reports_table.setHorizontalHeaderItem(1, item)
    header.setSectionResizeMode(1, QHeaderView.Stretch)
    item = QTableWidgetItem()
    window.reports_table.setHorizontalHeaderItem(2, item)
    item = QTableWidgetItem()
    window.reports_table.setHorizontalHeaderItem(3, item)
    item = window.reports_table.horizontalHeaderItem(0)
    item.setText("Submitter")
    item = window.reports_table.horizontalHeaderItem(1)
    item.setText("Issue Type")
    item = window.reports_table.horizontalHeaderItem(2)
    item.setText(" Severity ")
    item = window.reports_table.horizontalHeaderItem(3)
    item.setText(" Reported On ")


def load_text_browsers(window):
    window.report_text_browser.setGeometry(QtCore.QRect(10, 190, 321, 331))


def load_text_boxes(window):
    window.technician_report_notes.setGeometry(QtCore.QRect(340, 350, 241, 141))


def load_combo_boxes(window):
    window.case_status_combo_box.setGeometry(QtCore.QRect(340, 500, 151, 24))
    window.case_status_combo_box.addItem("Case Open")
    window.case_status_combo_box.addItem("Case In Progress")
    window.case_status_combo_box.addItem("Case Closed - Fixed")
    window.case_status_combo_box.addItem("Not A Bug")

    window.worker_type_combo_box.setGeometry(QtCore.QRect(400, 170, 181, 24))
    window.worker_type_combo_box.addItem("Employee")
    window.worker_type_combo_box.addItem("Manager")
    window.worker_type_combo_box.addItem("Supervisor")
    window.worker_type_combo_box.addItem("Department Head")


def load_graphics_view(window):
    window.screenshot_view.setGeometry(QtCore.QRect(340, 220, 241, 121))