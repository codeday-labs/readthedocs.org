# Generated by Django 3.2.11 on 2022-02-14 16:38

from django.db import migrations
from django.db.models import Q
from django.utils import timezone


def populate_null_fields(apps, schema_editor):
    now = timezone.now()
    query = Q(created__isnull=True) | Q(modified__isnull=True)
    Project = apps.get_model('projects', 'Project')
    Project.objects.filter(query).update(
        created=now,
        modified=now,
    )

    ImportedFile = apps.get_model('projects', 'ImportedFile')
    ImportedFile.objects.filter(query).update(
        created=now,
        modified=now,
    )

    Notification = apps.get_model('projects', 'Notification')
    Notification.objects.filter(query).update(
        created=now,
        modified=now,
    )

    Domain = apps.get_model('projects', 'Domain')
    Domain.objects.filter(query).update(
        created=now,
        modified=now,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0087_use_booleanfield_null'),
    ]

    operations = [
        migrations.RunPython(populate_null_fields)
    ]