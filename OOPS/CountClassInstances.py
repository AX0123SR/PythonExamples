class Instance:
    counter = 0
    def __init__(self):
         Instance.counter+=1


I = Instance()
I2 = Instance()
print(Instance.counter)

