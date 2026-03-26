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
        resultalabel_resultado.config(text=resultado)

ventana = tk.Tk()
ventana.title("Catalogo iblue.vzla")
ventana.geometry("1400x720")

tk.Label(ventana, text="Ingresa el nombre del producto:").pack(pady=10)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

tk.Button(ventana, text="Buscar Especificaciones", command=mostrar_info).pack(pady=10)

label_resultado = tk.Label(ventana, text="", justify="left", font=("Arial",10))
label_resultado.pack(pady=20)

ventana.mainloop()
