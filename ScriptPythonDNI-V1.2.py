from datetime import datetime, timedelta
import time

# Constantes para el cálculo del año de nacimiento
base_year = 1942.5
denominator = 736470
# constante: variable que no cambia

def calcular_anio_nacimiento(dni): 
    return  base_year + (dni / denominator)

def calcular_edad_exacta(anio_nacimiento):
    anio = int(anio_nacimiento)
    fraccion_anio = anio_nacimiento - anio
    dias_en_anio = 365.25
    dias_desde_comienzo = fraccion_anio * dias_en_anio

    fecha_nacimiento_aprox = datetime(anio, 1, 1) + timedelta(days=dias_desde_comienzo)
    return fecha_nacimiento_aprox

## Funcion para validar el DNI
def validar_dni(dni):
    return 1_000_000 < dni < 99_999_999
## edad exacta   
def edad_exacta(fecha_nacimiento_aprox):
    return int((datetime.now() - fecha_nacimiento_aprox).days / 365.25) 
## Funcion para mostrar los resultados
def mostrar_resultados(dni, anio_nacimiento, fecha_nacimiento_aprox, edad):
    print(f"📅 El año aproximado de nacimiento para el DNI {dni} es {anio_nacimiento:.2f}.")
    print(f"📌 Fecha aproximada de nacimiento: {fecha_nacimiento_aprox.strftime('%d de %B de %Y')}.")
    print(f"🎂 Edad actual aproximada: {edad} años.\n")
## Funcion para guardar el log
def guardar_log(dni, anio_nacimiento, fecha_nacimiento_aprox, edad):
    with open("logs.txt", "a") as archivo_log:
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo_log.write(f"Fecha: {fecha_actual}\n")
        archivo_log.write(f"Ingreso del DNI: {dni}\n")
        archivo_log.write(f"Año aproximado de nacimiento: {anio_nacimiento:.2f}\n")
        archivo_log.write(f"Fecha aproximada de nacimiento: {fecha_nacimiento_aprox.strftime('%d de %B de %Y')}\n")
        archivo_log.write(f"Edad actual aproximada: {edad} años\n")
        archivo_log.write("-" * 40 + "\n")

    

## Funcion principal
def main():
    print("¡Bienvenido al programa para calcular la fecha de nacimiento y edad aproximada! 🎉")
    print("Solo necesitas ingresar un número de DNI válido.")
    print("Escribe 'salir' para terminar el programa en cualquier momento.\n")
    
    while True:
        try:
            dni_input = input("Ingresa el DNI sin puntos (o escribe 'salir' para terminar): ")
            # salir del programa
            if dni_input.lower() == 'salir':
                print("\nGracias por usar este programa. Cerrando en 5 segundos...")
                print("© S1lence Bots | Visítanos en: https://github.com/S1lence23")
                time.sleep(5)
                break
            # Validar que el DNI sea un número
            if not  dni_input.isdigit():
                print("⚠️ Por favor, ingresa un número de DNI válido.")
                continue   

            dni = int(dni_input)
            # rango de DNI
            if not validar_dni(dni):
                print("⚠️ Por favor, ingresa un DNI válido (entre 1.000.000 y 99.999.999).")
                continue
            
            anio_nacimiento = calcular_anio_nacimiento(dni)
            fecha_nacimiento_aprox = calcular_edad_exacta(anio_nacimiento)
            edad = edad_exacta(fecha_nacimiento_aprox)
            
            mostrar_resultados(dni, anio_nacimiento, fecha_nacimiento_aprox, edad)
            guardar_log(dni, anio_nacimiento, fecha_nacimiento_aprox, edad)
        
        except Exception as e:
            print(f"⚠️ Ha ocurrido un error: {e}")
            continue
       
if __name__ == "__main__":
    main()
