# models.py
from django.db import models

class RobotModel(models.Model):
    linear_velocity = models.FloatField()
    angular_velocity = models.FloatField()

    def __str__(self):
        return f'Linear: {self.linear_velocity}, Angular: {self.angular_velocity}'
