from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
