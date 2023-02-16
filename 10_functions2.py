# Напишите здесь свой код :-)
def create_hw_list(model, role, status):
    """CREATE RECORDS"""
    record = {
        'model': model,
        'role': role,
        'status': status
    }
    return record


spb_gw = create_hw_list("Cisco4331", "router", "free")
krak_gw = create_hw_list("Cisco4451", "router", "in use")
lviv_sw = create_hw_list("Cisco2960X", "switch", "free")

print(spb_gw)
print(krak_gw)

def upload_cert(cert, *devices):
    for device in devices:
        print("CERTIFICATE " + cert + " has been uloaded to the " + device + " device")

upload_cert("hw.atffc.hui", "spb_gw")

upload_cert("vm.atffc.hui", "spb_gw", "krak_gw")
