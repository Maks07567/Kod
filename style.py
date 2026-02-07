STYLE = """
QWidget {
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 15px;
    font-weight: 300;
    background: #f8f8f8;
    color: #222;
}

QPushButton {
    border: 1px solid #cccccc;
    padding: 8px 16px;
    border-radius: 4px;
    background: #ffffff;
    font-weight: 500;
}

QPushButton:hover {
    background: #eeeeee;
}

QPushButton:pressed {
    background: #dddddd;
}

QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox {
    border: 1px solid #cccccc;
    padding: 6px;
    border-radius: 4px;
    background: #ffffff;
}

QLineEdit:focus, QComboBox:focus {
    border: 1px solid #0078d4;
}

QTableWidget {
    border: 1px solid #dddddd;
    gridline-color: #eaeaea;
    background: #ffffff;
}

QHeaderView::section {
    background: #f0f0f0;
    color: #222222;
    font-weight: bold;
    border: none;
    padding: 6px;
}

QLabel {
    color: #333333;
    font-weight: 500;
}
"""