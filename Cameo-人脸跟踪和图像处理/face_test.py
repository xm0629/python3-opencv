import cv2 as cv
from managers import WindowManager, CaptureManager


class Cameo(object):
    def __init__(self):
        # 创建一个窗口，并将键盘的回调函数传入
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        # 告诉程序数据来自摄像头， 还有镜面效果
        self._captureManager = CaptureManager(capture=cv.VideoCapture(0), previewWindowManager=self._windowManager, shouldMirrorPreview=True)

    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            # 这里的enterFrame就是告诉程序从摄像头中取数据
            self._captureManager.enterFrame()
            # 下面的这个frame是原始帧数据，这里没有做任何修改，后面的教程会对这个帧数据进行修改
            frame = self._captureManager._frame
            # exitFrame看起来是像是退出的意思，其实主要功能都是在这里方法里实现的，截屏、录像都是在这里
            self._captureManager.exitFrame()
            # 回调函数
            self._windowManager.processEvents()
    # 定义键盘的回调函数，用于self._windowManager.processEvents()的调用
    def onKeypress(self, keycode):
        '''
        快捷键设置：
        当按下“空格”键的时候，会进行抓屏。
        当按下‘tab’键的时候，就开始或者停止录像。
        当然相应的目录也会生成图片或者视频文件
        '''
        if keycode == 32:#space
            # 截屏保存的文件名字
            self._captureManager.writeImage('changeOnePixel.png')
        elif keycode == 9:#tab
            if not self._captureManager.isWritingVideo:
                # 告诉程序，录像保存的文件名字
                self._captureManager.startWritingVideo('record.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: #escape
            self._windowManager.destroyWindow()

if __name__=="__main__":
    Cameo().run()