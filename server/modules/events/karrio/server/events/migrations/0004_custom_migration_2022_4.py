# Generated by Django 3.2.3 on 2022-03-28 03:40

from django.db import migrations


def forwards_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Event = apps.get_model("events", "Event")
    Webhook = apps.get_model("events", "Webhook")

    for event in Event.objects.using(db_alias).filter(type__contains="."):
        event.type = event.type.replace(".", "_")
        event.save()

    for webhook in Webhook.objects.using(db_alias).all():
        webhook.enabled_events = [e.replace(".", "_") for e in webhook.enabled_events]
        webhook.save()


def reverse_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Event = apps.get_model("events", "Event")
    Webhook = apps.get_model("events", "Webhook")

    for event in Event.objects.using(db_alias).filter(type__contains="."):
        event.type = event.type.replace("_", ".")
        event.save()

    for webhook in Webhook.objects.using(db_alias).all():
        webhook.enabled_events = [e.replace("_", ".") for e in webhook.enabled_events]
        webhook.save()


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_auto_20220303_1210"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
