try:
    try:
        import sys, os, time, datetime, random
        from color.warna import orange
        from color.warna import putih
        from color.warna import merah
        from color.warna import hijau
        from color.warna import biru
        from color.warna import borange
        from color.warna import bputih
        from color.warna import bhijau
        from color.warna import bbiru
        from color.warna import bmerah
        from color.warna import kelabu
        from color.warna import borangekelip
        from color.warna import banmerah
        from color.warna import banhijau
        from color.warna import banorange
        from color.warna import reset
    except ImportError:
        print(' [!] Harap install ulang script ini dari repository github kami!');sys.exit()
    os.system("mkdir hasil_word")
    os.system("")
    os.system("cls||clear")
    
    banner = borange+"""
>==========================================================<
 | """+reset+putih+"""         ALGORITM - Wordlist File Creator For      """+borange+"""    |
 | """+reset+putih+"""           Riddles - Archive File Cracker!!      """+borange+"""      |
<+========================================================+>
 |"""+reset+hijau+""" Creator:   """+putih+""" Sreetx  """+borange+"""                                   |
 |"""+reset+hijau+""" Language:  """+putih+""" Python3  """+borange+"""                                  |
 |"""+reset+hijau+""" Version:   """+putih+""" 0.0.1  """+borange+"""                                    |
 |"""+reset+hijau+""" Github:   """+putih+"""  https://github.com/Sreetx   """+borange+"""               |
 |"""+reset+hijau+""" YouTube: """+putih+"""   https://www.youtube.com/@linggachannel4781 """+borange+"""|
 >========================================================<"""+reset+bputih+"""

 [*] Setiap file wordlist yang anda buat akan disimpan pada file "hasil_word" di folder script ini"""+reset

#STARTUP
    print(banner)
    c = ""
    print(kelabu+"\n ["+banorange+"ALGORITM"+reset+kelabu+"] "+orange+"Anda menggunakan script ALGORITM untuk membuat wordlist"+reset)
    panjang = input(kelabu+" ["+banhijau+"?"+reset+kelabu+"] Masukkan panjang kata untuk wordlist(1-100): "+reset)
    if panjang is c:
        print(kelabu+"\n ["+banmerah+"!"+reset+kelabu+"]"+merah+" Masukkan jumlah panjang kata!\n"+reset);sys.exit()
    number = input(kelabu+" ["+banhijau+"?"+reset+kelabu+"] Gunakan angka dan simbol dalam wordlist? ["+banhijau+"y/n"+reset+kelabu+"]: "+reset)
    total = input(kelabu+" ["+banhijau+"?"+reset+kelabu+"] Jumlah kata dalam Wordlist yang akan dibuat: "+reset)
    file_name = input(kelabu+" ["+banhijau+"?"+reset+kelabu+"] Masukkan nama file untuk file wordlist anda(*.txt): "+reset)
    if file_name is c:
        date = datetime.datetime.now()
        timestamp = date.strftime("%Y%m%d_%H%M%S")
        file_name = "hasil_word/"+timestamp+".txt"
        print(kelabu+'\n ['+banorange+'*'+reset+kelabu+']'+putih+' Nama file kosong. Nama default akan digunakan "'+hijau+file_name+reset+'"')
    
#CREATE
    print(kelabu+"\n ["+banhijau+"INFO"+reset+kelabu+"] "+orange+"Wordlist sedang dibuat. Tekan CTRL+C untuk keluar"+reset)
    if number.lower() == "y" or number.lower() == "Y":
        abjad = "abcdefghijklmnopqrstuvwxyz1234567890@#$_&-+()/?!;:'.~`|\}{=^%✓[]"
    if number.lower() == "n" or number.lower() == "N":
        abjad = "abcdefghijklmnopqrstuvwxyz"
    
    try:
        with open("hasil_word/"+file_name,"w") as d:
            for _ in range(int(total)):
                words = ''.join(random.choices(abjad, k=int(panjang)))
                print(kelabu+"\r ["+banhijau+"INFO"+reset+kelabu+"]"+orange+" Wordlist yang dibuat: "+reset+banhijau+words+reset, end='', flush=True)
                d.write(words+"\n")
                time.sleep(0.1)
        print(kelabu+"\n ["+banhijau+"*"+reset+kelabu+"] "+putih+"File telah dibuat! File disimpan dengan nama "+hijau+file_name+reset+putih+"pada folder hasil_word"+reset);sys.exit()
    except (KeyboardInterrupt, EOFError): print(kelabu+"\n ["+banhijau+"*"+reset+kelabu+"] "+putih+"File telah dibuat! File disimpan dengan nama "+hijau+file_name+reset+putih+"pada folder hasil_word"+reset);sys.exit()
except (KeyboardInterrupt, EOFError): print(merah+"\n [*] EXIT!!"+reset);sys.exit()