from django.db import models

class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)  # Masa numarası (örnek: 1, 2, 3)
    is_active = models.BooleanField(default=True)      # Aktif mi (kullanımda mı)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Masa {self.number}"
