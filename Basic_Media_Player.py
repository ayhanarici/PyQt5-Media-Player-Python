
class QtVideoPlayer(QWidget)
    def __init__(self,parent=None):
        super(QtMediaPlayer,self).__init__(parent)
        self.vWidget=QVideoWidget() #mediaplayer will be displayed here
        self.mPlayer=(QMediaPlayer(None, QMediaPlayer.VideoSurface)#create mediaplayer
