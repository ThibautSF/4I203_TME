import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Canvas import *
import resources

class MainWindow(QMainWindow):

    def __init__(self, parent = None ):
        QMainWindow.__init__(self, parent )
        print( "init mainwindow")
        self.resize(600, 500)

        bar = self.menuBar()
        fileMenu = bar.addMenu("File")
        actOpen = fileMenu.addAction( QIcon(":/icons/open.png"), "&Open...", self.open, QKeySequence("Ctrl+O") )
        actSave = fileMenu.addAction( QIcon(":/icons/save.png"), "&Save...", self.save, QKeySequence("Ctrl+S") )
        actQuit = fileMenu.addAction( QIcon(":/icons/quit.png"), "&Quit...", self.quit, QKeySequence("Ctrl+Q") )

        fileToolBar = QToolBar("File")
        self.addToolBar( fileToolBar )
        fileToolBar.addAction( actOpen )
        fileToolBar.addAction( actSave )
        fileToolBar.addAction( actQuit )

        colorMenu = bar.addMenu("Color")
        actPen = fileMenu.addAction(QIcon(":/icons/pen.png"), "&Pen color", self.pen_color, QKeySequence("Ctrl+P"))
        actBrush = fileMenu.addAction(QIcon(":/icons/brush.png"), "&Brush color", self.brush_color, QKeySequence("Ctrl+B"))

        colorToolBar = QToolBar("Color")
        self.addToolBar( colorToolBar )
        colorToolBar.addAction( actPen )
        colorToolBar.addAction( actBrush )

        shapeMenu = bar.addMenu("Shape")
        actRectangle = fileMenu.addAction(QIcon(":/icons/rectangle.png"), "&Rectangle", self.rectangle )
        actEllipse = fileMenu.addAction(QIcon(":/icons/ellipse.png"), "&Ellipse", self.ellipse)
        actFree = fileMenu.addAction(QIcon(":/icons/free.png"), "&Free drawing", self.free_drawing)

        shapeToolBar = QToolBar("Shape")
        self.addToolBar( shapeToolBar )
        shapeToolBar.addAction( actRectangle )
        shapeToolBar.addAction( actEllipse )
        shapeToolBar.addAction( actFree )

        modeMenu = bar.addMenu("Mode")
        actMove = modeMenu.addAction(QIcon(":/icons/move.png"), "&Move", self.move)
        actDraw = modeMenu.addAction(QIcon(":/icons/draw.png"), "&Draw", self.draw)
        actSelect = modeMenu.addAction(QIcon(":/icons/select.png"), "&Select", self.select)
        #actZoomIn = modeMenu.addAction(QIcon(":/icons/zoom-in.png"), "Zoom in", self.zoom_in)
        #actZoomOut = modeMenu.addAction(QIcon(":/icons/zoom-out.png"), "Zoom out", self.zoom_out)

        modeToolBar = QToolBar("Navigation")
        self.addToolBar( modeToolBar )
        modeToolBar.addAction( actMove )
        modeToolBar.addAction(actDraw)
        modeToolBar.addAction(actSelect)

        #navToolBar.addAction( actZoomIn )
        #navToolBar.addAction( actZoomOut )


        # self.container = QWidget(self)
        # vLayout = QVBoxLayout( self.container )
        # self.container.setLayout( vLayout )
        # self.textEdit = QTextEdit( self.container )
        # self.textEdit.setMaximumHeight( 50 )
        # self.canvas = Canvas( self.container )
        # vLayout.addWidget( self.canvas )
        # vLayout.addWidget( self.textEdit )
        # self.setCentralWidget( self.container )

        self.textEdit = QTextEdit( self )
        self.setCentralWidget(self.textEdit)


    ##############
    def pen_color(self):
        self.log_action("choose pen color")

    def brush_color(self):
        self.log_action("choose brush color")

    def rectangle(self):
        self.log_action("Shape mode: rectangle")

    def ellipse(self):
        self.log_action("Shape Mode: circle")

    def free_drawing(self):
        self.log_action("Shape mode: free drawing")

    def move(self):
        self.log_action("Mode: move")

    def draw(self):
        self.log_action("Mode: draw")

    def select(self):
        self.log_action("Mode: select")


    ##############
    def open(self):
        fileName = QFileDialog.getOpenFileName(self, "Open file", ".")
        file = open(fileName[0], 'r')
        str = file.readlines()
        str = '\n'.join(str)
        self.textEdit.setHtml( str )
        file.close()


    ###############
    def save(self):
        fileName = QFileDialog.getSaveFileName(self, "Save file", ".")
        with open(fileName[0], 'w') as fileSave:
            string = self.textEdit.toPlainText()
            fileSave.write(string)
            fileSave.close()
            print("Save... ", fileName[0], " saved.")

    ###############
    def quit(self):
        box = QMessageBox()
        b = box.question(self, 'Exit?', "Do you really want to exit ?", QMessageBox.Yes | QMessageBox.No)
        box.setIcon(QMessageBox.Question)
        if b == QMessageBox.Yes:
            sys.exit()

    def closeEvent(self, event):
        #event.ignore()
        #self.quit()
        return

    def log_action(self, str):
        content = self.textEdit.toPlainText()
        self.textEdit.setPlainText( content + "\n" + str)

if __name__=="__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()
