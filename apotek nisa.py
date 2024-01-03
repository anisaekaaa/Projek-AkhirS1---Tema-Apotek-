import tkinter as tk 
from tkinter import messagebox

daftar_obat = {
    "Paracetamol" : 12000,
    "Amoxicillin" : 23000,
    "Loratadine" : 18000,
    "Ibuprofen" : 14000,
    "Ambroxol Tab" : 16000,
    "Simvastatin" : 32000,
    "Omeprazole" : 23000,
    "Cetirizine" : 10000,
    "Pantoprazole" : 32000,
    "Metformin" : 28000,
    "Amlodipine 5 mg" : 10000,
    "Amlodipine 10 mg" : 13000,
    "Furosemide" : 12000,
    "Antasida Doen" : 12000,
    "Mefinter" : 10000,
    "Mefinal" : 11000
}

def tampilkan_daftar_obat():
    daftar_obat_window = tk.Toplevel(root)
    daftar_obat_window.title("Daftar Obat Apotek Wulandari")

    daftar_label = tk.Label(daftar_obat_window, text="Daftar Obat Apotek Wulandari : ")
    daftar_label.pack()
    for obat, harga in daftar_obat.items():
        obat_label = tk.Label(daftar_obat_window, text=f"{obat} - Rp. {harga}")
        obat_label.pack()

def hitung_total_harga(obat, jumlah):
    if obat in daftar_obat:
        harga = daftar_obat[obat]
        total = harga * jumlah
        return total
    else:
        return 0

def beli():
    total_pembelian = 0
    obat_text = obat_entry.get()
    jumlah_text = jumlah_entry.get()
    try:
        jumlah = int(jumlah_text)
        if jumlah <= 0:
            messagebox.showerror("Perhatian!", "Jumlah obat harus lebih dari 0.")
            return
        
        obat = obat_text.capitalize()

        total_pembelian = hitung_total_harga(obat, jumlah)

        if total_pembelian == 0:
            messagebox.showerror("Perhatian!", "Obat tidak ditemukan dalam daftar.")
        else:
            messagebox.showinfo("Total Harga", f"Total harga pembelian Anda di Apotek Wulandari adalah: Rp. {total_pembelian}")

        obat_entry.delete(0, tk.END)
        jumlah_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error!", "Masukkan jumlah harus berupa angka.")

def keluar():
    root.destroy()

root = tk.Tk()
root.title("Apotek Wulandari")

daftar_button = tk.Button(root, text="Daftar Obat Apotek Wulandari", command = tampilkan_daftar_obat)
daftar_button.pack()

obat_label = tk.Label(root, text = "Masukkan nama obat : ")
obat_label.pack()

obat_entry = tk.Entry(root)
obat_entry.pack()

jumlah_label = tk.Label(root, text = "Masukkan jumlah obat : ")
jumlah_label.pack()

jumlah_entry = tk.Entry(root)
jumlah_entry.pack()

beli_button = tk.Button(root, text = "Beli", command = beli)
beli_button.pack()

exit_button = tk.Button(root, text = "Keluar", command = keluar)
exit_button.pack()

root.mainloop()