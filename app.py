from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generar_respuesta(prompt):
    respuesta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente de escritura profesional."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return respuesta.choices[0].message.content


while True:
    print("\n=== ASISTENTE DE ESCRITURA ===")
    print("1. Generar texto")
    print("2. Corregir gramática")
    print("3. Mejorar estilo")
    print("4. Resumir texto")
    print("5. Traducir texto")
    print("6. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tema = input("Ingresa una idea o tema: ")
        prompt = f"Escribe un texto sobre: {tema}"
        print("\nGenerando texto...")
        print(generar_respuesta(prompt))

    elif opcion == "2":
        texto = input("Ingresa el texto a corregir: ")
        prompt = f"Corrige la gramática y ortografía del siguiente texto: {texto}"
        print("\nCorrigiendo texto...")
        print(generar_respuesta(prompt))

    elif opcion == "3":
        texto = input("Ingresa el texto a mejorar: ")
        prompt = f"Mejora el estilo y claridad del siguiente texto: {texto}"
        print("\nMejorando estilo...")
        print(generar_respuesta(prompt))

    elif opcion == "4":
        texto = input("Ingresa el texto a resumir: ")
        prompt = f"Resume el siguiente texto: {texto}"
        print("\nGenerando resumen...")
        print(generar_respuesta(prompt))

    elif opcion == "5":
        texto = input("Ingresa el texto a traducir: ")
        idioma = input("¿A qué idioma deseas traducirlo?: ")
        prompt = f"Traduce el siguiente texto al idioma {idioma}: {texto}"
        print("\nTraduciendo texto...")
        print(generar_respuesta(prompt))

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida")
