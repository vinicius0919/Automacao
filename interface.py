import tkinter as tk
import time

from automacao import executar

# Variáveis para personalizar o layout
fonte = ("Arial", 12)
cor_texto = "black"
espacamento = 10


# Associar a tecla 'Escape' à função de parada



def obter_dados():

    while (int(entrada_nota.get())<=int(parada.get())):
        time.sleep(2)
        numero_nota = int(entrada_nota.get())
        data_nota = entrada_data.get()
        numero_oci = int(entrada_oci.get())
        root.iconify()
        executar(str(numero_nota), data_nota, str(numero_oci))
        time.sleep(2)

        entrada_nota.delete(0,tk.END)
        entrada_nota.insert(0, str(numero_nota+1))

        entrada_oci.delete(0,tk.END)
        entrada_oci.insert(0, str(numero_oci+1))
    root.deiconify()

root = tk.Tk()
root.title("Interface para Dados")

# Labels
tk.Label(root, text="Número da Nota:", font=fonte, fg=cor_texto).pack()
entrada_nota = tk.Entry(root, font=fonte)
entrada_nota.pack(pady=espacamento)

tk.Label(root, text="Número de Parada:", font=fonte, fg=cor_texto).pack()
parada = tk.Entry(root, font=fonte)
parada.pack(pady=espacamento)

tk.Label(root, text="Data da Nota:", font=fonte, fg=cor_texto).pack()
entrada_data = tk.Entry(root, font=fonte)
entrada_data.pack(pady=espacamento)

tk.Label(root, text="Número da OCI:", font=fonte, fg=cor_texto).pack()
entrada_oci = tk.Entry(root, font=fonte)
entrada_oci.pack(pady=espacamento)

# Botão para obter os dados
btn_obter_dados = tk.Button(root, text="Obter Dados", font=fonte, command=obter_dados)
btn_obter_dados.pack(pady=espacamento)

root.mainloop()
