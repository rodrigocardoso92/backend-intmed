from django.urls import path
from django.conf.urls import include, url

from backend.apps.medicos.views import (
    ListarMedicos,
    detalhes_medico,
    ListarEspecialidades,
    detalhes_especialidade
)

urlpatterns = [
    path('api/medicos/', include([
        path('', ListarMedicos.as_view(), name='listar_medicos'),
        path('<int:pk>', detalhes_medico, name='detalhes_medico')
    ])),
    path('api/especialidades/', include([
        path('', ListarEspecialidades.as_view(), name='listar_especialidades'),
        path('<int:pk>', detalhes_especialidade, name='detalhes_especialidade')
    ]))
]
