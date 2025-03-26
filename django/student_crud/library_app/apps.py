from django.apps import AppConfig # type: ignore


class LibraryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library_app'
