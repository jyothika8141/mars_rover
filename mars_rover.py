from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap

import requests
import os
import json

api_key = os.getenv('API_KEY')

link_lst =[]
ind = 1

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 743)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.head_label = QtWidgets.QLabel(self.centralwidget)
        self.head_label.setGeometry(QtCore.QRect(220, 10, 241, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        self.head_label.setFont(font)
        self.head_label.setObjectName("head_label")
        self.l_rover = QtWidgets.QLabel(self.centralwidget)
        self.l_rover.setGeometry(QtCore.QRect(190, 70, 62, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.l_rover.setFont(font)
        self.l_rover.setObjectName("l_rover")
        self.l_datetype = QtWidgets.QLabel(self.centralwidget)
        self.l_datetype.setGeometry(QtCore.QRect(190, 120, 81, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.l_datetype.setFont(font)
        self.l_datetype.setObjectName("l_datetype")
        self.l_cam = QtWidgets.QLabel(self.centralwidget)
        self.l_cam.setGeometry(QtCore.QRect(190, 260, 62, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.l_cam.setFont(font)
        self.l_cam.setObjectName("l_cam")
        self.l_pic = QtWidgets.QLabel(self.centralwidget)
        self.l_pic.setGeometry(QtCore.QRect(100, 360, 481, 261))
        self.l_pic.setText("")
        self.l_pic.setPixmap(QtGui.QPixmap("mars.jpg"))
        self.l_pic.setScaledContents(True)
        self.l_pic.setObjectName("l_pic")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 310, 131, 25))
        self.pushButton.setObjectName("pushButton")
        self.l_date = QtWidgets.QLabel(self.centralwidget)
        self.l_date.setGeometry(QtCore.QRect(190, 170, 91, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.l_date.setFont(font)
        self.l_date.setObjectName("l_date")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 640, 83, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 640, 83, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.cb_rover = QtWidgets.QComboBox(self.centralwidget)
        self.cb_rover.setGeometry(QtCore.QRect(370, 70, 151, 25))
        self.cb_rover.setObjectName("cb_rover")
        self.cb_rover.addItem("")
        self.cb_rover.addItem("")
        self.cb_rover.addItem("")
        self.cb_datetype = QtWidgets.QComboBox(self.centralwidget)
        self.cb_datetype.setGeometry(QtCore.QRect(370, 120, 151, 25))
        self.cb_datetype.setObjectName("cb_datetype")
        self.cb_datetype.addItem("")
        self.cb_datetype.addItem("")
        self.cb_cam = QtWidgets.QComboBox(self.centralwidget)
        self.cb_cam.setGeometry(QtCore.QRect(370, 250, 151, 25))
        self.cb_cam.setObjectName("cb_cam")
        self.cb_cam.addItem("")
        self.cb_cam.setItemText(0, "")
        self.cb_cam.addItem("")
        self.cb_cam.addItem("")
        self.cb_cam.addItem("")
        self.cb_cam.addItem("")
        self.cb_cam.addItem("")
        self.cb_cam.addItem("")
        self.cb_cam.addItem("")
        self.l_sol = QtWidgets.QLabel(self.centralwidget)
        self.l_sol.setGeometry(QtCore.QRect(190, 220, 121, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.l_sol.setFont(font)
        self.l_sol.setObjectName("l_sol")
        self.lineEdit_sol = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sol.setGeometry(QtCore.QRect(370, 210, 151, 25))
        self.lineEdit_sol.setObjectName("lineEdit_sol")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(370, 160, 151, 31))
        self.dateEdit.setObjectName("dateEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.pressed)
        self.pushButton_2.clicked.connect(self.previous)
        self.pushButton_3.clicked.connect(self.next)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.head_label.setText(_translate("MainWindow", "Martian Rover Images"))
        self.l_rover.setText(_translate("MainWindow", "Rover"))
        self.l_datetype.setText(_translate("MainWindow", "Date Type"))
        self.l_cam.setText(_translate("MainWindow", "Camera"))
        self.pushButton.setText(_translate("MainWindow", "Fetch Images"))
        self.l_date.setText(_translate("MainWindow", "Earth_date"))
        self.pushButton_2.setText(_translate("MainWindow", "Previous"))
        self.pushButton_3.setText(_translate("MainWindow", "Next"))
        self.cb_rover.setItemText(0, _translate("MainWindow", "Curiosity"))
        self.cb_rover.setItemText(1, _translate("MainWindow", "Opportunity"))
        self.cb_rover.setItemText(2, _translate("MainWindow", "Spirit"))
        self.cb_datetype.setItemText(0, _translate("MainWindow", "Earth date"))
        self.cb_datetype.setItemText(1, _translate("MainWindow", "Martian sol"))
        self.cb_cam.setItemText(1, _translate("MainWindow", "FHAZ"))
        self.cb_cam.setItemText(2, _translate("MainWindow", "RHAZ"))
        self.cb_cam.setItemText(3, _translate("MainWindow", "MAST"))
        self.cb_cam.setItemText(4, _translate("MainWindow", "CHEMCAM"))
        self.cb_cam.setItemText(5, _translate("MainWindow", "MAHLI"))
        self.cb_cam.setItemText(6, _translate("MainWindow", "MARDI"))
        self.cb_cam.setItemText(7, _translate("MainWindow", "NAVCAM"))
        self.l_sol.setText(_translate("MainWindow", "Martian_sol"))

    def pressed(self):
        global link_lst
        global ind

        link_lst = []
        ind = 1

        rover = self.cb_rover.currentText().lower()
        datetype = self.cb_datetype.currentText()
        e_date = self.dateEdit.date().toPyDate()
        sol = self.lineEdit_sol.text()
        cam = self.cb_cam.currentText().lower()

        if datetype == 'Earth date':
            if cam == '':
                url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={e_date}&api_key={api_key}"

            else:
                url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={e_date}&camera={cam}&api_key={api_key}"
        else:
            if sol == '':
                sol = 1000
            if cam == '':
                url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?sol={sol}&api_key={api_key}"
            else:
                url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?sol={sol}&camera={cam}&api_key={api_key}"
            

        response = requests.get(url)
        data = json.loads(response.text)

        count = 0
        for info in data['photos']:
            link_lst.append(info['img_src'])
            count += 1
            if count == 15:
                break
        
        print(link_lst)
        print(count)

        if len(link_lst) != 0:
            link = link_lst[0]
            print(link)

            image = QImage()
            image.loadFromData(requests.get(link).content)
            x = requests.get(link).content

            with open("image", "wb") as bin_file:
                bin_file.write(x)


            self.l_pic.setPixmap(QPixmap(image))
            self.l_pic.show()
        else:
            print("no pics")

    def previous(self):
        print("in pre")
        global ind
        ind -= 1

        try:
            link = link_lst[ind]
        except IndexError:
            ind = 0
            link = link_lst[ind]
            

        image = QImage()
        image.loadFromData(requests.get(link).content)


        self.l_pic.setPixmap(QPixmap(image))
        self.l_pic.show()

    def next(self):
        print("in next")
        global ind
        ind += 1

        try:
            link = link_lst[ind]
        except IndexError:
            ind = 0
            link = link_lst[ind]
        
        image = QImage()
        image.loadFromData(requests.get(link).content)


        self.l_pic.setPixmap(QPixmap(image))
        self.l_pic.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
