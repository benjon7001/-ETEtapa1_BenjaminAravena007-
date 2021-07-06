from collections import namedtuple
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import form, VerColaboradores, modColaborador, dlColaborador, actl, form_colaboradores

urlpatterns = [
    path('', form, name="formulario"),
    path('form_colaboradores', form_colaboradores, name="form_colaboradores"),
    path('mostrar', VerColaboradores, name="mostrar" ),
    path('modColaborador/<id>', modColaborador, name="modColaborador"),
    path('delColaborador/<id>', dlColaborador, name="delColaborador"),
    path('actualizar', actl, name='actualizar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)