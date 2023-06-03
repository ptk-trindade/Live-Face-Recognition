import pyfirmata 
import time


class Arduino:
    last_activation: time.time = 0
    activation_interval = 3
    active_time = 3
    pin = 13 # output pin
    port = '/dev/ttyUSB0' 
    board = pyfirmata.Arduino(port)

    def __init__(self):
        self.board.digital[self.pin].write(0)
        self.turned_on = False

    def analog_write(self, value):
        # self.board.digital[pin].write(value)
        pin = self.board.get_pin(f'd:13:p')
        pin.write(value)

    def activate(self):
        if (time.time() - self.last_activation) > (self.activation_interval + self.active_time):
            print("Activating...")
            self.last_activation = time.time()
            self.board.digital[self.pin].write(1)
            self.turned_on = True
        else:
            print("Not activating...")

    def deactivate(self):
        if self.turned_on == False:
            print("Do nothing...")
            return
            
        print("Deactivating...")
        self.board.digital[self.pin].write(0)
        self.turned_on = False
    
    def run(self, activate=False):
        if activate:
            self.activate()
        else:
            self.deactivate()


if __name__ == '__main__':

    ard = Arduino()
    while True:
        i = float(input("Activate: "))
        if i == 0.0:
            ard.run(activate=True)
        elif i == 1.0:
            ard.run(activate=False)
        elif i > 1.0:
            break
        else:
            ard.analog_write(i)

