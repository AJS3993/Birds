# Generated by Django 2.2.6 on 2019-12-17 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1)),
                ('bird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Bird')),
            ],
        ),
    ]
