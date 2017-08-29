# coding: utf-8
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

import json
from pizzapy.config.config import CONFIG
from fbmq import Attachment, Template, QuickReply, NotificationType
from pizzapy.config.fbpage import page

def menu_pizzas(recipient):
    page.send(recipient, 'Checa nuestro menu de pizzas')
    page.send(recipient, Template.Generic([
        Template.GenericElement('5 carnes',
                                subtitle='Pepperoni, jamón, salchicha italiana, salami y carne molida',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503807009/cinco_carnes_mhmbsr.png',
                                buttons=[
                                    {'type':'postback','title':'pedir chica','payload':'5CARNES_CHICA'},
                                    {'type':'postback','title':'pedir grande','payload':'5CARNES_GRANDE'},
                                    {'type':'postback','title':'pedir mega','payload':'5CARNES_MEGA'}
                                ]),

        Template.GenericElement('Pizza Hawaiana',
                                subtitle='Jamón, piña y extra queso',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503807010/hawaiana_aiyw0u.png',
                                buttons=[
                                    {'type':'postback','title':'pedir chica','payload':'HAWAIANA_CHICA'},
                                    {'type':'postback','title':'pedir grande','payload':'HAWAIANA_GRANDE'},
                                    {'type':'postback','title':'pedir mega','payload':'HAWAIANA_MEGA'}
                                ]),
        Template.GenericElement('Cheese Pizza',
                                subtitle='Pizza con queso mozzarella',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503807010/queso_ozdew1.png',
                                buttons=[
                                    {'type':'postback','title':'pedir chica','payload':'CHEESE_CHICA'},
                                    {'type':'postback','title':'pedir grande','payload':'CHEESE_GRANDE'},
                                    {'type':'postback','title':'pedir mega','payload':'CHEESE_MEGA'}
                                ]),
        Template.GenericElement('Carne y tocino',
                                subtitle='Queso cheddar y mozzarella, con roastbeef, tocino y champinones',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503807010/carneytocino_ehbkbu.png',
                                buttons=[
                                    {'type':'postback','title':'pedir chica','payload':'CARNEYTOCINO_CHICA'},
                                    {'type':'postback','title':'pedir grande','payload':'CARNEYTOCINO_GRANDE'},
                                    {'type':'postback','title':'pedir mega','payload':'CARNEYTOCINO_MEGA'}
                                ]),
        Template.GenericElement('Pizza Americana',
                                subtitle='Pepperoni, salchicha italiana y champinones',
                                image_url='http://res.cloudinary.com/antikytheraton/image/upload/v1503807010/americana_sjjvoi.png',
                                buttons=[
                                    {'type':'postback','title':'pedir chica','payload':'AMERICANA_CHICA'},
                                    {'type':'postback','title':'pedir grande','payload':'AMERICANA_GRANDE'},
                                    {'type':'postback','title':'pedir mega','payload':'AMERICANA_MEGA'}
                                ])
    ]))
