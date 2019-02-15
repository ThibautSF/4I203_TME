import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import QFile, QTextStream, QIODevice


class MainWindow(QMainWindow):
	
	###############
	def __init__(self, *args, **kwargs):
		#Appel constructeur parent
		QMainWindow.__init__(self, *args, **kwargs)
		self.resize(300,300)
		
		#MenuBar
		menu = self.menuBar()
		fileM = menu.addMenu('Fichier')
		
		openAct = QAction(QIcon("open.png"), 'Open...', self )
		openAct.setShortcut( QKeySequence('Ctrl+O' ) )
		openAct.setToolTip('Open')
		openAct.setStatusTip('Open')
		openAct.triggered.connect(self.open)
		fileM.addAction(openAct)
		
		saveAct = QAction(QIcon("save.png"), 'Save', self )
		saveAct.setShortcut( QKeySequence('Ctrl+S' ) )
		saveAct.setToolTip('Save')
		saveAct.setStatusTip('Save')
		saveAct.triggered.connect(self.save)
		fileM.addAction(saveAct)
		
		quitAct = QAction(QIcon("quit.png"), 'Quit', self )
		quitAct.setShortcut( QKeySequence('Ctrl+Q' ) )
		quitAct.setToolTip('Quit')
		quitAct.setStatusTip('Quit')
		quitAct.triggered.connect(self.quit)
		fileM.addAction(quitAct)
		
		#Central
		textEdit = QTextEdit(self)
		self.setCentralWidget(textEdit)
		
		#StatusBar
		status = self.statusBar()
	
	###############
	def open(self):
		filename = QFileDialog.getOpenFileName(self, "Open text", "", "")
		
		if filename[0]!='':
			file = QFile(filename[0])
			
			if not file.open(QIODevice.ReadOnly | QIODevice.Text):
				return
			
			fileStream = QTextStream(file)
			
			lines = ''
			while not fileStream.atEnd():
				lines += '\n'+fileStream.readLine()
			
			textEdit = self.centralWidget()
			textEdit.setHtml(lines)
			
			file.close()
		
	
	###############
	def save(self):
		filename = QFileDialog.getSaveFileName(self, "Save file", "", "")
		
		if filename[0]!='':
			file = QFile(filename[0])
			
			if not file.open(QIODevice.WriteOnly | QIODevice.Text):
				return
			
			textEdit = self.centralWidget()
			fileStream = QTextStream(file)
			
			fileStream << textEdit.toHtml()
			
			file.close()
		

	###############
	def quit(self):
		print("Quit")


def main(args):
	#print("Hello World")
	app = QApplication(args)
	win = MainWindow()
	win.show()
	app.exec()
	

if __name__ == "__main__":
	main(sys.argv)
