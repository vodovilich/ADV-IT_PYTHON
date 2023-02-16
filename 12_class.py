
print("ty pidor")


class device():
    """Class to create a device"""
#functions in classes are called METHODS
#first method in a class is always __init__

    def __init__(self, name, status, ser_num):
        """initiate our device"""
        self.name = name
        self.stts = status
        self.sn = ser_num

    def show_device(self):
        """print all parameters of this device"""
        description = (self.name + " is " + self.stts + " SN: " + str(self.sn))
        print(description)

    def to_stock (self):
        """place a device to storage"""
        self.stts = "free"

    def set_sn(self):
        """set device's serial number"""
        self.sn = input("Enter Serial Number: ")
        print("Serial number set to " + self.sn)
###########################--MAIN--##########################################
device1 = device("gw01", "in use", 123)
device2 = device("sw02", "in use", 223)

device1.show_device()
device2.show_device()

print("move dev2 to stock")
device2.to_stock()
device2.show_device()

print("let's set device1 SN!")
device1.set_sn()

print("ty ne pidor")

#parameters can be modified manually, but it is better to do so via methods.