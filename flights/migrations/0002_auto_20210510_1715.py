# Generated by Django 3.2 on 2021-05-10 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='flight',
            name='source',
        ),
        migrations.AddField(
            model_name='flight',
            name='origin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='flights.airport'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flight',
            name='destions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival', to='flights.airport'),
        ),
    ]
