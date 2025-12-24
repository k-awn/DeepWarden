from toggle import CustomToggle
from threading import Thread
import os
import json
import keyboard
import threading
import assets_rc  # noqa: F401
from time import sleep
from pyqttoast import Toast, ToastPreset
#pyside6 imports
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt, QStandardPaths)
from PySide6.QtGui import (QFont, QIcon, QColor)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QWidget)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(688, 688)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.menuBar = QFrame(self.centralwidget)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setMinimumSize(QSize(50, 0))
        self.menuBar.setMaximumSize(QSize(50, 16777215))
        self.menuBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuBar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.menuBar)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 5, 0, 0)
        self.weaponsButton = QPushButton(self.menuBar)
        self.weaponsButton.setObjectName(u"weaponsButton")
        self.weaponsButton.setMinimumSize(QSize(50, 50))
        self.weaponsButton.setMaximumSize(QSize(50, 50))
        self.weaponsButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon = QIcon()
        icon.addFile(u":/icons/swords_24dp_FFFFF0_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.weaponsButton.setIcon(icon)
        self.weaponsButton.setIconSize(QSize(30, 30))
        self.weaponsButton.setFlat(True)

        self.gridLayout_3.addWidget(self.weaponsButton, 3, 0, 1, 1)

        self.progressionButton = QPushButton(self.menuBar)
        self.progressionButton.setObjectName(u"progressionButton")
        self.progressionButton.setMinimumSize(QSize(50, 50))
        self.progressionButton.setMaximumSize(QSize(50, 50))
        self.progressionButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon1 = QIcon()
        icon1.addFile(u":/icons/exercise_1000dp_FFFFF0_FILL0_wght400_GRAD0_opsz48(2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.progressionButton.setIcon(icon1)
        self.progressionButton.setIconSize(QSize(30, 30))
        self.progressionButton.setFlat(True)

        self.gridLayout_3.addWidget(self.progressionButton, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.bellButton = QPushButton(self.menuBar)
        self.bellButton.setObjectName(u"bellButton")
        self.bellButton.setMinimumSize(QSize(50, 50))
        self.bellButton.setMaximumSize(QSize(50, 50))
        self.bellButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon2 = QIcon()
        icon2.addFile(u":/icons/bell.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bellButton.setIcon(icon2)
        self.bellButton.setIconSize(QSize(30, 30))
        self.bellButton.setFlat(True)

        self.gridLayout_3.addWidget(self.bellButton, 1, 0, 1, 1)

        self.saveButton = QPushButton(self.menuBar)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(50, 50))
        self.saveButton.setMaximumSize(QSize(50, 50))
        self.saveButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon3 = QIcon()
        icon3.addFile(u":/icons/save_24dp_FFFFF0_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveButton.setIcon(icon3)
        self.saveButton.setIconSize(QSize(30, 30))
        self.saveButton.setFlat(True)

        self.gridLayout_3.addWidget(self.saveButton, 0, 0, 1, 1)

        self.miscButton = QPushButton(self.menuBar)
        self.miscButton.setObjectName(u"miscButton")
        self.miscButton.setMinimumSize(QSize(50, 50))
        self.miscButton.setMaximumSize(QSize(50, 50))
        self.miscButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon4 = QIcon()
        icon4.addFile(u":/icons/circle-ellipsis.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.miscButton.setIcon(icon4)
        self.miscButton.setIconSize(QSize(30, 30))
        self.miscButton.setFlat(True)

        self.gridLayout_3.addWidget(self.miscButton, 5, 0, 1, 1)

        self.settingsButton = QPushButton(self.menuBar)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(50, 50))
        self.settingsButton.setMaximumSize(QSize(50, 50))
        self.settingsButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon5 = QIcon()
        icon5.addFile(u":/icons/settings_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsButton.setIcon(icon5)
        self.settingsButton.setIconSize(QSize(30, 30))
        self.settingsButton.setFlat(True)

        self.gridLayout_3.addWidget(self.settingsButton, 8, 0, 1, 1)

        self.mantrasButton = QPushButton(self.menuBar)
        self.mantrasButton.setObjectName(u"mantrasButton")
        self.mantrasButton.setMinimumSize(QSize(50, 50))
        self.mantrasButton.setMaximumSize(QSize(50, 50))
        self.mantrasButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon6 = QIcon()
        icon6.addFile(u":/icons/wand-sparkles.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mantrasButton.setIcon(icon6)
        self.mantrasButton.setIconSize(QSize(30, 30))
        self.mantrasButton.setFlat(True)

        self.gridLayout_3.addWidget(self.mantrasButton, 2, 0, 1, 1)

        self.playButton = QPushButton(self.menuBar)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setMinimumSize(QSize(50, 50))
        self.playButton.setMaximumSize(QSize(50, 50))
        self.playButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon7 = QIcon()
        icon7.addFile(u":/icons/play_arrow_24dp_FFFFF0_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.playButton.setIcon(icon7)
        self.playButton.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.playButton, 7, 0, 1, 1)


        self.gridLayout.addWidget(self.menuBar, 1, 0, 1, 1)

        self.titleBar = QFrame(self.centralwidget)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMinimumSize(QSize(0, 50))
        self.titleBar.setMaximumSize(QSize(16777215, 50))
        self.titleBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.titleBar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.menuButton = QPushButton(self.titleBar)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(50, 50))
        self.menuButton.setMaximumSize(QSize(50, 50))
        self.menuButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon8 = QIcon()
        icon8.addFile(u":/icons/menu_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuButton.setIcon(icon8)
        self.menuButton.setIconSize(QSize(50, 50))
        self.menuButton.setFlat(True)

        self.gridLayout_2.addWidget(self.menuButton, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.pageName = QLabel(self.titleBar)
        self.pageName.setObjectName(u"pageName")

        self.gridLayout_2.addWidget(self.pageName, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.titleBar, 0, 0, 1, 2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(600, 600))
        self.stackedWidget.setStyleSheet(u"")
        self.bellPage = QWidget()
        self.bellPage.setObjectName(u"bellPage")
        self.gridLayout_5 = QGridLayout(self.bellPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.MovestackChoice = QComboBox(self.bellPage)
        self.MovestackChoice.addItem("")
        self.MovestackChoice.addItem("")
        self.MovestackChoice.setObjectName(u"MovestackChoice")

        self.gridLayout_5.addWidget(self.MovestackChoice, 2, 0, 1, 1)

        self.BellMovestack = QLabel(self.bellPage)
        self.BellMovestack.setObjectName(u"BellMovestack")

        self.gridLayout_5.addWidget(self.BellMovestack, 0, 0, 1, 2)

        self.label_40 = QLabel(self.bellPage)
        self.label_40.setObjectName(u"label_40")
        font = QFont()
        font.setPointSize(11)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet(u"color:grey;")

        self.gridLayout_5.addWidget(self.label_40, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.bellPage)
        self.mantrasPage = QWidget()
        self.mantrasPage.setObjectName(u"mantrasPage")
        self.gridLayout_6 = QGridLayout(self.mantrasPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.AutoMantraVariantsDescriptor = QLabel(self.mantrasPage)
        self.AutoMantraVariantsDescriptor.setObjectName(u"AutoMantraVariantsDescriptor")
        self.AutoMantraVariantsDescriptor.setFont(font)
        self.AutoMantraVariantsDescriptor.setStyleSheet(u"color:grey;")

        self.gridLayout_6.addWidget(self.AutoMantraVariantsDescriptor, 6, 0, 1, 2)

        self.label_47 = QLabel(self.mantrasPage)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font)
        self.label_47.setStyleSheet(u"color:grey;")

        self.gridLayout_6.addWidget(self.label_47, 12, 0, 1, 2)

        self.plainTextEdit_10 = QPlainTextEdit(self.mantrasPage)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")
        self.plainTextEdit_10.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_10.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.plainTextEdit_10, 2, 1, 1, 1)

        self.AutoMantraVariants = QLabel(self.mantrasPage)
        self.AutoMantraVariants.setObjectName(u"AutoMantraVariants")

        self.gridLayout_6.addWidget(self.AutoMantraVariants, 5, 0, 1, 1)

        self.label_21 = QLabel(self.mantrasPage)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_6.addWidget(self.label_21, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 16, 0, 1, 2)

        self.AutoMantraVariantsKeysLabel = QLabel(self.mantrasPage)
        self.AutoMantraVariantsKeysLabel.setObjectName(u"AutoMantraVariantsKeysLabel")

        self.gridLayout_6.addWidget(self.AutoMantraVariantsKeysLabel, 7, 0, 1, 1)

        self.plainTextEdit_3 = QPlainTextEdit(self.mantrasPage)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_3.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_3.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.plainTextEdit_3, 13, 1, 1, 1)

        self.label_8 = QLabel(self.mantrasPage)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 10, 0, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.mantrasPage)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_2.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_2.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.plainTextEdit_2, 10, 1, 1, 1)

        self.label_39 = QLabel(self.mantrasPage)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_6.addWidget(self.label_39, 3, 0, 1, 1)

        self.AutoMantraVariantsKeysArea = QPlainTextEdit(self.mantrasPage)
        self.AutoMantraVariantsKeysArea.setObjectName(u"AutoMantraVariantsKeysArea")
        self.AutoMantraVariantsKeysArea.setMinimumSize(QSize(0, 30))
        self.AutoMantraVariantsKeysArea.setMaximumSize(QSize(16777215, 30))
        self.AutoMantraVariantsKeysArea.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.AutoMantraVariantsKeysArea, 7, 1, 1, 1)

        self.label_46 = QLabel(self.mantrasPage)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)
        self.label_46.setStyleSheet(u"color:grey;")

        self.gridLayout_6.addWidget(self.label_46, 9, 0, 1, 2)

        self.AutoRitualCast = QLabel(self.mantrasPage)
        self.AutoRitualCast.setObjectName(u"AutoRitualCast")

        self.gridLayout_6.addWidget(self.AutoRitualCast, 0, 0, 1, 1)

        self.label_7 = QLabel(self.mantrasPage)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 8, 0, 1, 1)

        self.label_10 = QLabel(self.mantrasPage)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 13, 0, 1, 1)

        self.label_20 = QLabel(self.mantrasPage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"color:grey;")

        self.gridLayout_6.addWidget(self.label_20, 1, 0, 1, 2)

        self.label_9 = QLabel(self.mantrasPage)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 11, 0, 1, 1)

        self.label_44 = QLabel(self.mantrasPage)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_6.addWidget(self.label_44, 4, 0, 1, 1)

        self.screenResolution = QComboBox(self.mantrasPage)
        self.screenResolution.addItem("")
        self.screenResolution.addItem("")
        self.screenResolution.setObjectName(u"screenResolution")

        self.gridLayout_6.addWidget(self.screenResolution, 3, 1, 1, 1)

        self.screenScale = QComboBox(self.mantrasPage)
        self.screenScale.addItem("")
        self.screenScale.addItem("")
        self.screenScale.setObjectName(u"screenScale")

        self.gridLayout_6.addWidget(self.screenScale, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.mantrasPage)
        self.weaponsPage = QWidget()
        self.weaponsPage.setObjectName(u"weaponsPage")
        self.gridLayout_10 = QGridLayout(self.weaponsPage)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_24 = QLabel(self.weaponsPage)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"color:grey;")

        self.gridLayout_10.addWidget(self.label_24, 11, 0, 1, 2)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_13, 16, 1, 1, 2)

        self.label_16 = QLabel(self.weaponsPage)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_10.addWidget(self.label_16, 9, 0, 1, 1)

        self.MotifHotkeyLabel = QLabel(self.weaponsPage)
        self.MotifHotkeyLabel.setObjectName(u"MotifHotkeyLabel")

        self.gridLayout_10.addWidget(self.MotifHotkeyLabel, 7, 0, 1, 1)

        self.label_36 = QLabel(self.weaponsPage)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)
        self.label_36.setStyleSheet(u"color:grey;")

        self.gridLayout_10.addWidget(self.label_36, 13, 0, 1, 2)

        self.MotifToolbarNumberLabel = QLabel(self.weaponsPage)
        self.MotifToolbarNumberLabel.setObjectName(u"MotifToolbarNumberLabel")

        self.gridLayout_10.addWidget(self.MotifToolbarNumberLabel, 8, 0, 1, 1)

        self.label_2 = QLabel(self.weaponsPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:grey")
        self.label_2.setWordWrap(True)

        self.gridLayout_10.addWidget(self.label_2, 3, 0, 1, 2)

        self.label_12 = QLabel(self.weaponsPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color:grey;")
        self.label_12.setWordWrap(True)

        self.gridLayout_10.addWidget(self.label_12, 6, 0, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_7, 16, 0, 1, 1)

        self.label_18 = QLabel(self.weaponsPage)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_10.addWidget(self.label_18, 14, 0, 1, 1)

        self.HoldM1Label = QLabel(self.weaponsPage)
        self.HoldM1Label.setObjectName(u"HoldM1Label")

        self.gridLayout_10.addWidget(self.HoldM1Label, 2, 0, 1, 1)

        self.MotifSwapLabel = QLabel(self.weaponsPage)
        self.MotifSwapLabel.setObjectName(u"MotifSwapLabel")

        self.gridLayout_10.addWidget(self.MotifSwapLabel, 5, 0, 1, 1)

        self.label_11 = QLabel(self.weaponsPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color:grey;")
        self.label_11.setWordWrap(True)

        self.gridLayout_10.addWidget(self.label_11, 1, 0, 1, 2)

        self.label_23 = QLabel(self.weaponsPage)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_10.addWidget(self.label_23, 10, 0, 1, 1)

        self.AerialAirDashLabel = QLabel(self.weaponsPage)
        self.AerialAirDashLabel.setObjectName(u"AerialAirDashLabel")

        self.gridLayout_10.addWidget(self.AerialAirDashLabel, 0, 0, 1, 1)

        self.MotifHotkeyArea = QPlainTextEdit(self.weaponsPage)
        self.MotifHotkeyArea.setObjectName(u"MotifHotkeyArea")
        self.MotifHotkeyArea.setMinimumSize(QSize(0, 30))
        self.MotifHotkeyArea.setMaximumSize(QSize(16777215, 30))
        self.MotifHotkeyArea.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.MotifHotkeyArea, 7, 1, 1, 1)

        self.MotifToolbarNumberArea = QPlainTextEdit(self.weaponsPage)
        self.MotifToolbarNumberArea.setObjectName(u"MotifToolbarNumberArea")
        self.MotifToolbarNumberArea.setMinimumSize(QSize(0, 30))
        self.MotifToolbarNumberArea.setMaximumSize(QSize(16777215, 30))
        self.MotifToolbarNumberArea.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.MotifToolbarNumberArea, 8, 1, 1, 1)

        self.plainTextEdit_7 = QPlainTextEdit(self.weaponsPage)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_7.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_7.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.plainTextEdit_7, 9, 1, 1, 1)

        self.label_35 = QLabel(self.weaponsPage)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_10.addWidget(self.label_35, 12, 0, 1, 1)

        self.label_19 = QLabel(self.weaponsPage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color:grey;")

        self.gridLayout_10.addWidget(self.label_19, 15, 0, 1, 1)

        self.label_22 = QLabel(self.weaponsPage)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_10.addWidget(self.label_22, 4, 0, 1, 1)

        self.HoldM1Key = QPlainTextEdit(self.weaponsPage)
        self.HoldM1Key.setObjectName(u"HoldM1Key")
        self.HoldM1Key.setMinimumSize(QSize(0, 30))
        self.HoldM1Key.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_10.addWidget(self.HoldM1Key, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.weaponsPage)
        self.progressionPage = QWidget()
        self.progressionPage.setObjectName(u"progressionPage")
        self.gridLayout_12 = QGridLayout(self.progressionPage)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.CharismaAutofillLabel = QLabel(self.progressionPage)
        self.CharismaAutofillLabel.setObjectName(u"CharismaAutofillLabel")

        self.gridLayout_12.addWidget(self.CharismaAutofillLabel, 0, 0, 1, 2)

        self.label_26 = QLabel(self.progressionPage)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_12.addWidget(self.label_26, 7, 0, 1, 1)

        self.label_13 = QLabel(self.progressionPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color:grey;")

        self.gridLayout_12.addWidget(self.label_13, 1, 0, 1, 4)

        self.AnkleWeightsTrainingHotkey = QPlainTextEdit(self.progressionPage)
        self.AnkleWeightsTrainingHotkey.setObjectName(u"AnkleWeightsTrainingHotkey")
        self.AnkleWeightsTrainingHotkey.setMinimumSize(QSize(0, 30))
        self.AnkleWeightsTrainingHotkey.setMaximumSize(QSize(16777215, 30))
        self.AnkleWeightsTrainingHotkey.setStyleSheet(u"")

        self.gridLayout_12.addWidget(self.AnkleWeightsTrainingHotkey, 4, 3, 1, 1)

        self.AnkleWeightsLabel = QLabel(self.progressionPage)
        self.AnkleWeightsLabel.setObjectName(u"AnkleWeightsLabel")

        self.gridLayout_12.addWidget(self.AnkleWeightsLabel, 2, 0, 1, 2)

        self.BoulderTrainingHotkey = QPlainTextEdit(self.progressionPage)
        self.BoulderTrainingHotkey.setObjectName(u"BoulderTrainingHotkey")
        self.BoulderTrainingHotkey.setMinimumSize(QSize(0, 30))
        self.BoulderTrainingHotkey.setMaximumSize(QSize(16777215, 30))
        self.BoulderTrainingHotkey.setStyleSheet(u"")

        self.gridLayout_12.addWidget(self.BoulderTrainingHotkey, 7, 3, 1, 1)

        self.label_25 = QLabel(self.progressionPage)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_12.addWidget(self.label_25, 4, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_6, 16, 3, 1, 1)

        self.WillpowerTrainingHotkey = QPlainTextEdit(self.progressionPage)
        self.WillpowerTrainingHotkey.setObjectName(u"WillpowerTrainingHotkey")
        self.WillpowerTrainingHotkey.setMinimumSize(QSize(0, 30))
        self.WillpowerTrainingHotkey.setMaximumSize(QSize(16777215, 30))
        self.WillpowerTrainingHotkey.setStyleSheet(u"")

        self.gridLayout_12.addWidget(self.WillpowerTrainingHotkey, 15, 3, 1, 1)

        self.label_27 = QLabel(self.progressionPage)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"color:grey;")

        self.gridLayout_12.addWidget(self.label_27, 3, 0, 1, 4)

        self.label_30 = QLabel(self.progressionPage)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_12.addWidget(self.label_30, 15, 0, 1, 1)

        self.BoulderTrainingLabel = QLabel(self.progressionPage)
        self.BoulderTrainingLabel.setObjectName(u"BoulderTrainingLabel")

        self.gridLayout_12.addWidget(self.BoulderTrainingLabel, 5, 0, 1, 3)

        self.WillpowerTrainingLabel = QLabel(self.progressionPage)
        self.WillpowerTrainingLabel.setObjectName(u"WillpowerTrainingLabel")

        self.gridLayout_12.addWidget(self.WillpowerTrainingLabel, 13, 0, 1, 1)

        self.label_28 = QLabel(self.progressionPage)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"color:grey;")

        self.gridLayout_12.addWidget(self.label_28, 6, 0, 1, 4)

        self.label_38 = QLabel(self.progressionPage)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)
        self.label_38.setStyleSheet(u"color:grey;")

        self.gridLayout_12.addWidget(self.label_38, 14, 0, 1, 4)

        self.stackedWidget.addWidget(self.progressionPage)
        self.miscPage = QWidget()
        self.miscPage.setObjectName(u"miscPage")
        self.gridLayout_8 = QGridLayout(self.miscPage)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.plainTextEdit_14 = QPlainTextEdit(self.miscPage)
        self.plainTextEdit_14.setObjectName(u"plainTextEdit_14")
        self.plainTextEdit_14.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_14.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.plainTextEdit_14, 6, 1, 1, 1)

        self.DiscordGankPingLabel = QLabel(self.miscPage)
        self.DiscordGankPingLabel.setObjectName(u"DiscordGankPingLabel")

        self.gridLayout_8.addWidget(self.DiscordGankPingLabel, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.miscPage)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 30))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.plainTextEdit, 3, 1, 1, 1)

        self.MbAllHotkeyArea = QPlainTextEdit(self.miscPage)
        self.MbAllHotkeyArea.setObjectName(u"MbAllHotkeyArea")
        self.MbAllHotkeyArea.setMinimumSize(QSize(0, 30))
        self.MbAllHotkeyArea.setMaximumSize(QSize(16777215, 30))
        self.MbAllHotkeyArea.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.MbAllHotkeyArea, 12, 1, 1, 1)

        self.GoldenTongueLabel = QLabel(self.miscPage)
        self.GoldenTongueLabel.setObjectName(u"GoldenTongueLabel")

        self.gridLayout_8.addWidget(self.GoldenTongueLabel, 15, 0, 1, 2)

        self.plainTextEdit_15 = QPlainTextEdit(self.miscPage)
        self.plainTextEdit_15.setObjectName(u"plainTextEdit_15")
        self.plainTextEdit_15.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_15.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_15.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.plainTextEdit_15, 2, 1, 1, 1)

        self.GoldenTongueHotkeyArea = QPlainTextEdit(self.miscPage)
        self.GoldenTongueHotkeyArea.setObjectName(u"GoldenTongueHotkeyArea")
        self.GoldenTongueHotkeyArea.setMaximumSize(QSize(16777215, 30))
        self.GoldenTongueHotkeyArea.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.GoldenTongueHotkeyArea, 17, 1, 1, 1)

        self.label_6 = QLabel(self.miscPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color:grey;")

        self.gridLayout_8.addWidget(self.label_6, 16, 0, 1, 2)

        self.label_49 = QLabel(self.miscPage)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)
        self.label_49.setStyleSheet(u"color:grey;")

        self.gridLayout_8.addWidget(self.label_49, 8, 0, 1, 2)

        self.label_14 = QLabel(self.miscPage)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_8.addWidget(self.label_14, 18, 0, 1, 1)

        self.label_50 = QLabel(self.miscPage)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)
        self.label_50.setStyleSheet(u"color:grey;")

        self.gridLayout_8.addWidget(self.label_50, 11, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 19, 0, 1, 1)

        self.plainTextEdit_12 = QPlainTextEdit(self.miscPage)
        self.plainTextEdit_12.setObjectName(u"plainTextEdit_12")
        self.plainTextEdit_12.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_12.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.plainTextEdit_12, 4, 1, 1, 1)

        self.plainTextEdit_13 = QPlainTextEdit(self.miscPage)
        self.plainTextEdit_13.setObjectName(u"plainTextEdit_13")
        self.plainTextEdit_13.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_13.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.plainTextEdit_13, 5, 1, 1, 1)

        self.label_29 = QLabel(self.miscPage)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_8.addWidget(self.label_29, 4, 0, 1, 1)

        self.label = QLabel(self.miscPage)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:grey;")

        self.gridLayout_8.addWidget(self.label, 14, 0, 1, 2)

        self.DiscordGankPingSettings = QLabel(self.miscPage)
        self.DiscordGankPingSettings.setObjectName(u"DiscordGankPingSettings")

        self.gridLayout_8.addWidget(self.DiscordGankPingSettings, 3, 0, 1, 1)

        self.plainTextEdit_6 = QPlainTextEdit(self.miscPage)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_6.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.plainTextEdit_6, 18, 1, 1, 1)

        self.label_31 = QLabel(self.miscPage)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_8.addWidget(self.label_31, 7, 0, 1, 1)

        self.label_32 = QLabel(self.miscPage)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_8.addWidget(self.label_32, 5, 0, 1, 1)

        self.MbAllDropdown = QLabel(self.miscPage)
        self.MbAllDropdown.setObjectName(u"MbAllDropdown")

        self.gridLayout_8.addWidget(self.MbAllDropdown, 12, 0, 1, 1)

        self.label_34 = QLabel(self.miscPage)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_8.addWidget(self.label_34, 2, 0, 1, 1)

        self.FlashmapLabel = QLabel(self.miscPage)
        self.FlashmapLabel.setObjectName(u"FlashmapLabel")
        self.FlashmapLabel.setMinimumSize(QSize(0, 35))

        self.gridLayout_8.addWidget(self.FlashmapLabel, 13, 0, 1, 1)

        self.label_15 = QLabel(self.miscPage)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_8.addWidget(self.label_15, 17, 0, 1, 1)

        self.MbAllLabel = QLabel(self.miscPage)
        self.MbAllLabel.setObjectName(u"MbAllLabel")

        self.gridLayout_8.addWidget(self.MbAllLabel, 10, 0, 1, 1)

        self.label_33 = QLabel(self.miscPage)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_8.addWidget(self.label_33, 6, 0, 1, 1)

        self.label_48 = QLabel(self.miscPage)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)
        self.label_48.setStyleSheet(u"color:grey;")
        self.label_48.setWordWrap(True)

        self.gridLayout_8.addWidget(self.label_48, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.miscPage)
        self.movementPage = QWidget()
        self.movementPage.setObjectName(u"movementPage")
        self.gridLayout_11 = QGridLayout(self.movementPage)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.movementPage)
        self.savePage = QWidget()
        self.savePage.setObjectName(u"savePage")
        self.savePage.setEnabled(True)
        self.gridLayout_13 = QGridLayout(self.savePage)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_3 = QLabel(self.savePage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_13.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_17 = QLabel(self.savePage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setWordWrap(True)

        self.gridLayout_13.addWidget(self.label_17, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.savePage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 400))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 392, 572))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.Preset10EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset10EditName.setObjectName(u"Preset10EditName")
        self.Preset10EditName.setEnabled(True)
        self.Preset10EditName.setMinimumSize(QSize(50, 50))
        self.Preset10EditName.setMaximumSize(QSize(50, 50))
        self.Preset10EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/editName_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Preset10EditName.setIcon(icon9)
        self.Preset10EditName.setIconSize(QSize(30, 30))
        self.Preset10EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset10EditName, 9, 0, 1, 1)

        self.Preset9Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset9Save.setObjectName(u"Preset9Save")
        self.Preset9Save.setEnabled(True)
        self.Preset9Save.setMinimumSize(QSize(50, 50))
        self.Preset9Save.setMaximumSize(QSize(50, 50))
        self.Preset9Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon10 = QIcon()
        icon10.addFile(u":/icons/save_24dp_2E6F40_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Preset9Save.setIcon(icon10)
        self.Preset9Save.setIconSize(QSize(30, 30))
        self.Preset9Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset9Save, 8, 3, 1, 1)

        self.Preset7Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset7Load.setObjectName(u"Preset7Load")
        self.Preset7Load.setEnabled(True)
        self.Preset7Load.setMinimumSize(QSize(50, 50))
        self.Preset7Load.setMaximumSize(QSize(50, 50))
        self.Preset7Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon11 = QIcon()
        icon11.addFile(u":/icons/cloud_upload_24dp_705CCC_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Preset7Load.setIcon(icon11)
        self.Preset7Load.setIconSize(QSize(30, 30))
        self.Preset7Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset7Load, 6, 4, 1, 1)

        self.Preset6Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset6Name.setObjectName(u"Preset6Name")
        self.Preset6Name.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Preset6Name.sizePolicy().hasHeightForWidth())
        self.Preset6Name.setSizePolicy(sizePolicy)
        self.Preset6Name.setMinimumSize(QSize(200, 0))
        self.Preset6Name.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.Preset6Name.setFont(font1)
        self.Preset6Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset6Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset6Name, 5, 1, 1, 1)

        self.Preset10Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset10Name.setObjectName(u"Preset10Name")
        self.Preset10Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset10Name.sizePolicy().hasHeightForWidth())
        self.Preset10Name.setSizePolicy(sizePolicy)
        self.Preset10Name.setMinimumSize(QSize(200, 0))
        self.Preset10Name.setMaximumSize(QSize(200, 16777215))
        self.Preset10Name.setFont(font1)
        self.Preset10Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset10Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset10Name, 9, 1, 1, 1)

        self.Preset2Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset2Name.setObjectName(u"Preset2Name")
        self.Preset2Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset2Name.sizePolicy().hasHeightForWidth())
        self.Preset2Name.setSizePolicy(sizePolicy)
        self.Preset2Name.setMinimumSize(QSize(200, 0))
        self.Preset2Name.setMaximumSize(QSize(200, 16777215))
        self.Preset2Name.setFont(font1)
        self.Preset2Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset2Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset2Name, 1, 1, 1, 1)

        self.Preset3EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset3EditName.setObjectName(u"Preset3EditName")
        self.Preset3EditName.setEnabled(True)
        self.Preset3EditName.setMinimumSize(QSize(50, 50))
        self.Preset3EditName.setMaximumSize(QSize(50, 50))
        self.Preset3EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset3EditName.setIcon(icon9)
        self.Preset3EditName.setIconSize(QSize(30, 30))
        self.Preset3EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset3EditName, 2, 0, 1, 1)

        self.Preset1Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset1Name.setObjectName(u"Preset1Name")
        self.Preset1Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset1Name.sizePolicy().hasHeightForWidth())
        self.Preset1Name.setSizePolicy(sizePolicy)
        self.Preset1Name.setMinimumSize(QSize(200, 0))
        self.Preset1Name.setMaximumSize(QSize(200, 16777215))
        self.Preset1Name.setFont(font1)
        self.Preset1Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset1Name.setMaxLength(20)
        self.Preset1Name.setReadOnly(True)
        self.Preset1Name.setClearButtonEnabled(False)

        self.gridLayout_15.addWidget(self.Preset1Name, 0, 1, 1, 1)

        self.Preset5EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset5EditName.setObjectName(u"Preset5EditName")
        self.Preset5EditName.setEnabled(True)
        self.Preset5EditName.setMinimumSize(QSize(50, 50))
        self.Preset5EditName.setMaximumSize(QSize(50, 50))
        self.Preset5EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset5EditName.setIcon(icon9)
        self.Preset5EditName.setIconSize(QSize(30, 30))
        self.Preset5EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset5EditName, 4, 0, 1, 1)

        self.Preset9Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset9Load.setObjectName(u"Preset9Load")
        self.Preset9Load.setEnabled(True)
        self.Preset9Load.setMinimumSize(QSize(50, 50))
        self.Preset9Load.setMaximumSize(QSize(50, 50))
        self.Preset9Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset9Load.setIcon(icon11)
        self.Preset9Load.setIconSize(QSize(30, 30))
        self.Preset9Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset9Load, 8, 4, 1, 1)

        self.Preset6Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset6Load.setObjectName(u"Preset6Load")
        self.Preset6Load.setEnabled(True)
        self.Preset6Load.setMinimumSize(QSize(50, 50))
        self.Preset6Load.setMaximumSize(QSize(50, 50))
        self.Preset6Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset6Load.setIcon(icon11)
        self.Preset6Load.setIconSize(QSize(30, 30))
        self.Preset6Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset6Load, 5, 4, 1, 1)

        self.Preset9Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset9Name.setObjectName(u"Preset9Name")
        self.Preset9Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset9Name.sizePolicy().hasHeightForWidth())
        self.Preset9Name.setSizePolicy(sizePolicy)
        self.Preset9Name.setMinimumSize(QSize(200, 0))
        self.Preset9Name.setMaximumSize(QSize(200, 16777215))
        self.Preset9Name.setFont(font1)
        self.Preset9Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset9Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset9Name, 8, 1, 1, 1)

        self.Preset6Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset6Save.setObjectName(u"Preset6Save")
        self.Preset6Save.setEnabled(True)
        self.Preset6Save.setMinimumSize(QSize(50, 50))
        self.Preset6Save.setMaximumSize(QSize(50, 50))
        self.Preset6Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset6Save.setIcon(icon10)
        self.Preset6Save.setIconSize(QSize(30, 30))
        self.Preset6Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset6Save, 5, 3, 1, 1)

        self.Preset7Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset7Save.setObjectName(u"Preset7Save")
        self.Preset7Save.setEnabled(True)
        self.Preset7Save.setMinimumSize(QSize(50, 50))
        self.Preset7Save.setMaximumSize(QSize(50, 50))
        self.Preset7Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset7Save.setIcon(icon10)
        self.Preset7Save.setIconSize(QSize(30, 30))
        self.Preset7Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset7Save, 6, 3, 1, 1)

        self.Preset6EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset6EditName.setObjectName(u"Preset6EditName")
        self.Preset6EditName.setEnabled(True)
        self.Preset6EditName.setMinimumSize(QSize(50, 50))
        self.Preset6EditName.setMaximumSize(QSize(50, 50))
        self.Preset6EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset6EditName.setIcon(icon9)
        self.Preset6EditName.setIconSize(QSize(30, 30))
        self.Preset6EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset6EditName, 5, 0, 1, 1)

        self.Preset7EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset7EditName.setObjectName(u"Preset7EditName")
        self.Preset7EditName.setEnabled(True)
        self.Preset7EditName.setMinimumSize(QSize(50, 50))
        self.Preset7EditName.setMaximumSize(QSize(50, 50))
        self.Preset7EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset7EditName.setIcon(icon9)
        self.Preset7EditName.setIconSize(QSize(30, 30))
        self.Preset7EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset7EditName, 6, 0, 1, 1)

        self.Preset2Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset2Save.setObjectName(u"Preset2Save")
        self.Preset2Save.setEnabled(True)
        self.Preset2Save.setMinimumSize(QSize(50, 50))
        self.Preset2Save.setMaximumSize(QSize(50, 50))
        self.Preset2Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset2Save.setIcon(icon10)
        self.Preset2Save.setIconSize(QSize(30, 30))
        self.Preset2Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset2Save, 1, 3, 1, 1)

        self.Preset4Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset4Load.setObjectName(u"Preset4Load")
        self.Preset4Load.setEnabled(True)
        self.Preset4Load.setMinimumSize(QSize(50, 50))
        self.Preset4Load.setMaximumSize(QSize(50, 50))
        self.Preset4Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset4Load.setIcon(icon11)
        self.Preset4Load.setIconSize(QSize(30, 30))
        self.Preset4Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset4Load, 3, 4, 1, 1)

        self.Preset3Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset3Load.setObjectName(u"Preset3Load")
        self.Preset3Load.setEnabled(True)
        self.Preset3Load.setMinimumSize(QSize(50, 50))
        self.Preset3Load.setMaximumSize(QSize(50, 50))
        self.Preset3Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset3Load.setIcon(icon11)
        self.Preset3Load.setIconSize(QSize(30, 30))
        self.Preset3Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset3Load, 2, 4, 1, 1)

        self.Preset1EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset1EditName.setObjectName(u"Preset1EditName")
        self.Preset1EditName.setEnabled(True)
        self.Preset1EditName.setMinimumSize(QSize(50, 50))
        self.Preset1EditName.setMaximumSize(QSize(50, 50))
        self.Preset1EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset1EditName.setIcon(icon9)
        self.Preset1EditName.setIconSize(QSize(30, 30))
        self.Preset1EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset1EditName, 0, 0, 1, 1)

        self.Preset2EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset2EditName.setObjectName(u"Preset2EditName")
        self.Preset2EditName.setEnabled(True)
        self.Preset2EditName.setMinimumSize(QSize(50, 50))
        self.Preset2EditName.setMaximumSize(QSize(50, 50))
        self.Preset2EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset2EditName.setIcon(icon9)
        self.Preset2EditName.setIconSize(QSize(30, 30))
        self.Preset2EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset2EditName, 1, 0, 1, 1)

        self.Preset9EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset9EditName.setObjectName(u"Preset9EditName")
        self.Preset9EditName.setEnabled(True)
        self.Preset9EditName.setMinimumSize(QSize(50, 50))
        self.Preset9EditName.setMaximumSize(QSize(50, 50))
        self.Preset9EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset9EditName.setIcon(icon9)
        self.Preset9EditName.setIconSize(QSize(30, 30))
        self.Preset9EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset9EditName, 8, 0, 1, 1)

        self.Preset2Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset2Load.setObjectName(u"Preset2Load")
        self.Preset2Load.setEnabled(True)
        self.Preset2Load.setMinimumSize(QSize(50, 50))
        self.Preset2Load.setMaximumSize(QSize(50, 50))
        self.Preset2Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset2Load.setIcon(icon11)
        self.Preset2Load.setIconSize(QSize(30, 30))
        self.Preset2Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset2Load, 1, 4, 1, 1)

        self.Preset8Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset8Name.setObjectName(u"Preset8Name")
        self.Preset8Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset8Name.sizePolicy().hasHeightForWidth())
        self.Preset8Name.setSizePolicy(sizePolicy)
        self.Preset8Name.setMinimumSize(QSize(200, 0))
        self.Preset8Name.setMaximumSize(QSize(200, 16777215))
        self.Preset8Name.setFont(font1)
        self.Preset8Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset8Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset8Name, 7, 1, 1, 1)

        self.Preset10Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset10Load.setObjectName(u"Preset10Load")
        self.Preset10Load.setEnabled(True)
        self.Preset10Load.setMinimumSize(QSize(50, 50))
        self.Preset10Load.setMaximumSize(QSize(50, 50))
        self.Preset10Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset10Load.setIcon(icon11)
        self.Preset10Load.setIconSize(QSize(30, 30))
        self.Preset10Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset10Load, 9, 4, 1, 1)

        self.Preset4Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset4Save.setObjectName(u"Preset4Save")
        self.Preset4Save.setEnabled(True)
        self.Preset4Save.setMinimumSize(QSize(50, 50))
        self.Preset4Save.setMaximumSize(QSize(50, 50))
        self.Preset4Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset4Save.setIcon(icon10)
        self.Preset4Save.setIconSize(QSize(30, 30))
        self.Preset4Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset4Save, 3, 3, 1, 1)

        self.Preset8EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset8EditName.setObjectName(u"Preset8EditName")
        self.Preset8EditName.setEnabled(True)
        self.Preset8EditName.setMinimumSize(QSize(50, 50))
        self.Preset8EditName.setMaximumSize(QSize(50, 50))
        self.Preset8EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset8EditName.setIcon(icon9)
        self.Preset8EditName.setIconSize(QSize(30, 30))
        self.Preset8EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset8EditName, 7, 0, 1, 1)

        self.Preset8Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset8Load.setObjectName(u"Preset8Load")
        self.Preset8Load.setEnabled(True)
        self.Preset8Load.setMinimumSize(QSize(50, 50))
        self.Preset8Load.setMaximumSize(QSize(50, 50))
        self.Preset8Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset8Load.setIcon(icon11)
        self.Preset8Load.setIconSize(QSize(30, 30))
        self.Preset8Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset8Load, 7, 4, 1, 1)

        self.Preset1Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset1Save.setObjectName(u"Preset1Save")
        self.Preset1Save.setEnabled(True)
        self.Preset1Save.setMinimumSize(QSize(50, 50))
        self.Preset1Save.setMaximumSize(QSize(50, 50))
        self.Preset1Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset1Save.setIcon(icon10)
        self.Preset1Save.setIconSize(QSize(30, 30))
        self.Preset1Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset1Save, 0, 3, 1, 1)

        self.Preset3Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset3Name.setObjectName(u"Preset3Name")
        self.Preset3Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset3Name.sizePolicy().hasHeightForWidth())
        self.Preset3Name.setSizePolicy(sizePolicy)
        self.Preset3Name.setMinimumSize(QSize(200, 0))
        self.Preset3Name.setMaximumSize(QSize(200, 16777215))
        self.Preset3Name.setFont(font1)
        self.Preset3Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset3Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset3Name, 2, 1, 1, 1)

        self.Preset5Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset5Name.setObjectName(u"Preset5Name")
        self.Preset5Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset5Name.sizePolicy().hasHeightForWidth())
        self.Preset5Name.setSizePolicy(sizePolicy)
        self.Preset5Name.setMinimumSize(QSize(200, 0))
        self.Preset5Name.setMaximumSize(QSize(200, 16777215))
        self.Preset5Name.setFont(font1)
        self.Preset5Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset5Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset5Name, 4, 1, 1, 1)

        self.Preset10Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset10Save.setObjectName(u"Preset10Save")
        self.Preset10Save.setEnabled(True)
        self.Preset10Save.setMinimumSize(QSize(50, 50))
        self.Preset10Save.setMaximumSize(QSize(50, 50))
        self.Preset10Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset10Save.setIcon(icon10)
        self.Preset10Save.setIconSize(QSize(30, 30))
        self.Preset10Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset10Save, 9, 3, 1, 1)

        self.Preset5Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset5Load.setObjectName(u"Preset5Load")
        self.Preset5Load.setEnabled(True)
        self.Preset5Load.setMinimumSize(QSize(50, 50))
        self.Preset5Load.setMaximumSize(QSize(50, 50))
        self.Preset5Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset5Load.setIcon(icon11)
        self.Preset5Load.setIconSize(QSize(30, 30))
        self.Preset5Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset5Load, 4, 4, 1, 1)

        self.Preset8Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset8Save.setObjectName(u"Preset8Save")
        self.Preset8Save.setEnabled(True)
        self.Preset8Save.setMinimumSize(QSize(50, 50))
        self.Preset8Save.setMaximumSize(QSize(50, 50))
        self.Preset8Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset8Save.setIcon(icon10)
        self.Preset8Save.setIconSize(QSize(30, 30))
        self.Preset8Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset8Save, 7, 3, 1, 1)

        self.Preset5Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset5Save.setObjectName(u"Preset5Save")
        self.Preset5Save.setEnabled(True)
        self.Preset5Save.setMinimumSize(QSize(50, 50))
        self.Preset5Save.setMaximumSize(QSize(50, 50))
        self.Preset5Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset5Save.setIcon(icon10)
        self.Preset5Save.setIconSize(QSize(30, 30))
        self.Preset5Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset5Save, 4, 3, 1, 1)

        self.Preset4EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset4EditName.setObjectName(u"Preset4EditName")
        self.Preset4EditName.setEnabled(True)
        self.Preset4EditName.setMinimumSize(QSize(50, 50))
        self.Preset4EditName.setMaximumSize(QSize(50, 50))
        self.Preset4EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset4EditName.setIcon(icon9)
        self.Preset4EditName.setIconSize(QSize(30, 30))
        self.Preset4EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset4EditName, 3, 0, 1, 1)

        self.Preset1Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset1Load.setObjectName(u"Preset1Load")
        self.Preset1Load.setEnabled(True)
        self.Preset1Load.setMinimumSize(QSize(50, 50))
        self.Preset1Load.setMaximumSize(QSize(50, 50))
        self.Preset1Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset1Load.setIcon(icon11)
        self.Preset1Load.setIconSize(QSize(30, 30))
        self.Preset1Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset1Load, 0, 4, 1, 1)

        self.Preset4Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset4Name.setObjectName(u"Preset4Name")
        self.Preset4Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset4Name.sizePolicy().hasHeightForWidth())
        self.Preset4Name.setSizePolicy(sizePolicy)
        self.Preset4Name.setMinimumSize(QSize(200, 0))
        self.Preset4Name.setMaximumSize(QSize(200, 16777215))
        self.Preset4Name.setFont(font1)
        self.Preset4Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset4Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset4Name, 3, 1, 1, 1)

        self.Preset3Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset3Save.setObjectName(u"Preset3Save")
        self.Preset3Save.setEnabled(True)
        self.Preset3Save.setMinimumSize(QSize(50, 50))
        self.Preset3Save.setMaximumSize(QSize(50, 50))
        self.Preset3Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset3Save.setIcon(icon10)
        self.Preset3Save.setIconSize(QSize(30, 30))
        self.Preset3Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset3Save, 2, 3, 1, 1)

        self.Preset7Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset7Name.setObjectName(u"Preset7Name")
        self.Preset7Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset7Name.sizePolicy().hasHeightForWidth())
        self.Preset7Name.setSizePolicy(sizePolicy)
        self.Preset7Name.setMinimumSize(QSize(200, 0))
        self.Preset7Name.setMaximumSize(QSize(200, 16777215))
        self.Preset7Name.setFont(font1)
        self.Preset7Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset7Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset7Name, 6, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_12, 9, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_11, 8, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_10, 7, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_9, 6, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_8, 5, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_7, 4, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_6, 3, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_9.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_2, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.savePage)
        self.runPage = QWidget()
        self.runPage.setObjectName(u"runPage")
        self.gridLayout_14 = QGridLayout(self.runPage)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_5 = QLabel(self.runPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color:grey;")

        self.gridLayout_14.addWidget(self.label_5, 1, 0, 1, 2)

        self.label_43 = QLabel(self.runPage)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)
        self.label_43.setStyleSheet(u"color:grey;")

        self.gridLayout_14.addWidget(self.label_43, 3, 0, 1, 2)

        self.label_4 = QLabel(self.runPage)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_14.addWidget(self.label_4, 0, 0, 1, 2)

        self.label_42 = QLabel(self.runPage)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_14.addWidget(self.label_42, 2, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 545, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_11, 5, 1, 1, 1)

        self.label_37 = QLabel(self.runPage)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_14.addWidget(self.label_37, 4, 0, 1, 1)

        self.plainTextEdit_17 = QPlainTextEdit(self.runPage)
        self.plainTextEdit_17.setObjectName(u"plainTextEdit_17")
        self.plainTextEdit_17.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_17.setStyleSheet(u"")

        self.gridLayout_14.addWidget(self.plainTextEdit_17, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.runPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.gridLayout_7 = QGridLayout(self.settingsPage)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.themeLabel = QLabel(self.settingsPage)
        self.themeLabel.setObjectName(u"themeLabel")

        self.gridLayout_7.addWidget(self.themeLabel, 2, 0, 1, 1)

        self.themeComboBox = QComboBox(self.settingsPage)
        self.themeComboBox.addItem("")
        self.themeComboBox.addItem("")
        self.themeComboBox.setObjectName(u"themeComboBox")

        self.gridLayout_7.addWidget(self.themeComboBox, 2, 1, 1, 1)

        self.toggleNotifsLabel = QLabel(self.settingsPage)
        self.toggleNotifsLabel.setObjectName(u"toggleNotifsLabel")

        self.gridLayout_7.addWidget(self.toggleNotifsLabel, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.label_41 = QLabel(self.settingsPage)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)
        self.label_41.setStyleSheet(u"color:grey;")
        self.label_41.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_41, 1, 0, 1, 2)

        self.label_45 = QLabel(self.settingsPage)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)
        self.label_45.setStyleSheet(u"color:grey;")

        self.gridLayout_7.addWidget(self.label_45, 3, 0, 1, 2)

        self.stackedWidget.addWidget(self.settingsPage)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.weaponsButton.setText("")
        self.progressionButton.setText("")
        self.bellButton.setText("")
        self.saveButton.setText("")
        self.miscButton.setText("")
        self.settingsButton.setText("")
        self.mantrasButton.setText("")
        self.playButton.setText("")
        self.menuButton.setText("")
        self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Save</span></p></body></html>", None))
        self.MovestackChoice.setItemText(0, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.MovestackChoice.setItemText(1, QCoreApplication.translate("MainWindow", u"Parry", None))

        self.BellMovestack.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Bell Movestack</span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Rolls or parries whenever you press C (activating bell)", None))
        self.AutoMantraVariantsDescriptor.setText(QCoreApplication.translate("MainWindow", u"Performs the special variant of a mantra activated by pressing F during windup", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Performs a roll when using a mantra", None))
        self.plainTextEdit_10.setPlainText("")
        self.plainTextEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Approximate ping, default is 100 (Shift + F3 to see ping)", None))
        self.AutoMantraVariants.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Mantra Variants </span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Ping</span></p></body></html>", None))
        self.AutoMantraVariantsKeysLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Mantra Keys</span></p></body></html>", None))
        self.plainTextEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numbers or letters separated by commas, like 1,2,e,3,z", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Mantra Keys</span></p></body></html>", None))
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numbers or letters separated by commas, like 1,2,e,3,z", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Screen Resolution</span></p></body></html>", None))
        self.AutoMantraVariantsKeysArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numbers or letters separated by commas, like 1,2,e,3,z", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Performs a slide when using a mantra while running", None))
        self.AutoRitualCast.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Ritual Casts</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Mantra Slide Tech</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Mantra Keys</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Automatically activates all ritual casts.</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Mantra Roll Tech</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Screen Scale</span></p></body></html>", None))
        self.screenResolution.setItemText(0, QCoreApplication.translate("MainWindow", u"1920 x 1080", None))
        self.screenResolution.setItemText(1, QCoreApplication.translate("MainWindow", u"1920 x 1200", None))

        self.screenResolution.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your computer's screen resolution", None))
        self.screenScale.setItemText(0, QCoreApplication.translate("MainWindow", u"100%", None))
        self.screenScale.setItemText(1, QCoreApplication.translate("MainWindow", u"125%", None))

        self.screenScale.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your computer screen's scale (%)", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Uppercuts as soon as you press ctrl", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Weapon Toolbar Number</span></p></body></html>", None))
        self.MotifHotkeyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Same as auto uppercut but doesn't trigger when you're running", None))
        self.MotifToolbarNumberLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Motif Toolbar Number</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Automatically spams any key when M1 is held (default `). The key MUST be binded to basic attack (you can have two keybinds at a time)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Quickly swaps your weapon's motif (the critical attack of your weapon) for you.", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Feint</span></p></body></html>", None))
        self.HoldM1Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Faster Hold M1</span></p></body></html>", None))
        self.MotifSwapLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Motif Swap</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Does an air dash / roll in the middle of your aerial attack. Does not activate when you do not jump shortly before", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Uppercut</span></p></body></html>", None))
        self.AerialAirDashLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Aerial M1 Dash</span></p></body></html>", None))
        self.MotifHotkeyArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The key you want to press to swap motifs", None))
        self.MotifToolbarNumberArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The toolbar number of the motif", None))
        self.plainTextEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The toolbar number of the weapon", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Dynamic Uppercuts</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Feints for you when you press F</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Key</span></p></body></html>", None))
        self.HoldM1Key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The key you want to be spammed when m1 is held", None))
        self.CharismaAutofillLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Charisma Autofill</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Type out part of the charisma line and it will finish it for you", None))
        self.AnkleWeightsTrainingHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hotkey to start/stop training agility", None))
        self.AnkleWeightsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Agility Auto-train</span></p></body></html>", None))
        self.BoulderTrainingHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hotkey to start/stop training fortitude(boulder)", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.WillpowerTrainingHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hotkey to start/stop training willpower", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Make sure the Ankle Weights tool is equipped before starting", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.BoulderTrainingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Boulder Auto-train</span></p></body></html>", None))
        self.WillpowerTrainingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Prayer Auto-train</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Make sure the Boulder tool is held out before starting and you are near a campfire", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Make sure the Prayer Beads tool is held out before starting", None))
        self.plainTextEdit_14.setPlainText("")
        self.plainTextEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leave blank if you do not want a custom one", None))
        self.DiscordGankPingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Discord Message</span></p></body></html>", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Found in Server Settings > Integrations > Webhooks", None))
        self.MbAllHotkeyArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say mb all", None))
        self.GoldenTongueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Golden Tongue</span></p></body></html>", None))
        self.plainTextEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to send the message", None))
        self.GoldenTongueHotkeyArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say your thing", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and types whatever you want when you press a hotkey", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Useful to let people know where you are", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and says mb all whenever you press the hotkey", None))
        self.plainTextEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Message you want the bot to send", None))
        self.plainTextEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leave blank if you do not want a custom one", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Message</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Keeps map open while holding m and then closes it when you release m", None))
        self.DiscordGankPingSettings.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Discord Webhook</span></p></body></html>", None))
        self.plainTextEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thing you want to say (can be a sentence)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Take Screenshot</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Username</span></p></body></html>", None))
        self.MbAllDropdown.setText(QCoreApplication.translate("MainWindow", u"Hotkey", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.FlashmapLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Flash Map</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Hotkey", None))
        self.MbAllLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Mb All </span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Profile Picture Link</span></p></body></html>", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Automatically sends a discord message when a key is pressed", None))
        self.savePage.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Presets</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Note: If you load a preset and change it, it will NOT automatically save.</span></p></body></html>", None))
        self.Preset10EditName.setText("")
        self.Preset9Save.setText("")
        self.Preset7Load.setText("")
        self.Preset6Name.setText(QCoreApplication.translate("MainWindow", u"Preset 6", None))
        self.Preset10Name.setText(QCoreApplication.translate("MainWindow", u"Preset 10", None))
        self.Preset2Name.setText(QCoreApplication.translate("MainWindow", u"Preset 2", None))
        self.Preset3EditName.setText("")
        self.Preset1Name.setText(QCoreApplication.translate("MainWindow", u"Preset 1", None))
        self.Preset5EditName.setText("")
        self.Preset9Load.setText("")
        self.Preset6Load.setText("")
        self.Preset9Name.setText(QCoreApplication.translate("MainWindow", u"Preset 9", None))
        self.Preset6Save.setText("")
        self.Preset7Save.setText("")
        self.Preset6EditName.setText("")
        self.Preset7EditName.setText("")
        self.Preset2Save.setText("")
        self.Preset4Load.setText("")
        self.Preset3Load.setText("")
        self.Preset1EditName.setText("")
        self.Preset2EditName.setText("")
        self.Preset9EditName.setText("")
        self.Preset2Load.setText("")
        self.Preset8Name.setText(QCoreApplication.translate("MainWindow", u"Preset 8", None))
        self.Preset10Load.setText("")
        self.Preset4Save.setText("")
        self.Preset8EditName.setText("")
        self.Preset8Load.setText("")
        self.Preset1Save.setText("")
        self.Preset3Name.setText(QCoreApplication.translate("MainWindow", u"Preset 3", None))
        self.Preset5Name.setText(QCoreApplication.translate("MainWindow", u"Preset 5", None))
        self.Preset10Save.setText("")
        self.Preset5Load.setText("")
        self.Preset8Save.setText("")
        self.Preset5Save.setText("")
        self.Preset4EditName.setText("")
        self.Preset1Load.setText("")
        self.Preset4Name.setText(QCoreApplication.translate("MainWindow", u"Preset 4", None))
        self.Preset3Save.setText("")
        self.Preset7Name.setText(QCoreApplication.translate("MainWindow", u"Preset 7", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Activates / deactivates all toggled macros", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Activates / deactivates macros with a keypress instead of having to click the toggle", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Activate Macros</span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Activate Macros Hotkey</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Keybind to toggle the macros </span></p></body></html>", None))
        self.themeLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Theme</span></p></body></html>", None))
        self.themeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Dark", None))
        self.themeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Navy Blue", None))

        self.toggleNotifsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Toggle Notifications</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"When something togglable is used, such as \"Toggle Activate Macros\", a small popup will be activated in the bottom right of the screen", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Changes the theme of the application</p></body></html>", None))
    # retranslateUi

        print('importing macros')
        from macros.training import autocharisma, autofortitude, autoagility, autowillpower
        from macros import threadedkeyb, holdm1, autovariants, mball, goldentongue, motifswap, gankpinger, flashmap, autofeint, autoritualcast
        from macros.bellStack import bellStackParry, bellStackDodge
        from macros.mantraTech import mantraTechRoll, mantraTechSlide
        from macros.uppercuts import autoUppercutAlways, autoUppercutDYNAMIC
        print('macros imported')
        # talents, bells, mantras, weapons, movement, progression, misc, settings
        self.bellButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.mantrasButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.weaponsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.progressionButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.miscButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        #self.movementButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.saveButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.playButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        self.settingsButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(8))
        def changeBarVis():
            if self.menuBar.isVisible():
                self.menuBar.hide()
            elif self.menuBar.isHidden():
                self.menuBar.show()
        self.menuButton.clicked.connect(changeBarVis)

        self.bellButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Bells</span></p></body></html>", None)))
        self.mantrasButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Mantras</span></p></body></html>", None)))
        self.weaponsButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Weapons</span></p></body></html>", None)))
        self.progressionButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Progression</span></p></body></html>", None)))
        self.miscButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Miscellaneous</span></p></body></html>", None)))
        #self.movementButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Movement</span></p></body></html>", None)))
        self.saveButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Save</span></p></body></html>", None)))
        self.playButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Run</span></p></body></html>", None)))
        self.settingsButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Settings</span></p></body></html>", None)))

        #! Toggles
        #!BELLS
        self.BellMovestackToggle = CustomToggle(self.bellPage)
        self.gridLayout_5.addWidget(self.BellMovestackToggle, 0, 1, 1, 2)

        #!MANTRAS
        self.RitualCastToggle = CustomToggle(self.mantrasPage)
        self.gridLayout_6.addWidget(self.RitualCastToggle, 0,1,1,1)
        self.mantraVariantToggle = CustomToggle(self.mantrasPage)
        self.gridLayout_6.addWidget(self.mantraVariantToggle, 5, 1, 1, 1)
        self.mantraTechRollToggle = CustomToggle(self.mantrasPage)
        self.gridLayout_6.addWidget(self.mantraTechRollToggle, 11,1,1,2)
        self.mantraTechSlidetoggle = CustomToggle(self.mantrasPage)
        self.gridLayout_6.addWidget(self.mantraTechSlidetoggle, 8,1,1,2)



        # label 9 = mantra roll label 7 = mantra slide
        # AutoMantraVariantsKeysArea


        #! WEAPONS
        #toggles
        self.AirDashToggle = CustomToggle(self.weaponsPage)
        self.gridLayout_10.addWidget(self.AirDashToggle, 0,1,1,2)
        self.HoldM1Toggle = CustomToggle(self.weaponsPage)
        self.gridLayout_10.addWidget(self.HoldM1Toggle, 2,1,1,2)
        self.MotifSwapToggle = CustomToggle(self.weaponsPage)
        self.gridLayout_10.addWidget(self.MotifSwapToggle, 5,1,1,2)
        self.uppercutToggle = CustomToggle(self.weaponsPage)
        self.gridLayout_10.addWidget(self.uppercutToggle, 10,1,1,1)
        self.uppercutDynamicToggle = CustomToggle(self.weaponsPage)
        self.gridLayout_10.addWidget(self.uppercutDynamicToggle, 12,1,1,1)
        self.autoFeintToggle = CustomToggle(self.weaponsPage)
        self.gridLayout_10.addWidget(self.autoFeintToggle, 14,1,1,1)

        #functions

        #!RUNNING
        self.RunToggle = CustomToggle(self.runPage)
        self.gridLayout_14.addWidget(self.RunToggle, 0,1,1,2)
        self.RunKeybindToggle = CustomToggle(self.runPage)
        self.gridLayout_14.addWidget(self.RunKeybindToggle, 2, 1, 1, 1)

        
        #!MISCELLANEOUS
        self.MbAllToggle = CustomToggle(self.miscPage)
        self.gridLayout_8.addWidget(self.MbAllToggle, 10, 1, 1, 1)
        self.GoldenTongueToggle = CustomToggle(self.miscPage)
        self.gridLayout_8.addWidget(self.GoldenTongueToggle, 15, 1, 1, 2)
        self.GankPingerToggle = CustomToggle(self.miscPage)
        self.gridLayout_8.addWidget(self.GankPingerToggle, 0,1,1,1)
        self.ScreenshotToggle = CustomToggle(self.miscPage)
        self.gridLayout_8.addWidget(self.ScreenshotToggle, 7,1,1,1)
        self.FlashMapToggle = CustomToggle(self.miscPage)
        self.gridLayout_8.addWidget(self.FlashMapToggle, 13,1,1,2)

        #!PROGRESSION
        self.CharismaAutofillToggle = CustomToggle(self.miscPage)
        self.gridLayout_12.addWidget(self.CharismaAutofillToggle, 0,3,1,1)
        self.AutoAgilityToggle = CustomToggle(self.miscPage)
        self.gridLayout_12.addWidget(self.AutoAgilityToggle, 2,3,1,1)
        self.AutoFortitudeToggle = CustomToggle(self.miscPage)
        self.gridLayout_12.addWidget(self.AutoFortitudeToggle, 5,3,1,1)
        self.AutoWillpowerToggle = CustomToggle(self.miscPage)
        self.gridLayout_12.addWidget(self.AutoWillpowerToggle, 13,3,1,1)

        #!SETTINGS
        self.toggleNotifsToggle = CustomToggle(self.settingsPage)
        self.gridLayout_7.addWidget(self.toggleNotifsToggle, 0,1,1,1)

        self.toggles = [
                self.BellMovestackToggle,

                self.mantraVariantToggle,
                self.mantraTechRollToggle,
                self.mantraTechSlidetoggle,
                self.RitualCastToggle,

                self.AirDashToggle,
                self.HoldM1Toggle,
                self.MotifSwapToggle,
                self.uppercutToggle,
                self.uppercutDynamicToggle,
                self.autoFeintToggle,

                self.MbAllToggle,
                self.GoldenTongueToggle,
                self.GankPingerToggle,
                self.ScreenshotToggle,

                self.CharismaAutofillToggle,
                self.AutoAgilityToggle,
                self.AutoFortitudeToggle,
                self.AutoWillpowerToggle
        ]
        for toggle in self.toggles:
                toggle.toggled.connect(lambda: self.RunToggle.setChecked(False))
        dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
        settingsPath = os.path.join(dataLocation, 'data/Settings.json') 
        with open(settingsPath) as f:
                currentInfo = json.load(f)
                if currentInfo['notifs']:
                        self.toggleNotifsToggle.setChecked(True)
                elif not currentInfo['notifs']:
                       self.toggleNotifsToggle.setChecked(False)




        #! conditional toggles
        def disableDynUp():
               if self.uppercutToggle._is_checked == 2:
                      self.uppercutDynamicToggle.setChecked(False)
        def disableNormUp():
               if self.uppercutDynamicToggle._is_checked == 2:
                      self.uppercutToggle.setChecked(False)
        self.uppercutToggle.toggled.connect(disableDynUp)
        self.uppercutDynamicToggle.toggled.connect(disableNormUp)

        def toggleNotifs():
                if self.toggleNotifsToggle._is_checked == 2: 
                        dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                        settingsPath = os.path.join(dataLocation, 'data/Settings.json')
                        with open(settingsPath) as f:
                                currentSettings = json.load(f)
                        f.close()
                        currentSettings['notifs'] = True
                        with open(settingsPath, 'w') as f:
                               json.dump(currentSettings, f)
                if self.toggleNotifsToggle._is_checked == 0:
                        dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                        settingsPath = os.path.join(dataLocation, 'data/Settings.json')
                        with open(settingsPath) as f:
                                currentSettings = json.load(f)
                        f.close()
                        currentSettings['notifs'] = False
                        with open(settingsPath, 'w') as f:
                               json.dump(currentSettings, f)
        self.toggleNotifsToggle.toggled.connect(toggleNotifs)
                                                      



               


                             
        def runToggle():
                def addMacro(name:str, toggle, listener_class, **run_kwargs):
                        if toggle._is_checked != 2:
                               return
                        listener_instance = listener_class()
                        setattr(self, name, listener_instance)
                        self.threads.append(listener_instance)
                        thread = Thread(
                                        target=lambda: listener_instance.run(**run_kwargs),
                                        name=f"{name} Thread"
                        )
                        thread.daemon = True
                        thread.start()
                if self.RunToggle._is_checked == 2:  # is checked
                        self.threads = []       
                        addMacro('Air Dash M1 Movestack', self.AirDashToggle, threadedkeyb.AirListener)
                        addMacro('Faster Hold M1', self.HoldM1Toggle, holdm1.M1Listener, key=self.HoldM1Key.toPlainText())
                        if self.BellMovestackToggle._is_checked == 2:
                                if self.MovestackChoice.currentIndex() == 1:     
                                        addMacro('Bell Stack Parry', self.BellMovestackToggle, bellStackParry.BellStackParryListener) # Either a logic error or i need to fix some jank on this one
                                elif self.MovestackChoice.currentIndex() == 0:
                                        addMacro('Bell Stack Dodge', self.BellMovestackToggle, bellStackDodge.BellStackDodgeListener)
                        addMacro('Mantra Roll Tech', self.mantraTechRollToggle, mantraTechRoll.MantraRollTechListener, keybinds=self.plainTextEdit_3.toPlainText())
                        addMacro('Mantra Slide Tech', self.mantraTechSlidetoggle, mantraTechSlide.MantraSlideTechListener, keybinds=self.plainTextEdit_2.toPlainText())
                        addMacro('Mb All', self.MbAllToggle, mball.MbAllListener, keybind=self.MbAllHotkeyArea.toPlainText())
                        addMacro('Golden Tongue', self.GoldenTongueToggle, goldentongue.GoldenTongueListener, keybind=self.GoldenTongueHotkeyArea.toPlainText(), content=self.plainTextEdit_6.toPlainText())
                        addMacro('Mantra Variants', self.mantraVariantToggle, autovariants.MantraVariantListener, keybinds=self.AutoMantraVariantsKeysArea.toPlainText())
                        #To test:
                        addMacro('Motif Swap', self.MotifSwapToggle, motifswap.MotifSwapListener, keybind=self.MotifHotkeyArea.toPlainText(), motifnum=self.MotifToolbarNumberArea.toPlainText(), weaponnum=self.plainTextEdit_7.toPlainText())
                        templatepath = os.path.dirname(os.path.abspath(__file__))
                        templatepath = os.path.join(templatepath, 'assets/letter_templates')
                        print(templatepath)
                        addMacro('Ritual Cast', self.RitualCastToggle, autoritualcast.RitualCastListener, ping_ms=self.plainTextEdit_10.toPlainText(), basepath=templatepath, scale=self.screenScale.currentIndex(), resolution=self.screenResolution.currentIndex())
                        addMacro('Charisma Autofill', self.CharismaAutofillToggle, autocharisma.autoCharismaListener)
                        addMacro('Auto Fortitude', self.AutoFortitudeToggle, autofortitude.AutoFortitudeListener, keybind=self.BoulderTrainingHotkey.toPlainText())
                        addMacro('Auto Willpower', self.AutoWillpowerToggle, autowillpower.AutoWillpowerListener, keybind=self.WillpowerTrainingHotkey.toPlainText())

                        addMacro('Auto Agility', self.AutoAgilityToggle, autoagility.AutoAgilityListener, keybind=self.AnkleWeightsTrainingHotkey.toPlainText())
                        addMacro('Gank Pinger', self.GankPingerToggle, gankpinger.GankPingListener, hotkey=self.plainTextEdit_15.toPlainText(),  webhook_url=self.plainTextEdit.toPlainText(), message=self.plainTextEdit_12.toPlainText(), username=self.plainTextEdit_13.toPlainText(), avatar_url=self.plainTextEdit_14.toPlainText(), ScreenshotToggle=(self.ScreenshotToggle._is_checked == 2))
                        addMacro('Auto Uppercut', self.uppercutToggle, autoUppercutAlways.UppercutListener)
                        addMacro('Dynamic Auto Uppercut', self.uppercutDynamicToggle, autoUppercutDYNAMIC.DynamicUppercutListener)
                        addMacro('Auto Feint', self.autoFeintToggle, autofeint.autoFeintListener)
                        addMacro('Flash Map', self.FlashMapToggle, flashmap.flashMapListener)                            
        
                else:
                        print('start')
                        try:
                                for thread in self.threads:
                                        thread.stop()
                                        print('stopped ' + thread.__class__.__name__)
                                self.threads = []  # Clear thread list
                                print('RAN')
                        except Exception as e:
                                print(f'Error stopping {thread}: {e}')

        def show_toast(title='', text=''):
                # configurations
                toast = Toast(self.centralwidget)
                toast.setStayOnTop(True)
                toast.setDuration(3000)  # 3 seconds
                toast.setTitle(title)
                toast.setText(text)
                
                # style preset
                toast.applyPreset(ToastPreset.SUCCESS)

                # background color
                toast.setBackgroundColor(QColor("#333333"))  # Use QColor instead of string
                
                # stylesheet
                toast.setStyleSheet("""
                QWidget {
                        background-color: #333333;  /* Dark gray background */
                        border: 0px solid #555555;  /* Light gray border */
                        border-radius: 5px;         /* Rounded corners */
                        color: #ffffff
                }
                
                """)

                # Show the toast
                toast.setTitleColor(QColor("#D3D3D3"))
                toast.setTextColor(QColor("#D3D3D3"))
                toast.setCloseButtonIconColor(QColor("#ff073a"))
                toast.setBorderRadius(5)
                toast.show()
        self.RunToggle.toggled.connect(runToggle)
        def notifs():
                dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                settingsPath = os.path.join(dataLocation, 'data/Settings.json')
                with open(settingsPath) as f:
                        currentSettings = json.load(f)
                if currentSettings['notifs']:
                        if self.RunToggle._is_checked == 2:
                               show_toast(title='Macro activated!')
                        elif self.RunToggle._is_checked == 0:
                               show_toast(title='Macro disabled.')
                else:
                       print('no')
        self.RunToggle.toggled.connect(notifs)
        def toggling():
                def on_key(event):
                        if event.name == self.plainTextEdit_17.toPlainText():
                                print('toggling the toggle')
                                if self.RunToggle._is_checked == 2:
                                        self.RunToggle.setChecked(False)
                                elif self.RunToggle._is_checked == 0:
                                        self.RunToggle.setChecked(True)
                
                # Register the key press handler ONCE outside the on_key function
                keyboard.on_press(on_key)
                
                # Keep the thread alive
                while True:
                        sleep(0.1)  # Prevent high CPU usage

        def startStopToggling():
                global t1  # Make thread accessible globally
                if self.RunKeybindToggle._is_checked == 2:
                        t1 = threading.Thread(target=toggling)
                        t1.daemon = True
                        t1.start()
                elif self.RunKeybindToggle._is_checked == 0:
                        print('disabling!')
                        # Unregister all keyboard handlers when stopping
                        keyboard.unhook_all()

        self.RunKeybindToggle.toggled.connect(startStopToggling)


        
        #! saving mechanism (fuck this)

        def saveCurrentData(number):

                currentData = {}
                def saveMacro(currentData, toggleName, params=None, elements=None):
                        element = getattr(self, toggleName)
                        if element._is_checked == 2:
                                currentData[toggleName] = True
                                if params and elements:
                                       for i in range(len(params)):
                                              parameterName = params[i]
                                              elementName = getattr(self, elements[i])
                                              currentData[parameterName] = elementName.toPlainText()
                        else:
                                currentData[toggleName] = False
                        
                       
                #!bells
                if self.BellMovestackToggle._is_checked == 2:
                        currentData['BellMovestackToggle'] = True
                        currentData['MovestackChoice'] = self.MovestackChoice.currentIndex()
                else:
                       currentData['BellMovestackToggle'] = False

                #!mantras
                if self.RitualCastToggle._is_checked == 2:
                       currentData['RitualCastToggle'] = True
                       currentData['ritualCastPing'] = self.plainTextEdit_10.toPlainText()
                       currentData['screenResolution'] = self.screenResolution.currentIndex()
                       currentData['screenScale'] = self.screenScale.currentIndex()
                else:
                       currentData['RitualCastToggle'] = False

                saveMacro(currentData, 'mantraVariantToggle', params=['AutoMantraVariantsKeysArea'], elements=['AutoMantraVariantsKeysArea'])
                saveMacro(currentData, 'mantraTechSlidetoggle', params=['mantraTechSlidetoggleKeysArea'], elements=['plainTextEdit_2'])
                saveMacro(currentData, 'mantraTechRollToggle', params=['mantraTechRollToggleKeysArea'], elements=['plainTextEdit_3'])

                #!weapons

                saveMacro(currentData, 'AirDashToggle')
                saveMacro(currentData, 'HoldM1Toggle')
                saveMacro(currentData, 'MotifSwapToggle', params=['MotifHotkeyArea', 'MotifToolbarNumberArea', 'MotifWeaponNumberArea'], elements=['MotifHotkeyArea', 'MotifToolbarNumberArea', 'plainTextEdit_7'])
                saveMacro(currentData, 'uppercutToggle')
                saveMacro(currentData, 'uppercutDynamicToggle')
                saveMacro(currentData, 'autoFeintToggle')

                #! misc

                saveMacro(currentData, 'MbAllToggle', params=['MbAllHotkeyArea'], elements=['MbAllHotkeyArea'])
                saveMacro(currentData, 'GoldenTongueToggle', params=['GoldenTongueHotkeyArea', 'GoldenTongueTextArea'], elements=['GoldenTongueHotkeyArea', 'plainTextEdit_6'])
                saveMacro(currentData, 'GankPingerToggle', params=['GankPingerHotkey', 'webhook_url', 'message', 'username', 'avatar_url', 'ScreenshotToggle'], elements=['plainTextEdit_15', 'plainTextEdit', 'plainTextEdit_12', 'plainTextEdit_13', 'plainTextEdit_14'])

                #! progresssion

                saveMacro(currentData, 'CharismaAutofillToggle')
                saveMacro(currentData, 'AutoFortitudeToggle', params=['BoulderTrainingHotkey'], elements=['BoulderTrainingHotkey'])
                saveMacro(currentData, 'AutoWillpowerToggle', params=['WillpowerTrainingHotkey'], elements=['WillpowerTrainingHotkey'])
                saveMacro(currentData, 'AutoAgilityToggle', params=['AnkleWeightsTrainingHotkey'], elements=['AnkleWeightsTrainingHotkey'])

                dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                filename = os.path.join(dataLocation, f'data/Preset{number}Data.json')
                try:
                        # Create the file if it doesn't exist
                        with open(filename, 'x') as f:
                                json.dump({}, f)  # create empty JSON object
                except FileExistsError:
                        print('file already exists')
                #!running

                saveMacro(currentData, 'RunKeybindToggle', params=['RunKeybindToggleKeybind'], elements=['plainTextEdit_17'])

                # Write the current data
                with open(filename, 'w') as f:
                        json.dump(currentData, f)
                

        def loadData(number):
                #!opening fiel
                dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                filepath = os.path.join(dataLocation, f'data/Preset{number}Data.json')
                with open(filepath) as f:
                        savedData = json.load(f)
                def loadMacro(savedData, name, elementName=None, elementData = None): # generic loader for most toggles
                        toggle = getattr(self, name)
                        if savedData[name]:
                                toggle.setChecked(True)
                                if elementName and elementData:
                                        for i in range(len(elementName)):
                                                try:
                                                        nameOfElement = elementName[i]
                                                        dataOfElement = elementData[i] # location of element data in json
                                                except:
                                                        print('macro fields not filled out properly')
                                                element = getattr(self, nameOfElement)
                                                element.setPlainText(str(savedData[dataOfElement]))
                                return True
                        elif not savedData[name]:
                                toggle.setChecked(False)
                                return False
                        #load toggle data if applicable

                #!bells

                if savedData['BellMovestackToggle']: # can't pass element data here bc of combobox
                        self.BellMovestackToggle.setChecked(True)
                        self.MovestackChoice.setCurrentIndex(int(savedData['MovestackChoice']))
                elif not savedData['BellMovestackToggle']:
                       self.BellMovestackToggle.setChecked(False)

                if savedData['RitualCastToggle']:
                       self.RitualCastToggle.setChecked(True)
                       self.screenScale.setCurrentIndex(int(savedData['screenScale']))
                       self.screenResolution.setCurrentIndex(int(savedData['screenResolution']))
                       self.plainTextEdit_10.setPlainText(str(savedData['ritualCastPing']))
                else:
                       self.RitualCastToggle.setChecked(False)
                loadMacro(savedData, 'mantraVariantToggle', ['AutoMantraVariantsKeysArea'], ['AutoMantraVariantsKeysArea'])
                loadMacro(savedData, 'mantraTechRollToggle', ['plainTextEdit_3'], ['mantraTechRollToggleKeysArea'])
                loadMacro(savedData, 'mantraTechSlidetoggle', ['plainTextEdit_2'], ['mantraTechSlidetoggleKeysArea'])

                #!weapons

                loadMacro(savedData, 'HoldM1Toggle')
                loadMacro(savedData, 'AirDashToggle')
                loadMacro(savedData, 'uppercutDynamicToggle')
                loadMacro(savedData, 'uppercutToggle')
                loadMacro(savedData, 'autoFeintToggle')
                loadMacro(savedData, 'MotifSwapToggle', ['MotifHotkeyArea', 'MotifToolbarNumberArea', 'plainTextEdit_7'], ['MotifHotkeyArea', 'MotifToolbarNumberArea', 'MotifWeaponNumberArea'])

                #!misc
                loadMacro(savedData, 'MbAllToggle')
                loadMacro(savedData, 'GoldenTongueToggle', ['GoldenTongueHotkeyArea', 'plainTextEdit_6'], ['GoldenTongueHotkeyArea', 'GoldenTongueTextArea'])

                if loadMacro(savedData, 'GankPingerToggle', ['plainTextEdit_15', 'plainTextEdit', 'plainTextEdit_12', 'plainTextEdit_13', 'plainTextEdit_14'], ['GankPingerHotkey', 'webhook_url', 'message', 'username', 'avatar_url']):
                        loadMacro(savedData, 'ScreenshotToggle')
                
                       
                #!progression

                loadMacro(savedData, 'CharismaAutofillToggle')
                loadMacro(savedData, 'AutoFortitudeToggle', ['BoulderTrainingHotkey'],['BoulderTrainingHotkey'])
                loadMacro(savedData, 'AutoWillpowerToggle', ['WillpowerTrainingHotkey'], ['WillpowerTrainingHotkey'])
                loadMacro(savedData, 'AutoAgilityToggle', ['AnkleWeightsTrainingHotkey'], ['AnkleWeightsTrainingHotkey'])
                
                #!running
                loadMacro(savedData, 'RunKeybindToggle', ['plainTextEdit_17'], ['RunKeybindToggleKeybind'])
                

                
        self.Preset1Save.clicked.connect(lambda:saveCurrentData(1))
        self.Preset1Load.clicked.connect(lambda:loadData(1))

        self.Preset2Save.clicked.connect(lambda:saveCurrentData(2))
        self.Preset2Load.clicked.connect(lambda:loadData(2))

        self.Preset3Save.clicked.connect(lambda:saveCurrentData(3))
        self.Preset3Load.clicked.connect(lambda:loadData(3))

        self.Preset4Save.clicked.connect(lambda:saveCurrentData(4))
        self.Preset4Load.clicked.connect(lambda:loadData(4))

        self.Preset5Save.clicked.connect(lambda:saveCurrentData(5))
        self.Preset5Load.clicked.connect(lambda:loadData(5))

        self.Preset6Save.clicked.connect(lambda:saveCurrentData(6))
        self.Preset6Load.clicked.connect(lambda:loadData(6))

        self.Preset7Save.clicked.connect(lambda:saveCurrentData(7))
        self.Preset7Load.clicked.connect(lambda:loadData(7))

        self.Preset8Save.clicked.connect(lambda:saveCurrentData(8))
        self.Preset8Load.clicked.connect(lambda:loadData(8))

        self.Preset9Save.clicked.connect(lambda:saveCurrentData(9))
        self.Preset9Load.clicked.connect(lambda:loadData(9))

        self.Preset10Save.clicked.connect(lambda:saveCurrentData(10))
        self.Preset10Load.clicked.connect(lambda:loadData(10))        
        def CheckNames():
                dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                filename = os.path.join(dataLocation, 'data/PresetNames.json')
                with open(filename) as f:
                        presetNames = json.load(f)
                self.Preset1Name.setText(presetNames['Preset1Name'])
                self.Preset2Name.setText(presetNames['Preset2Name'])
                self.Preset3Name.setText(presetNames['Preset3Name'])
                self.Preset4Name.setText(presetNames['Preset4Name'])
                self.Preset5Name.setText(presetNames['Preset5Name'])
                self.Preset6Name.setText(presetNames['Preset6Name'])
                self.Preset7Name.setText(presetNames['Preset7Name'])
                self.Preset8Name.setText(presetNames['Preset8Name'])
                self.Preset9Name.setText(presetNames['Preset9Name'])
                self.Preset10Name.setText(presetNames['Preset10Name'])
        CheckNames()

        def NameEditor(number):
                preset_widget = getattr(self, f"Preset{number}Name")
                preset_widget.setEnabled(True)
                preset_widget.setReadOnly(False)
                # Select all text and set focus
                preset_widget.setFocus()
                preset_widget.selectAll()
        
                def on_focus_lost(event):
                        preset_widget.setEnabled(False)
                        preset_widget.setReadOnly(True)
                        dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                        filename = os.path.join(dataLocation, 'data/PresetNames.json')
                        with open(filename) as f:
                                prevData = json.load(f)
                                varname = f'Preset{number}Name'
                                prevData[varname] = preset_widget.text()
                                f.close()
                        with open(filename, 'w') as f:
                                json.dump(prevData, f)
        
                preset_widget.focusOutEvent = on_focus_lost

        self.Preset1EditName.clicked.connect(lambda:NameEditor(1))
        self.Preset2EditName.clicked.connect(lambda:NameEditor(2))
        self.Preset3EditName.clicked.connect(lambda:NameEditor(3))
        self.Preset4EditName.clicked.connect(lambda:NameEditor(4))
        self.Preset5EditName.clicked.connect(lambda:NameEditor(5))
        self.Preset6EditName.clicked.connect(lambda:NameEditor(6))
        self.Preset7EditName.clicked.connect(lambda:NameEditor(7))
        self.Preset8EditName.clicked.connect(lambda:NameEditor(8))
        self.Preset9EditName.clicked.connect(lambda:NameEditor(9))
        self.Preset10EditName.clicked.connect(lambda:NameEditor(10))
        # Starting the thread (inside some class or context)