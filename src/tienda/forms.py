from dal import autocomplete
from django import forms
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.db.models import ManyToOneRel
from django.forms import DateField



from proyecto2 import settings
from .models import Factura, Producto, CategoriaProducto
    # ,Timbrado,CategoriaProducto,Producto,Existencia,TipoPago,CompraCabecera,CompraDetalle,VentaCabecera,VentaDetalle,Pagos



#Formulario factura
class FomularioFactura(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['nombre','ruc','actividad_economica','direccion','telefono','numero_timbrado','punto_emision','nro_inicial','nro_final','vigencia_desde','vigencia_hasta','estado']


# #Formulario CategoriaProducto
# class FomularioCategoriaProducto(forms.ModelForm):
#     class Meta:
#         model = CategoriaProducto
#         fields = ['', '', '', '', '', '', '', '', '', '']
#
# #Formulario CategoriaProducto
class FomularioCategoriaProducto(forms.ModelForm):
     class Meta:
         model = CategoriaProducto
         fields = ['nombre', 'descripcion']
#
# #Formulario Producto
class FomularioProducto(forms.ModelForm):
     class Meta:
         model = Producto
         fields = ['nombre', 'descripcion', 'categoria', 'precio', 'descuento', 'iva', 'estado']

# #Formulario Existencia
# class FormularioExistencia(forms.ModelForm):
#     class Meta:
#         model = Existencia
#         fields = ['', '', '', '', '', '', '', '', '', '']
#
# #Formulario TipoPago
# class FormularioTipoPago(forms.ModelForm):
#     class Meta:
#         model = TipoPago
#         fields = ['', '', '', '', '', '', '', '', '', '']
#
# #Formulario CompraCabecera
# class FormularioCompraCabecera(forms.ModelForm):
#     class Meta:
#         model = CompraCabecera
#         fields = ['', '', '', '', '', '', '', '', '', '']
#
#
# #Formulario CompraDetalle
# class FormularioCompraDetalle(forms.ModelForm):
#     class Meta:
#         model = CompraDetalle
#         fields = ['', '', '', '', '', '', '', '', '', '']
#
# #Formulario VentaCabecera
# class FormularioVentaCabecera(forms.ModelForm):
#     class Meta:
#         model = VentaCabecera
#         fields = ['', '', '', '', '', '', '', '', '', '']
#
# #Formulario VentaDetalle
# class FormularioVentaDetalle(forms.ModelForm):
#     class Meta:
#         model = VentaDetalle
#         fields = ['', '', '', '', '', '', '', '', '', '']
#
#
# #Formulario Pagos
#
# class FormularioPago(forms.ModelForm):
#     class Meta:
#         model = Pagos
#         fields = ['', '', '', '', '', '', '', '', '', '']