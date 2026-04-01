#Segunda actualizacion, se cambio la ventana.

import tkinter as tk
from tkinter import messagebox

iphone = {
    "IPHONE 15": {"almacenamiento": "128GB+", "procesador": "A16 Bionic", "camara": "48MP", "precio": "$520"},
    "IPHONE 15 PRO": {"almacenamiento": "128GB-1TB", "procesador": "A17 Pro", "camara": "48MP (Pro)", "precio": "$620"},
}
accesorios = {
    "CARGADOR 25W": {"Puerto": "USB-C", "Velocidad": "Carga rápida 50%", "Precio": "$25"},
    "AIRPODS PRO": {"Chip": "H2", "Cancelación": "Activa", "Precio": "$249"},
    "FORROS": {"Silicone case": "Todos los colores", "Forros 360": "Pocas unidades"},
}



def mostrar_info():
    label_resultado.config(text="")
    busqueda = entrada.get().upper().strip()

    if busqueda in iphone:
        datos = iphone[busqueda]
        categoria = "📱IPHONE"
    elif busqueda in accesorios:
        datos = accesorios[busqueda]
        categoria = "🎧ACCESORIOS"
    else:
        messagebox.showerror("Error", "Producto no encontrado")
        return
    
    resultado = f"{categoria}: {busqueda}\n" + "-"*30 + "\n"
    for clave, valor in datos.items():
        resultado += f"🔹 {clave}: {valor}\n"
        label_resultado.config(text=resultado)

ventana = tk.Tk()
ventana.title("Catalogo iblue.vzla")
ventana.geometry("800x720")
ventana.configure(padx=30,pady=30)

tk.Label(ventana, text="CATÁLOGO iblue.vzla", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(ventana, text="Ingresa el nombre del producto (ej: iPhone 15):", font=("Arial",10)).pack()

entrada = tk.Entry(ventana, font=("Arial", 12), width=30)
entrada.pack(pady=10)
# Permite buscar al presionar "Enter"
entrada.bind('<Return>', lambda event: mostrar_info())

tk.Button(ventana, text="BUSCAR INFO", command=mostrar_info, bg="#007AFF", fg="white", font=("Arial", 10, "bold"), width=20, height=2, cursor="hand2").pack(pady=15)

label_resultado = tk.Label(ventana, text="", justify="left", font=("Consolas",12), bg="#F8F9FA",relief="flat", width=40, height=10, anchor="nw", padx=15, pady=15)
label_resultado.pack(pady=20)

ventana.mainloop()
