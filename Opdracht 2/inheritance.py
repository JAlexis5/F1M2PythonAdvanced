# inheritance.py

class AlA:
    var1 = "I spent literally 4 days trying to get this thing to work, God this unit is hard."
    var2 = 0
    var3 = 10.0
    var4 = True

    def var4truth(self):
        print(f"var4 in Class AlA is {AlA.var4}.")   
  
    def printvar1(self):
        print(AlA.var1)



class BeB(AlA):
    var5 = [1, 2, 3]
    var6 = range(1, 6)

    def __init__(self):
        var1 = "There is now text here"
        var4 = False
    
    def var4truth(self):
        print(f"var4 is now {BeB.var4} in Class BeB.")
    
    def printvar1(self):
        super().printvar1()
        print("This function was put in class B, and therefore has been updated to display this text by using the super() function.")

instanceA = AlA()
instanceB = BeB()

print(f"Variable 1 of Class AlA is {instanceA.var1}.")
print(f"Variable 2 of Class AlA is {instanceA.var2}.")
print(f"Variable 3 of Class AlA is {instanceA.var3}.")
print(f"Variable 4 of Class AlA is {instanceA.var4}.")
print(f"Variable 5 of Class BeB is {instanceB.var5}.")
print(f"Variable 6 of Class BeB is {instanceB.var6}.")

instanceA.var4truth()
instanceB.var4truth()
instanceB.printvar1()