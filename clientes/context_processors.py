from facturas.models import Factura


def carrito_context(request):
    factura_abierta_id = None
    if request.user.is_authenticated:

        factura_abierta = request.user.facturas.filter(estado = 'abierta').order_by('-fecha_emision').first()

        if factura_abierta:
            factura_abierta_id = factura_abierta.id

    return {
        'factura_abierta_id' : factura_abierta_id
    }
    