# Generated by Django 4.2.16 on 2025-01-17 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sets', models.PositiveIntegerField()),
                ('rep_range_min', models.PositiveIntegerField()),
                ('rep_range_max', models.PositiveIntegerField()),
                ('weight_min', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight_max', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.weekday')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout_days', to='workouts.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('exercises', models.ManyToManyField(through='workouts.WorkoutDay', to='workouts.exercise')),
            ],
        ),
        migrations.AddField(
            model_name='workoutday',
            name='workout_week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout_days', to='workouts.workoutweek'),
        ),
    ]
