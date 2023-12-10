import sys

from PyQt6.QtWidgets import QApplication, QLabel

# 创建一个app，应用
app = QApplication(sys.argv)
# 创建一个widget，或继承自widget的组件(QLabel)
label = QLabel("Hello World!")
# 显示该widget
label.show()
# app进入循环, 等待操作
app.exec()
