from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys

class QtVideoPlayer(QWidget):
    def __init__(self,parent = None):
        super(QtVideoPlayer,self).__init__(parent)
        self.setStyleSheet('background-color: black;')
        self.vWidget = QVideoWidget() #mediaplayer will be displayed here
        self.mPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface) #create mediaplayer
        self.mPlayer.setVideoOutput(self.vWidget)

        self.mainLayout = QVBoxLayout() #create main layout

        self.mainLayout.addWidget(self.vWidget) #add Video Widget in main Layout

        self.setLayout(self.mainLayout) #set main layout


if __name__ == '__main__':

    myapp=QApplication(sys.argv)
    myplayer=QtVideoPlayer()
    myplayer.resize(640,480)
    myplayer.show()

    sys.exit(myapp.exec_())
                      
