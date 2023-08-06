from django.db import models

# Create your models here.
class Tamu(models.Model):
    Nama    = models.CharField(max_length=20)
    NIK     = models.CharField(max_length=18)
    Alamat  = models.CharField(max_length=100)
    no_telp = models.CharField(max_length=13)
    KTP     = models.ImageField(upload_to="uploads/image/")

    def __str__(self):
        return "{}".format(self.Nama)
    
class Datang(models.Model):

    Nama            = models.CharField(max_length=21)
    Tanggal_Datang  = models.DateField()
    Hari_Penginapan = models.CharField(max_length=2)

    def __str__(self):
        return "{}".format(self.Nama)
    
class Pulang(models.Model):
    Nama            = models.CharField(max_length=21)
    Tanggal_Pulang  = models.DateField()
    Saran_Masukan   = models.TextField(max_length=250)

    def __str__(self):
        return "{}".format(self.Nama)