from django.contrib import admin
from django.contrib.auth.models import User
from backend.models import Product

# Register your models here.


class BackendAmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'descpription', 'image', 'user']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(id=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

        def get_queryset(self, request):
            qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


admin.site.register(Product, BackendAmin)
