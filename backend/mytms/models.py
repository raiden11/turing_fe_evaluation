
import uuid
from django.db import models

class Campaign(models.Model):
    """
    Campaign represents a group of trainers and tasks associated with them.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, help_text="Name of the campaign")

    created_at = models.DateTimeField(auto_now_add=True, help_text="Time when the campaign was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Time when the campaign was last updated")

    class Meta:
        ordering = ['name']

class Member(models.Model):
    """
    Member represents an individual who is either a trainer or a lead.
    """
    ROLE_CHOICES = [
        ('trainer', 'Trainer'),
        ('lead', 'Lead'),
    ]

    email = models.EmailField(primary_key=True, help_text="Email address of the member")
    full_name = models.CharField(max_length=255, help_text="Full name of the member")
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, help_text="Role of the member (Trainer or Lead)")

    created_at = models.DateTimeField(auto_now_add=True, help_text="Time when the member was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Time when the member was last updated")

    class Meta:
        ordering = ['full_name']

class Task(models.Model):
    """
    Task represents a task submitted by a trainer or reviewed by a lead.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('completed', 'Completed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, help_text="Name of the task")
    score = models.IntegerField(help_text="Score of the task")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, help_text="Status of the task")

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="tasks", help_text="Campaign this task belongs to")
    trainer = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="tasks", limit_choices_to={'role': 'trainer'}, help_text="Trainer who submitted the task")
    lead = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True, related_name="reviewed_tasks", limit_choices_to={'role': 'lead'}, help_text="Lead who reviewed the task")

    created_at = models.DateTimeField(auto_now_add=True, help_text="Time when the task was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Time when the task was last updated")

    class Meta:
        ordering = ['name']

