# Generated by Django 3.2.2 on 2021-05-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_student_stu_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='login_id',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
