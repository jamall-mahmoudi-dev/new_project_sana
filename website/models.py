from django.db import models

# Create your models here.

class Posts(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    subject = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    discription = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'پست ها '
        verbose_name_plural = 'پست '
    
    
    def __str__(self):
        return f"{self.name} - {self.created_at} - {self.email}"
    
