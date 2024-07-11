import random
import csv
import statistics
#import statistics geometric mean

def asignar_sueldos (trabajador):
  sueldo_trabajadores={}
  for trabajador in trabajadores.items():
      sueldo=random.randint(300000,2500000)
      sueldo_trabajadores[trabajador]=sueldo
  print("Sueldos asignados correctamente")
  print(sueldo_trabajadores)
  return sueldo_trabajadores

    
def clasificar_sueldos(sueldo_trabajadores):
  menores_800={}
  entre_800_2M={}
  mayores_2M={}
  
  for trabajador, sueldo in sueldo_trabajadores.items():
    if sueldo_trabajadores<800:
      menores_800 = sueldo
      print("El total de sueldos menores a $800.000 es de ", menores_800)

    elif sueldo_trabajadores>=800000 and sueldo_trabajadores<=2000000:
      entre_800_2M=sueldo
      print("El total de sueldos menores a $800.000 es de ", entre_800_2M)
    elif sueldo_trabajadores>2000000:
      mayores_2M=sueldo
      print("El total de sueldos menores a $800.000 es de ", mayores_2M)
    else:
      print("debe inicializar sueldos")
  

def estadisticas(sueldo_trabajadores):
  
  sueldo_max=max(sueldo)
  sueldo_min=min(sueldo)
  promedio_sueldos=sum(sueldo)/len(sueldo)
  media_geometric=statistics.median(sueldo)

  #sueldo_min, sueldo_max, promedio_sueldos,media_geometrica = sueldo_trabajador


#descuento_AFP= sueldo*0.12
#descuento_salud= sueldo*0.07  
#sueldo_liquido= sueldo-descuento_AFP-descuento_salud  

def reporte_sueldos (sueldo_trabajadores):
  with open ("reporte_sueldos.csv","w",newline="") as archivo:
    escritor=csv.writer(archivo,delimiter=',')
    escritor.writerow(["Nombre trabajador","Sueldo Base", "Descuento Salud","Descuento AFP","Sueldo líquido"])
    for trabajador in trabajadores:
      escritor.writerow([trabajador,sueldo, descuento_salud, descuento_AFP, sueldo_liquido])
  print("El reporte ha sido generado correctamente en csv")