from django.db import models
from django.core.exceptions import ValidationError


def validate_transaction_reference_required(value):
    if value is None or value.strip() == '':
        raise ValidationError(
            'Transaction reference is required when paid is True.')


class Donation(models.Model):
    FREQUENCY_CHOICES = (
        ('one-time', 'One-Time'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('semi-annually', 'Every 6 Months'),
        ('annually', 'Annually'),
        # Add more choices as needed
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Added paystack_transaction_reference field
    reference = models.CharField(
        max_length=100, null=True, blank=True, validators=[validate_transaction_reference_required])
    paid = models.BooleanField(default=False, null=True, blank=True)  # Added paid status field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Added updated_at field

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.amount} ({self.frequency})"

    class Meta:
        ordering = ['-created_at']
