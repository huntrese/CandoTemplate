# gui.py
import sys
import threading
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class LiveReloadWebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.reload_page)
        self.timer.start(2000)  # Refresh every 2 seconds (adjust as needed)

    def reload_page(self):
        self.runJavaScript("location.reload();")

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser with Live Reload")
        self.setGeometry(1000, 100, 1024, 768)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        self.browser = QWebEngineView(self)
        layout.addWidget(self.browser)
        self.browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Create a custom QWebEnginePage with live reload
        self.page = LiveReloadWebPage(self.browser)
        self.browser.setPage(self.page)

        # Load the web page
        self.load_web_page()

    def load_web_page(self):
        url = QUrl("http://localhost/index.php")
        self.browser.setUrl(url)

def run_browser():
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec_())

def run_browser_in_thread():
    browser_thread = threading.Thread(target=run_browser)
    browser_thread.start()

if __name__ == "__main__":
    run_browser_in_thread()
