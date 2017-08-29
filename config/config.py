# coding: utf-8
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

CONFIG = {
    'FACEBOOK_TOKEN': os.env['access_token'],
    'VERIFY_TOKEN': os.env['verify_token'],
    'SERVER_URL': 'https://pizza-bootbot.herokuapp.com'
}
