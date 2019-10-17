from django.db import models
from django.utils import timezone

from django.core.validators import validate_ipv4_address
from users.models import CustomUser


class Environment(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Agent(models.Model):
    env = models.ForeignKey(
            Environment,
            on_delete=models.deletion.DO_NOTHING,
            related_name='environment',
        )
    version = models.CharField(max_length=5)
    address = models.GenericIPAddressField(
            max_length=39,
            validators=[validate_ipv4_address],
            default='255.255.255.255',
            )

    def __str__(self):
        return self.address


class Event(models.Model):
    EVENT_TYPES = [
        ('C', 'Critical'),
        ('D', 'Debug'),
        ('E', 'Error'),
        ('W', 'Warning'),
        ('I', 'Info')
    ]
    level = models.CharField(
            max_length=20,
            choices=EVENT_TYPES,
            null=True
            )
    details = models.TextField(null=True)
    archived = models.BooleanField(default=False)
    date = models.DateTimeField()
    agent = models.ForeignKey(
        Agent,
        on_delete=models.deletion.DO_NOTHING,
        related_name='agent'
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.deletion.DO_NOTHING,
        related_name='user'
        )

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date = timezone.now()
        return super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.date
