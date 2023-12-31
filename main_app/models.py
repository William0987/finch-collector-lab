from django.db import models
from django.urls import reverse

SEEDS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'toy_id': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Birdseed(models.Model):
    date = models.DateField('feeding date')
    seed = models.CharField(
        max_length=1,
        choices=SEEDS,
        default=SEEDS[0][0]
    )

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_seed_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
