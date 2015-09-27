from django.shortcuts import render
from appusers.models import UserApp, TipoUserApp
from appusers.serializers import UserAppSerializer, TipoUserAppSerializer, OficioSerializer
from empresas.models import Oficio, TipoTrabajo, Empresa, Vacante, Salario
from empresas.serializers import TipoTrabajoSerializer, EmpresaSerializer, VacanteSerializer, SalarioSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from django.views.generic import TemplateView
from rest_framework import generics
from .Permissions import QuietBasicAuthentication

"""
User app list class api view
"""
class UserAppList( generics.ListCreateAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializer

    def list( self, request, *args, **kwargs ):
        """ list function that lists all the objects """
        instance = self.filter_queryset( self.get_queryset() )
        page = self.paginate_queryset( instance )
        if page is not None :
            serializer = self.get_pagination_serializer( page)
        else:
            serializer = self.get_serializer( instance, many=True )
        
        data = {
            "data" : serializer.data
        }
        
        return Response(data)
    #End of list function   

#End of this mutherfucker shit class

class UserAppDetailIOS( generics.CreateAPIView, generics.UpdateAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializer
    
    def create(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    #End of create function
    
#End of user app detail ios api view

class EmpresaDetailIOS( generics.CreateAPIView, generics.UpdateAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    
    def create(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    #End of create function
    
#End of user app detail ios api view

"""
User app detail class api view
"""
class UserAppDetail( generics.RetrieveUpdateDestroyAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializer
    
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    
#End of userapp detail class

"""
TipoUserApp list class api view
"""
class TipoUserAppList( generics.ListCreateAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = TipoUserApp.objects.all()
    serializer_class = TipoUserAppSerializer
    
    def list( self, request, *args, **kwargs ):
        """ list function that lists all the objects """
        instance = self.filter_queryset( self.get_queryset() )
        page = self.paginate_queryset( instance )
        if page is not None :
            serializer = self.get_pagination_serializer( page)
        else:
            serializer = self.get_serializer( instance, many=True )
        
        data = { 
            "data" : serializer.data
        }
        
        return Response(data)
    #End of list function   
    
#End of tipo user app list api view

"""
Tipo user app list api view
"""
class TipoUserAppDetail( generics.RetrieveUpdateDestroyAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = TipoUserApp.objects.all()
    serializer_class = TipoUserAppSerializer

    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
        
#End of tipo user app detail class

"""
Vacante list
"""
class VacanteList( generics.ListCreateAPIView  ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = Vacante.objects.all()
    serializer_class = VacanteSerializer

    def list( self, request, *args, **kwargs ):
        """ list function that lists all the objects """
        instance = self.filter_queryset( self.get_queryset() )
        page = self.paginate_queryset( instance )
        if page is not None :
            serializer = self.get_pagination_serializer( page)
        else:
            serializer = self.get_serializer( instance, many=True )
        
        data = { 
            "data" : serializer.data
        }
        
        return Response(data)
    #End of list function    
    
#End of vacante list function

"""
Vacante list by empresa
"""
class VacanteListByEmpresa( generics.ListAPIView  ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = Vacante.objects.all()
    serializer_class = VacanteSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        empresa_id = self.request.GET['empresa']
        return Vacante.objects.filter(empresa=empresa_id)
        
    def list(self, request, *args, **kwargs):
        """ list function that lists all the objects """
        instance = self.filter_queryset( self.get_queryset() )
        page = self.paginate_queryset( instance )
        if page is not None :
            serializer = self.get_pagination_serializer( page)
        else:
            serializer = self.get_serializer( instance, many=True )
        
        data = { 
            "data" : serializer.data
        }
        
        return Response(data)
    #End of list function    
    
#End of vacante list function

"""
Vacante list by empresa
"""
class VacanteListByFilters( generics.ListAPIView  ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = Vacante.objects.all()
    serializer_class = VacanteSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        tipo_trabajo_id = self.request.GET['tipo_trabajo']
        oficio_id = self.request.GET['oficio']
        salario_id = self.request.GET['salario']
        estado = self.request.GET['estado']
        return Vacante.objects.filter(oficio=oficio_id, tipo_trabajo=tipo_trabajo_id, salario=salario_id )
        
    def list(self, request, *args, **kwargs):
        """ list function that lists all the objects """
        instance = self.filter_queryset( self.get_queryset() )
        page = self.paginate_queryset( instance )
        if page is not None :
            serializer = self.get_pagination_serializer( page)
        else:
            serializer = self.get_serializer( instance, many=True )
        
        data = { 
            "data" : serializer.data
        }
        
        return Response(data)
    #End of list function    
    
#End of vacante list function

"""
Vacante list by empresa
"""
class UserAppListByFilters( generics.ListAPIView  ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        oficio_id = self.request.GET['oficio']
        estado = self.request.GET['estado']
        return UserApp.objects.filter(oficio=oficio_id, estado=estado )
        
    def list(self, request, *args, **kwargs):
        """ list function that lists all the objects """
        instance = self.filter_queryset( self.get_queryset() )
        page = self.paginate_queryset( instance )
        if page is not None :
            serializer = self.get_pagination_serializer( page)
        else:
            serializer = self.get_serializer( instance, many=True )
        
        data = { 
            "data" : serializer.data
        }
        
        return Response(data)
    #End of list function    
    
#End of vacante list function


"""
Vacante detail
"""
class VacanteDetail( generics.RetrieveUpdateDestroyAPIView  ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = Vacante.objects.all()
    serializer_class = VacanteSerializer
    
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
        
#End of vacante detail class

"""
Empresa list
"""
class EmpresaList( generics.ListCreateAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    def list( self, request, *args, **kwargs ):
        """ list function that lists all the objects """
        instance = self.filter_queryset( self.get_queryset() )
        page = self.paginate_queryset( instance )
        if page is not None :
            serializer = self.get_pagination_serializer( page)
        else:
            serializer = self.get_serializer( instance, many=True )
        
        data = { 
            "data" : serializer.data
        }
        
        return Response(data)
    #End of list function   
    
#End of emrpesa list class 

"""
Empresa detail
"""
class EmpresaDetail( generics.RetrieveUpdateDestroyAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
        
#End of empresa detail class    

"""
Tipo de trabajo list
"""
class TipoTrabajoList( generics.ListCreateAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = TipoTrabajo.objects.all()
    serializer_class = TipoTrabajoSerializer
    
    def list( self, request, *args, **kwargs ):
        """ list function that lists all the objects """
        instance = self.filter_queryset( self.get_queryset() )
        page = self.paginate_queryset( instance )
        if page is not None :
            serializer = self.get_pagination_serializer( page)
        else:
            serializer = self.get_serializer( instance, many=True )
        
        data = { 
            "data" : serializer.data
        }
        
        return Response(data)
    #End of list function   
    
#End fo tipo trabajo list

"""
Tipo trabajo detail
"""
class TipoTrabajoDetail( generics.RetrieveUpdateDestroyAPIView ) :

    authentication_classes = ( QuietBasicAuthentication, )
    queryset = TipoTrabajo.objects.all()
    serializer_class = TipoTrabajoSerializer

#End of tipo trabajo detail class

"""
Oficio List
"""
class OficioList( generics.ListCreateAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = Oficio.objects.all()
    serializer_class = OficioSerializer
    
    def list( self, request, *args, **kwargs ):
        """ list function that lists all the objects """
        instance = self.filter_queryset( self.get_queryset() )
        page = self.paginate_queryset( instance )
        if page is not None :
            serializer = self.get_pagination_serializer( page)
        else:
            serializer = self.get_serializer( instance, many=True )
        
        data = { 
            "data" : serializer.data
        }
        
        return Response(data)
    #End of list function   
    
#End of oficio list class

"""
Oficio detail
"""
class OficioDetail( generics.RetrieveUpdateDestroyAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = Oficio.objects.all()
    serializer_class = OficioSerializer

    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
        
#End of oficio detail class

"""
Salario List
"""
class SalarioList( generics.ListCreateAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = Salario.objects.all()
    serializer_class = SalarioSerializer
    
    def list( self, request, *args, **kwargs ):
        """ list function that lists all the objects """
        instance = self.filter_queryset( self.get_queryset() )
        page = self.paginate_queryset( instance )
        if page is not None :
            serializer = self.get_pagination_serializer( page)
        else:
            serializer = self.get_serializer( instance, many=True )
        
        data = { 
            "data" : serializer.data
        }
        
        return Response(data)
    #End of list function   
    
#End of salario list class

"""
Salario detail
"""
class SalarioDetail( generics.RetrieveUpdateDestroyAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = Salario.objects.all()
    serializer_class = SalarioSerializer

    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
        
#End of salario detail class

"""
login_validation api view
"""
class LoginValidation( generics.ListCreateAPIView ) :
    
    authentication_classes = ( QuietBasicAuthentication, )
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializer
    
    def create(self, request, *args, **kwargs):
        """
        detail for the user app detail function
        """
        try:
            user = UserApp.objects.get( email = request.data[ "email" ] )
        except UserApp.DoesNotExist:
            return Response( status = status.HTTP_400_BAD_REQUEST )
            
        if user :
            if user.password == request.data[ "password" ] :
                serializer = UserAppSerializer( user )
                data = {
                    'data' : serializer.data  
                }
                return Response( data )
            else :
                return Response( status = status.HTTP_204_NO_CONTENT )
    #End of create function 
    
#End of login_validation class