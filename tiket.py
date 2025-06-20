from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog  
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 40, 281, 211))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(parent=self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(2, "")
        self.gridLayout.addWidget(self.comboBox, 8, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 9, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # untuk menghubungkan tombol ke fungsi (signal slot)
        self.pushButton.clicked.connect(self.hitung_total)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "Solo-Jogja"))
        self.comboBox.setItemText(1, _translate("Dialog", "Jogja-Solo"))
        self.pushButton.setText(_translate("Dialog", "Beli!"))
        self.label_2.setText(_translate("Dialog", "jumlah penumpang :"))
        self.label_3.setText(_translate("Dialog", "Asal - Tujuan"))
        self.label.setText(_translate("Dialog", "Tiket KRL JOGJA SOLO"))
        self.label_4.setText(_translate("Dialog", "Rp 8000/penumpang"))

    def hitung_total(self):
        try:
            jumlah = int(self.lineEdit_2.text())
            if jumlah <= 0:
                raise ValueError

            harga_per_penumpang = 8000
            total = jumlah * harga_per_penumpang
            rute = self.comboBox.currentText()

            
            pesan = (
                f"Pembelian Berhasil!\n\n"
                f"Rute: {rute}\n"
                f"Jumlah Penumpang: {jumlah}\n"
                f"Total Harga: Rp {total}"
            )

            QtWidgets.QMessageBox.information(
                self.Dialog,
                "Tiket KRL",
                pesan
            )

        except ValueError:
            QtWidgets.QMessageBox.warning(
                self.Dialog,
                "Input Tidak Valid",
                "Masukkan jumlah penumpang sebagai angka lebih dari nol."
            )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
