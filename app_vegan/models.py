from django.db import models

# Create your models here.
# (models.Model) -> Herdar da class model

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    contacto = models.PositiveBigIntegerField()
    password = models.CharField(max_length=20)
   
    
    def __str__(self):
        return f"User: {self.username}"

class pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    pedido = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Nº: {self.id_pedido}: {self.pedido} "