# UAS_PENGOLAHAN_CITRA

- Nama : Imam Solehudin
- Nim : 312110290
- Kelas  : TI.21.C.1

# Membuat Aplikasi Perbaikan Citra menggunakan metode Fedian Filter dan menghitung nilai MSE dan PSNR

Median filter adalah salah satu teknik pengolahan citra yang digunakan untuk mengurangi noise pada citra digital. Tujuan utama median filter adalah untuk menghilangkan atau mengurangi efek noise seperti derau salt-and-pepper (titik-titik hitam atau putih yang tersebar acak pada citra).

Berikut program yang telah saya buat.


1. Import library python yang kita butuhkan. disini saya inmport library tkinter, numpy dan matplotlib. Setelah itu kita buat definisi untuk untuk menampilkan teks, menampilkan median filter, menampilkan histogram, menghitung nilai mse psnr. Berikut programnnya :

![gambar](Perbaikan_Citra_Median_Filter(MSE&PSNR)/1.png)

2. selanjutnya buat definisi untuk mengambil file gambar dengan format .jpg .jpeg dan .png. pada bagian ini kita juga mengatur ukuran dan tata letak gambar, Menghitung kernel size median filter pada gambar dan Menghitung nilai mse dan psnr dan 


![gambar](Perbaikan_Citra_Median_Filter(MSE&PSNR)/2.png)


3. Program menampilkan MSE PSNR dan histogram pada canvas gui. 

![gambar](Perbaikan_Citra_Median_Filter(MSE&PSNR)/3.png)

4. Membuat jendela GUI agar program yang didefiniskan sebelumnya dapat ditampilkan di jendela python GUI.

![gambar](Perbaikan_Citra_Median_Filter(MSE&PSNR)/4.png)


5. Tampilan sebelum memilih gambar untuk dieksekusi.

![gambar](Perbaikan_Citra_Median_Filter(MSE&PSNR)/5.png)


6. Tampilan ketika sudah memilih gambar yang akan dieksekusi menggunakan metode median filter.


![gambar](Perbaikan_Citra_Median_Filter(MSE&PSNR)/6.png)


7. Metode median filter digunakan untuk mengurangi noise pada citra digital. Pada gambar berikut bintik yang ada pada citra asli menjadi blur ketika diubah menggunakan metode median filter.

![gambar](Perbaikan_Citra_Median_Filter(MSE&PSNR)/7.png)


8. Dari hasil histogram tersebut, gambar asli dan hasil filter memiliki histogram yang terpusat ke tengah yang berarti menunjukan intensitas yang seimbang.

![gambar](Perbaikan_Citra_Median_Filter(MSE&PSNR)/8.png)


9. Nilai MSE=51.78 cukup tinggi, semakin besar perbedaan antara citra asli dan citra yang dihasilkan. Nilai PSNR sebesar 30.99 dB menunjukkan bahwa citra yang dihasilkan memiliki tingkat keakuratan yang cukup tinggi dalam merepresentasikan citra asli.

![gambar](Perbaikan_Citra_Median_Filter(MSE&PSNR)/9.png)
