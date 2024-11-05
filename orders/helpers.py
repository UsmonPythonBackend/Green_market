from django.db import models

class OrderStatus(models.TextChoices):
    PROCESSING = 'process', 'Processing'
    SUCCESS = 'success', 'Success'

class PaymentStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    PROCESSING = 'processing', 'Processing'
    COMPLETED = 'completed', 'Completed'
    FAILED = 'failed', 'Failed'
    CANCELLED = 'cancelled', 'Cancelled'
