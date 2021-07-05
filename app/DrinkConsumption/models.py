from django.db import models
from django.contrib.auth.models import User


class Container(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.FloatField(help_text="Capacity of the container in Liters.")
    def __str__(self):
        return self.name + " (" + str(self.capacity) + " L)"


class Product(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class ProductContainer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    def __str__(self):
        return self.product.name + " - " + self.container.__str__()


class PersonnalContainer(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    capacity = models.FloatField(help_text="Capacity of the container in Liters.")
    cost = models.FloatField(default=0, help_text="Cost of a filling in CAD$")
    def __str__(self):
        return self.name + " (" + str(self.capacity) + " L)"


class PersonnalTag(models.Model):
    uid = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    linked_container = models.ForeignKey(PersonnalContainer, on_delete=models.CASCADE)
    def __str__(self):
        return self.uid


class PersonnalConsumption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(PersonnalTag, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductContainer, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + " - " + self.product.product.name
