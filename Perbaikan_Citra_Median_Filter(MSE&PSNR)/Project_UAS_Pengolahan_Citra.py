import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
from scipy.ndimage import median_filter
import matplotlib.pyplot as plt
import io

def display_text():
    text = entry.get()
    label.config(text=text)

def apply_median_filter(image, kernel_size):
    filtered_image = median_filter(image, size=kernel_size)
    return filtered_image

def calculate_mse(original_image, filtered_image):
    mse = np.mean((original_image - filtered_image) ** 2)
    return mse

def calculate_psnr(mse):
    max_pixel = 255
    psnr = 10 * np.log10((max_pixel ** 2) / mse)
    return psnr

def plot_histogram(image_array, canvas_width, canvas_height):
    fig, ax = plt.subplots(figsize=(canvas_width/50, canvas_height/45), dpi=15)
    ax.hist(image_array.ravel(), bins=256, range=(0, 256), color='gray', alpha=1)
    ax.set_xlabel('Pixel Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram')
    canvas = plt.gcf().canvas
    canvas.draw()
    buf = canvas.tostring_rgb()
    width, height = canvas.get_width_height()
    hist_image = Image.frombytes('RGB', (width, height), buf)
    hist_image_tk = ImageTk.PhotoImage(hist_image)
    return hist_image_tk

def open_image():
    # Memilih file citra grayscale
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    if file_path:
        # Membaca gambar
        image = Image.open(file_path)

        # Mengubah ukuran gambar menjadi 200x200
        image = image.resize((240, 200))

        # Mengonversi gambar ke citra grayscale NumPy array
        image_array = np.array(image.convert("L"))

        # Menerapkan median filter pada gambar
        kernel_size = 2,6  # Ubah ukuran kernel sesuai kebutuhan
        filtered_image_array = apply_median_filter(image_array, kernel_size)

        # Mengonversi gambar hasil filter ke format yang dapat ditampilkan oleh Tkinter
        filtered_image = Image.fromarray(filtered_image_array)
        filtered_image_tk = ImageTk.PhotoImage(filtered_image)

        # Menggabungkan gambar asli dan gambar hasil filter dalam satu canvas
        merged_image = Image.new("RGB",  (700, 200),"yellow")
        merged_image.paste(image, (0, 0))
        merged_image.paste(filtered_image, (350, 0))
        merged_image_tk = ImageTk.PhotoImage(merged_image)

        # Menampilkan gambar gabungan di canvas
        canvas.itemconfig(image_item, image=merged_image_tk)
        canvas.image = merged_image_tk

        # Menghitung nilai MSE dan PSNR
        mse = calculate_mse(image_array, filtered_image_array)
        psnr = calculate_psnr(mse)

        # Menampilkan nilai MSE dan PSNR pada canvas
        mse_text = "MSE: {:.2f}".format(mse)
        psnr_text = "PSNR: {:.2f}".format(psnr)
        canvas.itemconfig(mse_item, text=mse_text)
        canvas.itemconfig(psnr_item, text=psnr_text)

        # Menampilkan histogram di canvas
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        original_hist_image = plot_histogram(image_array, canvas_width, canvas_height)
        filtered_hist_image = plot_histogram(filtered_image_array, canvas_width, canvas_height)
        canvas.itemconfig(original_hist_item, image=original_hist_image)
        canvas.itemconfig(filtered_hist_item, image=filtered_hist_image)
        canvas.original_hist_image = original_hist_image
        canvas.filtered_hist_image = filtered_hist_image

def exit_program():
    window.quit()

# Membuat jendela GUI
window = tk.Tk()
window.title("Image Display")
window.geometry("1000x800")
window.configure(bg="grey")

# Membuat canvas untuk menampilkan gambar
canvas = tk.Canvas(window, width=800, height=700, bg='yellow')
canvas.pack()
text1 = canvas.create_text(400,50, text="Aplikasi perbaikan Citra Menggunakan Median Filter", font=("arial",16), fill="black")
text2 = canvas.create_text(418,70, text="dan Menampilkan Nilai MSE dan PSNR", font=("arial",16), fill="black")
text3 = canvas.create_text(218,100, text="Citra Asli", font=("arial",16), fill="black")
text4 = canvas.create_text(590,100, text="Citra Median Filter", font=("arial",16), fill="black")

# Menentukan koordinat dan ukuran gambar pada canvas
image_item = canvas.create_image(120, 120, anchor=tk.NW, image=None)

# Menampilkan histogram gambar asli
original_hist_item = canvas.create_image(120, 400, anchor=tk.NW, image=None)

# Menampilkan histogram gambar hasil filter
filtered_hist_item = canvas.create_image(470, 400, anchor=tk.NW, image=None)

# Menentukan koordinat dan teks nilai MSE pada canvas
mse_item = canvas.create_text(10, 650, anchor=tk.W, text="MSE: ")
psnr_item = canvas.create_text(10, 670, anchor=tk.W, text="PSNR: ")

# Tombol "Pilih Gambar"
btn = tk.Button(window, text="Pilih Gambar", command=open_image)
btn.pack()

# Tombol "Keluar"
exit_btn = tk.Button(window, text="Keluar", command=exit_program)
exit_btn.pack()

# Menjalankan GUI
window.mainloop()
