
banner = '''
   ______                _ __   ______                           __            
  / ____/___ ___  ____ _(_) /  / ____/__  ____  ___  _________ _/ /_____  _____
 / __/ / __ `__ \/ __ `/ / /  / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
/ /___/ / / / / / /_/ / / /  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
\____/_/ /_/ /_/\__,_/_/_/   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
'''
# ganti arthur besok nya meninggal
name = "Acep Triana"
prodi = "Sistem Informasi"
tools = "Auto Generate Email Uniku"
version = "V.1 Beta Release"

info = f'''
Arthur: {name}
Prodi: {prodi}
Tools: {tools}
Version: {version}
'''

print(banner)
print(info)

import os
from colorama import init, Fore

# Inisialisasi colorama
init()

def generate_email():
    fakultas_list = {
        '1': {'name': 'Ilmu Komputer (FKOM)', 'prodi': {
            '1': {'name': 'Sistem Informasi', 'kode': '0910'},
            '2': {'name': 'Teknik Informatika', 'kode': '0810'},
            '3': {'name': 'Desain Komunikasi Visual', 'kode': '1810'},
            '4': {'name': 'Teknik Sipil', 'kode': '2210'},
            '5': {'name': 'Manajemen Informatika', 'kode': '1110'}
        }},
        '2': {'name': 'Ekonomi & Bisnis (FEB)', 'prodi': {
            '1': {'name': 'Manajemen', 'kode': '0510'},
            '2': {'name': 'Akuntansi', 'kode': '0610'}
        }},
        '3': {'name': 'Keguruan & Ilmu Pendidikan (FKIP)', 'prodi': {
            '1': {'name': 'Pendidikan Bahasa & Sastra Indonesia', 'kode': '0110'},
            '2': {'name': 'Pendidikan Biologi', 'kode': '0210'},
            '3': {'name': 'Pendidikan Ekonomi', 'kode': '0310'},
            '4': {'name': 'Pendidikan Bahasa Inggris', 'kode': '0410'},
            '5': {'name': 'Pendidikan Guru Sekolah Dasar', 'kode': '1510'},
            '6': {'name': 'Pendidikan Matematika', 'kode': '1610'}
        }},
        '4': {'name': 'Hukum (FH)', 'prodi': {
            '1': {'name': 'Ilmu Hukum', 'kode': '1410'}
        }},
        '5': {'name': 'Kehutanan & Ilmu Lingkungan (FHUT)', 'prodi': {
            '1': {'name': 'Kehutanan', 'kode': '0710'},
            '2': {'name': 'Ilmu Lingkungan', 'kode': '1910'}
        }}
    }

    print("Pilih Fakultas:")
    for key, value in fakultas_list.items():
        print(f"{Fore.GREEN}{key}. {value['name']}{Fore.RESET}")
    
    fakultas = input("Masukkan pilihan Anda: ")
    
    if fakultas not in fakultas_list.keys():
        print(f"{Fore.RED}Pilihan Fakultas tidak valid.{Fore.RESET}")
        return
    
    fakultas_name = fakultas_list[fakultas]['name']
    
    prodi_list = fakultas_list[fakultas]['prodi']
    
    print("Pilih Prodi:")
    for key, value in prodi_list.items():
        print(f"{Fore.GREEN}{key}. {value['name']}{Fore.RESET}")
    
    prodi = input("Masukkan pilihan Anda: ")
    
    if prodi not in prodi_list.keys():
        print(f"{Fore.RED}Pilihan Prodi tidak valid.{Fore.RESET}")
        return
    
    prodi_name = prodi_list[prodi]['name']
    kode = prodi_list[prodi]['kode']
    
    angkatan_list = {
        '1': '2018',
        '2': '2019',
        '3': '2020',
        '4': '2021',
        '5': '2022',
        '6': '2023'
    }
    
    print("Pilih Angkatan:")
    for key, value in angkatan_list.items():
        print(f"{Fore.GREEN}{key}. {value}{Fore.RESET}")
    
    angkatan = input("Masukkan pilihan Anda: ")
    
    if angkatan not in angkatan_list.keys():
        print(f"{Fore.RED}Pilihan Angkatan tidak valid.{Fore.RESET}")
        return
    
    jumlah_mahasiswa = input("Masukkan jumlah mahasiswa: ")
    
    email_prefix = angkatan_list[angkatan] + kode
    
    emails = []
    for i in range(1, int(jumlah_mahasiswa) + 1):
        email = email_prefix + str(i).zfill(3) + "@uniku.ac.id"
        emails.append(email)
    
    file_path = f"result/{fakultas_name}-{prodi_name}-{angkatan}.txt"
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w') as file:
        file.write('\n'.join(emails))
    
    print(f"{Fore.GREEN}Email berhasil dibuat dan disimpan di: {file_path}{Fore.RESET}")


generate_email()
