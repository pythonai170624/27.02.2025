import weakref

class StockGrabber:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        # Store a weak reference to the observer
        self._observers.append(weakref.ref(observer))

    def notify(self, message):
        for ref in self._observers:
            observer = ref()
            if observer is not None:
                observer.update(message)

class Observer:
    def update(self, message):
        print("Observer received:", message)

stock_grabber = StockGrabber()
observer = Observer()

stock_grabber.add_observer(observer)
stock_grabber.notify("Hello, Observers!")

# Remove the strong reference to observer:
del observer

# Force garbage collection to show that the observer can now be collected:
import gc
gc.collect()

print("Notifying after observer deletion:")
stock_grabber.notify("This message should not be received if observer was collected.")
