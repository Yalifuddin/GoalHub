import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('sepatu bola', 'Sepatu Bola'),
        ('jersey', 'Jersey'),
        ('bola', 'Bola'),
        ('aksesoris', 'Aksesoris'),
        ('alat latihan', 'Alat Latihan'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    stok = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    @property
    def increment_stok(self, jumlah):
        self.stok += jumlah
        self.save()

    def decrement_stok(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            self.save()
        else:
            raise ValueError("Stok tidak mencukupi")