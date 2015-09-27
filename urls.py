# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import *

#url patterns
urlpatterns = patterns(
    
    'api.views',
    url(r'^user/$', UserAppList.as_view() , name='userapp.list'),
    url(r'^tipouser/$', TipoUserAppList.as_view(), name='tipouserapp.list'),
    url(r'^oficio/$', OficioList.as_view(), name='oficio.list'),
    url(r'^tipotrabajo/$', TipoTrabajoList.as_view(), name='tipotrabajo.list'),
    url(r'^empresa/$', EmpresaList.as_view(), name='empresa.list'),
    url(r'^vacante/$', VacanteList.as_view(), name='vacante.list'),
    url(r'^salario/$', SalarioList.as_view(), name='salario.list'),
    url(r'^user/detail/(?P<pk>[0-9]+)$', UserAppDetail.as_view() , name='userapp.detail'),
    url(r'^tipouser/detail/(?P<pk>[0-9]+)$', TipoUserAppDetail.as_view(), name='tipouserapp.detail'),
    url(r'^vacante/detail/(?P<pk>[0-9]+)$', VacanteDetail.as_view(), name='vacante.detail'),
    url(r'^empresa/detail/(?P<pk>[0-9]+)$', EmpresaDetail.as_view(), name='empresa.detail'),
    url(r'^tipotrabajo/detail/(?P<pk>[0-9]+)$', TipoTrabajoDetail.as_view(), name='tipotrabajo.detail'),
    url(r'^oficio/detail/(?P<pk>[0-9]+)$', OficioDetail.as_view(), name='oficio.detail'),
    url(r'^salario/detail/(?P<pk>[0-9]+)$', SalarioDetail.as_view(), name='salario.detail'),
    #authentication shit login_validation
    url(r'^auth/', LoginValidation.as_view(), name='login.validation'),
    #urls especiales bitch!!! UserAppDetailIOS  VacanteListByEmpresa
    url(r'^ios/user/detail/(?P<pk>[0-9]+)$', UserAppDetailIOS.as_view(), name='userapp.ios.detail'),
    url(r'^ios/empresa/detail/(?P<pk>[0-9]+)$', EmpresaDetailIOS.as_view(), name='empresa.ios.detail'),
    #Complex pettitions VacanteListByFilters  UserAppListByFilters
    url(r'^vacanteByEmpresa/$', VacanteListByEmpresa.as_view(), name='vacante.listbyempresa'),
    url(r'^vacanteByFilters/$', VacanteListByFilters.as_view(), name='vacante.listbyfilters'),
    url(r'^userByFilters/$', UserAppListByFilters.as_view(), name='user.listbyfilters'),
)#End of url patterns 