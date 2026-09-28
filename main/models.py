import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ("internship", "Internship"),
        ("research", "Research"),
        ("volunteer", "Volunteer"),
        ("part-time", "Part-Time"),
        ("full-time", "Full-Time"),
        ("freelance", "Freelance"),
        ("organization", "Organization"),
        ("commitee", "Commitee"),
        ("seminar", "Seminar"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default="full-time",
    )
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    tech_stack = models.CharField(max_length=255, blank=True, default="")
    experience_url = models.URLField(blank=True)
    experience_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(User, related_name="starred_experiences", blank=True)

    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None

class Skills(models.Model):
    SKILLS_CHOICES = [
            ("hard skill", "Hard skill"),
            ("soft skill", "Soft skill"),
            ("language", "Language"),
        ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    category = models.CharField(
        max_length=20,
        choices=SKILLS_CHOICES,
        default="hard skill",
    )
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    tech_stack = models.CharField(max_length=255, blank=True, default="")
    skills_url = models.URLField(blank=True)
    skills_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(User, related_name="starred_skills", blank=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model):
    EDUCATION_CHOICE = [
        ("kuliah", "Kuliah"),
        ("sma", "SMA"),
        ("smp", "SMP"),
        ("sd", "SD"), 
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=EDUCATION_CHOICE,
        default="sd",
    )
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    tech_stack = models.CharField(max_length=255, blank=True, default="")
    education_url = models.URLField(blank=True)
    education_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(User, related_name="starred_educations", blank=True)
        
    def __str__(self):
        return self.title
        
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Project(models.Model):
    PROJECT_CHOICE = [
        ("it", "IT"),
        ("non-it", "Non-IT")
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=PROJECT_CHOICE,
        default="it",
    )
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    tech_stack = models.CharField(max_length=255, blank=True, default="")
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )


        
    def __str__(self):
        return self.title
        
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Achievement(models.Model):
    ACHIEVEMENT_CHOICE = [
        ("internasional", "Internasional"),
        ("provinsi", "Provinsi"),
        ("kabupaten", "Kabupaten"),
        ("sekolah", "Sekolah"), 
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=ACHIEVEMENT_CHOICE,
        default="sekolah",
    )
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    tech_stack = models.CharField(max_length=255, blank=True, default="")
    achievement_url = models.URLField(blank=True)
    achievement_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(
            User, related_name="starred_achievements", blank=True
        )
        
    def __str__(self):
        return self.title
        
    @property
    def is_ongoing(self):
        return self.ended_at is None


