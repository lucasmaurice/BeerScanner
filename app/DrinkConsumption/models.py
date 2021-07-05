from django.db import models
from django.contrib.auth.models import User


class Container(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.FloatField(help_text="Capacity of the container in Liters.")
    def __str__(self):
        return self.name + " (" + str(self.capacity) + " L)"


class Product(models.Model):
    name = models.CharField(max_length=200)
    style = models.CharField(max_length=200, blank=True, default="")
    producer = models.CharField(max_length=200, blank=True, default="")
    abv = models.FloatField(help_text="Alcohol By Volume.", default=0)
    def __str__(self):
        return self.name


class ProductContainer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    def __str__(self):
        refills = Refill.objects.all().filter(product=self)
        consumed = 0 
        for r in refills:
            consumed += r.container.capacity
        return self.product.name + " (" + str(self.container.capacity - consumed) + " L)"


class PersonalContainer(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    capacity = models.FloatField(help_text="Capacity of the container in Liters.")
    cost = models.FloatField(default=0, help_text="Cost of a filling in CAD$")
    def __str__(self):
        return self.name + " (" + str(self.capacity) + " L)"


class PersonalTag(models.Model):
    uid = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    linked_container = models.ForeignKey(PersonalContainer, on_delete=models.CASCADE)
    def __str__(self):
        return self.uid


class Refill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(PersonalTag, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(ProductContainer, on_delete=models.CASCADE)
    container = models.ForeignKey(PersonalContainer, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.user.username + " - " + self.product.product.name


class Tap(models.Model):
    name = models.CharField(max_length=200, unique=True)
    onTap = models.OneToOneField(ProductContainer, on_delete=models.CASCADE, blank=True, null=True, unique=True)
