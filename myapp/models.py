from django.db import models

class ip_table(models.Model):
    ip=models.CharField(max_length=50)

    def __str__(self):
        return self.ip
