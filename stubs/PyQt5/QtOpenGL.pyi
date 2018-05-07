# The PEP 484 type hints stub file for the QtOpenGL module.
#
# Generated by SIP 4.19.8
#
# Copyright (c) 2017 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QGL(sip.simplewrapper):

    class FormatOption(int): ...
    DoubleBuffer = ... # type: 'QGL.FormatOption'
    DepthBuffer = ... # type: 'QGL.FormatOption'
    Rgba = ... # type: 'QGL.FormatOption'
    AlphaChannel = ... # type: 'QGL.FormatOption'
    AccumBuffer = ... # type: 'QGL.FormatOption'
    StencilBuffer = ... # type: 'QGL.FormatOption'
    StereoBuffers = ... # type: 'QGL.FormatOption'
    DirectRendering = ... # type: 'QGL.FormatOption'
    HasOverlay = ... # type: 'QGL.FormatOption'
    SampleBuffers = ... # type: 'QGL.FormatOption'
    SingleBuffer = ... # type: 'QGL.FormatOption'
    NoDepthBuffer = ... # type: 'QGL.FormatOption'
    ColorIndex = ... # type: 'QGL.FormatOption'
    NoAlphaChannel = ... # type: 'QGL.FormatOption'
    NoAccumBuffer = ... # type: 'QGL.FormatOption'
    NoStencilBuffer = ... # type: 'QGL.FormatOption'
    NoStereoBuffers = ... # type: 'QGL.FormatOption'
    IndirectRendering = ... # type: 'QGL.FormatOption'
    NoOverlay = ... # type: 'QGL.FormatOption'
    NoSampleBuffers = ... # type: 'QGL.FormatOption'
    DeprecatedFunctions = ... # type: 'QGL.FormatOption'
    NoDeprecatedFunctions = ... # type: 'QGL.FormatOption'

    class FormatOptions(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QGL.FormatOptions', 'QGL.FormatOption']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QGL.FormatOptions') -> None: ...

        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QGL.FormatOptions': ...
        def __int__(self) -> int: ...


class QGLFormat(sip.simplewrapper):

    class OpenGLContextProfile(int): ...
    NoProfile = ... # type: 'QGLFormat.OpenGLContextProfile'
    CoreProfile = ... # type: 'QGLFormat.OpenGLContextProfile'
    CompatibilityProfile = ... # type: 'QGLFormat.OpenGLContextProfile'

    class OpenGLVersionFlag(int): ...
    OpenGL_Version_None = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_1_1 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_1_2 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_1_3 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_1_4 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_1_5 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_2_0 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_2_1 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_3_0 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_3_1 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_3_2 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_3_3 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_4_0 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_4_1 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_4_2 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_4_3 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_ES_Common_Version_1_0 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_ES_CommonLite_Version_1_0 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_ES_Common_Version_1_1 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_ES_CommonLite_Version_1_1 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_ES_Version_2_0 = ... # type: 'QGLFormat.OpenGLVersionFlag'

    class OpenGLVersionFlags(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QGLFormat.OpenGLVersionFlags', 'QGLFormat.OpenGLVersionFlag']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QGLFormat.OpenGLVersionFlags') -> None: ...

        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QGLFormat.OpenGLVersionFlags': ...
        def __int__(self) -> int: ...

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, options: typing.Union[QGL.FormatOptions, QGL.FormatOption], plane: int = ...) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGLFormat') -> None: ...

    def profile(self) -> 'QGLFormat.OpenGLContextProfile': ...
    def setProfile(self, profile: 'QGLFormat.OpenGLContextProfile') -> None: ...
    def minorVersion(self) -> int: ...
    def majorVersion(self) -> int: ...
    def setVersion(self, major: int, minor: int) -> None: ...
    @staticmethod
    def openGLVersionFlags() -> 'QGLFormat.OpenGLVersionFlags': ...
    def swapInterval(self) -> int: ...
    def setSwapInterval(self, interval: int) -> None: ...
    def blueBufferSize(self) -> int: ...
    def setBlueBufferSize(self, size: int) -> None: ...
    def greenBufferSize(self) -> int: ...
    def setGreenBufferSize(self, size: int) -> None: ...
    def redBufferSize(self) -> int: ...
    def setRedBufferSize(self, size: int) -> None: ...
    def sampleBuffers(self) -> bool: ...
    def hasOverlay(self) -> bool: ...
    def directRendering(self) -> bool: ...
    def stereo(self) -> bool: ...
    def stencil(self) -> bool: ...
    def accum(self) -> bool: ...
    def alpha(self) -> bool: ...
    def rgba(self) -> bool: ...
    def depth(self) -> bool: ...
    def doubleBuffer(self) -> bool: ...
    @staticmethod
    def hasOpenGLOverlays() -> bool: ...
    @staticmethod
    def hasOpenGL() -> bool: ...
    @staticmethod
    def setDefaultOverlayFormat(f: 'QGLFormat') -> None: ...
    @staticmethod
    def defaultOverlayFormat() -> 'QGLFormat': ...
    @staticmethod
    def setDefaultFormat(f: 'QGLFormat') -> None: ...
    @staticmethod
    def defaultFormat() -> 'QGLFormat': ...
    def testOption(self, opt: typing.Union[QGL.FormatOptions, QGL.FormatOption]) -> bool: ...
    def setOption(self, opt: typing.Union[QGL.FormatOptions, QGL.FormatOption]) -> None: ...
    def setPlane(self, plane: int) -> None: ...
    def plane(self) -> int: ...
    def setOverlay(self, enable: bool) -> None: ...
    def setDirectRendering(self, enable: bool) -> None: ...
    def setStereo(self, enable: bool) -> None: ...
    def setStencil(self, enable: bool) -> None: ...
    def setAccum(self, enable: bool) -> None: ...
    def setAlpha(self, enable: bool) -> None: ...
    def setRgba(self, enable: bool) -> None: ...
    def setDepth(self, enable: bool) -> None: ...
    def setDoubleBuffer(self, enable: bool) -> None: ...
    def samples(self) -> int: ...
    def setSamples(self, numSamples: int) -> None: ...
    def setSampleBuffers(self, enable: bool) -> None: ...
    def stencilBufferSize(self) -> int: ...
    def setStencilBufferSize(self, size: int) -> None: ...
    def alphaBufferSize(self) -> int: ...
    def setAlphaBufferSize(self, size: int) -> None: ...
    def accumBufferSize(self) -> int: ...
    def setAccumBufferSize(self, size: int) -> None: ...
    def depthBufferSize(self) -> int: ...
    def setDepthBufferSize(self, size: int) -> None: ...


class QGLContext(sip.wrapper):

    class BindOption(int): ...
    NoBindOption = ... # type: 'QGLContext.BindOption'
    InvertedYBindOption = ... # type: 'QGLContext.BindOption'
    MipmapBindOption = ... # type: 'QGLContext.BindOption'
    PremultipliedAlphaBindOption = ... # type: 'QGLContext.BindOption'
    LinearFilteringBindOption = ... # type: 'QGLContext.BindOption'
    DefaultBindOption = ... # type: 'QGLContext.BindOption'

    class BindOptions(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QGLContext.BindOptions', 'QGLContext.BindOption']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QGLContext.BindOptions') -> None: ...

        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QGLContext.BindOptions': ...
        def __int__(self) -> int: ...

    def __init__(self, format: QGLFormat) -> None: ...

    def moveToThread(self, thread: QtCore.QThread) -> None: ...
    @staticmethod
    def areSharing(context1: 'QGLContext', context2: 'QGLContext') -> bool: ...
    def setInitialized(self, on: bool) -> None: ...
    def initialized(self) -> bool: ...
    def setWindowCreated(self, on: bool) -> None: ...
    def windowCreated(self) -> bool: ...
    def deviceIsPixmap(self) -> bool: ...
    def chooseContext(self, shareContext: typing.Optional['QGLContext'] = ...) -> bool: ...
    @staticmethod
    def currentContext() -> 'QGLContext': ...
    def overlayTransparentColor(self) -> QtGui.QColor: ...
    def device(self) -> QtGui.QPaintDevice: ...
    def getProcAddress(self, proc: str) -> sip.voidptr: ...
    @staticmethod
    def textureCacheLimit() -> int: ...
    @staticmethod
    def setTextureCacheLimit(size: int) -> None: ...
    def deleteTexture(self, tx_id: int) -> None: ...
    @typing.overload
    def drawTexture(self, target: QtCore.QRectF, textureId: int, textureTarget: int = ...) -> None: ...
    @typing.overload
    def drawTexture(self, point: typing.Union[QtCore.QPointF, QtCore.QPoint], textureId: int, textureTarget: int = ...) -> None: ...
    @typing.overload
    def bindTexture(self, image: QtGui.QImage, target: int = ..., format: int = ...) -> int: ...
    @typing.overload
    def bindTexture(self, pixmap: QtGui.QPixmap, target: int = ..., format: int = ...) -> int: ...
    @typing.overload
    def bindTexture(self, fileName: str) -> int: ...
    @typing.overload
    def bindTexture(self, image: QtGui.QImage, target: int, format: int, options: typing.Union['QGLContext.BindOptions', 'QGLContext.BindOption']) -> int: ...
    @typing.overload
    def bindTexture(self, pixmap: QtGui.QPixmap, target: int, format: int, options: typing.Union['QGLContext.BindOptions', 'QGLContext.BindOption']) -> int: ...
    def swapBuffers(self) -> None: ...
    def doneCurrent(self) -> None: ...
    def makeCurrent(self) -> None: ...
    def setFormat(self, format: QGLFormat) -> None: ...
    def requestedFormat(self) -> QGLFormat: ...
    def format(self) -> QGLFormat: ...
    def reset(self) -> None: ...
    def isSharing(self) -> bool: ...
    def isValid(self) -> bool: ...
    def create(self, shareContext: typing.Optional['QGLContext'] = ...) -> bool: ...


class QGLWidget(QtWidgets.QWidget):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ..., shareWidget: typing.Optional['QGLWidget'] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...
    @typing.overload
    def __init__(self, context: QGLContext, parent: typing.Optional[QtWidgets.QWidget] = ..., shareWidget: typing.Optional['QGLWidget'] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...
    @typing.overload
    def __init__(self, format: QGLFormat, parent: typing.Optional[QtWidgets.QWidget] = ..., shareWidget: typing.Optional['QGLWidget'] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...

    def glDraw(self) -> None: ...
    def glInit(self) -> None: ...
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None: ...
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None: ...
    def autoBufferSwap(self) -> bool: ...
    def setAutoBufferSwap(self, on: bool) -> None: ...
    def paintOverlayGL(self) -> None: ...
    def resizeOverlayGL(self, w: int, h: int) -> None: ...
    def initializeOverlayGL(self) -> None: ...
    def paintGL(self) -> None: ...
    def resizeGL(self, w: int, h: int) -> None: ...
    def initializeGL(self) -> None: ...
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def updateOverlayGL(self) -> None: ...
    def updateGL(self) -> None: ...
    def deleteTexture(self, tx_id: int) -> None: ...
    @typing.overload
    def drawTexture(self, target: QtCore.QRectF, textureId: int, textureTarget: int = ...) -> None: ...
    @typing.overload
    def drawTexture(self, point: typing.Union[QtCore.QPointF, QtCore.QPoint], textureId: int, textureTarget: int = ...) -> None: ...
    @typing.overload
    def bindTexture(self, image: QtGui.QImage, target: int = ..., format: int = ...) -> int: ...
    @typing.overload
    def bindTexture(self, pixmap: QtGui.QPixmap, target: int = ..., format: int = ...) -> int: ...
    @typing.overload
    def bindTexture(self, fileName: str) -> int: ...
    @typing.overload
    def bindTexture(self, image: QtGui.QImage, target: int, format: int, options: typing.Union[QGLContext.BindOptions, QGLContext.BindOption]) -> int: ...
    @typing.overload
    def bindTexture(self, pixmap: QtGui.QPixmap, target: int, format: int, options: typing.Union[QGLContext.BindOptions, QGLContext.BindOption]) -> int: ...
    def paintEngine(self) -> QtGui.QPaintEngine: ...
    @typing.overload
    def renderText(self, x: int, y: int, str: str, font: QtGui.QFont = ...) -> None: ...
    @typing.overload
    def renderText(self, x: float, y: float, z: float, str: str, font: QtGui.QFont = ...) -> None: ...
    @staticmethod
    def convertToGLFormat(img: QtGui.QImage) -> QtGui.QImage: ...
    def overlayContext(self) -> QGLContext: ...
    def makeOverlayCurrent(self) -> None: ...
    def grabFrameBuffer(self, withAlpha: bool = ...) -> QtGui.QImage: ...
    def renderPixmap(self, width: int = ..., height: int = ..., useContext: bool = ...) -> QtGui.QPixmap: ...
    def setContext(self, context: QGLContext, shareContext: typing.Optional[QGLContext] = ..., deleteOldContext: bool = ...) -> None: ...
    def context(self) -> QGLContext: ...
    def format(self) -> QGLFormat: ...
    def swapBuffers(self) -> None: ...
    def doubleBuffer(self) -> bool: ...
    def doneCurrent(self) -> None: ...
    def makeCurrent(self) -> None: ...
    def isSharing(self) -> bool: ...
    def isValid(self) -> bool: ...
    def qglClearColor(self, c: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def qglColor(self, c: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
