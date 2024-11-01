from ctypes import windll

def clear_clipboard():
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()

clear_clipboard()
