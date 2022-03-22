from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

import sys

class QtVideoPlayer(QWidget):
    def __init__(self,parent = None):
        super(QtVideoPlayer,self).__init__(parent)
        self.setWindowTitle("My Media Player Demo") #set window title
        self.vWidget = QVideoWidget() #mediaplayer will be displayed here
        self.mPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface) #create mediaplayer
        self.mPlayer.setVideoOutput(self.vWidget) #set mediaplayer Video Output
        self.vWidget.setStyleSheet('background-color: black;')

        self.mainLayout = QVBoxLayout() #create main layout
        self.commandLayout = QHBoxLayout() #create HBoxLayout for insert commands
        

        self.openFileBtn = QPushButton("Select Video File") #create button for select file
        self.openFileBtn.clicked.connect(self.selectFile) #connect openFileBtn clicked

        self.commandLayout.addWidget(self.openFileBtn) #add openFileBtn in commandLayout
        
        
        self.mainLayout.addWidget(self.vWidget) #add Video Widget in main Layout
        self.mainLayout.addLayout(self.commandLayout) #add commandLayout in main Layout

        self.setLayout(self.mainLayout) #set main layout

    def selectFile(self):
        filesTypes = "MPEG-4 Video File (*.mp4);;Audio Video Interleave File (*.avi);;Matroska Video File (*.mkv);;MPEG Video (*.mpeg);;Windows Media Video (*.wmv);;MPEG Video File (*.mpg);;All Files (*.*)"
        self.fileName = QFileDialog.getOpenFileName(self, "Select and Open Video", "/",filesTypes)[0] #open file dialog
        if self.fileName != '':
            self.mPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.fileName))) #set mediaplayer file


if __name__ == '__main__':

    myapp=QApplication(sys.argv) #create application
    myplayer=QtVideoPlayer() #create mediaplayer object
    myplayer.resize(640,480) #set size of mediaplayer object
    myplayer.show() #show mediaplayer object

    sys.exit(myapp.exec_())
                      
