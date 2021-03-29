from django.contrib import admin

from .models import Plato, TipoDePlato, Ingrediente

class PlatoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'precio', 'publicacion']}),
        ('Detalles del plato', {'fields': ['tipo','ingredientes']}),
    ]
    filter_horizontal = ('ingredientes',)



admin.site.register(Plato, PlatoAdmin)
admin.site.register(TipoDePlato)
admin.site.register(Ingrediente)
