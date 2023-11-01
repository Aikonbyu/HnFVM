from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QWidget, QDialog, QVBoxLayout, QMessageBox)
from transitions import Machine

saldoTotal = 0
saldoAwal = 0
pilihanSayur = []
pilihanDressing = []

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(499, 624)

        # Ui Section
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 311, 501))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 291, 261))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(140, 120, 16, 20))
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(140, 240, 16, 20))
        self.timun = QLabel(self.frame_2)
        self.timun.setObjectName(u"timun")
        self.timun.setGeometry(QRect(0, 180, 63, 51))
        self.timun.setPixmap(QPixmap(u"images/Timun.png"))
        self.timun.setScaledContents(True)
        self.timun.setWordWrap(False)
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(250, 240, 16, 20))
        self.alpukad = QLabel(self.frame_2)
        self.alpukad.setObjectName(u"alpukad")
        self.alpukad.setGeometry(QRect(230, 180, 51, 61))
        self.alpukad.setPixmap(QPixmap(u"images/Alpukad.png"))
        self.alpukad.setScaledContents(True)
        self.selada = QLabel(self.frame_2)
        self.selada.setObjectName(u"selada")
        self.selada.setGeometry(QRect(0, 60, 63, 61))
        self.selada.setPixmap(QPixmap(u"images/Selada.png"))
        self.selada.setScaledContents(True)
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(120, 0, 41, 20))
        self.kubis = QLabel(self.frame_2)
        self.kubis.setObjectName(u"kubis")
        self.kubis.setGeometry(QRect(110, 180, 63, 61))
        self.kubis.setPixmap(QPixmap(u"images/Kubis.png"))
        self.kubis.setScaledContents(True)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(250, 120, 16, 20))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 120, 16, 20))
        self.tomat = QLabel(self.frame_2)
        self.tomat.setObjectName(u"tomat")
        self.tomat.setGeometry(QRect(110, 60, 63, 61))
        self.tomat.setPixmap(QPixmap(u"images/Tomat.png"))
        self.tomat.setScaledContents(True)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 240, 16, 20))
        self.wortel = QLabel(self.frame_2)
        self.wortel.setObjectName(u"wortel")
        self.wortel.setGeometry(QRect(210, 60, 71, 61))
        self.wortel.setPixmap(QPixmap(u"images/Wortel.png"))
        self.wortel.setScaledContents(True)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 20, 41, 20))
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(120, 20, 41, 20))
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(230, 20, 41, 20))
        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 140, 41, 20))
        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(130, 140, 31, 20))
        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(230, 140, 51, 20))
        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 160, 63, 20))
        self.label_32 = QLabel(self.frame_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(230, 160, 71, 20))
        self.label_33 = QLabel(self.frame_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(120, 160, 63, 20))
        self.label_34 = QLabel(self.frame_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(10, 40, 63, 20))
        self.label_35 = QLabel(self.frame_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(120, 40, 63, 20))
        self.label_36 = QLabel(self.frame_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(230, 40, 63, 20))
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 270, 291, 221))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(120, 0, 51, 20))
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 40, 63, 61))
        self.label_15.setPixmap(QPixmap(u"images/plain.png"))
        self.label_15.setScaledContents(True)
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(190, 40, 63, 61))
        self.label_16.setPixmap(QPixmap(u"images/sm.png"))
        self.label_16.setScaledContents(True)
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(40, 140, 61, 61))
        self.label_17.setPixmap(QPixmap(u"images/oliveoil.png"))
        self.label_17.setScaledContents(True)
        self.saltn = QLabel(self.frame_3)
        self.saltn.setObjectName(u"saltn")
        self.saltn.setGeometry(QRect(190, 140, 63, 71))
        self.saltn.setPixmap(QPixmap(u"images/saltandpepper.png"))
        self.saltn.setScaledContents(True)
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(70, 100, 16, 20))
        self.label_24 = QLabel(self.frame_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(220, 100, 16, 20))
        self.label_25 = QLabel(self.frame_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(70, 200, 16, 20))
        self.label_26 = QLabel(self.frame_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(220, 200, 16, 20))
        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(20, 20, 101, 20))
        self.label_28 = QLabel(self.frame_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(170, 20, 101, 20))
        self.label_29 = QLabel(self.frame_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(50, 130, 51, 20))
        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(190, 130, 81, 20))
        self.frame_4 = QFrame(Widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(330, 50, 161, 191))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(70, 80, 31, 29))
        self.pushButton_d = QPushButton(self.frame_4)
        self.pushButton_d.setObjectName(u"pushButton_d")
        self.pushButton_d.setGeometry(QRect(60, 140, 31, 29))
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 80, 31, 29))
        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(40, 80, 31, 29))
        self.pushButton_c = QPushButton(self.frame_4)
        self.pushButton_c.setObjectName(u"pushButton_c")
        self.pushButton_c.setGeometry(QRect(20, 140, 31, 29))
        self.pushButton_next = QPushButton(self.frame_4)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setGeometry(QRect(120, 140, 31, 29))
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(70, 50, 31, 29))
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 31, 20))
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(40, 50, 31, 29))
        self.pushButton_a = QPushButton(self.frame_4)
        self.pushButton_a.setObjectName(u"pushButton_a")
        self.pushButton_a.setGeometry(QRect(20, 110, 31, 29))
        self.pushButton_1 = QPushButton(self.frame_4)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(10, 50, 31, 29))
        self.saldo = QLineEdit(self.frame_4)
        self.saldo.setObjectName(u"saldo")
        self.saldo.setGeometry(QRect(40, 10, 111, 25))
        self.saldo.setReadOnly(True)
        self.saldo.setText("Rp " + str(saldoTotal))
        self.pushButton_reset = QPushButton(self.frame_4)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setGeometry(QRect(120, 60, 31, 29))
        self.pushButton_cancel = QPushButton(self.frame_4)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(120, 100, 31, 29))
        self.pushButton_b = QPushButton(self.frame_4)
        self.pushButton_b.setObjectName(u"pushButton_b")
        self.pushButton_b.setGeometry(QRect(60, 110, 31, 29))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 250, 91, 20))
        self.pushButton_uang = QPushButton(Widget)
        self.pushButton_uang.setObjectName(u"pushButton_uang")
        self.pushButton_uang.setGeometry(QRect(330, 270, 161, 29))
        self.pushButton_salad = QPushButton(Widget)
        self.pushButton_salad.setObjectName(u"pushButton_salad")
        self.pushButton_salad.setGeometry(QRect(10, 520, 311, 91))
        self.pushButton_kembalian = QPushButton(Widget)
        self.pushButton_kembalian.setObjectName(u"pushButton_kembalian")
        self.pushButton_kembalian.setGeometry(QRect(360, 540, 61, 61))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 520, 63, 20))
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 530, 101, 41))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 570, 211, 20))
        self.textBrowser = QTextBrowser(Widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(330, 310, 161, 171))
        self.pushButton_1.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.pushButton_a.setDisabled(True)
        self.pushButton_b.setDisabled(True)
        self.pushButton_c.setDisabled(True)
        self.pushButton_d.setDisabled(True)
        self.pushButton_next.setDisabled(True)
        self.pushButton_reset.setDisabled(True)
        self.pushButton_cancel.setDisabled(True)
        self.pushButton_kembalian.setDisabled(True)
        self.pushButton_salad.setDisabled(True)

        self.retranslateUi(Widget)
        
        self.pushButton_uang.clicked.connect(self.openDompet)
        self.pushButton_kembalian.clicked.connect(lambda:self.tampilKembalian())
        self.pushButton_next.clicked.connect(lambda:vending_machine.next(self))
        self.pushButton_cancel.clicked.connect(lambda:vending_machine.cancel(self))
        self.pushButton_reset.clicked.connect(lambda:vending_machine.reset(self))
        self.pushButton_1.clicked.connect(lambda:vending_machine.pilih_sayuran(self, 'a'))
        self.pushButton_2.clicked.connect(lambda:vending_machine.pilih_sayuran(self, 'b'))
        self.pushButton_3.clicked.connect(lambda:vending_machine.pilih_sayuran(self, 'c'))
        self.pushButton_4.clicked.connect(lambda:vending_machine.pilih_sayuran(self, 'd'))
        self.pushButton_5.clicked.connect(lambda:vending_machine.pilih_sayuran(self, 'e'))
        self.pushButton_6.clicked.connect(lambda:vending_machine.pilih_sayuran(self, 'f'))
        self.pushButton_a.clicked.connect(lambda:vending_machine.pilih_dressing(self, 'g'))
        self.pushButton_b.clicked.connect(lambda:vending_machine.pilih_dressing(self, 'h'))
        self.pushButton_c.clicked.connect(lambda:vending_machine.pilih_dressing(self, 'i'))
        self.pushButton_d.clicked.connect(lambda:vending_machine.pilih_dressing(self, 'j'))


        self.pushButton_salad.clicked.connect(lambda:self.tampilSalad())

        QMetaObject.connectSlotsByName(Widget)

        # Funciton Section
        
    def tampilSalad(self):
        global pilihanSayur
        global pilihanDressing
        global saldoTotal
        global saldoAwal
        self.dialog = Salad()
        self.dialog.exec_()
        self.pushButton_salad.setDisabled(True)
        if saldoTotal > 0:
            self.pushButton_kembalian.setEnabled(True)
        if(saldoTotal == 0):
            self.pushButton_uang.setEnabled(True)
            pilihanDressing.clear()
            pilihanSayur.clear()
            saldoTotal = 0
            saldoAwal = 0
            self.saldo.setText("Rp " + str(saldoTotal))
        
        self.dialog.close()
    
    def tampilKembalian(self):
        global saldoTotal
        global saldoAwal
        global  pilihanSayur
        global pilihanDressing
        self.dialog = Kembalian()
        self.dialog.exec_()
        self.pushButton_kembalian.setDisabled(True)
        pilihanDressing.clear()
        pilihanSayur.clear()
        saldoTotal = 0
        saldoAwal = 0
        self.saldo.setText("Rp " + str(saldoTotal))
        self.pushButton_uang.setEnabled(True)
        self.dialog.close()

    def openDompet(self):
        self.dialog = Dompet()
        self.dialog.exec_()
        self.saldo.setText("Rp " + str(saldoTotal))
        if(saldoTotal >= 15000):
            self.pushButton_next.setEnabled(True)
        if(saldoTotal > 0):
            self.pushButton_cancel.setEnabled(True)
        self.dialog.close()
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"2", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"5", None))
        self.timun.setText("")
        self.label_12.setText(QCoreApplication.translate("Widget", u"6", None))
        self.alpukad.setText("")
        self.selada.setText("")
        self.label_13.setText(QCoreApplication.translate("Widget", u"Sayuran", None))
        self.kubis.setText("")
        self.label_9.setText(QCoreApplication.translate("Widget", u"3", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"1", None))
        self.tomat.setText("")
        self.label_10.setText(QCoreApplication.translate("Widget", u"4", None))
        self.wortel.setText("")
        self.label_7.setText(QCoreApplication.translate("Widget", u"Selada", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"Tomat", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"Wortel", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"Timun", None))
        self.label_21.setText(QCoreApplication.translate("Widget", u"Kubis", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"Alpukad", None))
        self.label_31.setText(QCoreApplication.translate("Widget", u"Rp 5.000", None))
        self.label_32.setText(QCoreApplication.translate("Widget", u"Rp 10.000", None))
        self.label_33.setText(QCoreApplication.translate("Widget", u"Rp 5.000", None))
        self.label_34.setText(QCoreApplication.translate("Widget", u"Rp 5.000", None))
        self.label_35.setText(QCoreApplication.translate("Widget", u"Rp 5.000", None))
        self.label_36.setText(QCoreApplication.translate("Widget", u"Rp 5.000", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"Dressing", None))
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.saltn.setText("")
        self.label_23.setText(QCoreApplication.translate("Widget", u"A", None))
        self.label_24.setText(QCoreApplication.translate("Widget", u"B", None))
        self.label_25.setText(QCoreApplication.translate("Widget", u"C", None))
        self.label_26.setText(QCoreApplication.translate("Widget", u"D", None))
        self.label_27.setText(QCoreApplication.translate("Widget", u"Plain Mayonnaise", None))
        self.label_28.setText(QCoreApplication.translate("Widget", u"Spicy Mayonnaise", None))
        self.label_29.setText(QCoreApplication.translate("Widget", u"Olive Oil", None))
        self.label_30.setText(QCoreApplication.translate("Widget", u"Salt & Pepper", None))
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"6", None))
        self.pushButton_d.setText(QCoreApplication.translate("Widget", u"D", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"5", None))
        self.pushButton_c.setText(QCoreApplication.translate("Widget", u"C", None))
        self.pushButton_next.setText(QCoreApplication.translate("Widget", u">", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"3", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Saldo", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"2", None))
        self.pushButton_a.setText(QCoreApplication.translate("Widget", u"A", None))
        self.pushButton_1.setText(QCoreApplication.translate("Widget", u"1", None))
        self.pushButton_reset.setText(QCoreApplication.translate("Widget", u"<", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Widget", u"x", None))
        self.pushButton_b.setText(QCoreApplication.translate("Widget", u"B", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Masukkan Uang", None))
        self.pushButton_uang.setText("")
        self.pushButton_salad.setText("")
        self.pushButton_kembalian.setText("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"Kembalian", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"P U L L", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Please open it when the light is flashing", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">Petunjuk Penggunaan:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">1. Masukkan uang dengan nominal 5.000, 10.000, dan 20.000, batas maksimum saldo senilai 40.000 dan minimum 15.000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">2. Pilih sayuran yang diinginkan dengan memilih angka yang sudah tersedia</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">3. Pilih dressing yang diinginkan dengan memilih huruf yang sudah tersedia</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">4. Ambil salad dan kembalian di tempat yang telah tersedia</span></p></body></html>", None))

class Salad(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Salad')
        self.setGeometry(400, 400, 300, 300)
        self.initUI()

    def initUI(self):
        global saldoTotal
        global saldoAwal
        global pilihanSayur
        global pilihanDressing

        layout = QVBoxLayout()

        # Widget Salad
        salad = QLabel(self)
        salad.setObjectName("salad")
        salad.setFixedSize(400, 200)
        salad.setPixmap(QPixmap("images/salad.png"))
        salad.setScaledContents(True)
        layout.addWidget(salad)

        # Widget SaladPilihan
        saladPilihan = QLabel("Sayuran yang dipilih: " + str(pilihanSayur))
        layout.addWidget(saladPilihan)

        # Widget DressingPilihan
        dressingPilihan = QLabel("Dressing yang dipilih: " + str(pilihanDressing))
        layout.addWidget(dressingPilihan)

        self.setLayout(layout)

class Kembalian(QDialog, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Kembalian')
        self.setGeometry(200, 200, 400, 600)
        self.initUI()
    
    def initUI(self):
        global saldoTotal
        layout = QVBoxLayout()

        if saldoTotal == 5000:
            kembalian1 = QLabel(self)
            kembalian1.setObjectName("kembalian1")
            kembalian1.setFixedSize(400, 200)
            kembalian1.setPixmap(QPixmap("images/5ribu.png"))
            kembalian1.setScaledContents(True)
            layout.addWidget(kembalian1)
        elif saldoTotal == 10000:
            kembalian2 = QLabel(self)
            kembalian2.setObjectName("kembalian2")
            kembalian2.setFixedSize(400, 200)
            kembalian2.setPixmap(QPixmap("images/10ribu.png"))
            kembalian2.setScaledContents(True)
            layout.addWidget(kembalian2)
        elif saldoTotal == 15000:
            kembalian1 = QLabel(self)
            kembalian1.setObjectName("kembalian1")
            kembalian1.setFixedSize(400, 200)
            kembalian1.setPixmap(QPixmap("images/5ribu.png"))
            kembalian1.setScaledContents(True)
            layout.addWidget(kembalian1)

            kembalian2 = QLabel(self)
            kembalian2.setObjectName("kembalian2")
            kembalian2.setFixedSize(400, 200)
            kembalian2.setPixmap(QPixmap("images/10ribu.png"))
            kembalian2.setScaledContents(True)
            layout.addWidget(kembalian2)
        elif saldoTotal == 20000:
            kembalian3 = QLabel(self)
            kembalian3.setObjectName("kembalian3")
            kembalian3.setFixedSize(400, 200)
            kembalian3.setPixmap(QPixmap("images/20ribu.png"))
            kembalian3.setScaledContents(True)
            layout.addWidget(kembalian3)
        elif saldoTotal == 25000:
            kembalian1 = QLabel(self)
            kembalian1.setObjectName("kembalian1")
            kembalian1.setFixedSize(400, 200)
            kembalian1.setPixmap(QPixmap("images/5ribu.png"))
            kembalian1.setScaledContents(True)
            layout.addWidget(kembalian1)

            kembalian3 = QLabel(self)
            kembalian3.setObjectName("kembalian3")
            kembalian3.setFixedSize(400, 200)
            kembalian3.setPixmap(QPixmap("images/20ribu.png"))
            kembalian3.setScaledContents(True)
            layout.addWidget(kembalian3)
        elif saldoTotal == 30000:
            kembalian2 = QLabel(self)
            kembalian2.setObjectName("kembalian2")
            kembalian2.setFixedSize(400, 200)
            kembalian2.setPixmap(QPixmap("images/10ribu.png"))
            kembalian2.setScaledContents(True)
            layout.addWidget(kembalian2)

            kembalian3 = QLabel(self)
            kembalian3.setObjectName("kembalian3")
            kembalian3.setFixedSize(400, 200)
            kembalian3.setPixmap(QPixmap("images/20ribu.png"))
            kembalian3.setScaledContents(True)
            layout.addWidget(kembalian3)
        elif saldoTotal == 35000:
            kembalian1 = QLabel(self)
            kembalian1.setObjectName("kembalian1")
            kembalian1.setFixedSize(400, 200)
            kembalian1.setPixmap(QPixmap("images/5ribu.png"))
            kembalian1.setScaledContents(True)
            layout.addWidget(kembalian1)

            kembalian2 = QLabel(self)
            kembalian2.setObjectName("kembalian2")
            kembalian2.setFixedSize(400, 200)
            kembalian2.setPixmap(QPixmap("images/10ribu.png"))
            kembalian2.setScaledContents(True)
            layout.addWidget(kembalian2)

            kembalian3 = QLabel(self)
            kembalian3.setObjectName("kembalian3")
            kembalian3.setFixedSize(400, 200)
            kembalian3.setPixmap(QPixmap("images/20ribu.png"))
            kembalian3.setScaledContents(True)
            layout.addWidget(kembalian3)
        elif saldoTotal == 40000:
            kembalian4 = QLabel(self)
            kembalian4.setObjectName("kembalian4")
            kembalian4.setFixedSize(400, 200)
            kembalian4.setPixmap(QPixmap("images/20ribu.png"))
            kembalian4.setScaledContents(True)
            layout.addWidget(kembalian4)

            kembalian5 = QLabel(self)
            kembalian5.setObjectName("kembalian5")
            kembalian5.setFixedSize(400, 200)
            kembalian5.setPixmap(QPixmap("images/20ribu.png"))
            kembalian5.setScaledContents(True)
            layout.addWidget(kembalian5)
        self.setLayout(layout)

    


class Dompet(QDialog, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dompet')
        self.setGeometry(200, 200, 300, 150)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Buat tombol tekan untuk gambar pertama
        button1 = QPushButton(self)
        button1.setFixedSize(400,200)
        button1.setIconSize(button1.size())
        pixmap1 = QPixmap(u"images/5ribu.png")
        button1.setIcon(pixmap1)
        layout.addWidget(button1)

        # Buat tombol tekan untuk gambar kedua
        button2 = QPushButton(self)
        button2.setFixedSize(400,200)
        button2.setIconSize(button2.size())
        pixmap2 = QPixmap(u"images/10ribu.png")
        button2.setIcon(pixmap2)
        layout.addWidget(button2)

        # Buat tombol tekan untuk gambar ketiga
        button3 = QPushButton(self)
        button3.setFixedSize(400,200)
        button3.setIconSize(button3.size())
        pixmap3 = QPixmap(u"images/20ribu.png")
        button3.setIcon(pixmap3)
        layout.addWidget(button3)

        self.setLayout(layout)
        button1.clicked.connect(lambda:self.tambahSaldo(5000))
        button2.clicked.connect(lambda:self.tambahSaldo(10000))
        button3.clicked.connect(lambda:self.tambahSaldo(20000))

    def show_alert(amount):   
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Uang Dikembalikan")
        msg_box.setText("Saldo yang anda masukkan melebihi batas maksimum!!!")
        msg_box.setText("Rp " + str(amount) + " telah dikembalikan")
        msg_box.addButton(QMessageBox.Ok)
        msg_box.exec()

    def tambahSaldo(self, uang):
        global saldoTotal
        if saldoTotal + uang > 40000:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Uang Dikembalikan")
            msg_box.setText("Saldo yang anda masukkan melebihi batas maksimum!!! \n Rp " + str(uang) + " telah dikembalikan")
            msg_box.addButton(QMessageBox.Ok)
            msg_box.exec()
            self.reject()
        else:
            saldoTotal += uang
            self.accept()

class vending_machine(object):
    states = ['Q0', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11' 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20' 'Q21', 'Q22', 'Q23']
    sayuran = ['Selada', 'Tomat', 'Wortel', 'Timun', 'Kubis', 'Alpukat']
    dressing = ['Plain Mayonnaise', 'Spicy Mayonnaise', 'Olive Oil', 'Salt & Pepper']
    amount = 0
    choice = 0

    def next(self):
        global pilihanSayur
        global pilihanDressing
        global saldoTotal
        global saldoAwal
        if len(pilihanSayur) == 0:
            self.pushButton_1.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.pushButton_uang.setDisabled(True)
            self.pushButton_cancel.setDisabled(True)
            self.pushButton_next.setDisabled(True)
            saldoAwal = saldoTotal
        elif len(pilihanSayur) != 0 and len(pilihanDressing) == 0:
            self.pushButton_1.setDisabled(True)
            self.pushButton_2.setDisabled(True)
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setDisabled(True)
            self.pushButton_5.setDisabled(True)
            self.pushButton_6.setDisabled(True)

            self.pushButton_a.setEnabled(True)
            self.pushButton_b.setEnabled(True)
            self.pushButton_c.setEnabled(True)
            self.pushButton_d.setEnabled(True)
            
            self.pushButton_next.setDisabled(True)
            self.pushButton_reset.setDisabled(True)
        elif len(pilihanDressing) != 0:
            self.pushButton_a.setDisabled(True)
            self.pushButton_b.setDisabled(True)
            self.pushButton_c.setDisabled(True)
            self.pushButton_d.setDisabled(True)
            self.pushButton_salad.setEnabled(True)
            self.pushButton_next.setDisabled(True)
            self.pushButton_reset.setDisabled(True)

    def cancel(self):
        self.pushButton_kembalian.setEnabled(True)
        self.pushButton_cancel.setDisabled(True)
        self.pushButton_next.setDisabled(True)
        self.pushButton_uang.setDisabled(True)
    
    def reset(self):
        global pilihanSayur
        global pilihanDressing
        global saldoTotal
        global saldoAwal

        if (len(pilihanSayur) != 0 and len(pilihanDressing) == 0):
            pilihanSayur.clear()
            saldoTotal = saldoAwal
            self.saldo.setText("Rp " + str(saldoTotal))
            self.pushButton_1.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.pushButton_next.setDisabled(True)
            self.pushButton_reset.setDisabled(True)
        if (len(pilihanSayur) != 0 and len(pilihanDressing) != 0):
            pilihanDressing.clear()
            self.pushButton_a.setEnabled(True)
            self.pushButton_b.setEnabled(True)
            self.pushButton_c.setEnabled(True)
            self.pushButton_d.setEnabled(True)
            self.pushButton_next.setDisabled(True)
            self.pushButton_reset.setDisabled(True)

    def pilih_sayuran(self, input):
        global pilihanSayur
        global saldoTotal
        global saldoAwal
        if input == 'a':
            pilihanSayur.append('Selada')
            saldoTotal -= 5000
            self.pushButton_1.setDisabled(True)
            self.pushButton_6.setEnabled(True)
        elif input == 'b':
            pilihanSayur.append('Tomat')
            saldoTotal -= 5000
            self.pushButton_1.setDisabled(True)
            self.pushButton_2.setDisabled(True)
            self.pushButton_6.setEnabled(True)
        elif input == 'c':
            pilihanSayur.append('Wortel')
            saldoTotal -= 5000
            self.pushButton_1.setDisabled(True)
            self.pushButton_2.setDisabled(True)
            self.pushButton_3.setDisabled(True)
            self.pushButton_6.setEnabled(True)
        elif input == 'd':
            pilihanSayur.append('Timun')
            saldoTotal -= 5000
            self.pushButton_1.setDisabled(True)
            self.pushButton_2.setDisabled(True)
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setDisabled(True)
            self.pushButton_6.setEnabled(True)
        elif input == 'e':
            pilihanSayur.append('Kubis')
            saldoTotal -= 5000
            self.pushButton_1.setDisabled(True)
            self.pushButton_2.setDisabled(True)
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setDisabled(True)
            self.pushButton_5.setDisabled(True)
            self.pushButton_6.setEnabled(True)
        elif input == 'f':
            pilihanSayur.append('Alpukat')
            saldoTotal -= 10000
            self.pushButton_1.setDisabled(True)
            self.pushButton_2.setDisabled(True)
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setDisabled(True)
            self.pushButton_5.setDisabled(True)
            self.pushButton_6.setDisabled(True)
        self.saldo.setText("Rp " + str(saldoTotal))

        if len(pilihanSayur) != 0:
            self.pushButton_reset.setEnabled(True)
        
        if saldoAwal - saldoTotal >= 15000:
            self.pushButton_next.setEnabled(True)

        if saldoTotal <= 5000:
            self.pushButton_6.setDisabled(True)
        if saldoTotal < 5000:
            self.pushButton_1.setDisabled(True)
            self.pushButton_2.setDisabled(True)
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setDisabled(True)
            self.pushButton_5.setDisabled(True)
            self.pushButton_6.setDisabled(True)

    def pilih_dressing(self, input):
        if input == 'g':
            pilihanDressing.append('Plain Mayonnaise')
            self.pushButton_a.setDisabled(True)
            self.pushButton_b.setDisabled(True)
            self.pushButton_c.setDisabled(True)
            self.pushButton_d.setDisabled(True)
        elif input == 'h':
            pilihanDressing.append('Spicy Mayonnaise')
            self.pushButton_a.setDisabled(True)
            self.pushButton_b.setDisabled(True)
            self.pushButton_c.setDisabled(True)
            self.pushButton_d.setDisabled(True)
        elif input == 'i':
            pilihanDressing.append('Olive Oil')
            self.pushButton_a.setDisabled(True)
            self.pushButton_b.setDisabled(True)
            self.pushButton_c.setDisabled(True)
            self.pushButton_d.setDisabled(True)
        elif input == 'j':
            pilihanDressing.append('Salt & Pepper')
            self.pushButton_a.setDisabled(True)
            self.pushButton_b.setDisabled(True)
            self.pushButton_c.setDisabled(True)
            self.pushButton_d.setDisabled(True)
        self.pushButton_next.setEnabled(True)
        self.pushButton_reset.setEnabled(True)

    def __init__(self):
        self.machine = Machine(model=self, states=vending_machine.states, initial='Q0')

        self.machine.add_transition('x', 'Q1', 'Q0')
        self.machine.add_transition('x', 'Q2', 'Q1')
        self.machine.add_transition('x', 'Q3', 'Q2')
        self.machine.add_transition('x', 'Q4', 'Q3')
        self.machine.add_transition('x', 'Q5', 'Q4')
        self.machine.add_transition('x', 'Q6', 'Q5')
        self.machine.add_transition('x', 'Q7', 'Q6')
        self.machine.add_transition('x', 'Q8', 'Q7')
        self.machine.add_transition('x', 'Q8', 'Q8')

        self.machine.add_transition('y', 'Q2', 'Q0')
        self.machine.add_transition('y', 'Q3', 'Q1')
        self.machine.add_transition('y', 'Q4', 'Q2')
        self.machine.add_transition('y', 'Q5', 'Q3')
        self.machine.add_transition('y', 'Q6', 'Q4')
        self.machine.add_transition('y', 'Q7', 'Q5')
        self.machine.add_transition('y', 'Q8', 'Q6')
        self.machine.add_transition('y', 'Q7', 'Q7')
        self.machine.add_transition('y', 'Q8', 'Q8')

        self.machine.add_transition('z', 'Q4', 'Q0')
        self.machine.add_transition('z', 'Q5', 'Q1')
        self.machine.add_transition('z', 'Q6', 'Q2')
        self.machine.add_transition('z', 'Q7', 'Q3')
        self.machine.add_transition('z', 'Q8', 'Q4')
        self.machine.add_transition('z', 'Q5', 'Q5')
        self.machine.add_transition('z', 'Q6', 'Q6')
        self.machine.add_transition('z', 'Q6', 'Q7')
        self.machine.add_transition('z', 'Q7', 'Q8')

        self.machine.add_transition('a', 'Q0', 'Q0')
        self.machine.add_transition('a', 'Q10', 'Q9')

        self.machine.add_transition('b', 'Q0', 'Q0')
        self.machine.add_transition('b', 'Q11', 'Q9')
        self.machine.add_transition('b', 'Q11', 'Q10')

        self.machine.add_transition('c', 'Q0', 'Q0')
        self.machine.add_transition('c', 'Q12', 'Q9')
        self.machine.add_transition('c', 'Q12', 'Q10')
        self.machine.add_transition('c', 'Q12', 'Q11')

        self.machine.add_transition('d', 'Q0', 'Q0')
        self.machine.add_transition('d', 'Q13', 'Q9')
        self.machine.add_transition('d', 'Q13', 'Q10')
        self.machine.add_transition('d', 'Q13', 'Q11')
        self.machine.add_transition('d', 'Q13', 'Q12')

        self.machine.add_transition('e', 'Q0', 'Q0')
        self.machine.add_transition('e', 'Q14', 'Q9')
        self.machine.add_transition('e', 'Q14', 'Q10')
        self.machine.add_transition('e', 'Q14', 'Q11')
        self.machine.add_transition('e', 'Q14', 'Q12')
        self.machine.add_transition('e', 'Q14', 'Q13')

        self.machine.add_transition('f', 'Q0', 'Q0')
        self.machine.add_transition('f', 'Q15', 'Q10')
        self.machine.add_transition('f', 'Q15', 'Q11')
        self.machine.add_transition('f', 'Q15', 'Q12')
        self.machine.add_transition('f', 'Q15', 'Q13')
        self.machine.add_transition('f', 'Q15', 'Q14')

        self.machine.add_transition('g', 'Q0', 'Q0')
        self.machine.add_transition('g', 'Q17', 'Q16')

        self.machine.add_transition('h', 'Q0', 'Q0')
        self.machine.add_transition('h', 'Q18', 'Q16')

        self.machine.add_transition('i', 'Q0', 'Q0')
        self.machine.add_transition('i', 'Q19', 'Q16')

        self.machine.add_transition('j', 'Q0', 'Q0')
        self.machine.add_transition('j', 'Q20', 'Q16')

        self.machine.add_transition('p', 'Q0', 'Q0')
        self.machine.add_transition('p', 'Q9', 'Q10')
        self.machine.add_transition('p', 'Q9', 'Q11')
        self.machine.add_transition('p', 'Q9', 'Q12')
        self.machine.add_transition('p', 'Q9', 'Q13')
        self.machine.add_transition('p', 'Q9', 'Q14')
        self.machine.add_transition('p', 'Q9', 'Q15')
        self.machine.add_transition('p', 'Q16', 'Q17')
        self.machine.add_transition('p', 'Q16', 'Q18')
        self.machine.add_transition('p', 'Q16', 'Q19')
        self.machine.add_transition('p', 'Q16', 'Q20')

        self.machine.add_transition('r', 'Q0', 'Q0')
        self.machine.add_transition('r', 'Q22', 'Q1')
        self.machine.add_transition('r', 'Q22', 'Q2')
        self.machine.add_transition('r', 'Q22', 'Q3')
        self.machine.add_transition('r', 'Q22', 'Q4')
        self.machine.add_transition('r', 'Q22', 'Q5')
        self.machine.add_transition('r', 'Q22', 'Q6')
        self.machine.add_transition('r', 'Q22', 'Q7')
        self.machine.add_transition('r', 'Q22', 'Q8')

        self.machine.add_transition('s', 'Q0', 'Q0')
        self.machine.add_transition('s', 'Q9', 'Q3')
        self.machine.add_transition('s', 'Q9', 'Q4')
        self.machine.add_transition('s', 'Q9', 'Q5')
        self.machine.add_transition('s', 'Q9', 'Q6')
        self.machine.add_transition('s', 'Q9', 'Q7')
        self.machine.add_transition('s', 'Q9', 'Q8')
        self.machine.add_transition('s', 'Q16', 'Q12')
        self.machine.add_transition('s', 'Q16', 'Q13')
        self.machine.add_transition('s', 'Q16', 'Q14')
        self.machine.add_transition('s', 'Q16', 'Q15')
        self.machine.add_transition('s', 'Q21', 'Q17')
        self.machine.add_transition('s', 'Q21', 'Q18')
        self.machine.add_transition('s', 'Q21', 'Q19')
        self.machine.add_transition('s', 'Q21', 'Q20')