# Generated by Django 3.0.6 on 2020-05-26 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200525_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(help_text='2020/05/26 10:25:00', verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('Do', 'Do'), ('Done', 'Done'), ('ToDo', 'ToDO')], default='ToDo', max_length=4),
        ),
    ]
