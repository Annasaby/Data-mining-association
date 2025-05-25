import tkinter as tk
from tkinter import ttk
import pandas as pd
import ast
from collections import Counter

# Load dan parsing data
rules = pd.read_csv('UASAlif/p/rules3.csv')
rules['antecedents'] = rules['Jurusan_Hari_Keperluan']
rules['consequents'] = rules['Nama Laboratorium']

# Fungsi hitung
def hitung_kemunculan(entitas):
    counter = Counter()

    if entitas == "Jurusan":
        for item in rules['antecedents']:
            bagian = item.split(" - ")
            if len(bagian) >= 1:
                counter[bagian[0].strip()] += 1

    elif entitas == "Hari":
        for item in rules['antecedents']:
            bagian = item.split(" - ")
            if len(bagian) >= 2:
                counter[bagian[1].strip()] += 1

    elif entitas == "Lab":
        for item in rules['consequents']:
            counter[item.strip()] += 1

    return counter


# Fungsi saat tombol ditekan
def tampilkan_hasil():
    pilihan = combo_entitas.get()
    hasil = hitung_kemunculan(pilihan)
    total = sum(hasil.values())

    text_output.delete('1.0', tk.END)

    if hasil:
        for key, value in hasil.items():
            text_output.insert(tk.END, f"{key}: {value}\n")
        text_output.insert(tk.END, f"\nTotal: {total}")
    else:
        text_output.insert(tk.END, "Tidak ditemukan data.")

# UI
root = tk.Tk()
root.title("Hitung Kemunculan Entitas pada Rules")

ttk.Label(root, text="Pilih Entitas yang Dihitung").pack()
combo_entitas = ttk.Combobox(root, values=["Jurusan", "Hari", "Lab"])
combo_entitas.pack(pady=5)

tk.Button(root, text="Hitung", command=tampilkan_hasil).pack(pady=10)

text_output = tk.Text(root, height=20, width=60)
text_output.pack(pady=10)

root.mainloop()
