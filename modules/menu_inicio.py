# coding: utf-8
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

import json
from pizzapy.config.config import CONFIG
from fbmq import Attachment, Template, QuickReply, NotificationType
from pizzapy.config.fbpage import page

def menu_inicio(recipient):
    page.send(recipient, "Bienvenido. Soy pizzaBot!!!")
    page.send(recipient, Template.Generic([
        Template.GenericElement("Pizzas",
                                subtitle="Pide una pizza y disfrutala con tus amigos",
                                # item_url="https://www.oculus.com/en-us/rift/",
                                image_url='https://i1.wp.com/www.dondeir.com/wp-content/uploads/2017/03/buffet-de-pizzas-en-cdmx-como-todo-que-puedas-por-149-pesos-3.jpg?ssl=1',
                                buttons=[{'type':'postback','title':'Ver Pizzas','payload':'MENU_PIZZAS'}]),
        Template.GenericElement("Extras",
                                subtitle='Prueba nuestras explosivas alitas endiabladas!!',
                                # item_url="https://www.oculus.com/en-us/touch/",
                                image_url='https://www.cicis.com/media/1196/wings_bbq.png',
                                buttons=[{'type':'postback','title':'Ver Extras','payload':'MENU_EXTRAS'}])
    ]))
