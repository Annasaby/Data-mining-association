import tkinter as tk
from tkinter import ttk
import pandas as pd
import ast

# Load data
rules = pd.read_csv('UAS/rules2.csv')
rules['antecedents'] = rules['antecedents'].apply(ast.literal_eval)
rules['consequents'] = rules['consequents'].apply(ast.literal_eval)

# Ekstrak semua jurusan, hari, dan lab unik
jurusan_set = set()
hari_set = set()
lab_set = set()

for ant_list in rules['antecedents']:
    for ant in ant_list:
        parts = ant.split(" - ")
        if len(parts) >= 2:
            jurusan_set.add(parts[0])
            hari_set.add(parts[1])

for cons_list in rules['consequents']:
    for cons in cons_list:
        lab_set.add(cons)

# Fungsi untuk filter rules
def filter_rules():
    jurusan = combo_jurusan.get()
    hari = combo_hari.get()
    lab = combo_lab.get()
    conf_min = conf_min_scale.get() / 100
    lift_min = lift_min_scale.get() / 10

    filtered = rules[
        rules['antecedents'].apply(
            lambda ant_list: any(jurusan in ant and hari in ant for ant in ant_list)
        ) &
        rules['consequents'].apply(
            lambda cons_list: lab in cons_list
        ) &
        (rules['confidence'] >= conf_min) &
        (rules['lift'] >= lift_min)
    ]

    text_output.delete('1.0', tk.END)
    if not filtered.empty:
        for _, row in filtered.iterrows():
            text_output.insert(tk.END, f"{row['antecedents']} => {row['consequents']} \n")
    else:
        text_output.insert(tk.END, "Tidak ditemukan rule yang sesuai.")

# UI
root = tk.Tk()
root.title("Filter Rules by Jurusan, Hari, Lab, Confidence, Lift")

# Jurusan
ttk.Label(root, text="Pilih Jurusan").pack()
combo_jurusan = ttk.Combobox(root, values=sorted(list(jurusan_set)))
combo_jurusan.pack(pady=5)

# Hari
ttk.Label(root, text="Pilih Hari").pack()
combo_hari = ttk.Combobox(root, values=sorted(list(hari_set)))
combo_hari.pack(pady=5)

# Lab
ttk.Label(root, text="Pilih Lab").pack()
combo_lab = ttk.Combobox(root, values=sorted(list(lab_set)))
combo_lab.pack(pady=5)

# Confidence Min
tk.Label(root, text="Minimum Confidence (%)").pack()
conf_min_scale = tk.Scale(root, from_=0, to=100, orient='horizontal')
conf_min_scale.set(50)
conf_min_scale.pack(pady=5)

# Lift Min
tk.Label(root, text="Minimum Lift").pack()
lift_min_scale = tk.Scale(root, from_=0, to=50, resolution=1, orient='horizontal')
lift_min_scale.set(1)
lift_min_scale.pack(pady=5)

# Tombol
tk.Button(root, text="Tampilkan Rules", command=filter_rules).pack(pady=10)

# Output
text_output = tk.Text(root, height=20, width=80)
text_output.pack(pady=10)

root.mainloop()
