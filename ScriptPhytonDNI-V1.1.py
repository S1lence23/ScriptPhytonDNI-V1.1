from datetime import datetime, timedelta
import time

def calcular_anio_nacimiento(dni):
    base_year = 1942.5
    denominator = 736470

    anio_nacimiento = base_year + (dni / denominator)
    return anio_nacimiento

def calcular_edad_exacta(anio_nacimiento):
    anio = int(anio_nacimiento)
    fraccion_anio = anio_nacimiento - anio
    dias_en_anio = 365.25
    dias_desde_comienzo = fraccion_anio * dias_en_anio

    fecha_nacimiento_aprox = datetime(anio, 1, 1) + timedelta(days=dias_desde_comienzo)
    return fecha_nacimiento_aprox

def guardar_log(dni, anio_nacimiento, fecha_nacimiento_aprox, edad):
    with open("logs.txt", "a") as archivo_log:
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo_log.write(f"Fecha: {fecha_actual}\n")
        archivo_log.write(f"Ingreso del DNI: {dni}\n")
        archivo_log.write(f"Año aproximado de nacimiento: {anio_nacimiento:.2f}\n")
        archivo_log.write(f"Fecha aproximada de nacimiento: {fecha_nacimiento_aprox.strftime('%d de %B de %Y')}\n")
        archivo_log.write(f"Edad actual aproximada: {edad} años\n")
        archivo_log.write("-" * 40 + "\n")

def main():
    print("¡Bienvenido al programa para calcular la fecha de nacimiento y edad aproximada! 🎉")
    print("Solo necesitas ingresar un número de DNI válido.")
    print("Escribe 'salir' para terminar el programa en cualquier momento.\n")
    
    while True:
        try:
            dni_input = input("Ingresa el DNI (o escribe 'salir' para terminar): ")

            if dni_input.lower() == 'salir':
                print("\nGracias por usar este programa. Cerrando en 5 segundos...")
                print("© S1lence Bots | Visítanos en: https://github.com/S1lence23")
                time.sleep(5)
                break

            dni = int(dni_input)

            if dni < 1000000 or dni > 99999999:
                print("⚠️ Por favor, ingresa un DNI válido (entre 1.000.000 y 99.999.999).")
                continue

            anio_nacimiento = calcular_anio_nacimiento(dni)
            print(f"📅 El año aproximado de nacimiento para el DNI {dni} es {anio_nacimiento:.2f}.")

            fecha_nacimiento_aprox = calcular_edad_exacta(anio_nacimiento)
            edad = (datetime.now() - fecha_nacimiento_aprox).days // 365
            
            print(f"📌 Fecha aproximada de nacimiento: {fecha_nacimiento_aprox.strftime('%d de %B de %Y')}.")
            print(f"🎂 Edad actual aproximada: {edad} años.\n")

            guardar_log(dni, anio_nacimiento, fecha_nacimiento_aprox, edad)

        except ValueError:
            print("❌ Error: Por favor, ingresa un número válido.\n")

if __name__ == "__main__":
    main()
