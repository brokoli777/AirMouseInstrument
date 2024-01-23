import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QMouseEvent, QPalette
from PyQt5.QtCore import Qt

class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle('Mouse Tracker')
        self.setGeometry(100, 100, 800, 600)  # Set initial size (will be fullscreen later)
        
        # Initialize label to display mouse position
        self.mouse_position_label = QLabel(self)
        self.mouse_position_label.setAlignment(Qt.AlignCenter)
        self.mouse_position_label.setGeometry(0, 0, self.width(), 30)

        # Set up different colored borders
        self.border_colors = [Qt.red, Qt.green, Qt.blue, Qt.yellow]
        self.current_border_color = 0
        self.update_border_color()

        # Make the window fullscreen
        self.showFullScreen()

    def update_border_color(self):
        # Update the window border color
        palette = QPalette()
        palette.setColor(QPalette.Window, self.border_colors[self.current_border_color])
        self.setPalette(palette)

    def mouseMoveEvent(self, event: QMouseEvent):
        # Update the mouse position label
        self.mouse_position_label.setText(f'Mouse Position: ({event.x()}, {event.y()})')

    def mousePressEvent(self, event: QMouseEvent):
        # Change the border color on mouse click
        self.current_border_color = (self.current_border_color + 1) % len(self.border_colors)
        self.update_border_color()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MouseTracker()
    sys.exit(app.exec_())
