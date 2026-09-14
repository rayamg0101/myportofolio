### Assignment 2
1.Kalo dari yang saya pelajari tadi, aplikasi urls.py ini membantu saya untuk mendapatkan akses terkait fitur-fitur yang ingin saya akses, seperti experience contohnya, dengan adanya urls.py, saya bisa mendapatkan akses untuk membuka halaman baru dari fitur experience itu, untuk tampilan, jujur saya masih mengikuti tutorial 2 yang saya pelajari tadi, jadi tidak begitu istimewa dan untuk modals, ia membantu saya menambahkan hal-hal yang saya ingin tambahkan dalam fitur yang saya akses, misal ke Skills, saya bisa menambahkan skill saya dengan cara from main.models import Skills
>>> Skills.objects.create(
... title="E-sports",
... category="soft skill",)
jadi masuk lah ke dalam list skill ku dan template berfungsi sebagai html atau halaman baru yang saya buat 
2.Karena jika kita mau menambahkannya di template, itu akan menjadi hard core dan itu tidak efisien buat menambahkannya, berbeda dengan python, dengan ada method:
from main.models import Skills
>>> Skills.objects.create(
... title="E-sports",
... category="soft skill",)
kita bisa menambahkan sesuka hati kita
3.Kalo makemigrations, ia hanya berfokus pada file models.py ku, sedangkan kalo migrate ia berfokus pada seluruh file-file migrasi yang belum diterapkan dan ia mengubah struktur database
