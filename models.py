from django.db import models


class Project(models.Model):

    project_name = models.CharField(max_length=100)

    project_description = models.TextField()

    def __str__(self):

        return self.project_name


class Team(models.Model):

    member_name = models.CharField(max_length=100)

    role = models.CharField(max_length=100)

    def __str__(self):

        return self.member_name


class Task(models.Model):

    task_name = models.CharField(max_length=100)

    task_status = models.CharField(max_length=50)

    project = models.ForeignKey(Project,on_delete=models.CASCADE)

    team = models.ForeignKey(Team,on_delete=models.CASCADE)

    def __str__(self):

        return self.task_name