"""Kérj be egy jelszót, és ha megegyezik a „titok” szóval, írd ki: „Belépés engedélyezve!”, különben „Helytelen jelszó!”.
"""

password = input("Kérem a jelszót: ")
if password == "juhuuu":
    print('A jelszó helyes')
else:
    print('A jelszó helytelen')

