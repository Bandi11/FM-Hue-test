from PySide2 import QtWidgets, QtCore, QtGui
from mainWindow import Ui_mainwidget as mPage
from base import Ui_MainWindow as baseWindow
from testFrame import Ui_testPage as testPage
from testFinalFrame import Ui_Form as finalPage
from ColorLabel import Ui_ColorLabel as CLabel
import json


class ColorLabel(CLabel, QtWidgets.QWidget):

    def __init__(self, ColorIndex, dragable, parentFrame, position):
        super(ColorLabel, self).__init__()
        self.setupUi(self)
        self.ColorIndex = ColorIndex
        self.setAcceptDrops(True)
        self.drag = dragable
        self.parentFrame = parentFrame
        self.positionIndex =position
        self.dragInfo = None

    def mousePressEvent(self, event):
        """this function is needed for the drag and drop"""
        if event.button() == QtCore.Qt.MouseButton.LeftButton and self.drag == True:

            self.dragInfo = "dragged"
            drag = QtGui.QDrag(self)
            #mimeData might be not needed
            mimeData = QtCore.QMimeData()
            mimeData.setText(json.dumps({"index": self.positionIndex, "color": self.ColorIndex}))
            drag.setMimeData(mimeData)
            tick = QtGui.QPixmap(r"C:\Users\Andras Meszaros\Desktop\tickTest")
            drag.setPixmap(tick)
            drag.exec_()


    def dropEvent(self, e):
        """this function is called when something is dropped on this widget"""

        #todo it changes only the label text not the colorlabel
        self.dragInfo = "dropped"
        dataTransfered = json.loads(e.mimeData().text())
        fromIndex = dataTransfered["index"]
        color = dataTransfered["color"]
        droppedIndex = self.positionIndex
        self.parentFrame.ShiftsGridValues(toIndex=droppedIndex, fromIndex=fromIndex)
        #self.label.setText(str(color))
    def dragEnterEvent(self, event: QtGui.QDragEnterEvent):

        if event.mimeData().hasFormat("text/plain") and self.drag:
            event.accept()
        else:
            event.ignore()



class finalPageApp(finalPage, QtWidgets.QWidget):

    def __init__(self):
        super(finalPageApp,self).__init__()
        self.setupUi(self)

class baseFrameError(Exception):
    def __init__(self):
        """needs to be implemented TODO"""
        pass

class OveriterrationError(Exception):
    def __init__(self):
        """todo"""
        pass
class testFrameApp(testPage, QtWidgets.QWidget):
    def __init__(self, parentFrame=None):
        super(testFrameApp, self).__init__()
        self.setupUi(self)
        self.parentFrame = parentFrame

    def ShiftsGridValues(self, fromIndex, toIndex):
        temporaryList = []
        i = 0
        while (self.horizontalLayout.itemAt(i)) is not None:
            temporaryList.append(self.horizontalLayout.itemAt(i).wid)
            i += 1
        orderedList = []
        minimum = min(fromIndex, toIndex)
        i = 0
        while i < minimum:
            orderedList.append(temporaryList[i])
            i += 1
        if minimum == toIndex:

            orderedList.append(temporaryList[fromIndex])
            while i < len(temporaryList):
                if i != fromIndex:
                    orderedList.append(temporaryList[i])
                i += 1
        elif minimum == fromIndex:
            i += 1
            while i <= toIndex:
                orderedList.append(temporaryList[i])
                i += 1

            orderedList.append(temporaryList[fromIndex])

            while i < len(temporaryList):
                orderedList.append(temporaryList[i])
                i += 1

        i = 0
        for element in orderedList:
            element.positionIndex = i
            i += 1
        #debug
        # for element in orderedList:
        #     print(element.ColorIndex)

        self.parentFrame.refreshTestPage(orderedList)



class testMainPage(mPage,QtWidgets.QWidget):
    def __init__(self):
        super(testMainPage, self).__init__()
        self.setupUi(self)

class App(baseWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)

        self.nextButton = None
        #testNum contains the row of the test it can be 0,1,2,3
        self.testNum = 0
        #actions
        self.actionRunNewTest.triggered.connect(self.changingToTest)
        self.actionLoad_test_results.triggered.connect(self.loadTestResults)
        if self.nextButton is not None:
            self.nextButton.show()
            self.nextButton.clicked.connect(self.nextButtonPushed)


        #startPage
        newPage = testMainPage()
        self.gridLayout.addWidget(newPage)
        del newPage

    def refreshTestPage(self, orderedList):
        """refreshes the testpage after a drag and drop event"""
        refreshed = testFrameApp(parentFrame=self)
        self.removingFrame()
        for element in orderedList:
            colorLabel = ColorLabel(ColorIndex=element.ColorIndex, dragable=element.drag,
                                    parentFrame=refreshed, position=element.positionIndex)
            colorLabel.setObjectName("colorLabel_"+str(element.ColorIndex))
            colorLabel.label.setText(str(element.ColorIndex))
            self.colorLabels[str(element.ColorIndex)] = colorLabel
            refreshed.horizontalLayout.addWidget(colorLabel)
        self.connect(refreshed.pushButton, QtCore.SIGNAL('clicked()'), self.nextButtonPushed)

        self.gridLayout.addWidget(refreshed)

    def removingFrame(self):
        """Use it only if there is only one frame in the basegrid otherwise use an other function"""
        if self.gridLayout.count() == 1:
            currentItem = self.gridLayout.itemAt(0)
        else:
            raise baseFrameError

        if currentItem is not None:
            currentWidget = currentItem.widget()
            currentWidget.deleteLater()

        self.gridLayout.removeItem(currentItem)

    def changingToMainPage(self):
        """changing back to the mainPage or startPage"""
        newPage = testMainPage()
        self.removingFrame()
        self.gridLayout.addWidget(newPage)

    def nextButtonPushed(self):
        """Loads the next page when button pushed"""
        self.testNum += 1
        self.changingToTest()
    def saveData(self):
        """TODO saves the data of the finish screen"""
        pass
    def finishButtonPushed(self):
        """TODO collect the data of the finish page"""
        self.saveData()
        self.changingToMainPage()

    def changingToTest(self):
        """ Changing to a testPage also changes between tests"""
        if self.testNum <=3:
            tPage = testFrameApp(parentFrame=self)
            tPage = self.fillingUpwithColorLabels(self.testNum, tPage)
            try:
                self.removingFrame()
            except baseFrameError:
                print("ERROR")
            self.gridLayout.addWidget(tPage)
            self.connect(tPage.pushButton, QtCore.SIGNAL('clicked()'), self.nextButtonPushed)
        else:
            self.testNum = 0
            fPage = finalPageApp()
            try:
                self.removingFrame()
            except baseFrameError:
                print("ERROR")
            self.gridLayout.addWidget(fPage)
            self.connect(fPage.finishButton, QtCore.SIGNAL('clicked()'), self.finishButtonPushed)


    def fillingUpwithColorLabels(self, testNumber, testFrameAppObject):
        """it fills up the the horizontal
        testNumber can be 0,1,2,3 depends which row of the FM hue test needs to be loaded"""
        tPage = testFrameAppObject
        self.colorLabels = {}
        if testNumber == 0:
            rangeOfColors = range(0, 24)
        elif testNumber == 1:
            rangeOfColors = range(22, 44)
        elif testNumber == 2:
            rangeOfColors = range(42, 65)
        elif testNumber == 3:
            rangeOfColors = range(63, 87)
        else:
            raise OveriterrationError

        pos = 0
        for i in rangeOfColors:
            if i == 0:
                value = 85
            else:
                value = i

            if rangeOfColors.start == i or rangeOfColors.stop == i+1:
                dragable = False
            else:
                dragable = True

            colorLabel = ColorLabel(ColorIndex=value, dragable=dragable, parentFrame=tPage, position=pos)
            colorLabel.setObjectName("colorLabel_"+str(value))
            colorLabel.label.setText(str(value))
            self.colorLabels[str(value)] = colorLabel
            tPage.horizontalLayout.addWidget(colorLabel)
            pos += 1

        return tPage


    def loadTestResults(self):
        pass



if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qtApp = App()
    qtApp.show()
    quit = app.exec_()
