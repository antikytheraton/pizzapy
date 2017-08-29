# coding: utf-8
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

import json
from pizzapy.config.config import CONFIG
from fbmq import Attachment, Template, QuickReply, NotificationType
from pizzapy.config.fbpage import page

def menu_extras(recipient):
    page.send(recipient, 'Elije entre nuestro menu de platilos para botanear y compartir')
    page.send(recipient, Template.Generic([
        Template.GenericElement('Alitas Barbacoa',
                                subtitle='Paquete Alitas con salsa BBQ',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503892966/alitas_barbacoa_jvtdul.png',
                                buttons=[{'type':'postback','title':'ordenar','payload':'ALITAS_BARBACOA'}]),
        Template.GenericElement('Alitas Cayenne',
                                subtitle='Alitas co un toque de canela',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503892966/alitas_cayenne_udollm.png',
                                buttons=[{'type':'postback','title':'ordenar','payload':'ALITAS_CAYENNE'}]),
        Template.GenericElement('Don Calzzone Deluxe',
                                subtitle='Don Calzzone de lujo',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503892966/don_calzzone_deluxe_m3eblt.png',
                                buttons=[{'type':'postback','title':'ordenar','payload':'DON_CALZONE_DELUXE'}]),
        Template.GenericElement('Don Calzzone Tropical',
                                subtitle='Con intoque de pina',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503892966/don_calzzone_tropical_yvayff.png',
                                buttons=[{'type':'postback','title':'ordenar','payload':'DON_CALZONE_TROPICAL'}]),
        Template.GenericElement('Chessy Breads',
                                subtitle='Deliciosos panes rellenos de queso',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503892966/cheese_breads_dx8q4q.png',
                                buttons=[{'type':'postback','title':'ordenar','payload':'CHESSY_BREAD'}]),
        Template.GenericElement('Lata Coca Cola',
                                subtitle='Refrescante bebida de lata',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503892965/coca_cola_mhim50.png',
                                buttons=[{'type':'postback','title':'ordenar','payload':'COCA_COLA'}]),
        Template.GenericElement('Lata Sprite',
                                subtitle='Refrescante bebida de lata',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503892970/sprite_obr3ja.png',
                                buttons=[{'type':'postback','title':'ordenar','payload':'SPRITE'}]),
        Template.GenericElement('Lata Fanta',
                                subtitle='Refrescante bebida de lata',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503892968/fanta_kznslc.png',
                                buttons=[{'type':'postback','title':'ordenar','payload':'FANTA'}])
    ]))
