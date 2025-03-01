from django.db import models

class Advice(models.Model):
    text = models.TextField('Texto do Conselho', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text[:50]