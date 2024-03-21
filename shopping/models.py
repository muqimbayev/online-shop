from django.db import models
from django.contrib.auth.hashers import make_password
from datetime import date

class Users(models.Model):
    nomi = models.CharField(max_length=50)
    telefon_raqami = models.CharField(max_length=15)
    parol = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self.parol:
            self.parol = make_password(self.parol)
        super(Users, self).save(*args, **kwargs)

    def __str__(self):
        return self.nomi

class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nomi

class Buyurtma(models.Model):
    foydalanuvchi_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdori = models.PositiveIntegerField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.narxi:
            self.narxi = self.hisoblovchi_metod()
        super(Buyurtma, self).save(*args, **kwargs)

    def hisoblovchi_metod(self):
        mahsulot_narxi = self.mahsulot.narxi

        miqdori = self.miqdori
        chegirma_obj = Chegirma.objects.filter(mahsulot=self.mahsulot).first()
        if chegirma_obj:
            chegirma_foizi = chegirma_obj.chegirma_foizi
            chegirma_muddati = chegirma_obj.chegirma_muddati
            hozirgi_sana = date.today()
            if hozirgi_sana < chegirma_muddati:
                mahsulot_narxi -= (mahsulot_narxi * chegirma_foizi / 100)
                return mahsulot_narxi * miqdori
        return mahsulot_narxi * miqdori

    def __str__(self):
        return str(self.mahsulot)

class Chegirma(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    chegirma_foizi = models.DecimalField(max_digits=5, decimal_places=2)
    chegirma_muddati = models.DateField()

    def __str__(self):
        return str(self.mahsulot)
