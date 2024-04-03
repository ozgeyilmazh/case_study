from django.db import models


class ECommerceApplication(models.Model):
    PLATFORM_CHOICES = (
        ('Trendyol', 'Trendyol'),
        ('Hepsiburada', 'Hepsiburada'),
        ('Amazon', 'Amazon')
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    store_url = models.URLField(null=True, blank=True)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.platform}"
