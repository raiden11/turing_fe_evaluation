
from django.core.management.base import BaseCommand
from mytms.models import Campaign, Member, Task
import random
import uuid

class Command(BaseCommand):
    help = 'Create dummy data for Campaign, Member, and Task models'

    def handle(self, *args, **kwargs):
        campaign1 = Campaign.objects.create(name="Campaign 1")
        campaign2 = Campaign.objects.create(name="Campaign 2")

        member1 = Member.objects.create(email="trainer1@turing.com", full_name="Trainer One", role="trainer")
        member2 = Member.objects.create(email="trainer2@turing.com", full_name="Trainer Two", role="trainer")
        lead1 = Member.objects.create(email="lead1@turing.com", full_name="Lead One", role="lead")

        Task.objects.create(name="Task 1", status="pending", score=random.randint(0, 7), campaign=campaign1, trainer=member1, lead=lead1)
        Task.objects.create(name="Task 2", status="completed", score=random.randint(0, 7), campaign=campaign1, trainer=member2, lead=lead1)
        Task.objects.create(name="Task 3", status="reviewed", score=random.randint(0, 7), campaign=campaign2, trainer=member1, lead=lead1)

        self.stdout.write(self.style.SUCCESS('Successfully created dummy data'))

