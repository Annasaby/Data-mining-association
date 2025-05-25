import ast
import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load rules dari file CSV
rules = pd.read_csv('D:\\VSCode\\Data Mining\\UAS\\rules2.csv')

def cari_lab(jurusan, hari, rules_df):
    input_user = f"{jurusan} - {hari}"

    for index, row in rules_df.iterrows():
        if input_user in row['antecedents']:
            consequents_str = row['consequents']
            consequents = ast.literal_eval(consequents_str)
            lab = list(consequents)[0]
            return lab
    return "Laboratorium tidak ditemukan"

def cari_confidence_lift(jurusan, hari, rules_df):
    input_user = f"{jurusan} - {hari}"
    for index, row in rules_df.iterrows():
        if input_user in row['antecedents']:
            confidence = row['confidence'] * 100
            confidence = round((confidence), 2)
            lift = row['lift']
            lift = round((lift), 2)
            return confidence, lift
    return None, None

def cek_lab():
    jurusan = combo_jurusan.get()
    hari = combo_hari.get()
    hasil = cari_lab(jurusan, hari, rules)
    label_hasil.config(text=f"Rekomendasi Lab: {hasil}")
    hasil_confidence_lift = cari_confidence_lift(jurusan, hari, rules)
    label_confidence_lift.config(text=f"Confidence: {hasil_confidence_lift[0]}% , Lift: {hasil_confidence_lift[1]}") 
# rules[rules['antecedents'] == f'{jurusan} - {hari}']['confidence'].values[0]}
# Tkinter UI
root = tk.Tk()
root.title("Rekomendasi Laboratorium")

combo_jurusan = ttk.Combobox(root, values=['Manajemen Informatika', 'Teknik Informatika Bilingual',
       'Teknik Komputer', 'Komputerisasi Akuntansi', 'Sistem Komputer',
       'Sistem Informasi Bilingual', 'Magister Ilmu Komputer'])
combo_jurusan.pack(pady=5)

combo_hari = ttk.Combobox(root, values=["Senin", "Selasa", "Rabu", "Kamis", "Jumat"])
combo_hari.pack(pady=5)

btn_cek = tk.Button(root, text="Cek Lab", command=cek_lab)
btn_cek.pack(pady=10)

label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=10)

label_confidence_lift = tk.Label(root, text="")
label_confidence_lift.pack(pady=10)

root.mainloop()
