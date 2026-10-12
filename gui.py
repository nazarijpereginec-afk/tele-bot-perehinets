import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QComboBox
)

# зчитування турів у ComboBox
def load_tours():
    tours = []
    try:
        with open("dataTours.txt", "r", encoding="utf-8") as f:
            for line in f:
                country = line.split(",")[0]
                tours.append(country)
    except:
        pass
    return tours

# зчитування стану RadioButton
def load_status():
    try:
        with open("status.txt", "r") as f:
            return f.read().strip()
    except:
        return "not_paid"


class TourApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Туристичне агентство")
        self.setGeometry(300, 200, 400, 300)

        layout = QVBoxLayout()

        # поле введення
        self.label1 = QLabel("Оберіть країну:")
        self.country_input = QLineEdit()
        self.btn_show = QPushButton("Показати")
        self.btn_show.clicked.connect(self.show_country)

        layout.addWidget(self.label1)
        layout.addWidget(self.country_input)
        layout.addWidget(self.btn_show)

        # ComboBox, значення з файлу
        self.combo = QComboBox()
        self.combo.addItems(load_tours())
        layout.addWidget(QLabel("Доступні тури:"))
        layout.addWidget(self.combo)

        # поля, запис у файл
        self.name_input = QLineEdit()
        self.count_input = QLineEdit()
        self.btn_save = QPushButton("Зберегти бронювання")
        self.btn_save.clicked.connect(self.save_booking)

        layout.addWidget(QLabel("Турист:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Кількість місць:"))
        layout.addWidget(self.count_input)
        layout.addWidget(self.btn_save)

        # RadioButton стан з файлу status.txt
        self.radio_paid = QRadioButton("Оплачено")
        self.radio_not_paid = QRadioButton("Не оплачено")

        status = load_status()
        if status == "paid":
            self.radio_paid.setChecked(True)
        else:
            self.radio_not_paid.setChecked(True)

        layout.addWidget(self.radio_paid)
        layout.addWidget(self.radio_not_paid)

        self.setLayout(layout)

    # кнопки
    def show_country(self):
        QMessageBox.information(
            self, "Вибір",
            f"Ви обрали тур у країну: {self.country_input.text()}"
        )

    def save_booking(self):
        with open("gui_bookings.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{self.name_input.text()},"
                f"{self.combo.currentText()},"
                f"{self.count_input.text()}\n"
            )
        QMessageBox.information(self, "OK", "Бронювання збережено")


app = QApplication(sys.argv)
win = TourApp()
win.show()
sys.exit(app.exec_())
