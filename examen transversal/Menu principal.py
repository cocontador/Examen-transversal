import Funciones as fn


trabajadores= [
    "Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"
    ]
sueldo_trabajadores={}

while True:
    print("*****MENÚ*****")
    print("0.Asignación de Sueldos")
    print("1.Clasificar Sueldos")
    print("2.Ver estádisticas")
    print("3.Reporte de sueldos")
    print("4.Salir del programa")
    
    opc=int(input("Ingrese una opción: "))

    if opc==0:
        sueldo_trabajadores={trabajador:0 for trabajador in trabajadores}
        print("la asignación de sueldos fue realizada correctamente")
    elif opc==1:
        fn.clasificar_sueldos
        print("se ha realizado clasificación")
    
    elif opc==2:
        if sueldo not in sueldo_trabajadores:
            print("Debe asignar sueldos")
        else:
            print("Sueldos ", fn.estadisticas)
        
    elif opc==3:
        print(fn.reporte_sueldos)
    
    elif opc==4:
        print("Finalizando programa...")
        print("Desarrollado por Constanza Contador")
        print("RUT 17.710.755-7")
        break
    
    else:
        print("Ingrese una opción válida entre 0 y 4")
