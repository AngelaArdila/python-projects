from datetime import datetime

import time

contador=60

while True:
    with open("hora_fecha.txt", "a") as actualizacion_hora:

        localtime = time.localtime()
        result = time.strftime("%d %B , %Y %I:%M:%S %p", localtime)

        actualizacion_hora.write("{}\n".format(result))
       
        contador -= 1
        if contador == 0 :
            break
            
        print(contador,result)
       
      

        time.sleep(1)
        
            
        
