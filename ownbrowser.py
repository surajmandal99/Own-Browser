
import sys
from turtle import forward
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtWebEngineWidgets import*
"""PyQtWebEngine is a set of Python bindings for The Qt Company’s Qt WebEngine framework.
 The framework provides the ability to embed web content in applications and is based on the Chrome browser. 
 The bindings sit on top of PyQt5 and are implemented as three separate modules corresponding to the different libraries that make up the framework."""
"""PyQt5 is cross-platform GUI toolkit,
 a set of python bindings for Qt v5. One can develop an interactive desktop application with so much ease because
 of the tools and simplicity provided by this library."""

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.co.in/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #nav bar
        navbar=QToolBar()
        self.addToolBar(navbar)
        back_btn=QAction("Back",self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn=QAction("Forward",self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn=QAction("Relod",self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn=QAction("Home",self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)


    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.co.in/"))
    
    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())



app=QApplication(sys.argv)
QApplication.setApplicationName("My own fucking browser!")
window=MainWindow()
app.exec_()
