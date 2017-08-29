import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

import json
from pizzapy.config.config import CONFIG
from fbmq import Attachment, Template, QuickReply, NotificationType
from pizzapy.config.fbpage import page

# cantidad_pedidos = '0'
list_of_items = []
elements = []
pizzas = ['5CARNES_CHICA','5CARNES_GRANDE','5CARNES_MEGA','HAWAIANA_CHICA','HAWAIANA_GRANDE','HAWAIANA_MEGA','CHEESE_CHICA','CHEESE_GRANDE','CHEESE_MEGA','CARNEYTOCINO_CHICA','CARNEYTOCINO_GRANDE','CARNEYTOCINO_MEGA','AMERICANA_CHICA','AMERICANA_GRANDE','AMERICANA_MEGA']
don = ['DON_CALZONE_DELUXE','DON_CALZONE_TROPICAL']
alitas = ['ALITAS_BARBACOA','ALITAS_CAYENNE']
refresco = ['COCA_COLA','SPRITE','FANTA']
image_url = {
    'pizza 5 carnes':'http://res.cloudinary.com/antikytheraton/image/upload/v1503807009/cinco_carnes_mhmbsr.png',
    'pizza hawaiana':'http://res.cloudinary.com/antikytheraton/image/upload/v1503807010/hawaiana_aiyw0u.png',
    'pizza cheese':'http://res.cloudinary.com/antikytheraton/image/upload/v1503807010/queso_ozdew1.png',
    'pizza carne y tocino':'http://res.cloudinary.com/antikytheraton/image/upload/v1503807010/carneytocino_ehbkbu.png',
    'pizza americana':'http://res.cloudinary.com/antikytheraton/image/upload/v1503807010/americana_sjjvoi.png',
    'alitas barbacoa':'http://res.cloudinary.com/antikytheraton/image/upload/v1503892966/alitas_barbacoa_jvtdul.png',
    'alitas cayenne':'http://res.cloudinary.com/antikytheraton/image/upload/v1503892966/alitas_cayenne_udollm.png',
    'don calzone deluxe':'http://res.cloudinary.com/antikytheraton/image/upload/v1503892966/don_calzzone_deluxe_m3eblt.png',
    'don calzone tropical':'http://res.cloudinary.com/antikytheraton/image/upload/v1503892966/don_calzzone_tropical_yvayff.png',
    'chessy':'http://res.cloudinary.com/antikytheraton/image/upload/v1503892966/cheese_breads_dx8q4q.png',
    'coca cola':'http://res.cloudinary.com/antikytheraton/image/upload/v1503892965/coca_cola_mhim50.png',
    'sprite':'http://res.cloudinary.com/antikytheraton/image/upload/v1503892970/sprite_obr3ja.png',
    'fanta':'http://res.cloudinary.com/antikytheraton/image/upload/v1503892968/fanta_kznslc.png'
}

def confirmar_seleccion(recipient, items_list):
    elements = []
    for i in range(len(items_list)):
        elements.append(
            Template.GenericElement(items_list[i]['title'],
                                    subtitle=items_list[i]['subtitle'],
                                    image_url=items_list[i]['image_url'],
                                    buttons=[
                                        # {'type':'postback','title':'confirmar','payload':'CONFIRMAR'},
                                        {'type':'postback','title':'anexar pizzas','payload':'MENU_PIZZAS'},
                                        {'type':'postback','title':'anexar extras', 'payload':'MENU_EXTRAS'}
                                    ])
        )
    page.send(recipient, Template.Generic(list(set(elements))))

    page.send(recipient, ':)', [
            QuickReply(title='Confirmar', payload='CONFIRMAR'),
            QuickReply(title='Cancelar', payload='CANCELAR')
    ])

def nombre_producto(recipient, seleccion):
    if seleccion in pizzas:
        nom_orden = seleccion.split('_')[0]
        tip_orden = seleccion.split('_')[1]
        if nom_orden == '5CARNES':
            nom_orden = 'PIZZA 5 CARNES'
        elif nom_orden == 'CARNEYTOCINO':
            nom_orden = 'PIZZA CARNE Y TOCINO'
        else:
            nom_orden = 'PIZZA ' + nom_orden
    elif seleccion in don:
        nom_orden = seleccion.replace('_',' ')
        tip_orden = ''
    elif seleccion in refresco:
        nom_orden = seleccion.replace('_',' ')
        tip_orden = 'LATA'
    elif seleccion in alitas:
        nom_orden = seleccion.replace('_',' ')
        tip_orden = ''
    else:
        nom_orden = seleccion.split('_')[0]
        tip_orden = seleccion.split('_')[1]

    return nom_orden, tip_orden

def pregunta_cantidad(recipient, nom_orden, tip_orden):
    quick_replies = [
        QuickReply(title='1', payload='CANTIDAD'),
        QuickReply(title='2', payload='CANTIDAD'),
        QuickReply(title='3', payload='CANTIDAD'),
        QuickReply(title='4', payload='CANTIDAD'),
        QuickReply(title='5', payload='CANTIDAD')
    ]
    page.send(recipient, 'Cuantas ordenes desea?',quick_replies=quick_replies)

    @page.handle_message
    def received_message(event):
        message = event.message
        message_text = message.get("text")
        quick_reply = message.get("quick_reply")
        quick_reply_payload = quick_reply.get('payload')

        item = {
            'title':nom_orden + ' ' + tip_orden,
            'subtitle':'Cantidad: ' + message_text,
            'image_url':image_url[nom_orden.lower()]
        }
        list_of_items.append(item)

        if quick_reply_payload in ['PAGO_1','PAGO_2']:
            page.send(recipient, 'En unos minutos recibiras tu pedido :)', [
                            QuickReply(title='Volver', payload='INIT')
            ])
        elif quick_reply_payload == 'CONFIRMAR':
            confirmar_operacion(recipient)
        elif quick_reply_payload == 'CANCELAR':
            cancelar_operacion(recipient)
            list_of_items = []
        elif len(list_of_items) == 0:
            page.send(recipient, 'no he recibido nada')
        elif len(list_of_items) > 0:
            # page.send(recipient, message_text)
            confirmar_seleccion(recipient, list_of_items)


def confirmar_operacion(recipient):
    page.send(recipient, 'Excelente, ahora selecciona tu forma de pago', [
                        QuickReply(title='Efectivo', payload='PAGO_1'),
                        QuickReply(title='Terminal portatil', payload='PAGO_2')
    ])

def cancelar_operacion(recipient):
    items_list = []
    page.send(recipient, 'Tu operacion fue cancelada' ,[
                        QuickReply(title='Volver', payload='INIT')
    ])
