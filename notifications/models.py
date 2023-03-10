from django.db import models
from users.models import User

# Create your models here.
class Notice(models.Model):
    TAGS = (
        ('Leave', 'Leave'),
        ('General', 'General'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100, choices=TAGS)
    on_leave_from = models.DateField(null=True)
    on_leave_till = models.DateField(null=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name}-{self.tag} ({self.created_on})"