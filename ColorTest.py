from PySide2 import QtWidgets, QtCore, QtGui
from mainWindow import Ui_mainwidget as mPage
from base import Ui_MainWindow as baseWindow
from testFrame import Ui_testPage as testPage
from testFinalFrame import Ui_Form as finalPage
from ColorLabel import Ui_ColorLabel as CLabel
import json
import pandas as pd
import os
import datetime
from randomFinal import Ui_randomFinal as rFinal
from selectingStartData import Ui_selectingStartData as selectStartData
import re
from showResultsFrame import Ui_testResults as showResults

class showResultsApp(showResults, QtWidgets.QWidget):

    def __init__(self, parentFrame):
        super(showResultsApp,self).__init__()
        self.setupUi(self)
        self.parentFrame = parentFrame

class selectStartDataApp(selectStartData, QtWidgets.QWidget):

    def __init__(self, parentFrame):
        super(selectStartDataApp, self).__init__()
        self.setupUi(self)

        self.parentFrame = parentFrame
        self.populateDropDown()

    def populateDropDown(self):

        root = "data\orders"
        if os.path.exists(root):
            files = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]
            pattern = re.compile("^(.*?)_([0-9]{4})_([1-9]+?)_([1-9]+?).(csv)$")
            csvFileMatches = [pattern.match(f) for f in files if pattern.match(f)]
            csvFiles = list(map(lambda x: x.group(), csvFileMatches))
            fileNames = list(map(lambda x: x.group(1), csvFileMatches))
            # objectDict stores the elements in the drop down menu, name---file name pairs
            self.parentFrame.objectDict = {}
            for k, v in zip(fileNames, csvFiles):
                self.parentFrame.objectDict[k] = v
            self.startDataList.addItems(fileNames)
        self.parentFrame.objectDict["No randomization"] = ""

class ColorLabel(CLabel, QtWidgets.QWidget):

    def __init__(self, ColorIndex, dragable, parentFrame, position):
        super(ColorLabel, self).__init__()
        self.setupUi(self)
        self.ColorIndex = ColorIndex
        self.setAcceptDrops(True)
        self.drag = dragable
        self.parentFrame = parentFrame
        self.positionIndex = position
        self.dragInfo = None

    def mousePressEvent(self, event):
        """this function is needed for the drag and drop"""
        if event.button() == QtCore.Qt.MouseButton.LeftButton and self.drag == True:

            self.dragInfo = "dragged"
            drag = QtGui.QDrag(self)
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
        droppedIndex = self.positionIndex
        self.parentFrame.ShiftsGridValues(toIndex=droppedIndex, fromIndex=fromIndex)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent):

        if event.mimeData().hasFormat("text/plain") and self.drag:
            event.accept()
        else:
            event.ignore()


class randomFinalApp(rFinal, QtWidgets.QWidget):

    def __init__(self):
        super(randomFinalApp, self).__init__()
        self.setupUi(self)

class finalPageApp(finalPage, QtWidgets.QWidget):

    def __init__(self):
        super(finalPageApp, self).__init__()
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
        self.colorLabels = {}
        #actions
        self.actionAdd_new_start_value.triggered.connect(self.createNewRandomization)
        self.actionRunNewTest.triggered.connect(self.startTest)
        self.actionLoad_test_results.triggered.connect(self.loadTestResults)
        if self.nextButton is not None:
            self.nextButton.show()
            self.nextButton.clicked.connect(self.nextButtonPushed)


        #stores the data of the test during testing, it is updated every time when the nextButton is pushed
        self.testData = {"0": [], "1": [], "2": [], "3": []}

        self.randomizing = False
        self.StartData = None
        
        #startPage
        newPage = testMainPage()
        self.gridLayout.addWidget(newPage)
        del newPage


    def startTest(self):
        """called when running new test selected"""
        #select randomization pops up first
        self.testData = {"0": [], "1": [], "2": [], "3": []}
        firstPage = selectStartDataApp(parentFrame=self)
        self.removingFrame()
        self.selectButton = firstPage.selectButton
        self.dropDownMenu = firstPage.startDataList
        self.gridLayout.addWidget(firstPage)
        self.connect(firstPage.selectButton, QtCore.SIGNAL('clicked()'), self.selectButtonPushed)


    def createNewRandomization(self):
        """creates new starting point"""
        self.changingToTest(startData=None, rand=True)

    def selectButtonPushed(self):
        """it is called when the user selects a randomization"""
        selectedValue = self.dropDownMenu.currentText()
        startDataFile = self.objectDict[selectedValue]
        if os.path.exists(os.path.join("data","orders",startDataFile)) and not selectedValue == "No randomization":
            self.changingToTest(rand=False, startData=os.path.join("data","orders",startDataFile))
        elif selectedValue == "No randomization":
            self.changingToTest(rand=False, startData=None)
        else:
            raise FileNotFoundError

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

    def dataPreprocess(self, jsonData, csvData):
        """returns all the necesarry information from the json, and csv file"""
        colorBlind = jsonData["colorBlind"]
        name = jsonData["name"]
        scoreList = csvData["score"]
        sumScore = sum(scoreList)
        date = jsonData["date"]
        #todo histogram integration
        return colorBlind, name, sumScore, date

    def changingtoResultsPage(self, colorBlind, name, sumScore, date):
        """pops a results page up when it is called"""
        resultPage = showResultsApp(self)
        self.removingFrame()
        resultPage.nameEditLabel.setText(str(name))
        resultPage.dateEditLabel.setText(str(date))
        resultPage.scoreEditLabel.setText(str(sumScore))
        resultPage.colorBlindnessCheckBox.setEnabled(True)
        resultPage.colorBlindnessCheckBox.setChecked(colorBlind)
        resultPage.colorBlindnessCheckBox.setEnabled(False)
        self.gridLayout.addWidget(resultPage)
        self.connect(resultPage.pushButton, QtCore.SIGNAL('clicked()'), self.backButtonPushed)

    def backButtonPushed(self):
        """returns to the main page when the back button is pushed"""
        self.changingToMainPage()


    def changingToMainPage(self):
        """changing back to the mainPage or startPage"""
        newPage = testMainPage()
        self.removingFrame()
        self.gridLayout.addWidget(newPage)


    def nextButtonPushed(self):
        """Loads the next page when button pushed"""

        currentItem = self.gridLayout.itemAt(0).wid
        # ColorLabelsLayout has all the colorLabels
        ColorLabelsLayout = currentItem.horizontalLayout
        # saving test data
        i = 0
        templist = []
        while ColorLabelsLayout.itemAt(i) is not None:
            colorLabeldata = ColorLabelsLayout.itemAt(i).wid.ColorIndex

            if colorLabeldata == 85 and self.testNum == 0:
                colorLabeldata = 0

            templist.append(colorLabeldata)
            i += 1
        self.testData[str(self.testNum)] = templist
        #changing page
        self.testNum += 1
        if self.randomizing:
            self.changingToTest(startData=None,rand=True)
        elif self.StartData:
            self.changingToTest(startData=self.StartData, rand=False)
        else:
            self.changingToTest(startData=None)
        print(self.testData)

    def saveButtonPushed(self):
        """it is called when the user pushes the save button on the randomization page"""

        currentItem = self.gridLayout.itemAt(0).wid
        nameEdit = currentItem.horizontalLayout.itemAt(1).wid
        nameEditText = nameEdit.text()
        if nameEdit.isModified() is False:
            pass
        else:
            nameEdit.clear()

            self.saveData(nameEditText, None,True)
            self.changingToMainPage()



    def saveData(self, nameEditValue, checkBoxValue, rand=False):
        """saves the data into the folder"""

        def evaulateData(self):
            """calculate test scores"""

            # generating template
            templateDict = {}
            for i in range(1, 86):
                templateDict[i] = None

            colorIndex = []
            for k, v in self.testData.items():
                # usedData doesn't contain fixed icons
                usedData = v[1:-1]
                fixedFirst = v[0]
                fixedLast = v[-1]
                for i in range(0, len(usedData)):
                    colorIndex.append(usedData[i])
                    if i == 0 or i == len(usedData)-1:
                        if i == 0:
                            score = abs((fixedFirst - usedData[i])) + abs((usedData[i + 1] - usedData[i]))
                        elif i == len(usedData)-1:
                            score = abs((usedData[i - 1] - usedData[i])) + abs((fixedLast - usedData[i]))
                    else:
                        score = abs((usedData[i - 1] - usedData[i])) + abs((usedData[i + 1] - usedData[i]))

                    templateDict[usedData[i]] = score

            return templateDict, colorIndex


        if not rand:
            scoreData, colorIndex = evaulateData(self)
            scoreDataValues = list(scoreData.values())
            scoreDataFrame = pd.DataFrame({"score": scoreDataValues, "colorIndex": colorIndex}, index=scoreData.keys())

            time = datetime.datetime.now()
            folderName = nameEditValue + "_" + str(time.year) + "_" + str(time.month) + "_" + str(time.day)
            #saving data into different files
            if not os.path.exists(os.path.join(r"data\results", folderName)):
                os.makedirs(os.path.join(r"data\results", folderName))

            scoreDataFrame.to_csv(r"data\results\{0}\{0}.csv".format(folderName), sep=",")

            userMetaData = {"name": nameEditValue, "colorBlind": checkBoxValue,
                            "date": str(time.year) + "." + str(time.month) + "." + str(time.day),
                            "histogram": None}
            #todo create histogram

            with open(r"data\results\{0}\{0}.json".format(folderName), "w") as f:
                json.dump(userMetaData, f, sort_keys=True, indent=4)

        else:
            scoreData, colorIndex = evaulateData(self)
            scoreDataValues = list(scoreData.values())
            scoreDataFrame = pd.DataFrame({"score": scoreDataValues, "colorIndex": colorIndex}, index=scoreData.keys())

            time = datetime.datetime.now()
            folderName = nameEditValue + "_" + str(time.year) + "_" + str(time.month) + "_" + str(time.day)

            scoreDataFrame.to_csv(r"data\orders\{0}.csv".format(folderName), sep=",")

        return folderName



    def finishButtonPushed(self):
        """it is called when the user pushes the finnishButton on the final page of the test"""
        currentItem = self.gridLayout.itemAt(0).wid
        nameEdit = currentItem.horizontalLayout.itemAt(1).wid
        nameEditText = nameEdit.text()
        if nameEdit.isModified() is False:
            pass
        else:
            nameEdit.clear()
            blindBox = currentItem.horizontalLayout_2.itemAt(1).wid
            blindBoxValue = blindBox.isChecked()
            fName = self.saveData(nameEditText, blindBoxValue)
            try:
                jsonD, csvD = self.loadingResult(fName)
            except FileNotFoundError:
                print ("File Not found")
                pass

            colorBlind, name, sumScore, date = self.dataPreprocess(jsonD,csvD)
            self.changingtoResultsPage(colorBlind=colorBlind, name=name, sumScore=sumScore, date=date)

    def loadingResult(self, fName):
        """loads result from files, based on filename. Filename is not equal to user name, it is the user name
        with the timestamp"""
        root = r"data\results"
        if os.path.exists(os.path.join(root, fName)):
            folder = os.path.join(root,fName)
            csvName = fName+".csv"
            jsonName = fName+".json"
            if os.path.exists(os.path.join(folder, csvName)) and os.path.exists(os.path.join(folder, jsonName)):
                #taking in csv and json data
                csvFile = os.path.join(folder, csvName)
                csvData = pd.read_csv(csvFile, sep=",")
                csvData.set_index("Unnamed: 0")

                jsonFile = os.path.join(folder, jsonName)
                with open (jsonFile, "r") as f:
                    jsonData = json.load(f)
            else:
                raise FileNotFoundError
        else:
            raise FileNotFoundError

        return jsonData, csvData



    def loadingRandomization(self, colorIndexes, tPage):
        """loads randomized data"""
        if self.testNum == 0:
            #this is needed to restore the fixed values, the .csv doesn't hold the fixed lables
            colors = [85]+colorIndexes[0:22] + [23]
        elif self.testNum == 1:
            colors = [22] + colorIndexes[22:42] + [43]
        elif self.testNum == 2:
            colors = [42] + colorIndexes[42:63] + [64]
        elif self.testNum == 3:
            colors = [63] + colorIndexes[63:] + [86]

        pos = 0
        for i in colors:
            if i == colors[0] or i == colors[-1]:
                dragable = False
            else:
                dragable = True

            colorLabel = ColorLabel(ColorIndex=i, dragable=dragable, parentFrame=tPage, position=pos)
            colorLabel.setObjectName("colorLabel_" + str(i))
            colorLabel.label.setText(str(i))
            self.colorLabels[str(i)] = colorLabel

            tPage.horizontalLayout.addWidget(colorLabel)
            pos += 1

        return tPage

    def changingToTest(self, rand=False, startData=None):
        """ Changing to a testPage also changes between tests
        if rand == True its create a new randomization
        if stratData is provided it loads the startData instead of the default color list"""


        def createOriginal():
            """creates original test, it is a solved test"""
            if self.testNum <= 3:
                tPage = testFrameApp(parentFrame=self)
                tPage = self.fillingUpwithColorLabels(tPage)
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



        def createRandomized(colorIndexes):
            """creates a randomized test"""

            if self.testNum <= 3:
                tPage = testFrameApp(parentFrame=self)
                tPage = self.loadingRandomization(colorIndexes, tPage)
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



        #this is where the changingtoTest really starts
        if not startData and not rand:
            self.StartData = None
            self.randomizing = False
            createOriginal()

        elif startData and not rand:
            self.StartData = startData
            self.randomizing = False
            rawData = pd.read_csv(startData, sep=",")
            rawData = rawData.set_index("Unnamed: 0")
            colorIndexes = list(rawData["colorIndex"])
            createRandomized(colorIndexes)

        elif rand:
            #this is evaluated if we choose to create new randomized order
            self.randomizing = True
            self.StartData = None

            if self.testNum <= 3:
                tPage = testFrameApp(parentFrame=self)
                tPage = self.fillingUpwithColorLabels(tPage)
                try:
                    self.removingFrame()
                except baseFrameError:
                    print("ERROR")
                self.gridLayout.addWidget(tPage)
                self.connect(tPage.pushButton, QtCore.SIGNAL('clicked()'), self.nextButtonPushed)
            else:
                self.testNum = 0
                fPage = randomFinalApp()
                try:
                    self.removingFrame()
                except baseFrameError:
                    print("ERROR")
                self.gridLayout.addWidget(fPage)
                self.connect(fPage.saveButton, QtCore.SIGNAL('clicked()'), self.saveButtonPushed)



    def fillingUpwithColorLabels(self, testFrameAppObject):
        """it fills up the the horizontal
        testNumber can be 0,1,2,3 depends which row of the FM hue test needs to be loaded"""
        tPage = testFrameAppObject
        self.colorLabels = {}
        if self.testNum == 0:
            rangeOfColors = range(0, 24)
        elif self.testNum == 1:
            rangeOfColors = range(22, 44)
        elif self.testNum == 2:
            rangeOfColors = range(42, 65)
        elif self.testNum == 3:
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
