from contextlib import nullcontext
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os

#Function untuk mengunggah file ke server
def Upload_File(file,fileName,host):
    with open('{}_{}'.format(host,fileName),'wb') as handle:
        handle.write(file.data)
        Activity_Update(host)
        return True

#Function untuk mengunduh file ke server
def Download_File(file,host):
    with open(file, 'rb') as handle:
        Activity_Update(host)
        return xmlrpc.client.Binary(handle.read())

#Function untuk melihat file yang tersedia pada server
def List_of_Files():
    return os.listdir()

#Function untuk mengecek ada tidaknya client dan juga untuk menambah client pada database berupa array
def Client_Availability(host):
    door=True
    if ( len(arr)==0 ):
        arr.append(host)
        arr_act.append(0)
    else:
        for i in range(len(arr)):
            if ( arr[i] == host ):
                door=False
        if(door==True):
            arr.append(host)
            arr_act.append(0)


#Function untuk memperbarui banyaknya aktivitas yang dilakukan oleh para client sekaligus untuk menampilkan client yang sedang aktif & yang paling aktif
def Activity_Update(host):
    for i in range(len(arr)):
        if(host==arr[i]):
            arr_act[i] +=1

    for i in range(len(arr)):
        print(i+1, ". HOSTNAME : ",arr[i])
        print("   Aktivitas : ",arr_act[i])
    
    max=0
    if len(arr)>0:    
        for i in range(len(arr)):
            if(arr_act[i]>arr_act[max]):
                max=i
    
    print("")
    print("USER PALING AKTIF SAAT INI: ")
    print("   HOSTNAME : ",arr[max])
    print("   Aktivitas : ",arr_act[max])
        
#Function utama untuk menjalankan server
def serverMain():
    server = SimpleXMLRPCServer(("25.32.157.175", 2620), allow_none=True)

    server.register_function(Upload_File, "upload")
    server.register_function(Download_File, "download")
    server.register_function(List_of_Files, "view")
    server.register_function(Client_Availability, "Client_Availability")
    server.serve_forever()

#Pembuatan variabel dengan tipe data aarray untuk menyimpan info client
arr=[]
arr_act=[]

#Pemanggilan function fucntion utama
serverMain()