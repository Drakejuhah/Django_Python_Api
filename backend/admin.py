from django.contrib import admin
from django.contrib.auth.models import User
from backend.models import Product
from django.utils.html import format_html
# Register your models here.


class BackendAmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="80" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['id', 'name', 'price', 'descpription', 'image_tag', 'user']

    # User Should Only see his id in selection
    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(id=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# User Should Only see products that belong to him
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


admin.site.register(Product, BackendAmin)
