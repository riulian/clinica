# -*- coding: utf-8 -*-
from datetime import date
dict_ore_incepere={'7':'0','9':'0','10':'1','11':'2','12':'3','13':'4','14':'5','15.15':'6','16.30':'7','17.30':'8'} #dictionarcu key=ora de incepere si valoare=pozitia in dict_tab_pac['i5']

db.define_table('combo1',
                Field('nr','integer',requires = IS_IN_SET([0,1,2,3])))
db.define_table('terapii',
                Field('nume',label='denumire',requires=IS_NOT_EMPTY(),represent=lambda v, r: '' if v is None else v),
                Field('tip',requires = IS_EMPTY_OR(IS_IN_SET(['de grup d','de grup','individuala','individuala in camera'])),represent=lambda v, r: '' if v is None else v),
                Field('durata','integer',requires=IS_NOT_EMPTY(),represent=lambda v, r: '' if v is None else v),
                Field('cuplaj_cu',requires = IS_EMPTY_OR(IS_IN_SET(['nu','respiratii','vocale','frecvente','cromoterapie','psihoterapie individuala'])),represent=lambda v, r: '' if v is None else v),
                Field('posibil_inainte_de',represent=lambda v, r: '' if v is None else v),
                Field('imposibil_inainte_de',represent=lambda v, r: '' if v is None else v),
                Field('posibil_dupa',represent=lambda v, r: '' if v is None else v),
                Field('imposibil_dupa',represent=lambda v, r: '' if v is None else v),
                Field('simultan_maxim',represent=lambda v, r: '' if v is None else v),
                #Field('cand',requires = IS_NOT_EMPTY_OR(IS_IN_SET(['doar dimineata','doar dupa pranz','doar seara','pranz si seara','altfel']))),
                Field('cand_se_poate',requires = IS_EMPTY_OR(IS_IN_SET(['doar dimineata','doar dupa pranz','doar seara','pranz si seara','altfel'])),represent=lambda v, r: '' if v is None else v),
                Field('pauza_aceeasi_terapie',requires=IS_INT_IN_RANGE(0,2000),represent=lambda v, r: '' if v is None else v), #se refera la cromoterapie, 10 min cu pauza 10 min sa se raceasca lampa
                Field('interval_inceput_ora',requires=IS_INT_IN_RANGE(7, 24),represent=lambda v, r: '' if v is None else v),   #atentie Inhalatia se poate face si la pranz si seara
                Field('interval_inceput_minut',requires=IS_INT_IN_RANGE(0, 60),represent=lambda v, r: '' if v is None else v),
                Field('interval_sfarsit_ora',requires=IS_INT_IN_RANGE(7, 24),represent=lambda v, r: '' if v is None else v),
                Field('interval_sfarsit_minut',requires=IS_INT_IN_RANGE(0, 60),represent=lambda v, r: '' if v is None else v),
                Field('mai_multe_intervale',requires = IS_EMPTY_OR(IS_IN_SET(['nu','2','3'])),represent=lambda v, r: '' if v is None else v),
                Field('interval2_inceput_ora',represent=lambda v, r: '' if v is None else v),
                Field('interval2_inceput_minut',represent=lambda v, r: '' if v is None else v),
                Field('interval2_sfarsit_ora',represent=lambda v, r: '' if v is None else v),
                Field('interval2_sfarsit_minut',represent=lambda v, r: '' if v is None else v),
                Field('interval3_inceput_ora',represent=lambda v, r: '' if v is None else v),
                Field('interval3_inceput_minut',represent=lambda v, r: '' if v is None else v),
                Field('interval3_sfarsit_ora',represent=lambda v, r: '' if v is None else v),
                Field('interval3_sfarsit_minut',represent=lambda v, r: '' if v is None else v),
                Field('cine_face','list:string',represent=lambda v, r: '' if v is None else v),
                Field('cine_nu_face','list:string',represent=lambda v, r: '' if v is None else v),
                Field('weekend','boolean',default=True,notnull=True,represent=lambda v, r: '' if v is None else v),
                Field('Obs','text',represent=lambda v, r: '' if v is None else v))
           

db.define_table('terapeuti',
                Field('nume',label='Nume',requires=IS_NOT_EMPTY()),
                Field('ce_terapii_face','list:string'),
                Field('ce_terapii_nu_face','list:string'))

#db.define_table('camere',
#               Field('camera',label='Camera',requires=IS_NOT_EMPTY()),
#               Field('max_locuri','integer',label='Nr maxim locuri'),
#               Field('nr_paturi_simple','integer'),
#               Field('nr_paturi_duble','integer'),
#               Field('pat','list:string'),
#               format='%(camera)')
                #format='%(camera)s' + ' - ' + '%(pat)s') aceasta face la fel cu lambda de mai jos pune 2 campuri
                #format=lambda r:'%s-%s' % (r.camera, r.pat[0]))

db.define_table('camere',
                Field('camera',label='Camera',requires=IS_NOT_EMPTY()),
                Field('pat',label='Pat',requires=IS_NOT_EMPTY()),
                Field('max_locuri','integer',label='Nr maxim locuri'),
                Field('nr_paturi_simple','integer'),
                Field('nr_paturi_duble','integer'),
                format='%(camera)s' + ' - ' + '%(pat)s')
                

        
db.define_table('pacienti',
                Field('camere','reference=camere',label='Camera/Pat:'),
                #Field('camere','reference=camere',label='Camera/Pat:',represent=lambda id, r: '%s %s %s' % (r.camere.camera,'-', r.camere.pat)),# cu lambda fac acelasi lucru ca si cu formatul de mai sus
                Field('nume',label='Nume:',requires=IS_NOT_EMPTY()),
                #Field('cnp','string',requires=IS_LENGTH(13,13),label='Cnp:'),
                Field('din_localitatea',label='Din Localitatea:',requires=IS_NOT_EMPTY()),
                Field('inceput_tt','date',format=('%Y-%m-%d'),label='Incepere tratament:',requires=IS_DATE()),
                Field('sfarsit_tt','date',format=('%Y-%m-%d'),label='Sfarsit tratament:',requires=IS_DATE()),
                Field('inceput_ss','date',requires = IS_DATE(format=('%Y-%m-%d')),label='Incepere sedere:'),
                Field('sfarsit_ss','date',requires = IS_DATE(format=('%Y-%m-%d')),label='Sfarsit sedere:'),
                #Field('p_or_a',label = 'Tip Pacient:',requires = IS_IN_SET(['pacient','ambulatoriu'])),
                Field('p_or_a',label = 'Tip Pacient:'),
                Field('ora_in',requires = IS_IN_SET(['7','9','10','11','12','13','14','15.15','16.30','17.30'])),
                Field('ora_out',requires = IS_IN_SET(['10','11','12','13','14','15','16.15','17.30','18.30','23'])),
                Field('terapii_necesare','list:string'),
                Field('terapii_importante','list:string'),
                format='%(camere)s')

db.define_table('orar_t',
                Field('dataa','date',format=('%Y-%m-%d'),label='Data:'),
                Field('terapeut_dim',requires = IS_EMPTY_OR(IS_IN_SET(['Catalin','Mirela','Mari','Lidia','Carmen','Carla','Iulia','Mihai','Ana','Nushu','Paula','Oana'])),represent=lambda v, r: '' if v is None else v),
                Field('terapeut_dup',requires = IS_EMPTY_OR(IS_IN_SET(['Catalin','Mirela','Mari','Lidia','Carmen','Carla','Iulia','Mihai','Ana','Nushu','Paula','Oana'])),represent=lambda v, r: '' if v is None else v),
                Field('terapeut_1',requires = IS_EMPTY_OR(IS_IN_SET(['Catalin','Mirela','Mari','Lidia','Carmen','Carla','Iulia','Mihai','Ana','Nushu','Paula','Oana'])),represent=lambda v, r: '' if v is None else v),
                Field('dispo1',requires = IS_EMPTY_OR(IS_IN_SET(['all','7-16','14-23','nu'])),represent=lambda v, r: '' if v is None else v),
                Field('terapeut_2',requires = IS_EMPTY_OR(IS_IN_SET(['Catalin','Mirela','Mari','Lidia','Carmen','Carla','Iulia','Mihai','Ana','Nushu','Paula','Oana'])),represent=lambda v, r: '' if v is None else v),
                Field('dispo2',requires = IS_EMPTY_OR(IS_IN_SET(['all','7-16','14-23','nu'])),represent=lambda v, r: '' if v is None else v),                                     
                Field('terapeut_3',requires = IS_EMPTY_OR(IS_IN_SET(['Catalin','Mirela','Mari','Lidia','Carmen','Carla','Iulia','Mihai','Ana','Nushu','Paula','Oana'])),represent=lambda v, r: '' if v is None else v),
                Field('dispo3',requires = IS_EMPTY_OR(IS_IN_SET(['all','7-16','14-23','nu'])),represent=lambda v, r: '' if v is None else v),
                Field('terapeut_4',requires = IS_EMPTY_OR(IS_IN_SET(['Catalin','Mirela','Mari','Lidia','Carmen','Carla','Iulia','Mihai','Ana','Nushu','Paula','Oana'])),represent=lambda v, r: '' if v is None else v),
                Field('dispo4',requires = IS_EMPTY_OR(IS_IN_SET(['all','7-16','14-23','nu'])),represent=lambda v, r: '' if v is None else v),
                Field('terapeut_5',requires = IS_EMPTY_OR(IS_IN_SET(['Catalin','Mirela','Mari','Lidia','Carmen','Carla','Iulia','Mihai','Ana','Nushu','Paula','Oana'])),represent=lambda v, r: '' if v is None else v),
                Field('dispo5',requires = IS_EMPTY_OR(IS_IN_SET(['all','7-16','14-23','nu'])),represent=lambda v, r: '' if v is None else v),
                Field('terapeut_6',requires = IS_EMPTY_OR(IS_IN_SET(['Catalin','Mirela','Mari','Lidia','Carmen','Carla','Iulia','Mihai','Ana','Nushu','Paula','Oana'])),represent=lambda v, r: '' if v is None else v),
                Field('dispo6',requires = IS_EMPTY_OR(IS_IN_SET(['all','7-16','14-23','nu'])),represent=lambda v, r: '' if v is None else v),
                Field('terapeut_7',requires = IS_EMPTY_OR(IS_IN_SET(['Catalin','Mirela','Mari','Lidia','Carmen','Carla','Iulia','Mihai','Ana','Nushu','Paula','Oana'])),represent=lambda v, r: '' if v is None else v),
                Field('dispo7',requires = IS_EMPTY_OR(IS_IN_SET(['all','7-16','14-23','nu'])),represent=lambda v, r: '' if v is None else v),
                Field('terapeut_8',requires = IS_EMPTY_OR(IS_IN_SET(['Catalin','Mirela','Mari','Lidia','Carmen','Carla','Iulia','Mihai','Ana','Nushu','Paula','Oana'])),represent=lambda v, r: '' if v is None else v),
                Field('dispo8',requires = IS_EMPTY_OR(IS_IN_SET(['all','7-16','14-23','nu'])),represent=lambda v, r: '' if v is None else v),
                Field('control','boolean'))
db.orar_t.dataa.requires = [IS_NOT_IN_DB(db,'orar_t.dataa'),IS_DATE()] #conteaza ordinea in care am pus conditiile de exemplu daca puneam IS_DATE() era altceva

db.define_table('orar_sablon',#sablonul orar
                Field('dataa','date',format=('%Y-%m-%d'),label='Data:'),
                Field('ora'),
                Field('info_generale'),
                Field('pacient_1',label='Pacient 1'),
                Field('pacient_2',label='Pacient 2'),
                Field('pacient_3',label='Pacient 3'),
                Field('pacient_4',label='Pacient 4'),
                Field('pacient_5',label='Pacient 5'),
                Field('pacient_6',label='Pacient 6'),
                Field('pacient_7',label='Pacient 7'), 
                Field('pacient_8',label='Pacient 8'),
                Field('pacient_9',label='Pacient 9'),
                Field('pacient_10',label='Pacient 10'),
                Field('pacient_11',label='Pacient 11'),
                Field('pacient_12',label='Pacient 12'),
                Field('pacient_13',label='Pacient 13'),
                Field('pacient_14',label='Pacient 14'),
                Field('pacient_15',label='Pacient 15'),
                Field('pacient_16',label='Pacient 16'),
                Field('pacient_17',label='Pacient 17'),
                Field('pacient_18',label='Pacient 18'),
                Field('pacient_19',label='Pacient 19'),
                Field('pacient_20',label='Pacient 20'))
                
db.define_table('orar',
                Field('dataa','date',format=('%Y-%m-%d'),label='Data:'),
                Field('ora'),
                Field('info_generale'),
                Field('pacient_1',label='Pacient 1',represent=lambda v, r: '' if v is None else v),
                Field('pacient_2',label='Pacient 2',represent=lambda v, r: '' if v is None else v),
                Field('pacient_3',label='Pacient 3',represent=lambda v, r: '' if v is None else v),
                Field('pacient_4',label='Pacient 4',represent=lambda v, r: '' if v is None else v),
                Field('pacient_5',label='Pacient 5',represent=lambda v, r: '' if v is None else v),
                Field('pacient_6',label='Pacient 6',represent=lambda v, r: '' if v is None else v),
                Field('pacient_7',label='Pacient 7',represent=lambda v, r: '' if v is None else v), 
                Field('pacient_8',label='Pacient 8',represent=lambda v, r: '' if v is None else v),
                Field('pacient_9',label='Pacient 9',represent=lambda v, r: '' if v is None else v),
                Field('pacient_10',label='Pacient 10',represent=lambda v, r: '' if v is None else v),
                Field('pacient_11',label='Pacient 11',represent=lambda v, r: '' if v is None else v),
                Field('pacient_12',label='Pacient 12',represent=lambda v, r: '' if v is None else v),
                Field('pacient_13',label='Pacient 13',represent=lambda v, r: '' if v is None else v),
                Field('pacient_14',label='Pacient 14',represent=lambda v, r: '' if v is None else v),
                Field('pacient_15',label='Pacient 15',represent=lambda v, r: '' if v is None else v),
                Field('pacient_16',label='Pacient 16',represent=lambda v, r: '' if v is None else v),
                Field('pacient_17',label='Pacient 17',represent=lambda v, r: '' if v is None else v),
                Field('pacient_18',label='Pacient 18',represent=lambda v, r: '' if v is None else v),
                Field('pacient_19',label='Pacient 19',represent=lambda v, r: '' if v is None else v),
                Field('pacient_20',label='Pacient 20',represent=lambda v, r: '' if v is None else v))    
    
db.define_table('orar_p', #aici sunt informatiile pt fiecare pacient pe zile
                Field('dataa','date',format=('%Y-%m-%d'),label='Data:'),# este inceput_tt din tabela pacienti
                Field('din_localitatea',label='Din Localitatea:',requires=IS_NOT_EMPTY()),# adaugata din pacienti
                Field('sfarsit_tt','date',format=('%Y-%m-%d'),label='Sfarsit tratament:',requires=IS_DATE()),# adaugata din pacienti
                Field('pacient'),
                Field('pacient_id'),
                Field('camere','reference camere'),
                Field('terapii_necesare','list:string'),
                Field('terapii_importante','list:string'),
                Field('individuala_nu','list:string'), #la inceput aici este plin si se tot transfera jos
                Field('individuala_da','list:string'), #la inceput aici este gol si se tot primeste de sus pe masura ce trece o zi si cand sw termina de sus si se umple jos se incheie un ciclu si umplem sus again
                Field('individuala_precedente','list:string'), #terapiile facute in ziua precedenta (individuale)
                Field('individuala_cicluri','integer'),
                Field('degrup_nu','list:string'), #la inceput aici este plin si se tot transfera jos
                Field('degrup_da','list:string'), #la inceput aici este gol si se tot primeste de sus pe masura ce trece o zi si cand sw termina de sus si se umple jos se incheie un ciclu si umplem sus again
                Field('degrup_precedente','list:string'), #terapiile facute in ziua precedenta (individuale)
                Field('degrup_cicluri','integer'),
                Field('degrupd','list:string'),
                Field('degrupd_da','list:string'),
                Field('individuala_camera','list:string'),
                Field('individuala_camera_da','list:string'),
                Field('p_or_a',label = 'Tip Pacient:'),
                Field('ora_in'),
                Field('ora_out'))

db.orar_p.dataa.requires = [IS_DATE()]
