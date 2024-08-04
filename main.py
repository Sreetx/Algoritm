try:
    try:
        import sys, os, time, datetime, random, string
        import threading
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
 |"""+reset+hijau+""" Version:   """+putih+""" 1.0.1  """+borange+"""                                    |
 |"""+reset+hijau+""" Github:   """+putih+"""  https://github.com/Sreetx   """+borange+"""               |
 |"""+reset+hijau+""" YouTube: """+putih+"""   https://www.youtube.com/@linggachannel4781 """+borange+"""|
 >========================================================<"""+reset+bputih+"""

 [*] Setiap file wordlist yang anda buat akan disimpan pada folder "hasil_word" di folder script ini"""+reset

#STARTUP
    print(banner)
    c = ""
    print(kelabu+"\n ["+banorange+"ALGORITM"+reset+kelabu+"] "+orange+"Anda menggunakan script ALGORITM untuk membuat wordlist"+reset)
    panjang = input(kelabu+" ["+banhijau+"?"+reset+kelabu+"] Masukkan panjang kata untuk wordlist(1-100): "+reset)
    if panjang is c:
        print(kelabu+"\n ["+banmerah+"!"+reset+kelabu+"]"+merah+" Masukkan jumlah panjang kata!\n"+reset);sys.exit()
    print(kelabu+"""["""+banorange+"""SELECT"""+reset+kelabu+"""] Pilih salah satu!"""+borange+"""
 (1) Gunakan huruf saja
 (2) Gunakan angka saja
 (3) Gunakan angka dan huruf saja
 (4) Gunakan semua termasuk simbol"""+reset)
    number = input(kelabu+" ["+banhijau+"?"+reset+kelabu+"] Pilih salah satu?: "+reset)
    total = input(kelabu+" ["+banhijau+"?"+reset+kelabu+"] Jumlah kata dalam Wordlist yang akan dibuat: "+reset)
    th = input(kelabu+" ["+banorange+"?"+reset+kelabu+"] Jumlah threads yang akan digunakan: "+reset)
    file_name = input(kelabu+" ["+banhijau+"?"+reset+kelabu+"] Masukkan nama file untuk file wordlist anda(*.txt): "+reset)
    if file_name is c:
        date = datetime.datetime.now()
        timestamp = date.strftime("%Y%m%d_%H%M%S")
        file_name = "hasil_word/"+timestamp+".txt"
        print(kelabu+'\n ['+banorange+'*'+reset+kelabu+']'+putih+' Nama file kosong. Nama default akan digunakan "'+hijau+file_name+reset+'"')
    
#CREATE
    print(kelabu+"\n ["+banhijau+"INFO"+reset+kelabu+"] "+orange+"Wordlist sedang dibuat. Tekan CTRL+C untuk keluar"+reset)
    if number.lower() == "4":
        abjad = '''abcdefghijklmnopqrstuvwxyz1234567890@#$_&-+()/*"':;!?~`|•√π÷×¶∆\}{=°^¥€¢£%©®™✓[]"'''
    if number.lower() == "1":
        abjad = "abcdefghijklmnopqrstuvwxyz"
    if number.lower() == "2":
        abjad = "1234567890"
    if number.lower() == "3":
        abjad = "abcdefghijklmnopqrstuvwxyz1234567890"
    try:
        def generate_random_word():
            return ''.join(random.choice(abjad) for _ in range(int(panjang)))
        words_per_thread = int(total)
        def thread_task():
            with open("hasil_word/"+file_name, 'w') as f:
                for j in range(words_per_thread):
                    word = generate_random_word()
                    f.write(word+"\n")
                    print(kelabu+"\r ["+banorange+"#"+reset+kelabu+"]"+hijau+" Generating "+str(file_name)+": "+banhijau, j + 1, "/", words_per_thread, reset+" words", end='')
                    sys.stdout.flush()
            print(putih+"\n ["+banorange+"*"+reset+putih+"] DONE!!"+reset)
        
        extra_words = int(total) % int(th)
        threads = []
        for i in range(int(th)):
            word_count = words_per_thread + (1 if i < extra_words else 0)
            t = threading.Thread(target=lambda wc=panjang: thread_task())
        threads.append(t)
        t.start()

        for t in threads:
            t.join()
        print(kelabu+" ["+banhijau+"DONE"+reset+kelabu+"]"+putih+" File disimpan pada folder 'hasil_word/"+file_name+"'\n"+reset)

    except (KeyboardInterrupt, EOFError): print(reset+kelabu+"\n ["+banhijau+"*"+reset+kelabu+"] "+putih+"File telah dibuat! File disimpan dengan nama "+hijau+file_name+reset+putih+" pada folder hasil_word"+reset);sys.exit()
except (KeyboardInterrupt, EOFError): print(merah+"\n [*] EXIT!!"+reset);sys.exit()