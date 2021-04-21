import sys

stdout = []
parking = []
leave = []
len_nop = 0
class parking_lot:
    def __init__(self, park_car, leave_car, len_nop):
        self.park_car = park_car
        self.leave_car = leave_car
        self.len_nop = int(len_nop)
    def listData(self):
        # getIndexStatus = stdout
        stdout.append("Slot No.1   Registration No.")
        for i in range(len(parking)):
            data = "{}  {}".format(i+1,parking[i])
            stdout.append(data.strip())            
            
    def addData(self):
        # print(len(parking))
        if "free" in parking:
            idxParkFree = parking.index("free")
            parking[idxParkFree] = self.park_car
            stdout.append("Allocated  slot  number: {}".format(idxParkFree+1))
        elif len(parking) < self.len_nop: 
            parking.append(self.park_car)
            indexPark = parking.index(self.park_car)
            stdout.append("Allocated  slot  number: {}".format(indexPark+1))
        elif len(parking) > self.len_nop:
            stdout.append("Sorry, parking lot is full")
    def remove(self, find = 0):
        no_car_leave = self.leave_car[1]               
        if no_car_leave in parking:
            idx = parking.index(no_car_leave)
            if int(self.leave_car[2]) <= 2:
                charge = 10
            elif int(self.leave_car[2]) > 2:
                charge = 10 + ((int(self.leave_car[2])-2)*10)
            
            find=1
            stdout.append("Registration number {} with Slot Number {} is free with Charge ${}"
                  .format(self.leave_car[1], idx+1, charge))
            parking[idx] = "free"
        elif find != 1:
            stdout.append("Registration number {} notfound".format(no_car_leave))
                
def inputDataFile():
    print("==============input==============")
    readSet = open("setting.txt","r")
    locInput = readSet.readline()
    readInput = open(locInput, "r")
    strLen_nop = readInput.readline().strip()
    print(strLen_nop)
    arrlen_nop = strLen_nop.split(" ")
    if arrlen_nop[0] == "create_parking_lot":
        len_nop = arrlen_nop[1]
        stdout.append("Create parking lot with : {}".format(len_nop))
    else:
        sys.exit("Ensure capacity of parking area")
    for x in readInput:
        print(x.strip())
        arrinp = x.strip().split(" ")
        if arrinp[0] == "status":
            parking_slot = parking_lot(parking, leave, len_nop)
            parking_slot.listData()
        elif arrinp[0] == "park":
            parking_slot = parking_lot(arrinp[1].strip(), leave, len_nop)
            parking_slot.addData()
            # x=arrinp[1]
            # parking.append(apprn)
        elif arrinp[0] == "leave":
            # leave.append(arrinp)
            parking_slot = parking_lot(parking, arrinp, len_nop)
            parking_slot.remove()
        # return parking, leave, len_nop, list_data
inputDataFile()
print("=============output=============")
for x in stdout:
    if x != "free":
        print(x)