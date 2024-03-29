# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.15.4 (for UI im too lazy to make a ui manually)

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import pyautogui
from keyboard import is_pressed
from time import sleep


pyautogui.FAILSAFE= True #Set this to false if you want to, if set to True it might turn off randomly while using the random mode

class Ui_Form(object):
    def setupUi(self, Form):
        
        #shortcuts
        QtWidgets.QShortcut(QtGui.QKeySequence('f1'), Form).activated.connect(lambda: self.start())

        #ui
        Form.setObjectName("Form")
        Form.resize(451, 183)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(970, 440))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("background-color: rgb(182, 239, 184);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 191, 111))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect((self.currentIndexChanged))
        
        self.x_sb = QtWidgets.QSpinBox(self.groupBox)
        self.x_sb.setGeometry(QtCore.QRect(40, 50, 141, 22))
        self.x_sb.setObjectName("x_sb")
        self.x_sb.setMaximum(width)
        
        self.y_sb = QtWidgets.QSpinBox(self.groupBox)
        self.y_sb.setGeometry(QtCore.QRect(40, 80, 141, 22))
        self.y_sb.setObjectName("y_sb")
        self.y_sb.setMaximum(height)
        
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 55, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 84, 16, 16))
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 0, 231, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 21, 47, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(185, 23, 16, 20))
        self.label_6.setObjectName("label_6")
        self.delay_sb = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.delay_sb.setGeometry(QtCore.QRect(50, 20, 131, 22))
        self.delay_sb.setObjectName("delay_sb")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 65, 180, 40))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.frame)

        self.runtype = 0
        self.running = True
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QtGui.QIcon('assets/Icon.png'))
        Form.setWindowTitle(_translate("Form", "PyAutoClicker"))
        self.label.setText(_translate("Form", "AUTOCLCIKER"))
        self.label_2.setText(_translate("Form", "By LandChit"))
        self.groupBox.setTitle(_translate("Form", "Location"))
        self.comboBox.setItemText(0, _translate("Form", "Use Coordinates"))
        self.comboBox.setItemText(1, _translate("Form", "Follow Mouse"))
        self.comboBox.setItemText(2, _translate("Form", "Random Location"))
        self.label_3.setText(_translate("Form", "X"))
        self.label_4.setText(_translate("Form", "Y"))
        self.groupBox_2.setTitle(_translate("Form", "Start"))
        self.label_5.setText(_translate("Form", "delay"))
        self.label_6.setText(_translate("Form", "s"))
        self.label_7.setText(_translate("Form", "Press F1 for start and F2 for stop\n hold F2 more than your delay time\nthis program doesnt utilize threading"))
        
    def currentIndexChanged(self, index):
        if self.comboBox.itemText(index) == "Use Coordinates":
            self.x_sb.setDisabled(False)
            self.y_sb.setDisabled(False)
            self.runtype = 0
        elif self.comboBox.itemText(index) == "Follow Mouse":
            self.x_sb.setDisabled(True)
            self.y_sb.setDisabled(True)
            self.runtype = 1
        elif self.comboBox.itemText(index) == "Random Location":
            self.x_sb.setDisabled(True)
            self.y_sb.setDisabled(True)
            self.runtype = 2

    
    # get values
    def random_coords(self):
        height_coords = random.randint(0, height)
        width_coords = random.randint(0, width)
        return width_coords, height_coords
    def get_values(self):
        return self.x_sb.value(), self.y_sb.value(), self.delay_sb.value()
    
    # clicker part
    def start(self):
        x,y,delay = self.get_values()
        
        while True:
            if is_pressed('f2'):
                break
            if self.runtype == 0:
                pyautogui.click(x,y)
            elif self.runtype == 1:
                pyautogui.click(pyautogui.position())
            elif self.runtype == 2:
                pyautogui.click(self.random_coords())
            sleep(delay)

    


#checks if its started from this file therefore if this was imported it wouldnt work
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    width,height = screen_rect.width(), screen_rect.height()
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
