# Generated by Django 4.2.16 on 2024-09-15 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competition_lifting', '0003_competitor_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competitor',
            options={},
        ),
        migrations.RenameField(
            model_name='competitor',
            old_name='heigth',
            new_name='height',
        ),
        migrations.CreateModel(
            name='Lift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('competitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lift_history', to='competition_lifting.competitor')),
            ],
        ),
        migrations.AddField(
            model_name='competitor',
            name='latest_lift',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='latest_for', to='competition_lifting.lift'),
        ),
    ]
