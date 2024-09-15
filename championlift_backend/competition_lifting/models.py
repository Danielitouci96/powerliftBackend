from django.db import models

class Competitor(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    weight_class = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    latest_lift = models.OneToOneField('Lift', on_delete=models.SET_NULL, null=True, related_name='latest_for')

    def __str__(self):
        return self.name

class Lift(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE, related_name='lift_history')

    def __str__(self):
        return f"{self.name} - {self.weight}kg"


class Competition(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()

    class Meta:
        verbose_name = "Competition"
        verbose_name_plural = "Competitions"

    def __str__(self):
        return self.name


class Modality(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Modality"
        verbose_name_plural = "Modalities"

    def __str__(self):
        return self.name


class Attempt(models.Model):
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    modality = models.ForeignKey(Modality, on_delete=models.CASCADE)
    attempt_number = models.IntegerField()
    weight_lifted = models.FloatField()

    class Meta:
        verbose_name = "Attempt"
        verbose_name_plural = "Attempts"
        constraints = [
            models.CheckConstraint(
                check=models.Q(attempt_number__gte=1) & models.Q(attempt_number__lte=3),
                name='attempt_number_between_1_and_3'
            )
        ]

    def __str__(self):
        return f"{self.competitor.name} - Attempt {self.attempt_number}"
