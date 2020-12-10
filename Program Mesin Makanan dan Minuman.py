{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#PROGRAM MESIN MAKANAN DAN MINUMAN\n",
    "def menampilkanjenis():\n",
    "    print(\"==================================================\")\n",
    "    print(\"Program Mesin Penjual Makanan dan Minuman Otomatis\")\n",
    "    print(\"==================================================\")\n",
    "    print(\"1. Makanan Ringan\")\n",
    "    print(\"2. Minuman Dingin\")\n",
    "    print(\"3. Coklat\")\n",
    "    print(\"0. Keluar\")\n",
    "    print(\"==================================================\")\n",
    "    print(\"\")\n",
    "\n",
    "    pilih = str(input(\"Masukkan Pilihan : \"))\n",
    "\n",
    "    if (pilih == \"1\"):\n",
    "        makananringan()\n",
    "    elif (pilih == \"2\"):\n",
    "        minumandingin()\n",
    "    elif (pilih == \"3\"):\n",
    "        coklat()\n",
    "    elif (pilih == \"0\"):\n",
    "        Membeli_lagi()\n",
    "    \n",
    "#MAKANAN RINGAN\n",
    "def makananringan():\n",
    "    keripik = [\"1. Chitato\",\"2. Maitos\",\"3. Qtela\"]\n",
    "    print(\"Pilih Makanan\")\n",
    "    print(keripik[0])\n",
    "    print(keripik[1])\n",
    "    print(keripik[2])\n",
    "    print(\"0. Keluar\")\n",
    "    print(\"===========================\")\n",
    "    \n",
    "    pilih = str(input(\"Masukkan Pilihan     : \"))\n",
    "\n",
    "    if (pilih == \"1\"):\n",
    "        Chitato()\n",
    "    elif (pilih == \"2\"):\n",
    "        Maitos()\n",
    "    elif (pilih == \"3\"):\n",
    "        Qtela()\n",
    "    elif (pilih == \"0\"):\n",
    "        Membeli_lagi()\n",
    "    else:\n",
    "        print(\"Makanan Tidak Tersedia\")\n",
    "        Kembali_ke_awal()\n",
    "\n",
    "#MINUMAN DINGIN\n",
    "def minumandingin():\n",
    "    minuman = [\"1. Aqua Botol\",\"2. Teh Pucuk\",\"3. Pocari Sweat\"]\n",
    "    print(\"Pilih Minuman\")\n",
    "    print(minuman[0])\n",
    "    print(minuman[1])\n",
    "    print(\"0. Keluar\")\n",
    "    print(\"============================\")\n",
    "\n",
    "    pilih = str(input(\"Masukkan Pilihan     : \"))\n",
    "\n",
    "    if (pilih == \"1\"):\n",
    "        Aqua_Botol()\n",
    "    elif (pilih == \"2\"):\n",
    "        Teh_Pucuk()\n",
    "    elif (pilih == \"3\"):\n",
    "        Pocari_Sweat()\n",
    "    elif (pilih == \"0\"):\n",
    "        Membeli_lagi()\n",
    "    else :\n",
    "        print(\"Minuman Tidak Tersedia\")\n",
    "        Kembali_ke_awal()\n",
    "\n",
    "#COKLAT\n",
    "def coklat():\n",
    "    coklat = [\"1. Toblerone \",\"2. Cadbury \",\"3. SilverQueen\"]\n",
    "    print(\"Pilih Minuman\")\n",
    "    print(coklat[0])\n",
    "    print(coklat[1])\n",
    "    print(coklat[2])\n",
    "    print(\"0. Keluar\")\n",
    "    print(\"============================\")\n",
    "\n",
    "    pilih = str(input(\"Masukkan Pilihan     : \"))\n",
    "\n",
    "    if (pilih == \"1\"):\n",
    "        Toblerone()\n",
    "    elif (pilih == \"2\"):\n",
    "        Cadbury()\n",
    "    elif (pilih == \"3\"):\n",
    "        SilverQueen()\n",
    "    elif (pilih == \"0\"):\n",
    "        Membeli_lagi()\n",
    "    else:\n",
    "        print(\"Coklat Tidak Tersedia\")\n",
    "        Kembali_ke_awal()\n",
    "\n",
    "#ingin membeli lagi\n",
    "def Membeli_lagi():\n",
    "    pilih = str(input(\"Ingin Membeli lagi (1) Ya (2) Tidak : \"))\n",
    "    if (pilih == \"1\"):\n",
    "        Kembali_ke_awal()\n",
    "    elif (pilih == \"2\"):\n",
    "        print(\"Terimakasih Telah Membeli\")\n",
    "        print(\"===========================\")\n",
    "        input(\"Tekan Enter untuk keluar\")\n",
    "        exit\n",
    "\n",
    "# Kembali ke awal\n",
    "def Kembali_ke_awal():\n",
    "    input(\"Tekan Enter untuk kembali...\")\n",
    "    print(\"\")\n",
    "    menampilkanjenis()\n",
    "\n",
    "#MAKANAN RINGAN\n",
    "def Chitato():\n",
    "    HargaC = 15000\n",
    "    x = int(input(\"Masukkan Uang Anda   : \"))\n",
    "    if (x >= HargaC):\n",
    "        print(\"Kembalian Anda       = Rp.\",x - HargaC)\n",
    "        print(\"Pembelian Berhasil\")\n",
    "        print(\"===========================\")\n",
    "        Membeli_lagi()\n",
    "    else :\n",
    "        print(\"Uang Anda Tidak Cukup\")\n",
    "        Kembali_ke_awal()\n",
    "\n",
    "def Maitos():\n",
    "    HargaM = 10000\n",
    "    x = int(input(\"Masukkan Uang Anda   : \"))\n",
    "    if (x >= HargaM):\n",
    "        print(\"Kembalian Anda       = Rp.\",x - HargaM)\n",
    "        print(\"Pembelian Berhasil\")\n",
    "        print(\"===========================\")\n",
    "        Membeli_lagi()\n",
    "    else :\n",
    "        print(\"Uang Anda Tidak Mencukupi\")\n",
    "        Kembali_ke_awal()\n",
    "\n",
    "def Qtela():\n",
    "    HargaQ = 8000\n",
    "    x = int(input(\"Masukkan Uang Anda   : \"))\n",
    "    if (x >= HargaQ):\n",
    "        print(\"Kembalian Anda       = Rp.\",x - HargaQ)\n",
    "        print(\"Pembelian Berhasil\")\n",
    "        print(\"===========================\")\n",
    "        Membeli_lagi()\n",
    "    else :\n",
    "        print(\"Uang Anda Tidak Mencukupi\")\n",
    "        Kembali_ke_awal()\n",
    "\n",
    "#MINUMAN DINGIN\n",
    "def Aqua_Botol():\n",
    "    HargaAB = 4000\n",
    "    x = int(input(\"Masukkan Uang Anda   : \"))\n",
    "    if (x >= HargaAB):\n",
    "        print(\"Kembalian Anda       = Rp.\",x - HargaAB)\n",
    "        print(\"Pembelian Berhasil\")\n",
    "        print(\"===========================\")\n",
    "        Membeli_lagi()\n",
    "    else :\n",
    "        print(\"Uang Anda Tidak Mencukupi\")\n",
    "        Kembali_ke_awal()\n",
    "\n",
    "def Teh_Pucuk():\n",
    "    HargaTP = 12500\n",
    "    x = int(input(\"Masukkan Uang Anda   : \"))\n",
    "    if (x >= HargaTP):\n",
    "        print(\"Kembalian Anda       = Rp.\",x - HargaTP)\n",
    "        print(\"Pembelian Berhasil\")\n",
    "        print(\"===========================\")\n",
    "        Membeli_lagi()\n",
    "    else :\n",
    "        print(\"Uang Anda Tidak Mencukupi\")\n",
    "        Kembali_ke_awal()\n",
    "\n",
    "def Pocari_Sweat():\n",
    "    HargaPS = 12500\n",
    "    x = int(input(\"Masukkan Uang Anda   : \"))\n",
    "    if (x >= HargaPS):\n",
    "        print(\"Kembalian Anda       = Rp.\",x - HargaPS)\n",
    "        print(\"Pembelian Berhasil\")\n",
    "        print(\"===========================\")\n",
    "        Membeli_lagi()\n",
    "    else :\n",
    "        print(\"Uang Anda Tidak Mencukupi\")\n",
    "        Kembali_ke_awal()\n",
    "        \n",
    "#COKLAT\n",
    "def Toblerone():\n",
    "    HargaT = 25000\n",
    "    x = int(input(\"Masukkan Uang Anda   : \"))\n",
    "    if (x >= HargaT):\n",
    "        print(\"Kembalian Anda       = Rp.\",x - HargaT)\n",
    "        print(\"Pembelian Berhasil\")\n",
    "        print(\"===========================\")\n",
    "        Membeli_lagi()\n",
    "    else :\n",
    "        print(\"Uang Anda Tidak Mencukupi\")\n",
    "        Kembali_ke_awal()\n",
    "\n",
    "def Cadbury():\n",
    "    HargaCB = 15000\n",
    "    x = int(input(\"Masukkan Uang Anda   : \"))\n",
    "    if (x >= HargaCB):\n",
    "        print(\"Kembalian Anda       = Rp.\",x - HargaCB)\n",
    "        print(\"Pembelian Berhasil\")\n",
    "        print(\"===========================\")\n",
    "        Membeli_lagi()\n",
    "    else :\n",
    "        print(\"Uang Anda Tidak Mencukupi\")\n",
    "        Kembali_ke_awal()\n",
    "\n",
    "def SilverQueen():\n",
    "    HargaSQ = 20000\n",
    "    x = int(input(\"Masukkan Uang Anda   : \"))\n",
    "    if (x >= HargaSQ):\n",
    "        print(\"Kembalian Anda       = Rp.\",x - HargaSQ)\n",
    "        print(\"Pembelian Berhasil\")\n",
    "        print(\"===========================\")\n",
    "        Membeli_lagi()\n",
    "    else :\n",
    "        print(\"Uang Anda Tidak Mencukupi\")\n",
    "        Kembali_ke_awal()\n",
    "\n",
    "menampilkanjenis() "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
