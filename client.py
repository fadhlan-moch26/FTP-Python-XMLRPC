import xmlrpc.client
import xmlrpc.client as xmlrpclib
import os
import socket

#function untuk mengunggah file ke server
def Upload_File(fileName,host):
    with open(fileName,'rb') as handle:
        file = xmlrpc.client.Binary(handle.read())
        server.upload(file,fileName,host)

#function untuk mengunduh file dari server
def Download_File(fileName,host):
    with open('download_{}'.format(fileName),'wb') as handle:
        handle.write(server.download(fileName,host).data)
        handle.close()

#function unutk menampilkan daftar file yang ada di server
def Get_Daftar_File():
    list = server.view()
    for i in list:
        print(i)

#function untuk menndapatkan nama/id host
def Get_Host():
    return socket.gethostname()

server = xmlrpc.client.ServerProxy ("http://25.32.157.175:2620/") #alamat IP server
host = Get_Host() #menyimpan nama/id host
server.Client_Availability(host) #memeriksa status client
clear = lambda: os.system("cls")

while True:
    print('Selamat Datang di Program FTP')
    print(' ')
    print('-------------------------------------------')
    print('Silahkan Pilih Nomor Menu :')
    print('1. Mengupload File ')
    print('2. Mendownload File ')
    print('-------------------------------------------')

    pilih = input('Masukkan Nomor : ')

    if(pilih=='1'):
        file = input('Pilih File yang Akan Diupload: ')
        Upload_File(file,host)
        clear()
        print('Upload File Berhasil !')
        input()
        clear()
    elif(pilih=='2'):
        Get_Daftar_File()
        file = input('Pilih File yang Akan Didownload: ')
        Download_File(file,host)
        clear()
        print('Download File Berhasi !')
        input()
        clear()
    else:
        clear()
        break