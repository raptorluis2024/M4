import os
import time
#print(os.path.abspath("archivos"))
try:
    file = open(os.path.abspath("archivos\\algo.txt"))
    #a = open("algo.txt")
    #print(file.read())
    lineas = file.readlines()
    for l in lineas:
        print(l.split(","))
    print(lineas)

    
except Exception as ex:
    print(ex)

else:
    #print("ok")
    file.close()
finally:
    #print("fin")
    pass

try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    #with open(f"{round(time.time())}.log", "w") as log:
    #with open("error.log", "w") as log:   
    with open("error.log", "r+") as log:   
        log.write(f"ERROR: {e}")