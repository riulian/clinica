# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

#response.menu = [
#    (T('Terapii'), False, URL('default', 'index'), [])
#]
response.menu += [
    #(T('Test'), False, URL('default', 'test'), []),
        (T('Generare Orar'), False, URL('default', 'generare_orare',args=[112]), []),
        (T('Orar'), False, URL('default', 'orar',args =[111]), []),
        (T('Orar terapeuti'), False, URL('default', 'orar_t'), [])
]


response.menu +=[(T('Pacienti'), False, None, [(T('Pacienti'), False,URL('default','pacienti')),(T('Ambulatoriu'), False,URL('default','ambulatoriu'))])]

#if auth.has_membership('managers'):
response.menu +=[(T('Manager'), False, None, [(T('Terapii'), False,URL('default','terapii')),(T('Terapeuti'), False,URL('default','terapeuti')),(T('Camere'), False,URL('default','camere')),(T('Useri'), False,URL('default','useri')),(T('Orar Sablon'), False,URL('default','orar_sablon'))])]
# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------
