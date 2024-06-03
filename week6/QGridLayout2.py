# Import necessary modules
import sys, json
from PySide6.QtWidgets import (QApplication, QWidget, 
                             QLabel, QCheckBox, QLineEdit, QGridLayout,
                             QMainWindow) 
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class MW(QMainWindow):
    
    # instance attribute is
    # QGridLayout instance

    def __init__(self):
        super().__init__() 
        self.init_ui()

    def init_ui(self):
        """Set up the application's GUI."""
        # self.setMinimumSize(500, 500) 
        self.setWindowTitle("QGridLayout Example")

        self.setup_mw()
        self.show()

    def setup_mw(self):                

        self.main_grid = QGridLayout()

        for i in range(5):
            cb = QCheckBox()
            cb.stateChanged.connect(self.print_text) # slot 연결.
            self.main_grid.addWidget(cb,i,0)
            ledit = QLineEdit()            
            ledit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.main_grid.addWidget(ledit,i,1,1,2)
        dp_label = QLabel("")
        dp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_grid.addWidget(dp_label,5,0,1,2)
        
        central_widget = QWidget()
        central_widget.setLayout(self.main_grid)
        self.setCentralWidget(central_widget)

    def print_text(self): # instance method
        dp_text = ""
        for i in range(5):
            # Retrieve the QLayoutItem object
            item = self.main_grid.itemAtPosition(i, 0)
            # Retrieve the widget (QCheckBox)
            widget = item.widget()            

            if widget.isChecked() == True:
                # Retrieve the QLayoutItem object
                item = self.main_grid.itemAtPosition(i, 1) 
                # Retrieve the widget (QLineEdit)
                widget = item.widget()
                text = widget.text()
                dp_text =dp_text+f"[{text}]"

        item = self.main_grid.itemAtPosition(5,0)
        widget = item.widget()
        widget.setText(dp_text)
        # self.dp_label.setText(dp_text) #이렇게 접근하는게 훨씬 단순하나 연습의 차원의로 위의3개행으로 처리.       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = MW()
    sys.exit(app.exec())