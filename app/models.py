from django.db import models
from django.contrib.auth.models import User


# 🧠 MAIN POST MODEL
class TravelPost(models.Model):

    CATEGORY_CHOICES = [
        ('story', 'Story'),
        ('guide', 'Guide'),
        ('experience', 'Experience'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()

    # optional extra content field (for blog detail pages)
    content = models.TextField(blank=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    picture = models.ImageField(upload_to='guides/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # ❤️ LIKE SYSTEM (FIXED)
    likes = models.ManyToManyField(User, blank=True, related_name="liked_posts")

    def __str__(self):
        return self.title

    # helper function (optional but useful)
    def total_likes(self):
        return self.likes.count()


# 💬 COMMENT MODEL
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    post = models.ForeignKey(
        TravelPost,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"
    

    
class Guide(models.Model):
    SPECIALTY_CHOICES = [
        ('k2', 'K2 Base Camp'),
        ('alpine', 'Alpine Mountaineering'),
        ('culture', 'Cultural Heritage'),
        ('photo', 'Photography'),
    ]

    REGION_CHOICES = [
        ('Skardu', 'Skardu'),
        ('Hunza', 'Hunza'),
        ('Swat', 'Swat'),
        ('Kalam', 'Kalam'),
    ]

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='guides/', null=True, blank=True)

    specialty = models.CharField(max_length=100, choices=SPECIALTY_CHOICES)
    experience = models.IntegerField()

    location = models.CharField(max_length=100, choices=REGION_CHOICES)

    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name 


class Booking(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guide = models.ForeignKey('Guide', on_delete=models.CASCADE)

    date = models.DateField()   # ⭐ IMPORTANT FIX
    message = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True, null=True) # ⭐ IMPORTANT FIX

    def __str__(self):
        return f"{self.user.username} - {self.guide.name} ({self.status})"



