import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfail import Ui_MainWindow  # đổi đúng tên file pyuic5 tạo ra
import requests

class PlayfairApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_Matrix.clicked.connect(self.call_api_create_matrix)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data["encrypted_text"])
                QMessageBox.information(self, "Thông báo", "Mã hóa thành công")
            else:
                QMessageBox.warning(self, "Lỗi", "Lỗi khi gọi API mã hóa")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data["decrypted_text"])
                QMessageBox.information(self, "Thông báo", "Giải mã thành công")
            else:
                QMessageBox.warning(self, "Lỗi", "Lỗi khi gọi API giải mã")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối: {str(e)}")

    def call_api_create_matrix(self):
        url = "http://127.0.0.1:5000/api/playfair/matrix"
        payload = {
            "key": self.ui.txt_key_matrix.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_maxtrix_text.setText(data["matrix"])
                QMessageBox.information(self, "Thông báo", "Tạo ma trận thành công")
            else:
                QMessageBox.warning(self, "Lỗi", "Lỗi khi tạo ma trận")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayfairApp()
    window.show()
    sys.exit(app.exec_())
