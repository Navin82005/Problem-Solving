import threading

LOCKED_BY = None

def thread01():
    if not LOCKED_BY or LOCKED_BY == 1:
        LOCKED_BY = 1
        while True:
            print("Log from thread 01 ")

def thread02():
    if not LOCKED_BY or LOCKED_BY == 2:
        LOCKED_BY = 2
        while True:
            print("Log from thread 02 ")



if __name__ == "__main__":
    threading.Thread(target=thread01, daemon=True).start()
    threading.Thread(target=thread02, daemon=True).start()
    while True:
        print("Log from main thread ")