import threading

class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.Lock()
        self.event = threading.Event()
