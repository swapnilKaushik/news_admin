from django.contrib import admin

from .models import City, Country, State


class CityInline(admin.TabularInline):
    model = City


class StateInline(admin.TabularInline):
    inlines = [CityInline]
    model = State


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    inlines = [StateInline]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    inlines = [CityInline]


admin.site.register(City)
