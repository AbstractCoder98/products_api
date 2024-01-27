from django.contrib import admin
import django.apps as dj


class ProductsAdminArea(admin.AdminSite):
    site_header = "Products Admin Page"


models = dj.apps.get_models()
products_admin = ProductsAdminArea(name="ProductsAdmin")

for model in models:
    try:
        products_admin.register(model)
    except products_admin.sites.AreadyRegistered:
        pass
