# Generated by Django 3.2.2 on 2021-05-26 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_student_login_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='login_id',
            field=models.CharField(max_length=12),
        ),
    ]