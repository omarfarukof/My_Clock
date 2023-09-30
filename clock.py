import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton, QLabel, QFrame
from PyQt5.QtCore import QTimer, Qt

class TimerClock(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Timer Clock')
        self.setGeometry(100, 100, 300, 300)

        # Create a vertical layout
        layout = QVBoxLayout()

        # Create a progress bar
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)
        layout.addWidget(self.progressBar)

        # Create a label for the completion status
        self.statusLabel = QLabel('0%')
        self.statusLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.statusLabel)

        # Create a start button
        self.startButton = QPushButton('Start')
        self.startButton.clicked.connect(self.startTimer)
        layout.addWidget(self.startButton)

        # Set the layout for the window
        self.setLayout(layout)

        # Set the timer interval in milliseconds
        self.timerInterval = 1000

        # Create a timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTimer)

    def startTimer(self):
        self.timer.start(self.timerInterval)

    def updateTimer(self):
        # Update the progress bar and status label
        value = self.progressBar.value() + 10
        self.progressBar.setValue(value)
        self.statusLabel.setText(f'{value}%')

        # Stop the timer when the progress bar is full
        if value >= 100:
            self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = TimerClock()
    clock.show()
    sys.exit(app.exec_())