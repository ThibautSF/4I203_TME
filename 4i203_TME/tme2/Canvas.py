from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Canvas(QWidget):
    mode = "draw"
    
    drawMode = "rectangle"
    penColor = Qt.black
    brushColor = Qt.white
    
    draws = []

    def __init__(self, parent = None):
        QWidget.__init__(self,parent)
        self.setMinimumSize(200, 200)
        self.isPressed = 0
    
    def mousePressEvent(self, event):
        self.isPressed = 1
        self.pStart = event.pos()
        
        return
    
    def mouseMoveEvent(self, event):
        if self.isPressed==1:
            self.pEnd = event.pos()
            
            self.update()
        
        return
    
    def mouseReleaseEvent(self, event):
        if self.isPressed==1:
            self.isPressed = 2
            self.pEnd = event.pos()
            
            self.update()
        
        return
    
    def paintEvent(self, event):
        painter = QPainter(self)
        
        if self.mode == "draw":
            self.drawAll(painter)
            if self.isPressed!=0:
                #Coloration adapté à l'affichage (temporaire/final)
                if self.isPressed==1:
                    #dessin fantôme
                    painter.setPen(self.penColor)
                    painter.setBrush(QColor(self.brushColor).lighter(150))
                    
                elif self.isPressed==2:
                    #dessin final
                    painter.setPen(self.penColor)
                    painter.setBrush(self.brushColor)
                
                if self.drawMode == "rectangle" or self.drawMode == "ellipse":
                    draw = QRect(self.pStart,self.pEnd)
                    
                    if self.drawMode == "rectangle":
                        painter.drawRect(draw)
                    elif self.drawMode == "ellipse":
                        draw = QRectF(draw)
                        painter.drawEllipse(draw)
                
                if self.isPressed==2:
                    one_draw = (draw, self.drawMode, self.penColor, self.brushColor)
                    self.draws.append(one_draw)
                    self.isPressed=0
        elif self.mode == "move":
            if self.isPressed==1:
                #move fantome (après)
                painter.translate(self.pEnd)
                self.drawAll(painter)
                
            elif self.isPressed==2:
                #dessin final
                #painter.save()
                
                painter.translate(self.pEnd)
                self.drawAll(painter)
                
                for i in range(len(self.draws)):
                    one_draw = self.draws[i]
                    one_draw[0].moveTo(one_draw[0].topLeft().x()+self.pEnd.x(),one_draw[0].topLeft().y()+self.pEnd.y())
                
                #painter.restore()
                self.isPressed=0
            
        elif self.mode == "select":
            self.drawAll(painter)
            if self.isPressed==2:
                i = len(self.draws)-1
                while i >= 0:
                    one_draw = self.draws[i]
                    if one_draw[0].contains(self.pEnd):
                        self.selectedObject = i
                        break
                    i-=1
                self.isPressed = 0
        
        return
    
    def reset(self):
        print("reset")
    
    def add_object(self):
        print("add object")
    
    def set_color(self, color ):
        print("set color")
    
    def drawAll(self, painter):
        for one_draw in self.draws :
            painter.setPen(one_draw[2])
            painter.setBrush(one_draw[3])
            
            if one_draw[1] == "rectangle":
                painter.drawRect(one_draw[0])
            elif one_draw[1] == "ellipse":
                painter.drawEllipse(one_draw[0])
            
        return
    
    def setMode(self, mode):
        self.mode = mode
    
    def setPenColor(self, color):
        if self.mode == "select":
            old_draw = self.draws[self.selectedObject];
            self.draws[self.selectedObject] = (old_draw[0],old_draw[1],color,old_draw[3])
            self.update()
        else:
            self.penColor = color
    
    def setBrushColor(self, color):
        if self.mode == "select":
            old_draw = self.draws[self.selectedObject];
            self.draws[self.selectedObject] = (old_draw[0],old_draw[1],old_draw[2],color)
            self.update()
        else:
            self.brushColor = color
    
    def setDrawMode(self, strMode):
        if self.mode == "select":
            old_draw = self.draws[self.selectedObject];
            if strMode == "rectangle":
                new_obj = QRect(QPoint(old_draw[0].topLeft().x(),old_draw[0].topLeft().y()), QPoint(old_draw[0].bottomRight().x(),old_draw[0].bottomRight().y()))
            elif strMode == "ellipse":
                new_obj = QRectF(old_draw[0].topLeft(),old_draw[0].bottomRight())
            self.draws[self.selectedObject] = (new_obj,strMode,old_draw[2],old_draw[3])
            self.update()
        else:
            self.drawMode = strMode;
    
    def removeLast(self):
        if len(self.draws)>0:
            self.draws.pop(-1)
            self.update()
    
    def removeAll(self):
        self.draws = []
        self.update()
