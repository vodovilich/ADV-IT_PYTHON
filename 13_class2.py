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

################### EXTENDED CLASS ######################
# parent class is called Super[Class]
class SuperDevice(device):
    """Class to create a SuperDevice"""
    def __init__(self, name, status, ser_num, license):
        """initiate a SuperDevice"""
        super().__init__(name, status, ser_num)
        self.license = license
        self.slaves = 25

    def enslave_ap(self):
        """Connect an AP"""
        self.slaves -=1

    def show_device(self):
        description = (self.name + " is " + self.stts + " SN: " + str(self.sn) + " Free licenses: " + str(self.slaves))
        print(description)

###########################--MAIN--##########################################



device1 = device("gw01", "free", "101")
wlc = SuperDevice("wlc01", "in use", "232", "5")

device1.show_device()
wlc.show_device()

print("\nAP joined the WLC!!!\n")
wlc.enslave_ap()
wlc.show_device()





print("ty ne pidor")