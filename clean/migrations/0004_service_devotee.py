# Generated by Django 3.0.3 on 2021-09-16 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clean', '0003_auto_20210916_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='devotee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='clean.Devotee'),
        ),
    ]
