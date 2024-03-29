# Generated by Django 4.2.6 on 2023-10-30 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cards", "0002_rename_user_card_card_owner_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="card",
            name="company",
        ),
        migrations.AddField(
            model_name="card",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="card",
            name="card_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cards.cardtype"
            ),
        ),
        migrations.AlterField(
            model_name="card",
            name="start_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="cardtype",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
