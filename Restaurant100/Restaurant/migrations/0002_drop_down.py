# Generated by Django 3.1.7 on 2021-04-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drop_Down',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DropDown', models.CharField(choices=[('Drop Down 1', 'Drop Down 1'), ('Deep Drop Down', (('Deep Drop Down 1', 'Deep Drop Down 1'), ('Deep Drop Down 2', 'Deep Drop Down 2'), ('Deep Drop Down 3', 'Deep Drop Down 3'), ('Deep Drop Down 4', 'Deep Drop Down 4'), ('Deep Drop Down 5', 'Deep Drop Down 5'))), ('Drop Down 2', 'Drop Down 2'), ('Drop Down 3', 'Drop Down 3'), ('Drop Down 4', 'Drop Down 4')], max_length=60)),
            ],
        ),
    ]
