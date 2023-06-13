import pyfirmata 
import time


class Arduino:
    last_activation: time.time = 0
    off_time = 3
    active_time = 0.8
    port = '/dev/ttyUSB0' 
    board = pyfirmata.Arduino(port)

    def __init__(self, pin_id = 11):
        self.pin = self.board.get_pin(f"d:{pin_id}:p")
        self.pin.write(0.5)
        self.turned_on = False


    def activate(self, p=0.9):
        print("Activating...")
        self.last_activation = time.time()
        self.pin.write(p)
        self.turned_on = True
        
    def deactivate(self):
        print("Deactivating...")
        self.pin.write(0.5)
        self.turned_on = False
    
    def run(self, activate=False):
        # checks if it's in middle of process
        time_elapsed = time.time() - self.last_activation
        if time_elapsed < (self.active_time + self.off_time):
            # checks if it's time to deactivate
            if self.turned_on and time_elapsed > self.active_time:
                self.deactivate()

        elif activate:
            self.activate()
            

if __name__ == '__main__':

    ard = Arduino()
    while True:
        # i = float(input("Activate: "))

        t = float(input("Time: "))
        ard.activate(0.9)
        ard.board.pass_time(t)
        # time.sleep(t)
        ard.activate(0.5)
        print("here!")

