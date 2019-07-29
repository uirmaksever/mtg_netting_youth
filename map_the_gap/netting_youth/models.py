from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Cheating a bit here
from vote.models import VoteModel
# Create your models here.

#Custom User
class Profile(models.Model):
    pass
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024, null=True)
    surname = models.CharField(max_length=1024, null=True)
    birth_date = models.DateField(null=True)
    city = models.CharField(max_length=1024, null=True)
    country = models.CharField(max_length=1024, null=True)
    related_facebook = models.CharField(max_length=1024, null=True)
    # It will be social auth later on
    type_of_membership = models.CharField(null=True,
        max_length=1024,
        choices=[
            ('ngo', 'Non-Governmental Organization'),
            ('youngster', 'Youngster'),
            ('company', 'Private Sector'),
            ('public_sector', 'Public Sector')])

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# That is thematic area, problems connected to this.
class ThematicArea(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name
# It consists of tasks and this model is connected to Problem by OnetoOne
class TaskList(models.Model):
    name = models.CharField(max_length=1024)

# Tasks are actions that should be taken on for a problem.
# They could be administrative, for the organization of an event and such.
class Task(models.Model):
    related_tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    # assigned_to
    title = models.CharField(max_length=1024)
    description_text = models.TextField()
    deadline = models.DateField()

# Problem is the main object. It gets voted by users, have a discussion board and such
class Problem(VoteModel, models.Model):
    related_thematic_area = models.ForeignKey(ThematicArea, on_delete=models.PROTECT)
    title = models.CharField(max_length=1024)
    description_text = models.TextField()
    number_of_votes = models.IntegerField()
    related_tasklist = models.OneToOneField(TaskList, on_delete=models.CASCADE)
    # created_by
    # related_ngos
    # related_public_institutions
    # related_private_institutions

    def __str__(self):
        return str(self.pk) + " - " + self.title

# Youngsters vote on problems. The more vote one problem gets,
# it becomes more popular and visible.
class Vote(models.Model):
    # who
    related_problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

# Events are offline meetings that make every stakeholder meet face to face.
class Event(models.Model):
    related_problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=1024)
    description_text = models.TextField()
