from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QHBoxLayout, QPushButton,QRadioButton,QButtonGroup,QGroupBox, QLabel, QVBoxLayout, QSpinBox

menu_btn = QPushButton("меню")
rest_btn = QPushButton('відпочити')
time_spin= QSpinBox()
time_spin.setValue(3)
time_lb = QLabel("хвилина")

row1 = QHBoxLayout()
row1.addWidget(menu_btn)
row1.addWidget(rest_btn)
row1.addWidget(time_spin)
row1.addWidget(time_lb)

question_lb = QLabel("Питання")
btn1 = QRadioButton("варіант1")
btn2 = QRadioButton("варіант2")
btn3 = QRadioButton("варіант 3")
btn4 = QRadioButton("варіант4")
row2 = QHBoxLayout()
radio_group = QButtonGroup()
radio_group.addButton(btn1)
radio_group.addButton(btn2)
radio_group.addButton(btn3)
radio_group.addButton(btn4)


group_box = QGroupBox("варіанти відпрвідей")
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget (btn1)
col1.addWidget (btn2)
col2.addWidget (btn3)
col2.addWidget (btn4)

row2.addLayout(col1)
row2.addLayout(col2)
group_box.setLayout(row2)


main_line = QVBoxLayout()
main_line.addLayout(row1)
main_line.addWidget(question_lb)
main_line.addWidget(group_box)
