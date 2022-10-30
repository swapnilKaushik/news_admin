from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=60)
    abbreviation = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self) -> str:
        return self.name


class State(models.Model):
    name = models.CharField(max_length=70)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='state_country')
    abbreviation = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name_plural = "States"

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(max_length=70)
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name='city_state')
    abbreviation = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self) -> str:
        return self.name
