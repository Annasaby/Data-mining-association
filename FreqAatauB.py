import tkinter as tk
from tkinter import ttk
import pandas as pd
from collections import Counter

# Load data
rules = pd.read_csv('UASAlif/p/rules3.csv')

# Fungsi hitung berdasarkan kolom yang dipilih
def hitung_kemunculan(kolom):
    counter = Counter()
    if kolom in rules.columns:
        for item in rules[kolom]:
            counter[str(item).strip()] += 1
    return counter

# Fungsi saat tombol ditekan
def tampilkan_hasil():
    pilihan_kolom = combo_entitas.get()
    hasil = hitung_kemunculan(pilihan_kolom)
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
root.title("Hitung Kemunculan Nilai dari Kolom")

ttk.Label(root, text="Pilih Kolom yang Dihitung").pack()
combo_entitas = ttk.Combobox(root, values=["Jurusan_Hari_Keperluan", "Nama Laboratorium"])
combo_entitas.pack(pady=5)
combo_entitas.current(0)  # default pilihan pertama

tk.Button(root, text="Hitung", command=tampilkan_hasil).pack(pady=10)

text_output = tk.Text(root, height=20, width=60)
text_output.pack(pady=10)

root.mainloop()
