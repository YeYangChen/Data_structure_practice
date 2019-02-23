import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from random import randint

class Example(QWidget):

	def __init__(self):
		super().__init__()
		self.num = randint(1,100)

		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle('Guess number')

		self.bt1 = QPushButton('guess', self)
		self.bt1.setGeometry(115, 150, 70, 30)
		self.bt1.setToolTip('<b>click to make a guess</b>')
		self.bt1.clicked.connect(self.showMessage)

		self.text = QLineEdit('enter your number', self)
		self.text.selectAll()
		self.text.setFocus()
		self.text.setGeometry(80, 50, 150 ,30)

		self.show()

	def showMessage(self):
		guessnumber = int(self.text.text())
		print(self.num)
		if guessnumber > self.num:
			QMessageBox.about(self,'your guess', 'is bigger')
			self.text.setFocus()
		elif guessnumber < self.num:
			QMessageBox.about(self,'your guess', 'is smaller')
			self.text.setFocus()
		else:
			QMessageBox.about(self,'you got the', 'right number!')
			self.num = randint(1,100)
			self.text.clear()
			self.text.setFocus()

	def closeEvent(self,event):
		reply = QMessageBox.question(self,'Sure','Sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if  reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

if __name__ == '__main__':

	app =  QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())