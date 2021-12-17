import datetime
import numpy as np 
import json
import ast
# -*- coding: utf-8 -*-
def modificare_orar():
    y1 = request.args[0]
    #y2=request.vars
    #dataa=y2['dataa']
    dataa = datetime.date(2020, 8, 15)
    if y1=='113':
        db(db.orar.dataa >= dataa).delete()
        y1="am sters"
    else:
        y1="nu am sters"
    
    
    return locals()
def test3():
    z=request.vars
    cc=z['cams']
    return locals()

def test():
    row=db(db.orar_p.id==237).select().first().individuala_da
    row1=(eval(row[2]))[0]
    
    row2=type(row1)
    
    #dddd = row1
    #ddddd = datetime.datetime.strptime(row1, '%Y-%m-%d')
    #ddd=ddddd.date()
    #d=type(ddd)
    #res = json.loads(row1)
    #res1=type(res)
           
    return locals()
def test1():
    vvv=request.vars
    y2 = vvv['z']
    yt_este=vvv['yt_este']
    voc_este=vvv['voc_este']
    contor_ter=vvv['contor_ter']
    id_yt=vvv['id_yt']
    key_ora_incepere=vvv['key_ora_incepere']
    key_valabilitate=vvv['key_valabilitate']
    i9=vvv['i9']
    i10=vvv['i10']
    return locals()

def vdata(): # aceasta functie este apelata cand apas pe butoanele cu zile: Luni, Marti... 14 butoane si ma redirectioneaza pe pagina 'orar' si afiseaza orarul din ziua respectiva
    zi1 = request.args
    zi=int(zi1[0]) # integerul cu ce zi este Ex: pt Luni curent este 1; pt Marti sapt viitoare este 9
    data_azi = datetime.datetime.now().strftime("%d-%m-%Y") #este doar pt a imi afisa in View. Nu o folosesc in calcule 15-08-2020
    zile_sapt = {"Monday": 1,"Tuesday": 2,"Wednesday": 3,"Thursday": 4,"Friday": 5,"Saturday": 6,"Sunday": 7}
    ziua_romana = {"1": "Luni","2": "Marti","3": "Miercuri","4": "Joi","5": "Vineri","6": "Sambata","7": "Duminica","8": "Luni","9": "Marti","10": "Miercuri","11": "Joi","12": "Vineri","13": "Sambata","14": "Duminica"}
    ziua_romana1 = ziua_romana[zi1[0]]
    dataa = datetime.datetime.now().date() #aceasta o sa o folosesc in calcule
    #dataa = datetime.date(2021, 2, 3) # subtitui dataa de mai sus cu aceasta pt teste
    nr_zi = (zile_sapt[dataa.strftime("%A")]) # aici imi da un integer a cata zi din saptamana este (in cazul nostru 6).
    defazare_zi= zi-nr_zi
    dataaa= (dataa+datetime.timedelta(days=defazare_zi))
    redirect(URL('default','orar',vars=dict(dataaa=dataaa,ziua_romana1=ziua_romana1)))
    return locals()

def orar(): # afiseaza orarul curent si din pagina aceasta orarul pe celelalte zile
   
    y1 = request.vars
    y=y1['dataaa']
    ziua_romana1 = y1['ziua_romana1']
    data_azi = datetime.datetime.now().strftime("%d-%m-%Y") #este doar pt a imi afisa in View. Nu o folosesc in calcule 15-08-2020
    zile_sapt = {"Monday": 1,"Tuesday": 2,"Wednesday": 3,"Thursday": 4,"Friday": 5,"Saturday": 6,"Sunday": 7}
   
    if y == None:
        dataa = datetime.datetime.now().date() #aceasta o sa o folosesc in calcule
        #dataa = datetime.date(2020, 8, 15) # subtitui dataa de mai sus cu aceasta pt teste
        nr_zi = (zile_sapt[dataa.strftime("%A")])
        ziua_romana = {"1": "Luni","2": "Marti","3": "Miercuri","4": "Joi","5": "Vineri","6": "Sambata","7": "Duminica","8": "Luni","9": "Marti","10": "Miercuri","11": "Joi","12": "Vineri","13": "Sambata","14": "Duminica"}
        ziua_romana1 = ziua_romana[str(nr_zi)]
    else:
        d = datetime.datetime.strptime(y, '%Y-%m-%d') # y1 vine ca si string si trebuie convertit din nou in data in formatul exemplu: 2020-08-15
        dataaa=d.date()
        dataa = dataaa
        
    nr_zi = (zile_sapt[dataa.strftime("%A")]) # aici imi da un integer a cata zi din saptamana este (in cazul nostru 6). Deci urmeaza sa generez programul pe 2 zile
    nr_copii_sablon = 15-nr_zi
    delta2= (dataa+datetime.timedelta(days=nr_copii_sablon-1)) # aceasta este ultima data (Duminica) ce va fi introdusa in tabela orar adica in exemplul nostru: 2020-08-16
    este_generat1 = db(db.orar).select(db.orar.dataa.max())[0] # aceste 2 linii imi dau data maxima din tabela orar
    este_generat = este_generat1['_extra']['MAX("orar"."dataa")'] # aceasta este data maxima din tabela orar
    nr_rec = db((db.orar.id>0)).count() # numarul de inregistrari din tabela orar
    #data_sf = (db(db.orar_t).select().last()).dataa #aceasta este data ultima introdusa din programul terapeutilor pt a vedea pana la ce data pot genera orarul
    querry_orar_o_zi = db.orar.dataa == dataa
    fields_orar = [db.orar.dataa,db.orar.ora,db.orar.info_generale,db.orar.pacient_1,db.orar.pacient_2,db.orar.pacient_3,db.orar.pacient_4,db.orar.pacient_5,db.orar.pacient_6,db.orar.pacient_7,db.orar.pacient_8,db.orar.pacient_9,db.orar.pacient_10,db.orar.pacient_11,db.orar.pacient_12,db.orar.pacient_13,db.orar.pacient_14,db.orar.pacient_15,db.orar.pacient_16,db.orar.pacient_17,db.orar.pacient_18,db.orar.pacient_19,db.orar.pacient_20]
    maxtextlengths_1 = {'orar.pacient_1':70,'orar.pacient_2':70,'orar.pacient_3':70,'orar.pacient_4':70,'orar.pacient_5':70,'orar.pacient_6':70,'orar.pacient_7':70,'orar.pacient_8':70,'orar.pacient_9':70,'orar.pacient_10':70,'orar.pacient_11':70,'orar.pacient_12':70,'orar.pacient_13':70,'orar.pacient_14':70,'orar.pacient_15':70,'orar.pacient_16':70,'orar.pacient_17':70,'orar.pacient_18':70,'orar.pacient_19':70,'orar.pacient_20':70}
   
    header_or ={'orar.dataa':'Data astazi','orar.ora':'Ora si Data','orar.pacient_1' : 'Pacient_______________________________1','orar.pacient_2' : 'Pacient 2________________________________','orar.pacient_3' : 'Pacient 3________________________________','orar.pacient_4' : 'Pacient 4________________________________','orar.pacient_5' : 'Pacient 5________________________________','orar.pacient_6' : 'Pacient 6________________________________','orar.pacient_7' : 'Pacient 7________________________________','orar.pacient_8' : 'Pacient 8________________________________','orar.pacient_9' : 'Pacient 9________________________________','orar.pacient_10' : 'Pacient 10________________________________','orar.pacient_11' : 'Pacient 11________________________________','orar.pacient_12' : 'Pacient 12________________________________','orar.pacient_13' : 'Pacient 13________________________________','orar.pacient_14' : 'Pacient14________________________________','orar.pacient_15' : 'Pacient 15________________________________','orar.pacient_16' : 'Pacient 16________________________________','orar.pacient_17' : 'Pacient 17________________________________','orar.pacient_18' : 'Pacient 18________________________________','orar.pacient_19' : 'Pacient 19________________________________','orar.pacient_20' : 'Pacient 20________________________________'}
    
    grid_orar = SQLFORM.grid(querry_orar_o_zi,maxtextlengths = maxtextlengths_1, fields=fields_orar,headers=header_or,user_signature=False,csv=True,paginate=30,create=False,searchable=False,sortable=False,editable=False,deletable=False,details=False)
    return locals()


def generare_orare(): # acest controler sabloanele si genereaza orarul
    i88=[]
    arr=[]
    tab28=[1,2,3]
    tab29=[4,5,6]
    arr.append(tab28)
    arr.append(tab29)
    np_arr=np.array(arr)
    pune_sambata_bo=-1
     
    
    
    y1 = request.args[0]
    
    data_azi = datetime.datetime.now().strftime("%d-%m-%Y") #este doar pt a imi afisa in View. Nu o folosesc in calcule 15-08-2020
    zile_sapt = {"Monday": 1,"Tuesday": 2,"Wednesday": 3,"Thursday": 4,"Friday": 5,"Saturday": 6,"Sunday": 7}
    dataa = datetime.datetime.now().date() #aceasta o sa o folosesc in calcule
    #dataa = datetime.date(2021, 2, 3) # subtitui dataa de mai sus cu aceasta pt teste
    este_generat1 = db(db.orar).select(db.orar.dataa.max())[0] #aici este o initializare  aceste 2 linii imi dau data maxima din tabela orar
    este_generat = este_generat1['_extra']['MAX("orar"."dataa")'] # aceasta este data maxima din tabela orar
    db(db.orar.dataa >= dataa).delete()
    nr_zi = (zile_sapt[dataa.strftime("%A")]) # aici imi da un integer a cata zi din saptamana este (in cazul nostru 6). Deci urmeaza sa generez programul pe 2 zile
    ver_intr_sabloane = 0 # este o variabila pe care o folosesc pt a vedea daca am introdus sabloane sau ele erau deja introduse
    if y1=="112":
        nr_copii_sablon = 15-nr_zi #am sch din 7 in 15
        delta2= (dataa+datetime.timedelta(days=nr_copii_sablon-1)) # aceasta este ultima data (Duminica) ce va fi introdusa in tabela orar adica in exemplul nostru: 2020-08-16
        nr_rec = db((db.orar.id>0)).count() # numarul de inregistrari din tabela orar
        #data_sf = (db(db.orar_t).select().last()).dataa #aceasta este data ultima introdusa din programul terapeutilor pt a vedea pana la ce data pot genera orarul
       
        ver_intr_sabloane = 1
        
        response.flash = T("Am generat orarul pentru %s zile")%(nr_copii_sablon)
        i=0
        row_sablon = db(db.orar_sablon).select()
        for i in range(nr_copii_sablon): # aici am introdus 2 copii in orar
            delta1= (dataa+datetime.timedelta(days=i))
            for row_s in row_sablon:
                db.orar.insert(**db.orar._filter_fields(row_s)) # ia linia din sablon si o copie in orar; for-ul copie 24 de astfel de linii
                row_last_in_orar=db(db.orar).select().last()
                row_last_in_orar.update_record(dataa=delta1)
            row_sablon = db(db.orar_sablon).select()
            i=i+1
        
    
######################################################################################### PANA aici am introdus cele maxim 14 sabloane pe saptamana in curs si sapt viitoare
    tabidx1=[]
    aintr=-1
    
    if nr_rec == 0 or (este_generat>=dataa)==True: #nr_rec=0 nu am inregistrari in tabela orar 
        aintr=-2
        tabidx1=[] # va cuprinde id-urile tuturor pacientilor Pp la care voi sterge istoricul pana la data de azi inclusiv
        dataafinal= (dataa+datetime.timedelta(days=nr_copii_sablon-1))
        rows123= db(db.orar_p.dataa<=dataafinal).select() & (db(db.orar_p.sfarsit_tt>=dataa)).select()
        for row in rows123:
            if row.p_or_a=='pacient':
                tabidx1.append(row.id)
        
        for i7 in tabidx1:
            row=db(db.orar_p.id==i7).select().first()
            tabord=row.individuala_da
            if row.individuala_da!=None:
                aintr=0        
                i9=0 
                for i8888 in row.individuala_da:
                    if (eval(i8888))[0]>=dataa:
                        aintr=1
                        indexdeundesterg=i9
                        del tabord[i9:-1]
                        del tabord[-1]
                        if len(tabord)>0:
                            row.update_record(individuala_da=tabord)
                        else:
                            row.update_record(individuala_da=None)    
                        break
                    
                    i9=i9+1
        
        for i7 in tabidx1:
            row=db(db.orar_p.id==i7).select().first()
            tabord=row.degrup_da
            if row.degrup_da!=None:
                aintr=0        
                i9=0 
                for i8888 in row.degrup_da:
                    if (eval(i8888))[0]>=dataa:
                        aintr=1
                        indexdeundesterg=i9
                        del tabord[i9:-1]
                        del tabord[-1]
                        if len(tabord)>0:
                            row.update_record(degrup_da=tabord)
                        else:
                            row.update_record(degrup_da=None)    
                        break
                    
                    i9=i9+1



           

    TI_ordonate=['BIOTERAPIE','PSIHOTERAPIE INDIVIDUALA','DDS MERIDIANE','MASAJ TERAPEUTIC','MASAJ REFLEXO','MASAJ RELAXARE','OLEATIE SACULET (include sauna)','OLEATIE COLACEL','SHIRODHARA (OLEATIE CAP)']
    BI_ord=['Nushu']
    PI_ord=['Carla','Mirela']
    DDS_ord=['Lidia','Carmen']
    Mter_ord=['Catalin','Lidia','Carmen']
    Mref_ord=['Paula','Mari','Ana','Catalin','Lidia','Carmen','Nushu']
    Mrel_ord=['Paula','Mihai','Iulia','Ana','Mari','Catalin','Carmen','Lidia']
    Ols_ord=['Mihai','Iulia','Ana','Mari','Catalin','Carmen','Lidia','Nushu']
    Olc_ord=['Mihai','Iulia','Ana','Mari','Catalin','Carmen','Lidia','Mirela']
    Shi_ord=['Mihai','Iulia','Ana','Mari','Catalin','Carmen','Lidia','Carla','Mirela']
    dictTI_ord={'BIOTERAPIE':'BI_ord','PSIHOTERAPIE INDIVIDUALA':'PI_ord','DDS MERIDIANE':'DDS_ord','MASAJ TERAPEUTIC':'Mter_ord','MASAJ REFLEXO':'Mref_ord','MASAJ RELAXARE':'Mrel_ord',
                'OLEATIE SACULET (include sauna)':'Ols_ord','OLEATIE COLACEL':'Olc_ord','SHIRODHARA (OLEATIE CAP)':'Shi_ord'}
    terapeutul=0
    dictTI_prescurtari={'BIOTERAPIE':'BIOTERAPIE','PSIHOTERAPIE INDIVIDUALA':'PSIHO IND','DDS MERIDIANE':'DDS','MASAJ TERAPEUTIC':'M TERAPEUTIC','MASAJ REFLEXO':'M REFLEXO','MASAJ RELAXARE':'M RELAXARE',
                'OLEATIE SACULET (include sauna)':'OL SACULET','OLEATIE COLACEL':'OL COLACEL','SHIRODHARA (OLEATIE CAP)':'SHIRODARA'}
                
############## de aici in jos pun in orar date: ar_pacienti
    if y1=="112" and ver_intr_sabloane == 1: # initial ver_intr_sabloane == 0 iar apoi devine 1 sau 2 doar daca se introduc sabloane; altfel el este 0
        nr_copii_sablon = 15-nr_zi #2 in exemplul nostru
        delta2= (dataa+datetime.timedelta(days=nr_copii_sablon-1)) # aceasta este ultima data (Duminica) ce va fi introdusa in tabela orar adica in exemplul nostru: 2020-08-16
        este_generat1 = db(db.orar).select(db.orar.dataa.max())[0] #dupa ce am facut sabloanele va fi o data maxima aceste 2 linii imi dau data maxima din tabela orar
        este_generat = este_generat1['_extra']['MAX("orar"."dataa")'] # aceasta este data maxima din tabela orar
        nr_rec = db((db.orar.id>0)).count() # numarul de inregistrari din tabela orar
        #data_sf = (db(db.orar_t).select().last()).dataa #aceasta este data ultima introdusa din programul terapeutilor pt a vedea pana la ce data pot genera orarul
        data_min = dataa # 2020-08-15
        data_max = delta2 # 2020-08-16
        
        i=0
        #nr_pacienti=9
        ##inceput 789 creez arrayurile cu terapii degrup d, individuale si cu cele de grup(aparatele)
        rows_terapii_degrupd=db(db.terapii.tip=='de grup d').select()    
        terapii_degrupd=[]
        for i2 in rows_terapii_degrupd:
            terapii_degrupd.append(i2.nume) 
        rows_terapii_individuale=db(db.terapii.tip=='individuala').select()
        terapii_individuale=[]
        for i2 in rows_terapii_individuale:
            terapii_individuale.append(i2.nume)
        rows_terapii_aparate=db(db.terapii.tip=='de grup').select()       
        terapii_aparate=[]
        for i2 in rows_terapii_aparate:
            terapii_aparate.append(i2.nume)
        rows_terapii_ind_apa=db(db.terapii.tip=='individuala').select() | (db(db.terapii.tip=='de grup')).select()     
        terapii_ind_tot=[]
        for i2 in rows_terapii_ind_apa:
            terapii_ind_tot.append(i2.nume)
           
            
        ##sfarsit 789 creez arrayurile cu terapii individuale si cu cele de grup(aparatele) si concatenarea lor 
        #nr_zi1=[]  
        for i in range(nr_copii_sablon): #
            
            
            ocupat_masa_oleatie1415=0
            ocupat_masa_masaj1415=0
            ocupat_masa_oleatie1516=0
            ocupat_masa_masaj1516=0
            ocupat_masa_oleatie1617=0
            ocupat_masa_masaj1617=0
            ocupat_masa_masaj1416=0
            ocupat_masa_oleatie1416=0
            delta_data_min= (data_min+datetime.timedelta(days=i))# aceasta este data curenta intai 15 apoi 16
            pacienti_all = db(db.orar_p.dataa<=delta_data_min).select() & (db(db.orar_p.sfarsit_tt>=delta_data_min)).select()
            pacienti_all_yt = db(db.orar_p.dataa<=delta_data_min).select() & (db(db.orar_p.sfarsit_tt>=delta_data_min)).select()
            array_yogaterapeutica=[]
            array_codv=[]
            array_t_individuala=[]
            delta1= (data_min+datetime.timedelta(days=i)) #delta1 este data cu care iau sablonul
            nr_zi1=(zile_sapt[delta1.strftime("%A")]) # vad in ce zi a saptamanii sant Ex: 7. Daca sunt in 6 sau 7 sunt in Week-end
            data_prima = (db(db.orar.dataa==delta1).select()).first() #aceasta este prima inregistrare de la care pleaca sablonul de 24 linii
            id_first_sablon = data_prima.id           # id-ul pe care o sa operez in tabela orar si in functie de el pun date in cele 24 linii
            date_linia_6 = (db(db.orar.id==id_first_sablon+6).select()).first()# 9-10 SI 9.30-10.30 YOGA TERAPEUTICA sau alta terapie daca vine de la 9
            date_linia_7 = (db(db.orar.id==id_first_sablon+7).select()).first()# 10-11 YOGA TERAPEUTICA sau alta terapie daca vine de la 9 sau de la 10 
            date_linia_8 = (db(db.orar.id==id_first_sablon+8).select()).first()# 11-12            
            date_linia_9 = (db(db.orar.id==id_first_sablon+9).select()).first()# 12-13
            date_linia_10 = (db(db.orar.id==id_first_sablon+10).select()).first()# 13-14 
            date_linia_12 = (db(db.orar.id==id_first_sablon+12).select()).first()# 14-15
            date_linia_14 = (db(db.orar.id==id_first_sablon+14).select()).first()# 15.15-16.15
            date_linia_16 = (db(db.orar.id==id_first_sablon+16).select()).first()# 16.30-17 sau 17.30 ultima terapie o pun si pe randul 16 si pe randul 17
            date_linia_17 = (db(db.orar.id==id_first_sablon+17).select()).first()# 16.30sau17- 17-30 ultima terapie o pun si pe randul 16 si pe randul 17
            date_linia_18 = (db(db.orar.id==id_first_sablon+18).select()).first()# 17.30-18.30 
            date_linia_21 = (db(db.orar.id==id_first_sablon+21).select()).first()# pentru terapiile de seara
            

            arraypacienti=arraypacienti1(pacienti_all,delta_data_min)
            #array_row=arraypacienti['array_row']
            array_datele_orar_p=arraypacienti['array_datele_orar_p'] #acesta este un array f mare ce contine toate datele despre toti pacientii,ambulatorii din ziua respectiva 19 campuri/pacient
            array_pacienti=arraypacienti['array_pacienti'] #array_pacienti=['Dobre Ana 1-1', 'Irimia Maria 1-2','test5-ambulatoriuP',test1-ambulatoriu','test6-ambulatoriu', 'test8aa-ambulatoriu']
            nr_pacienti_ambulatoriu=arraypacienti['nr_pacienti_ambulatoriu']  #sunt absolut toti ambulatorii Ex: 8 
            array_pacientii=arraypacienti['array_pacientii']
            array_pacienti_ambulatoriu=arraypacienti['array_pacienti_ambulatoriu']
            array_pacienti_p_si_aP=arraypacienti['array_pacienti_p_si_aP']
            array_pacienti_p=arraypacienti['array_pacienti_p']
            array_pacienti_aP=arraypacienti['array_pacienti_aP']
            array_pacienti_a=arraypacienti['array_pacienti_a']
            
            #############################inceput cod pt a vedea diverse variabile pentru terapiile individuale
            #xox1=array_datele_orar_p
            #xox1=array_datele_orar_p[19*nr_pacienti_pacienti]
            nr_pacienti=len(array_pacienti) # variabila pt a vedea nr de pacienti in ziua respectiva:6 am vazut Ex: nr_pacienti=14
            nr_pacienti_p_si_aP = len([i1 for i1 in array_datele_orar_p if i1=='pacientt' or i1=='ambulatoriup']) #nr pacienti de tipul pacienti care pot fi si pacienti si ambulatori Ex:nr_pacienti_p_si_aP=8
            nr_pacienti_p = len([i1 for i1 in array_datele_orar_p if i1=='pacientt']) #nr pacienti de tipul pacienti care pot fi doar pacienti Ex: nr_pacienti_p = 6
            nr_pacienti_aP = nr_pacienti_p_si_aP-nr_pacienti_p #Ex: nr_pacienti_aP=2
            nr_pacienti_a = nr_pacienti-nr_pacienti_p_si_aP #nr pacienti de tipul ambulatori care vin si pleaca la orice ora Ex: nr_pacienti_a = 6
            
            id=[i2 for i2, j2 in enumerate(array_datele_orar_p) if j2!=None and (j2=='pacientt' or j2=='ambulatoriup')] #indexul in array-ul array_datele_orar_p unde este 'pacientt' si 'ambulatoriup' 
            
            
            
            #delta_data_min este data curenta
            #array_id_orar_p este array-ul cu id-urile pacientilor din data respectiva din tabela orar_p
            #aici122 se intoduc in linia 1 a sablonului toti pacientii
            for j77 in range(nr_pacienti):  #aici se intoduc in linia 1 a sablonului toti pacientii
                zzzz= 'pacient_'+str(j77+1)
                zzz = {'1':zzzz}
                #data_prima.update_record(pacient_1=array_pacienti[j])
                data_prima.update_record(**{zzz['1']:array_pacienti[j77]})

            #aici122 sfarsitse intoduc in linia 1 a sablonului toti pacientii 


            ###inceput cod1347 pt a pune in array-uri terapeutii:toti,toti fara principali,dim,dup,nu
            vedem_daca_exista = db(db.orar_t.dataa==delta_data_min).select().first()
            nu_am_terapeuti=0
            
            if vedem_daca_exista!=None:
                arrayuri_terapeuti=arrayuri_terapeuti1(delta_data_min)
                array_terapeuti_ziua_respectiva=arrayuri_terapeuti['array_terapeuti_ziua_respectiva']
                ter_dim=arrayuri_terapeuti['ter_dim']
                ter_dup=arrayuri_terapeuti['ter_dup']
                ter_dim1=arrayuri_terapeuti['ter_dim1']
                ter_dup1=arrayuri_terapeuti['ter_dup1']
                ter_toti=arrayuri_terapeuti['ter_toti']
                ter_nu=arrayuri_terapeuti['ter_nu']
            else:
                nu_am_terapeuti=1
            if nu_am_terapeuti==0: #adica am terapeuti          
                ###sfarsit cod1347 pt a pune in array-ul array_terapeuti_ziua_respectiva terapeutii cu intervalul in care lucreaza:['Catalin','7-16','Mari','14-23','Lidia','all',etc]
                ##### inceput11 cod pt a vedea terapiile posibile pe intervale de ore
                arrayuriterapii=arrayuriterapii1(terapii_degrupd,terapii_individuale,ter_dim,terapii_aparate,terapii_ind_tot,ter_dim1,ter_toti,ter_dup)
                terapii_degrupd1714=arrayuriterapii['terapii_degrupd1714']
                terapii_individuale714=arrayuriterapii['terapii_individuale714']
                terapii_aparate714=arrayuriterapii['terapii_aparate714']
                terapii_individuale_tot714=arrayuriterapii['terapii_individuale_tot714']
                terapii_individuale1714=arrayuriterapii['terapii_individuale1714']
                terapii_aparate1714=arrayuriterapii['terapii_aparate1714']
                terapii_individuale_tot1714=arrayuriterapii['terapii_individuale_tot1714']
                terapii_degrupd1416=arrayuriterapii['terapii_degrupd1416']
                terapii_individuale1416=arrayuriterapii['terapii_individuale1416']
                terapii_individuale1416x2=list(map(lambda x:x+x,terapii_individuale1416))
                terapii_aparate1416=arrayuriterapii['terapii_aparate1416']
                terapii_individuale_tot1416=arrayuriterapii['terapii_individuale_tot1416']
                terapii_degrupd1623=arrayuriterapii['terapii_degrupd1623']
                terapii_individuale1623=arrayuriterapii['terapii_individuale1623']
                terapii_aparate1623=arrayuriterapii['terapii_aparate1623']
                terapii_individuale_tot1623=arrayuriterapii['terapii_individuale_tot1623']
                ##### sfarsit11 cod pt a vedea terapiile posibile pe intervale de ore
                ####inceput1132 cod pt a realiza cele 3 linii de la pranz
                ##inceput144 cod pt a face arrayurile pt fiecare pacient, ambulator..
                dict_tab_pac={}
                #dict_ore_incepere={'7':'0','9':'0','10':'1','11':'2','12':'3','13':'4','14':'5','15.15':'6','16.30':'7','17.30':'8','17':'7'} #dictionar cu key=ora de inceperesi valoare=pozitia in dict_tab_pac['i5']
                for i5 in range(nr_pacienti):
                    ii5=str(i5)
                    dict_tab_pac[ii5]=[]# dict_tab_pac['0'] este numele primului array al primului pacient si tot asa... dict_tab_pac['14'] este numele ultimului pacient (15)
                    for i6 in range(9):
                        dict_tab_pac[ii5].append('-')
                if nr_pacienti_a!=0: #aici completez pt ambulatorii ambulatori tabelele de tip dict_tab_pac['8'] pana la dict_tab_pac['14']
                    for i5 in range(nr_pacienti):
                        if i5>=(nr_pacienti_p_si_aP):
                            ora_de_incepere=array_datele_orar_p[-(nr_pacienti-i5)*19+17] #este ora cand incepe ambulatoriu.ambulatoriu terapiile
                            ora_de_plecare=array_datele_orar_p[-(nr_pacienti-i5)*19+18]
                            valoarekey=int(float(dict_ore_incepere[ora_de_incepere]))
                            valoarekey1=int(float(dict_ore_incepere[ora_de_incepere]))
                            key_yv=0#variabila de control pt a vedea daca avem YT sau VOCALE pt acest ambulator: 0-nu am nici YT nici VOCALE; 1-am VOCALE; 2-am YT; 3-am tot
                            
                            if ('VOCALE' in array_datele_orar_p[-(nr_pacienti-i5)*19+1])==True or ('RESPIRATII' in array_datele_orar_p[-(nr_pacienti-i5)*19+1])==True or ('PSIHOTERAPIE DE GRUP (CODUL VINDECARII, IERTARE, MEDITATIE)' in array_datele_orar_p[-(nr_pacienti-i5)*19+1])==True:
                                (dict_tab_pac[str((i5))])[0]='VOCALE,RESPIRATII,CODUL V'
                                (dict_tab_pac[str((i5))])[1]='VOCALE,RESPIRATII,CODUL V'
                                key_yv=key_yv+1
                            if ('YOGA TERAPEUTICA' in array_datele_orar_p[-(nr_pacienti-i5)*19+1])==True:
                                (dict_tab_pac[str((i5))])[2]='YOGA TERAPEUTICA'
                                key_yv=key_yv+2
                            if key_yv==0: #nu am YT si nici VOCALE si pun direct individualele si aparatelele
                                if (array_datele_orar_p[-(nr_pacienti-i5)*19+3])==None or (array_datele_orar_p[-(nr_pacienti-i5)*19+3])==[]:
                                    pass
                                else:
                                    for i7 in array_datele_orar_p[-(nr_pacienti-i5)*19+3]:
                                        (dict_tab_pac[str((i5))])[valoarekey]=i7
                                        valoarekey=valoarekey+1
                                
                                if (array_datele_orar_p[-(nr_pacienti-i5)*19+7])==None or (array_datele_orar_p[-(nr_pacienti-i5)*19+7])==[]:
                                    pass
                                else:
                                    for i7 in array_datele_orar_p[-(nr_pacienti-i5)*19+7]:
                                        if i7=='CROMOTERAPIE':
                                            valoarekey=valoarekey-1
                                            if (dict_tab_pac[str((i5))])[valoarekey]=='LAMPA FRECVENTE':
                                                (dict_tab_pac[str((i5))])[valoarekey]='Frecv-CR'
                                                valoarekey=valoarekey+1
                                            else:
                                                valoarekey=valoarekey+1
                                                (dict_tab_pac[str((i5))])[valoarekey]=i7    
                                        else:
                                            (dict_tab_pac[str((i5))])[valoarekey]=i7
                                            valoarekey=valoarekey+1                         

                            if key_yv==1: # am doar Vocale si pun individualele si aparatele dupa ele
                                if int(float(ora_de_incepere))<=11:
                                    valoarekey=2
                                    if (array_datele_orar_p[-(nr_pacienti-i5)*19+3])==None or (array_datele_orar_p[-(nr_pacienti-i5)*19+3])==[]:
                                        pass
                                    else:
                                        for i7 in array_datele_orar_p[-(nr_pacienti-i5)*19+3]:
                                            (dict_tab_pac[str((i5))])[valoarekey]=i7
                                            valoarekey=valoarekey+1
                                    if (array_datele_orar_p[-(nr_pacienti-i5)*19+7])==None or (array_datele_orar_p[-(nr_pacienti-i5)*19+7])==[]:
                                        pass
                                    else:
                                        for i7 in array_datele_orar_p[-(nr_pacienti-i5)*19+7]:
                                            if i7=='CROMOTERAPIE':
                                                valoarekey=valoarekey-1
                                                if (dict_tab_pac[str((i5))])[valoarekey]=='LAMPA FRECVENTE':
                                                    (dict_tab_pac[str((i5))])[valoarekey]='Frecv-CR'
                                                    valoarekey=valoarekey+1
                                                else:
                                                    valoarekey=valoarekey+1
                                                    (dict_tab_pac[str((i5))])[valoarekey]=i7    
                                            else:
                                                (dict_tab_pac[str((i5))])[valoarekey]=i7
                                                valoarekey=valoarekey+1  
                                if int(float(ora_de_incepere))>11:
                                    valoarekey=int(dict_ore_incepere[ora_de_incepere])
                                    if (array_datele_orar_p[-(nr_pacienti-i5)*19+3])==None or (array_datele_orar_p[-(nr_pacienti-i5)*19+3])==[]:
                                        pass
                                    else:
                                        for i7 in array_datele_orar_p[-(nr_pacienti-i5)*19+3]:
                                            (dict_tab_pac[str((i5))])[valoarekey]=i7
                                            valoarekey=valoarekey+1
                                    if (array_datele_orar_p[-(nr_pacienti-i5)*19+7])==None or (array_datele_orar_p[-(nr_pacienti-i5)*19+7])==[]:
                                        pass
                                    else:
                                        for i7 in array_datele_orar_p[-(nr_pacienti-i5)*19+7]:
                                            if i7=='CROMOTERAPIE':
                                                valoarekey=valoarekey-1
                                                if (dict_tab_pac[str((i5))])[valoarekey]=='LAMPA FRECVENTE':
                                                    (dict_tab_pac[str((i5))])[valoarekey]='Frecv-CR'
                                                    valoarekey=valoarekey+1
                                                else:
                                                    valoarekey=valoarekey+1
                                                    (dict_tab_pac[str((i5))])[valoarekey]=i7    
                                            else:
                                                (dict_tab_pac[str((i5))])[valoarekey]=i7
                                                valoarekey=valoarekey+1  
                            if key_yv==2: # am doar YT de la 11-12 si pun individualele si aparatele posibil si inainte si si dupa!!!
                                valoarekey=int(dict_ore_incepere[ora_de_incepere])
                                if (array_datele_orar_p[-(nr_pacienti-i5)*19+3])==None or (array_datele_orar_p[-(nr_pacienti-i5)*19+3])==[]:
                                    pass
                                else:
                                    for i7 in array_datele_orar_p[-(nr_pacienti-i5)*19+3]:
                                        if valoarekey!=2:
                                            (dict_tab_pac[str((i5))])[valoarekey]=i7
                                            valoarekey=valoarekey+1
                                        else:
                                            valoarekey=valoarekey+1
                                            (dict_tab_pac[str((i5))])[valoarekey]=i7
                                            valoarekey=valoarekey+1   
                                if (array_datele_orar_p[-(nr_pacienti-i5)*19+7])==None or (array_datele_orar_p[-(nr_pacienti-i5)*19+7])==[]:
                                    pass
                                else:
                                    for i7 in array_datele_orar_p[-(nr_pacienti-i5)*19+7]:
                                        if valoarekey!=2:
                                            if i7=='CROMOTERAPIE':
                                                valoarekey=valoarekey-1
                                                if (dict_tab_pac[str((i5))])[valoarekey]=='LAMPA FRECVENTE':
                                                    (dict_tab_pac[str((i5))])[valoarekey]='Frecv-CR'
                                                    valoarekey=valoarekey+1
                                                else:
                                                    valoarekey=valoarekey+1
                                                    (dict_tab_pac[str((i5))])[valoarekey]=i7    
                                            else:
                                                (dict_tab_pac[str((i5))])[valoarekey]=i7
                                                valoarekey=valoarekey+1  
                                        else:        
                                            valoarekey=valoarekey+1
                                            if i7=='CROMOTERAPIE':
                                                valoarekey=valoarekey-1
                                                if (dict_tab_pac[str((i5))])[valoarekey]=='LAMPA FRECVENTE':
                                                    (dict_tab_pac[str((i5))])[valoarekey]='Frecv-CR'
                                                    valoarekey=valoarekey+1
                                                elif (dict_tab_pac[str((i5))])[valoarekey]=='YOGA TERAPEUTICA':
                                                    valoarekey=valoarekey-1
                                                    (dict_tab_pac[str((i5))])[valoarekey]='Frecv-CR'
                                                    valoarekey=valoarekey+2
                                                else:
                                                    valoarekey=valoarekey+1
                                                    (dict_tab_pac[str((i5))])[valoarekey]=i7    
                                            else:
                                                (dict_tab_pac[str((i5))])[valoarekey]=i7
                                                valoarekey=valoarekey+1  
                            if key_yv==3:
                                valoarekey=int(dict_ore_incepere[ora_de_incepere])
                                if valoarekey<=2:
                                    valoarekey=3
                                if (array_datele_orar_p[-(nr_pacienti-i5)*19+3])==None or (array_datele_orar_p[-(nr_pacienti-i5)*19+3])==[]:
                                    pass
                                else:
                                    for i7 in array_datele_orar_p[-(nr_pacienti-i5)*19+3]:
                                        (dict_tab_pac[str((i5))])[valoarekey]=i7
                                        valoarekey=valoarekey+1
                                        
                                if (array_datele_orar_p[-(nr_pacienti-i5)*19+7])==None or (array_datele_orar_p[-(nr_pacienti-i5)*19+7])==[]:
                                    pass
                                else:
                                    for i7 in array_datele_orar_p[-(nr_pacienti-i5)*19+7]:
                                        if i7=='CROMOTERAPIE':
                                            valoarekey=valoarekey-1
                                            if (dict_tab_pac[str((i5))])[valoarekey]=='LAMPA FRECVENTE':
                                                (dict_tab_pac[str((i5))])[valoarekey]='Frecv-CR'
                                                valoarekey=valoarekey+1
                                            else:
                                                valoarekey=valoarekey+1
                                                (dict_tab_pac[str((i5))])[valoarekey]=i7    
                                        else:
                                            (dict_tab_pac[str((i5))])[valoarekey]=i7
                                            valoarekey=valoarekey+1                            
                
                
                if nr_pacienti_aP!=0: 
                    for i5 in range(nr_pacienti):
                        if i5>=(nr_pacienti_p) and i5<(nr_pacienti_p_si_aP):
                            if ('VOCALE' in array_datele_orar_p[-(nr_pacienti-i5)*19+1])==True or ('RESPIRATII' in array_datele_orar_p[-(nr_pacienti-i5)*19+1])==True or ('PSIHOTERAPIE DE GRUP (CODUL VINDECARII, IERTARE, MEDITATIE)' in array_datele_orar_p[-(nr_pacienti-i5)*19+1])==True:
                                (dict_tab_pac[str((i5))])[0]='VOCALE,RESPIRATII,CODUL V'
                                (dict_tab_pac[str((i5))])[1]='VOCALE,RESPIRATII,CODUL V'
                                
                            if ('YOGA TERAPEUTICA' in array_datele_orar_p[-(nr_pacienti-i5)*19+1])==True:
                                (dict_tab_pac[str((i5))])[2]='YOGA TERAPEUTICA'
                            if len(array_datele_orar_p[-(nr_pacienti-i5)*19+3])>0:
                                t_individ=(array_datele_orar_p[-(nr_pacienti-i5)*19+3])[0]
                                (dict_tab_pac[str((i5))])[5]=t_individ
                            (dict_tab_pac[str((i5))])[6]='--'
                            (dict_tab_pac[str((i5))])[7]='---'

                if nr_pacienti_p!=0: 
                    for i5 in range(nr_pacienti):
                        if i5<(nr_pacienti_p):
                            if ('VOCALE' in array_datele_orar_p[-(nr_pacienti-i5)*19+1])==True or ('RESPIRATII' in array_datele_orar_p[-(nr_pacienti-i5)*19+1])==True or ('PSIHOTERAPIE DE GRUP (CODUL VINDECARII, IERTARE, MEDITATIE)' in array_datele_orar_p[-(nr_pacienti-i5)*19+1])==True:
                                (dict_tab_pac[str((i5))])[0]='VOCALE,RESPIRATII,CODUL V'
                                (dict_tab_pac[str((i5))])[1]='VOCALE,RESPIRATII,CODUL V'
                                
                            if ('YOGA TERAPEUTICA' in array_datele_orar_p[-(nr_pacienti-i5)*19+1])==True:
                                (dict_tab_pac[str((i5))])[2]='YOGA TERAPEUTICA'
                            if len(array_datele_orar_p[-(nr_pacienti-i5)*19+3])>0:
                                #t_individ=(array_datele_orar_p[-(nr_pacienti-i5)*19+3])[0]
                                t_individ='+'
                                (dict_tab_pac[str((i5))])[5]=t_individ
                            (dict_tab_pac[str((i5))])[6]='--'
                            (dict_tab_pac[str((i5))])[7]='---'
                ##sfarsit 144 cod pt a face arrayurile pt fiecare pacient ambulator..     are 160 linii
                ##inceput1133 construire matrici 
                matrix_A=[]
                for i10 in range(nr_pacienti):
                    oooo= 'dict_tab_pac['+"'"+str(i10)+"'"+']'
                    matrix_A.append(eval(oooo))
                            

                matrix_A=np.array(matrix_A)    
                matrix_TA=matrix_A.transpose()
                ##sfarsit1133 construire matrici
                ##


                s_a_rezolvat_aici=0
                
                #mA=matrix_TA[:]
                #mA=matrix_TA.copy()
                mA=1
                #ar_pacienti2 = ar_pacienti.copy() #face ce face si linia de mai sus -sunt echivalente

                if nr_pacienti>0:
                    ######## inceput cod11 aflu prin variabila contor_t_individuala_1416 cate terapii individuale am in primele 2 intervale de la 14-15 si 15.15-16.15. Daca este impar se paseaza o terapie in 16.30-17.30
                    ##
                    
                    ##
                    
                    contor_terapeuti1617=[]
                    for row in range(len(ter_dup)):
                        contor_terapeuti1617.append(0)
                    
                        
                                                                                    


                                


                    
                    mutare_da_sau_nu57=0
                    mutare5775_imparul=0
                    contor_t_individuala_1416=0
                    for row in matrix_TA[5]:
                        if (row in terapii_individuale)==True or row=='+':
                            contor_t_individuala_1416=contor_t_individuala_1416+1
                    for row in matrix_TA[6]:
                        if (row in terapii_individuale)==True or row=='+':
                            contor_t_individuala_1416=contor_t_individuala_1416+1
                    contor_t_individuala_1416PplusAP=0 #variabila contor_t_individuala_1416PplusAP imi spune cate terapii individuale exista pt pacienti si pt pacienti-ambulatori in linia matrix_TA[5]
                    iii5=0
                    for row in matrix_TA[5]:
                        if iii5<nr_pacienti_p_si_aP:
                            if (row in terapii_individuale)==True or row=='+':
                                contor_t_individuala_1416PplusAP=contor_t_individuala_1416PplusAP+1        
                        iii5=iii5+1
                    terapii_individuale1623_scot_ambulatorii_ambulatori=terapii_individuale1623[:]  #Ex: terapii_individuale1623_scot_ambulatorii_ambulatori=[0, 2, 2, 2, 2, 0, 3, 0, 0] am scos ambulat-ambulat din linia3
                    for iii5 in range(nr_pacienti_p_si_aP,nr_pacienti):
                            if (matrix_TA[7][iii5] in terapii_individuale)==True:
                                idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==matrix_TA[7][iii5]][0]
                                terapii_individuale1623_scot_ambulatorii_ambulatori[idx]=terapii_individuale1623[idx]-1
                        
                    ######## sfarsit cod11 aflu prin variabila contor_t_individuala_1416 cate terapii individuale am in primele 2 intervale de la 14-15 si 15.15-16.15. Daca este impar se paseaza o terapie in 16.30-17.30
                    ###aflu terapeutii necesari
                    nr_terapeuti_necesari=int(contor_t_individuala_1416/2)
                    ###sfarsit aflu terapeutii necesari
                    
                    ##inceput 55 creez duplicat pe care o sa operez pt arrayiul : terapii_individuale1416x2. Arrayul duplicat pe care o sa operez va fi terapii_individuale1416x2dupa
                    terapii_individuale1416x2dupa=[]
                    for row in terapii_individuale1416x2:
                        terapii_individuale1416x2dupa.append(row)
                    ##sfarsit 55 creez duplicat pe care o sa operez pt arrayiul : terapii_individuale1416x2. Arrayul duplicat pe care o sa operez va fi terapii_individuale1416x2dupa   
                    ##inceput cod121 inceput pt a scoate din array-ul terapii_individuale1416x2 terapiile tuturor ambulatorilor. Va arata astfel:[1, 4, 4, 4, 6, 0, 5, 0, 1]
                    for row in matrix_TA[5]:
                        if (row in terapii_individuale)==True:        
                            idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==row][0] #am gasit de exemplu pt DDS indexul este 8
                            terapii_individuale1416x2dupa[idx]=terapii_individuale1416x2dupa[idx]-1
                            if  idx==1 or idx==2 or idx==3:
                                ocupat_masa_oleatie1415=ocupat_masa_oleatie1415+1
                            if  idx==4 or idx==5 or idx==6 or idx==7 or idx==8:
                                ocupat_masa_masaj1415=ocupat_masa_masaj1415+1
                    for row in matrix_TA[6]:
                        if (row in terapii_individuale)==True:        
                            idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==row][0] #am gasit de exemplu pt DDS indexul este 8
                            terapii_individuale1416x2dupa[idx]=terapii_individuale1416x2dupa[idx]-1
                            if  idx==1 or idx==2 or idx==3:
                                ocupat_masa_oleatie1516=ocupat_masa_oleatie1516+1
                            if  idx==4 or idx==5 or idx==6 or idx==7 or idx==8:
                                ocupat_masa_masaj1516=ocupat_masa_masaj1516+1
                    for row in matrix_TA[7]:
                        if (row in terapii_individuale)==True:        
                            idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==row][0] #am gasit de exemplu pt DDS indexul este 8
                            
                            if  idx==1 or idx==2 or idx==3:
                                ocupat_masa_oleatie1617=ocupat_masa_oleatie1617+1
                            if  idx==4 or idx==5 or idx==6 or idx==7 or idx==8:
                                ocupat_masa_masaj1617=ocupat_masa_masaj1617+1
                    ocupat_masa_masaj1416=ocupat_masa_masaj1415+ocupat_masa_masaj1516
                    ocupat_masa_oleatie1416=ocupat_masa_oleatie1415+ocupat_masa_oleatie1516
                    ##sfarsit cod121 inceput pt a scoate din array-ul terapii_individuale1416x2 terapiile tuturor ambulatorilor. Va arata astfel:[1, 4, 4, 4, 6, 0, 5, 0, 1]
                    ##AICI AM DEJA ARRAYUL terapii_individuale1416x2dupa care are scoase terapiile individuale ale TUTUROR ambulatorilor. De aici pun TI pt pacienti
                    ##inceput cod78 pt a face arrayul cu TI ramase doar pentru pacienti: TI_doar_pentru_pacienti=['PSIHOTERAPIE INDIVIDUALA', 'SHIRODHARA (OLEATIE CAP)', 'OLEATIE COLACEL',.. 'MASAJ REFLEXO','DDS MERIDIANE']
                    TI_doar_pentru_pacienti=[]
                    i7=0
                    for row in terapii_individuale:
                        if terapii_individuale1416x2dupa[i7]>0:
                            TI_doar_pentru_pacienti.append(row)
                        i7=i7+1
                    ##sfarsit cod78 pt a face arrayul cu TI ramase doar pentru pacienti: TI_doar_pentru_pacienti=['PSIHOTERAPIE INDIVIDUALA', 'SHIRODHARA (OLEATIE CAP)', 'OLEATIE COLACEL',.. 'MASAJ REFLEXO','DDS MERIDIANE']

                    ##inceput1471 creez arrayurile cu terapiile individuale ale fiecaruia
                    dict_tab_pac_ii={}
                    for i5 in range(nr_pacienti):
                        ii5=str(i5)
                        dict_tab_pac_ii[ii5]=[]# dict_tab_pac_ii['0'] este numele primului array al primului pacient si tot asa... dict_tab_pac['14'] este numele ultimului pacient (15)
                        if len(array_datele_orar_p[-(nr_pacienti-i5)*19+3])>0:
                            for i6 in (array_datele_orar_p[-(nr_pacienti-i5)*19+3]):
                                dict_tab_pac_ii[ii5].append(i6)
                    ##sfarsit1471 creez arrayurile cu terapiile individuale ale fiecaruia
                    ##inceput cod149 scot din arrayurile dict_tab_pac_ii[-] toate terapiile care nu au terapeuti deloc adica scot ce nu e in arrayul: TI_doar_pentru_pacienti
                    for i5 in range(nr_pacienti_p):
                        ii5=str(i5)
                        iii5=dict_tab_pac_ii[ii5][:]
                        for row in iii5:
                            if row not in TI_doar_pentru_pacienti:
                                dict_tab_pac_ii[ii5].remove(row)

                    ##sfarsit cod149 scot din arrayurile dict_tab_pac_ii[-] toate terapiile care nu au terapeuti deloc adica scot ce nu e in arrayul: TI_doar_pentru_pacienti
                    
                    ###########inceput cod1367 ordonez arrayul fiecarui PACIENT in ordinea terapiilor (fac analiza ultimei inregistrari din orar_p.individuala_da) dict_tab_pac_ii_sort[15]-asa vor arata arrayurile
                    
                    dict_tab_pac_ii_sort={} #am creat dictionarul de arrayuri in care vor fi arrayurile sortate
                    for i5 in range(nr_pacienti):
                        ii5=str(i5)
                        dict_tab_pac_ii_sort[ii5]=[]
                        
                    for i5 in range(nr_pacienti):
                        ii5=str(i5)
                        iii5=0
                        for iii5 in range(nr_pacienti): 
                            if ((array_datele_orar_p[-(nr_pacienti-iii5)*19+15])=='pacient' and i5==iii5):

                                if ((array_datele_orar_p[-(nr_pacienti-iii5)*19+4])==None): #campul individuala_nu
                                    
                                    
                                    if (array_datele_orar_p[-(nr_pacienti-iii5)*19+2])==None: #campul terapie importanta
                                        
                                        dict_tab_pac_ii_sort[ii5]=dict_tab_pac_ii[ii5][:]
                                        
                                        
                                    else:
                                        dict_tab_pac_ii_sort[ii5].append((array_datele_orar_p[-(nr_pacienti-iii5)*19+2])[0])
                                        
                                        for row1 in dict_tab_pac_ii[ii5]:
                                            if row1!=(array_datele_orar_p[-(nr_pacienti-iii5)*19+2])[0]:
                                                dict_tab_pac_ii_sort[ii5].append(row1)

                                else:
                                    array_last_TI= eval((array_datele_orar_p[-(nr_pacienti-iii5)*19+4])[-1])[1]
                                    

                                    array_last_TI1 = array_last_TI[:]
                                    array_last_TI1.sort(key=lambda x: array_last_TI.count(x))
                                    seen={}
                                    array_last_TI2=[seen.setdefault(x, x) for x in array_last_TI1 if x not in seen]#acesta este arrayul SORTAT cu ce terapii s-au facut pana azi in ordinea crescatoare a nr aparitiei
                                    array_last_TI3=array_last_TI2[:]
                                    for row in (array_datele_orar_p[-(nr_pacienti-iii5)*19+3])[::-1]: #parcurgere de la ultimul la primul
                                        if row not in array_last_TI3:
                                            array_last_TI2.insert(0,row)
                                    if (array_datele_orar_p[-(nr_pacienti-iii5)*19+2])==None: #campul terapie importanta
                                        pass
                                    else:
                                        if (array_datele_orar_p[-(nr_pacienti-iii5)*19+2])[0] ==  array_last_TI[-1]:
                                            array_last_TI2.append((array_datele_orar_p[-(nr_pacienti-iii5)*19+2])[0])
                                            for row in array_last_TI2:
                                                if row == (array_datele_orar_p[-(nr_pacienti-iii5)*19+2])[0]:
                                                    array_last_TI2.remove(row)
                                                    break
                                        else:
                                            array_last_TI2.remove((array_datele_orar_p[-(nr_pacienti-iii5)*19+2])[0])
                                            array_last_TI2.insert(0,(array_datele_orar_p[-(nr_pacienti-iii5)*19+2])[0])

                                    dict_tab_pac_ii_sort[ii5]=array_last_TI2
                            elif ((array_datele_orar_p[-(nr_pacienti-iii5)*19+15])=='ambulatoriu' and i5==iii5):
                                dict_tab_pac_ii_sort[ii5]=dict_tab_pac_ii[ii5][:]
                                
                            iii5=iii5+1 
                    ##inceput cod1149 scot din arrayurile dict_tab_pac_ii[-] toate terapiile care nu au terapeuti deloc adica scot ce nu e in arrayul: TI_doar_pentru_pacienti
                    for i5 in range(nr_pacienti_p):
                        ii5=str(i5)
                        iii5=dict_tab_pac_ii_sort[ii5][:]
                        for row in iii5:
                            if row not in TI_doar_pentru_pacienti:
                                dict_tab_pac_ii_sort[ii5].remove(row)

                    ##sfarsit cod1149 scot din arrayurile dict_tab_pac_ii[-] toate terapiile care nu au terapeuti deloc adica scot ce nu e in arrayul: TI_doar_pentru_pacienti                                   
                    ##############sfarsit cod1367 ordonez arrayul fiecarui PACIENT in ordinea terapiilor (fac analiza ultimei inregistrari din orar_p.individuala_da)  dict_tab_pac_ii_sort[15]-asa vor arata arrayurile
                    ##inceput fac13 un array cu arrayurile pacientilor
                    ar_pacienti=[] #array cu arrayurile tuturor pacientilor ordonati
                    ar_pacienti_doarTI=[] #array cu 13 terapii (doar care sunt principale+cele ale ambulatorilor si"-" daca nu sunt principale, dar pica ca si nr de pacienti + pac-amb)
                    ar_pacienti_doarTI3=[] #array mic 2 itemi ca exemplu. doar cu TI ale ambulatorilor+pacientilor care depaseste si trebuie coborat aici.ar_pacienti_doarTI3=['PSIHOTERAPIE INDIVIDUALA', 'DDS MERIDIANE']
                    ar_pacienti_doarTI33=[] #array doar cu TI doar ale pacientilor chiar daca se repeta.ar_pacienti_doarTI33=['PSIHOTERAPIE INDIVIDUALA', 'PSIHOTERAPIE INDIVIDUALA', 'PSIHOTERAPIE INDIVIDUALA',...]
                    ar_pacienti_doarTI333=[] # arrayul de mai sus dar nu se repeta ex: ar_pacienti_doarTI333=['PSIHOTERAPIE INDIVIDUALA', 'DDS MERIDIANE']
                    ar_Ap_din_matrixTA5=[]#arrayul cu toate terapiile pacientilor-ambulatori Ex:ar_Ap_din_matrixTA5=['DDS MERIDIANE', 'PSIHOTERAPIE INDIVIDUALA', '-']
                    ar_Ap_din_matrixTA51=[]#arrayul cu toate terapiile pacientilor-ambulatori in ordine descrescatoare cu duplicate Ex:ar_Ap_din_matrixTA5=['PSIHOTERAPIE INDIVIDUALA', 'DDS MERIDIANE']
                    ar_Ap_din_matrixTA511=[]#arrayul cu toate terapiile pacientilor-ambulatori in ordine descrescatoare fara duplicate Ex:ar_Ap_din_matrixTA5=['PSIHOTERAPIE INDIVIDUALA', 'DDS MERIDIANE']
                    lista_indecsi_AP=[]
                    array_indecsi_aP=[] #indecsii din matrix_TA[5] ce apartin pacientilor-ambulatori 
                    var_index_coboara_la_linia3=0
                    for row in range(nr_pacienti_p):
                        ar_pacienti.append(dict_tab_pac_ii_sort[str(row)])
                    ##sfarsit fac13 un array cu arrayurile pacientilor. 
                    ####inceput cod478 verificare daca opresc sau nu terapeutul de dimineata
                    ar_pacienti_plus_Ap_plus_Aa1416=ar_pacienti[:]
                    ar_pacientiApAa=[]
                    i8=0
                    
                    for i7 in matrix_TA[5]:# nu il intereseaza pacientii ci doar cei de Pa si Aa
                        if i8>nr_pacienti_p-1:
                            if i7 in terapii_individuale:
                                ar_pacientiApAa.append(i7)
                                
                              
                        i8=i8+1
                    
                    for i7 in matrix_TA[6]:
                        if i7 in terapii_individuale:
                            ar_pacientiApAa.append(i7)
                            
                    i8=0
                    Pp_Ti5=0
                    Pa_Ti5=0
                    Aa_Ti5=0
                    Aa_Ti6=0
                    verificare_terapie_pentru_terapeutul_de_dimineata='-'
                    for i7 in matrix_TA[5]:
                        if i7 in terapii_individuale or i7=='+':
                            if i8<nr_pacienti_p:
                                Pp_Ti5=Pp_Ti5+1
                            if i8 in range(nr_pacienti_p,nr_pacienti_p_si_aP):
                                Pa_Ti5=Pa_Ti5+1
                            if i8 in range(nr_pacienti_p_si_aP,nr_pacienti):
                                Aa_Ti5=Aa_Ti5+1    
                        i8=i8+1
                    i8=0    
                    for i7 in matrix_TA[6]:
                        if i7 in terapii_individuale:
                            if i8 in range(nr_pacienti_p_si_aP,nr_pacienti):
                                Aa_Ti6=Aa_Ti6+1
                        i8=i8+1    
                    i8=0
                    ar_pacientiPpApAa_neaparat=[]
                    for i7 in ar_pacienti:
                        if len(i7)!=0 and (array_datele_orar_p[-(nr_pacienti-i8)*19+2])!=None:
                            if i7[0]==((array_datele_orar_p[-(nr_pacienti-i8)*19+2])[0]):
                                ar_pacientiPpApAa_neaparat.append(i7[0])
                        i8=i8+1    
                    for i7 in ar_pacientiApAa: #este[]
                        ar_pacientiPpApAa_neaparat.append(i7)
                    terapeut_dimineata_ramane='da'
                    var_terapeut_dimineata_ramane=0
                    uu=0
                    for i7 in ar_pacientiPpApAa_neaparat:
                        for i8 in ter_dup:
                            if i8!='lipsa T dup':
                                
                                terap=db(db.terapeuti.nume==i8).select().first()
                                if (i7 in terap.ce_terapii_face)==True:
                                    terapeut_dimineata_ramane='nu'
                                    var_terapeut_dimineata_ramane=1
                                    uu=1
                                    break
                                else:
                                    terapeut_dimineata_ramane='da'
                                    var_terapeut_dimineata_ramane=0
                                
                        if var_terapeut_dimineata_ramane==0:
                            break
                        
                    if Aa_Ti5>len(ter_dup) or Aa_Ti6>len(ter_dup):
                        terapeut_dimineata_ramane='da'

                    #Aa_Ti5x=ar_pacientiPpApAa_neaparat

                    ####sfarsit cod478 verificare daca opresc sau nu terapeutul de dimineata
                    ###inceput cod45 continuare de mai sus  pt a vedea daca terapeutul de dimineata pleaca acasa
                    pacienti3unulmutatinlinia3=0
                    if contor_t_individuala_1416==3 and contor_t_individuala_1416PplusAP>0:
                        i8=0
                        for i7 in matrix_TA[7]:
                            if i8<nr_pacienti_p_si_aP:
                                if  i7!='-' or i7!='--' or i7!='---':
                                    pacienti3unulmutatinlinia3=1
                                    break
                            i8=i8+1
                        if  terapeut_dimineata_ramane=='nu' and pacienti3unulmutatinlinia3==0 and len(ter_dup)==1:
                            terapeut_dimineata_ramane='da'
                    variabila1=0
                    if contor_t_individuala_1416<4 and terapeut_dimineata_ramane=='nu':
                        ter_toti=ter_dup[:]
                        variabila1=1
                    pleaca=0
                    trebuiesastea=0
                    
                    
                    if len(ter_dup)>0 and ter_dup[0]!='lipsa T dup':
                        if variabila1==0 and contor_t_individuala_1416<4:
                            
                            if contor_t_individuala_1416<4:
                                if len(ar_pacienti)>0:
                                    i8=0
                                    for i7 in ar_pacienti:
                                        if len(i7)>0:
                                            
                                            if (array_datele_orar_p[-(nr_pacienti-i8)*19+2])!=None and ar_pacienti[i8][0]==(array_datele_orar_p[-(nr_pacienti-i8)*19+2])[0]:
                                                for i9 in ter_dup:
                                                    w1=db(db.terapeuti.nume==i9).select().first()
                                                    w=w1.ce_terapii_face
                                                    if ar_pacienti[i8][0] in w:
                                                        pleaca=0
                                                        
                                                        break
                                                    else: 
                                                        pleaca=1
                                                        
                                                if pleaca==1:
                                                    trebuiesastea=1
                                                    break    
                                            elif ((array_datele_orar_p[-(nr_pacienti-i8)*19+2])!=None and ar_pacienti[i8][0]!=(array_datele_orar_p[-(nr_pacienti-i8)*19+2])[0]) or ((array_datele_orar_p[-(nr_pacienti-i8)*19+2])==None):
                                                                                              
                                                for i11 in ar_pacienti[i8]: #[a,b,c] Shirodara
                                                    for i9 in ter_dup: #Mari

                                                        w1=db(db.terapeuti.nume==i9).select().first()
                                                        w=w1.ce_terapii_face
                                                        
                                                        if i11 in w:
                                                            vptbreak=1
                                                            pleaca=0
                                                            break
                                                        else:
                                                            pleaca=1
                                                    if pleaca==0:
                                                        
                                                        break        
                                                           
                                                if pleaca==1:
                                                    trebuiesastea=1
                                                    break                    
                                                    
                                                                   
                                        i8=i8+1
                            if trebuiesastea==0:
                                ter_toti=ter_dup[:]
                        #pass
                      
                    contor_terapeuti1416=[]
                    for row in range(len(ter_toti)):
                        contor_terapeuti1416.append(0)
                    contor_terapeuti1415=[]
                    for row in range(len(ter_toti)):
                        contor_terapeuti1415.append(0)
                    contor_terapeuti1516=[]
                    for row in range(len(ter_toti)):
                        contor_terapeuti1516.append(0)
                    
                    ###sfarsit cod45 continuare de mai sus  pt a vedea daca terapeutul de dimineata pleaca acasa
                    #####inceput cod12 aleg pacientul care merge pe a 3-a linie daca este un nr impar de TI pe primele doua linii si >=3
                    ttt=0
                    var_index_coboara_la_linia3=0
                    if contor_t_individuala_1416>2 and contor_t_individuala_1416%2==1 and contor_t_individuala_1416PplusAP>0: #contor_t_individuala_1416PplusAP terapiileindiv exista pt pacienti si pt pacienti-ambulatori 
                        ##inceput cod34 am facut arrayul ar_pacienti_doarTI in care am pus doar TI-importante + terapiile ambulatorilor-pacienti EX: ['PI', 'PI', '-', 'PI', 'PI', 'PI', 'PI', '-', 'PI', '-', 'DDS', 'PI', '-']
                        iii5=0
                        for row in ar_pacienti:
                            if (array_datele_orar_p[-(nr_pacienti-iii5)*19+2])!=None:
                                if len(row)>0:
                                    if row[0]==(array_datele_orar_p[-(nr_pacienti-iii5)*19+2])[0]:  #daca este TI-importanta
                                        ar_pacienti_doarTI.append(row[0])
                                    else:
                                        ar_pacienti_doarTI.append('-')
                            else:
                                ar_pacienti_doarTI.append('-')
                            iii5=iii5+1          
                        i7=0
                        E=list(ar_pacienti_doarTI)
                        E.sort(key=lambda x: ar_pacienti_doarTI.count(x))
                        seen={}
                        ar_pacienti_doarTI33 = ([seen.setdefault(x, x) for x in E if x!='-'])[::-1]
                        seen={}
                        ar_pacienti_doarTI333 =  ([seen.setdefault(x, x) for x in E if x not in seen and x!='-']) [::-1]
                        for row in matrix_TA[5]:
                            if i7>=nr_pacienti_p and i7<nr_pacienti_p_si_aP:
                                ar_pacienti_doarTI.append(row)
                            i7=i7+1
                        iii5=0
                        for iii5 in range(nr_pacienti_p,nr_pacienti):
                            if matrix_TA[5][iii5] in terapii_individuale:
                                ar_Ap_din_matrixTA5.append(matrix_TA[5][iii5])
                            else:
                                ar_Ap_din_matrixTA5.append('-')
                        for iii5 in range(nr_pacienti_p_si_aP,nr_pacienti):            
                            if matrix_TA[6][iii5] in terapii_individuale:
                                ar_Ap_din_matrixTA5.append(matrix_TA[6][iii5])
                            else:
                                ar_Ap_din_matrixTA5.append('-')
                        F=list(ar_Ap_din_matrixTA5)
                        F.sort(key=lambda x: ar_Ap_din_matrixTA5.count(x))
                        seen={}
                        ar_Ap_din_matrixTA51 = ([seen.setdefault(x, x) for x in F if x!='-'])[::-1] #sunt in ordine descrescatoare
                        seen={}
                        ar_Ap_din_matrixTA511 =  ([seen.setdefault(x, x) for x in F if x not in seen and x!='-']) [::-1]
                        
                        ##sfarsit cod34 am facut arrayul ar_pacienti_doarTI in care am pus doar TI-importante + terapiile ambulatorilor-pacienti EX: ['PI', 'PI', '-', 'PI', 'PI', 'PI', 'PI', '-', 'PI', '-', 'DDS', 'PI', '-']
                        ##inceput cod11 fac un array doar cu terapiile care apar de mai multe ori decat am posibilitatea in arrayul ar_pacienti_doarTI si care exista in linia a 3-a
                        B = list(ar_pacienti_doarTI)
                        B.sort(key=lambda x: ar_pacienti_doarTI.count(x))
                        seen={}
                        ar_pacienti_doarTI3 = ([seen.setdefault(x, x) for x in B if x not in seen])[::-1]
                        
                        for row in ar_pacienti_doarTI:
                            ##inceput1 verifica cate sunt disponibile pt acea terapie intre 1416
                            if row!='-':
                                idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==row][0] #am gasit de exemplu pt DDS indexul este 8
                                vall_TI = terapii_individuale1416x2dupa[idx]
                                #vall_TI = terapii_individuale1416x2[idx]
                            ##sfarsit1 verifica cate sunt disponibile pt acea terapie intre 1416  Ex: vall_TI=1
                                if ar_pacienti_doarTI.count(row)<=vall_TI:
                                    next((ar_pacienti_doarTI3.pop(i7) for i7, l in enumerate(ar_pacienti_doarTI3) if l == row), None) #aici raman in ar_pacienti_doarTI3 doar TI care sunt mai mult de 3
                        next((ar_pacienti_doarTI3.pop(i7) for i7, l in enumerate(ar_pacienti_doarTI3) if l == '-'), None)         
                        i7=0
                        for row in terapii_individuale:
                            if row in ar_pacienti_doarTI3:
                                if terapii_individuale1623[i7]==0:
                                    ar_pacienti_doarTI3.remove(row)
                            i7=i7+1        
                        ##sfarsit cod11 fac un array doar cu terapiile care apar de mai multe ori in arrayul ar_pacienti_doarTI si care exista in linia a 3-a
                        

                        ###inceput44 cod mutare din linia 1 in linia 3
                        
                        
                        for i7 in range(nr_pacienti_p_si_aP):
                            if i7>=nr_pacienti_p:
                                array_indecsi_aP.append(i7)
                        i7=0
                        iii5=0
                        
                        for row in ar_Ap_din_matrixTA511: # aici incerc sa mut un pacient-ambulator care depaseste impreuna (pacientii ambulatori din linia 5 si ambulatorii-ambulatori din liniile 5,6 posibilitatile)
                            for iii5 in range(nr_pacienti_p,nr_pacienti_p_si_aP):
                                if row==matrix_TA[5][iii5]:
                                    nr_aparitii_TI_in_acea_zi=ar_Ap_din_matrixTA51.count(row)
                                    idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==row][0]
                                    lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[terapii_individuale[idx]])
                                    for i12 in lista_cu_terapeuti_ai_terapiei_ordonata:
                                        if (i12 in ter_dup)==True:
                                            idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==i12][0]
                                            if (i12 in lista_cu_terapeuti_ai_terapiei_ordonata)==True and contor_terapeuti1617[idx_terapeut1617]<1:
                                                gasire_terapeut=i12
                                                break
                                            else:
                                                gasire_terapeut=0    
                                    if nr_aparitii_TI_in_acea_zi>terapii_individuale1416x2[idx] and terapii_individuale1623_scot_ambulatorii_ambulatori[idx]>0 and gasire_terapeut!=0:
                                        lista_indecsi_AP.append(iii5)
                                        lista_indecsi_AP.append(row)
                                        var_index_coboara_la_linia3=1
                                        ttt=1 #verificata ramura lista_indecsi_AP=[11, 'PSIHOTERAPIE INDIVIDUALA']
                                        break
                            if var_index_coboara_la_linia3==1:
                                break

                            iii5=iii5+1
                        
                        if len(ar_pacienti_doarTI3)>0:
                            
                            i7=0    
                            if var_index_coboara_la_linia3==0:
                                for i8 in range(len(ar_pacienti_doarTI3)): #aici incerc sa cobor un ambulator-pacient daca este suprapopulat      ar_pacienti_doarTI3=['PSIHOTERAPIE INDIVIDUALA', 'DDS MERIDIANE']
                                    idx10=[i2 for i2, j2 in enumerate(ar_pacienti_doarTI) if j2==ar_pacienti_doarTI3[i7]] #array cu indecsii din arrayul ar_pacienti_doarTI
                                    idx11=[]
                                    idx11 = list(filter(lambda x:x in idx10, array_indecsi_aP))#aceasta este lista cu indexii care va  cobori eventual(doar unul din ei) de la linia 1 la linia 3 in matrix_TA
                                    idx12=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==ar_pacienti_doarTI3[i8]][0] #indexul din terapii_individuale corespunzator terapiei
                                    lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[terapii_individuale[idx12]])
                                    for i12 in lista_cu_terapeuti_ai_terapiei_ordonata:
                                        if (i12 in ter_dup)==True:
                                            idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==i12][0]
                                            if (i12 in lista_cu_terapeuti_ai_terapiei_ordonata)==True and contor_terapeuti1617[idx_terapeut1617]<1:
                                                gasire_terapeut=i12
                                                break
                                            else:
                                                gasire_terapeut=0    
                                    for i9 in range(len(idx11)):
                                        
                                        if len(idx11)>0 and terapii_individuale1623_scot_ambulatorii_ambulatori[idx12]>0 and gasire_terapeut!=0: #daca da am rezolvat ce index coboara in linia 3
                                            lista_indecsi_AP.append(idx11[i9])
                                            lista_indecsi_AP.append(ar_pacienti_doarTI3[i7])#aici am adaugat la sfarsit si terapia care trebuie sa coboareEx: [11,'PSIHOTERAPIE INDIVIDUALA']
                                            var_index_coboara_la_linia3=1
                                            ttt=2 #verificata ramura lista_indecsi_AP=[10, 'DDS MERIDIANE']
                                            break
                                    if var_index_coboara_la_linia3==1:
                                        break
                                    i7=i7+1

                    


                            
                            if var_index_coboara_la_linia3==0: #aici incerc sa cobor un pacient cu TI daca este suprapupulat la pacienti+ambulatoriP
                                iii5=0
                                for row in ar_pacienti:
                                    if (array_datele_orar_p[-(nr_pacienti-iii5)*19+2])!=None and len(row)>0:
                                        idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==row[0]][0]
                                        lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[terapii_individuale[idx]])
                                        for i12 in lista_cu_terapeuti_ai_terapiei_ordonata:
                                            if (i12 in ter_dup)==True:
                                                idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==i12][0]
                                                if (i12 in lista_cu_terapeuti_ai_terapiei_ordonata)==True and contor_terapeuti1617[idx_terapeut1617]<1:
                                                    gasire_terapeut=i12
                                                    break
                                                else:
                                                    gasire_terapeut=0    
                                        if row[0]==(array_datele_orar_p[-(nr_pacienti-iii5)*19+2])[0]:  #daca este TI-importanta
                                            if row[0] in ar_pacienti_doarTI3  and terapii_individuale1623_scot_ambulatorii_ambulatori[idx]>0 and gasire_terapeut!=0:
                                                lista_indecsi_AP.append(iii5)
                                                lista_indecsi_AP.append(row[0])
                                                var_index_coboara_la_linia3=1
                                                ttt=3 #verificata ramura lista_indecsi_AP=[0, 'PSIHOTERAPIE INDIVIDUALA']
                                                break
                                    iii5=iii5+1 
                        
                    
                        if var_index_coboara_la_linia3==0: #aici incerc sa cobor un pacient cu TI daca este suprapupulat
                            iii5=0

                            for row in ar_pacienti_doarTI333:

                                #nr_aparitii_TI_in_acea_zi=ar_pacienti_doarTI33.count(row)
                                idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==row][0]
                                if terapii_individuale1416x2dupa[idx]>0:
                                    if terapii_individuale1623[idx]>0:
                                        iii5=0
                                        for row1 in ar_pacienti:
                                            if (array_datele_orar_p[-(nr_pacienti-iii5)*19+2])!=None and len(row1)>0:
                                                lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[terapii_individuale[idx]])
                                                for i12 in lista_cu_terapeuti_ai_terapiei_ordonata:
                                                    if (i12 in ter_dup)==True:
                                                        idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==i12][0]
                                                        if (i12 in lista_cu_terapeuti_ai_terapiei_ordonata)==True and contor_terapeuti1617[idx_terapeut1617]<1:
                                                            gasire_terapeut=i12
                                                            break
                                                        else:
                                                            gasire_terapeut=0    

                                                if row1[0]==row and terapii_individuale1623_scot_ambulatorii_ambulatori[idx]>0 and gasire_terapeut!=0:
                                                    lista_indecsi_AP.append(iii5)
                                                    lista_indecsi_AP.append(row)
                                                    var_index_coboara_la_linia3=1
                                                    ttt=4 #verificata ramura lista_indecsi_AP=[0, 'PSIHOTERAPIE INDIVIDUALA']
                                                    break
                                            iii5=iii5+1        
                                if var_index_coboara_la_linia3==1:
                                    break        
                                        
                                        
                                        
                        
                        if var_index_coboara_la_linia3==0: #aici incerc sa cobor un pacient sau un pacient ambulator daca nu am destule mese de oleatie sau masaj, iau in considerare doar Terapia importanta
                            iii5=0
                            var_ocupat_masa_masaj1416=ocupat_masa_masaj1416
                            var_ocupat_masa_oleatie1416=ocupat_masa_oleatie1416 
                            for row in ar_pacienti:
                                if (array_datele_orar_p[-(nr_pacienti-iii5)*19+2])!=None and len(row)>0:
                                    if row[0]==(array_datele_orar_p[-(nr_pacienti-iii5)*19+2])[0]:
                                        idx3=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==row[0]][0]

                                        if  idx3==1 or idx3==2 or idx3==3: 
                                            var_ocupat_masa_oleatie1416=var_ocupat_masa_oleatie1416+1
                                            lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[terapii_individuale[idx3]])
                                            for i12 in lista_cu_terapeuti_ai_terapiei_ordonata:
                                                if (i12 in ter_dup)==True:
                                                    idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==i12][0]
                                                    if (i12 in lista_cu_terapeuti_ai_terapiei_ordonata)==True and contor_terapeuti1617[idx_terapeut1617]<1:
                                                        gasire_terapeut=i12
                                                        break
                                                    else:
                                                        gasire_terapeut=0    
                                            if var_ocupat_masa_oleatie1416>4  and terapii_individuale1623_scot_ambulatorii_ambulatori[idx3]>0 and gasire_terapeut!=0 and ocupat_masa_oleatie1617<2:
                                                lista_indecsi_AP.append(iii5)
                                                lista_indecsi_AP.append(row[0])
                                                var_index_coboara_la_linia3=1
                                                ttt=5 #verificata ramura lista_indecsi_AP=[2, 'OLEATIE SACULET (include sauna)']
                                                break
                                        if  idx3==4 or idx3==5 or idx3==6 or idx3==7 or idx3==8:
                                            var_ocupat_masa_masaj1416=var_ocupat_masa_masaj1416+1
                                            lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[terapii_individuale[idx3]])
                                            for i12 in lista_cu_terapeuti_ai_terapiei_ordonata:
                                                if (i12 in ter_dup)==True:
                                                    idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==i12][0]
                                                    if (i12 in lista_cu_terapeuti_ai_terapiei_ordonata)==True and contor_terapeuti1617[idx_terapeut1617]<1:
                                                        gasire_terapeut=i12
                                                        break
                                                    else:
                                                        gasire_terapeut=0    
                                            if var_ocupat_masa_masaj1416>6  and terapii_individuale1623_scot_ambulatorii_ambulatori[idx3]>0 and gasire_terapeut!=0 and ocupat_masa_masaj1617<3:
                                                lista_indecsi_AP.append(iii5)
                                                lista_indecsi_AP.append(row[0])
                                                var_index_coboara_la_linia3=1
                                                break
                                iii5=iii5+1

                        iii5=0
                        #lista_indecsi_AP=[]
                        #var_index_coboara_la_linia3=0
                        
                        if var_index_coboara_la_linia3==0: #aici incerc sa cobor un pacient-oricare cu TI.
                            for row in ar_pacienti:
                                if (array_datele_orar_p[-(nr_pacienti-iii5)*19+2])!=None and len(array_datele_orar_p[-(nr_pacienti-iii5)*19+3])>0:
                                    if len(array_datele_orar_p[-(nr_pacienti-iii5)*19+2])==1:
                                        if (array_datele_orar_p[-(nr_pacienti-iii5)*19+2][0] in ar_pacienti_doarTI)==True:
                                            idx3=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==array_datele_orar_p[-(nr_pacienti-iii5)*19+2][0]][0]
                                            lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[terapii_individuale[idx3]])
                                            for i12 in lista_cu_terapeuti_ai_terapiei_ordonata:
                                                if (i12 in ter_dup)==True:
                                                    idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==i12][0]
                                                    if (i12 in lista_cu_terapeuti_ai_terapiei_ordonata)==True and contor_terapeuti1617[idx_terapeut1617]<1:
                                                        gasire_terapeut=i12
                                                        break
                                                    else:
                                                        gasire_terapeut=0
                                            if terapii_individuale1623[idx3]>0  and terapii_individuale1623_scot_ambulatorii_ambulatori[idx3]>0 and gasire_terapeut!=0:
                                                lista_indecsi_AP.append(iii5)
                                                lista_indecsi_AP.append(row[i7])
                                                var_index_coboara_la_linia3=1
                                                ttt=55 #verificata ramura lista_indecsi_AP=[3, 'SHIRODARA-Ana']
                                                break
                                iii5=iii5+1            
                                if var_index_coboara_la_linia3==1:
                                    break
                                        
                        iii5=0
                        if var_index_coboara_la_linia3==0: #aici incerc sa cobor un pacient-oricare cu sau fara TI. Aici caut toate solutiile, toate terapiile pacientilor
                            for row in ar_pacienti:
                                if len(array_datele_orar_p[-(nr_pacienti-iii5)*19+3])>0:
                                    for i7 in range(len(row)): 
                                        idx2=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==row[i7]][0]
                                        lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[terapii_individuale[idx2]])
                                        for i12 in lista_cu_terapeuti_ai_terapiei_ordonata:
                                            if (i12 in ter_dup)==True:
                                                idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==i12][0]
                                                if (i12 in lista_cu_terapeuti_ai_terapiei_ordonata)==True and contor_terapeuti1617[idx_terapeut1617]<1:
                                                    gasire_terapeut=i12
                                                    break
                                                else:
                                                    gasire_terapeut=0    
                                        if terapii_individuale1623[idx2]>0  and terapii_individuale1623_scot_ambulatorii_ambulatori[idx2]>0 and gasire_terapeut!=0:
                                            lista_indecsi_AP.append(iii5)
                                            lista_indecsi_AP.append(row[i7])
                                            var_index_coboara_la_linia3=1
                                            ttt=6 #verificata ramura lista_indecsi_AP=[0, 'PSIHOTERAPIE INDIVIDUALA']
                                            break
                                            
                                iii5=iii5+1
                                if var_index_coboara_la_linia3==1:
                                    break            
                                
                        
                        if var_index_coboara_la_linia3==0: #aici incerc sa cobor un pacient-ambulator cu terapia lui
                            for iii5 in range(nr_pacienti_p,nr_pacienti_p_si_aP):
                                
                                if len(array_datele_orar_p[-(nr_pacienti-iii5)*19+3])>0:
                                    idx2=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==(array_datele_orar_p[-(nr_pacienti-iii5)*19+3])[0]][0]
                                    lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[terapii_individuale[idx2]])
                                    for i12 in lista_cu_terapeuti_ai_terapiei_ordonata:
                                        if (i12 in ter_dup)==True:
                                            idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==i12][0]
                                            if (i12 in lista_cu_terapeuti_ai_terapiei_ordonata)==True and contor_terapeuti1617[idx_terapeut1617]<1:
                                                gasire_terapeut=i12
                                                break
                                            else:
                                                gasire_terapeut=0    
                                    if terapii_individuale1623[idx2]>0 and terapii_individuale1623_scot_ambulatorii_ambulatori[idx2]>0 and gasire_terapeut!=0:
                                        lista_indecsi_AP.append(iii5)
                                        lista_indecsi_AP.append((array_datele_orar_p[-(nr_pacienti-iii5)*19+3])[0])
                                        var_index_coboara_la_linia3=1
                                        ttt=7 #verificata ramura lista_indecsi_AP=[10, 'DDS MERIDIANE']
                                        break
                                iii5=iii5+1

                                
                        if var_index_coboara_la_linia3==0: #aici incerc sa cobor un pacient-macar sa aiba o terapie. Aici caut toate solutiile inclusiv daca nu exista terapeut de la ora 16, toate terapiile pacientilor
                            iii5=0
                            for row in ar_pacienti:
                                if len(row)>0 :
                                    lista_indecsi_AP.append(iii5)
                                    lista_indecsi_AP.append(row[0])
                                    lista_indecsi_AP.append('FARA TERAPEUT')
                                    var_index_coboara_la_linia3=1
                                    ttt=8 #verificata ramura lista_indecsi_AP=[0, 'PSIHOTERAPIE INDIVIDUALA-FARA TERAPEUT']
                                    break
                            iii5=iii5+1    
                        
                        #lista_indecsi_AP=[]
                        #var_index_coboara_la_linia3=9
                        if var_index_coboara_la_linia3==0:#aici incerc sa cobor un pacient-ambulator macar sa aiba o terapieIndiv.Caut toate solutiile inclusiv daca nu exista terapeut de la ora 16 pt un pacient-ambulator
                            for iii5 in range(nr_pacienti_p,nr_pacienti_p_si_aP):
                                if matrix_TA[5][iii5] in terapii_individuale:
                                    lista_indecsi_AP.append(iii5)
                                    lista_indecsi_AP.append(matrix_TA[5][iii5])
                                    lista_indecsi_AP.append('-FARA TERAPEUT')
                                    var_index_coboara_la_linia3=1
                                    ttt=9 #verificata ramura lista_indecsi_AP=[10, 'DDS MERIDIANE'] sau daca nu are terapie individuala va fi: lista_indecsi_AP=[]
                                    break
                    
                    ###############################sfarsit cod12 aleg pacientul care merge pe a 3-a linie daca este un nr impar de TI pe primele doua linii si >=3. Aici am: lista_indecsi_AP=[10, 'DDS MERIDIANE']
                    ar_PpTi7=[]            
                    for i7 in range(nr_pacienti):
                        ar_PpTi7.append(50)
                    
                    ####inceput cod4571 pt a aloca Aa terapeuti
                    ter5=[]
                    ter6=[]
                    ter7=[]
                    ter8=[]
                    ter5w=[]
                    ter6w=[]
                    ter7w=[]
                    ter8w=[]
                    nr_Tahioni5=0
                    nr_FrCr5=0
                    nr_Tahioni6=0
                    nr_FrCr6=0
                    nr_Tahioni7=0
                    nr_FrCr7=0
                    nr_Tahioni8=0
                    nr_FrCr8=0
                    nr_Ozon5=0
                    nr_Sauna5=0
                    nr_Ozon6=0
                    nr_Sauna6=0
                    nr_Ozon7=0
                    nr_Sauna7=0
                    nr_Ozon8=0
                    nr_Sauna8=0
                    TIAa5=[]
                    TIAa6=[]
                    TIAa7=[]
                    TIAa8=[]
                    TercuTI8=[]

                    for i7 in range(9):
                        i9=0
                        i11=0
                        var43=0
                        arr_buffer=[]
                        for i8 in matrix_TA[i7]:
                            if i9>nr_pacienti_p_si_aP-1: #vreau doar pt Aa i9 pleaca de la 13
                                if i8 not in terapii_individuale and i8!='-' and i8!='--' and i8!='---' and i8!='VOCALE,RESPIRATII,CODUL V' and i8!='YOGA TERAPEUTICA':
                                    if i7<=2:
                                        ttt1=ter_dim1[:]
                                    if i7>2 and i7<5:
                                        ttt1=ter_dim[:]        
                                    if i7>=5:
                                        if var43==0:
                                            i11=0
                                        #ttt1=ter_dup[:]
                                    if i7==5 or i7==6:
                                        if len(ter_dup)>0:
                                            ttt1=ter_dup[:]
                                        else:
                                            ttt1=ter_toti[:]   
                                    if i7>6:
                                        ttt1=ter_dup[:]    
                                            


                                    if len(ttt1)>0:
                                        if i11<2:
                                            matrix_TA[i7][i9]=i8+'-'+ttt1[0]
                                            i11=i11+1
                                            var43=var43+1
                                            nri=0
                                        if  i11>=2 and i11<4 and len(ttt1)>1:
                                            matrix_TA[i7][i9]=i8+'-'+ttt1[1]
                                            i11=i11+1
                                            var43=var43+1
                                            nri=1
                                        if i11>=4 and len(ttt1)>2:
                                            matrix_TA[i7][i9]=i8+'-'+ttt1[2]
                                            i11=i11+1
                                            var43=var43+1
                                            nri=2
                                        if i7==5:
                                            ter5.append(ttt1[nri])
                                            if i8=='TAHION':
                                                nr_Tahioni5=nr_Tahioni5+1
                                            if i8=='Frecv-CR':
                                                nr_FrCr5=nr_FrCr5+1
                                            if i8=='SAUNA':
                                                nr_Sauna5=nr_Sauna5+1
                                                if nr_Tahioni5+nr_FrCr5+nr_Sauna5+nr_Ozon5<7:
                                                    ter5w.append(ttt1[0])
                                                else:
                                                    if len(ttt1)>1:
                                                        ter5w.append(ttt1[1])

                                            if i8=='BAIE OZON':
                                                nr_Ozon5=nr_Ozon5+1   
                                                if nr_Tahioni5+nr_FrCr5+nr_Sauna5+nr_Ozon5<7:
                                                    ter5w.append(ttt1[0])
                                                else:
                                                    if len(ttt1)>1:
                                                        ter5w.append(ttt1[1])
                                        if i7==6:
                                            ter6.append(ttt1[nri])
                                            if i8=='TAHION':
                                                nr_Tahioni6=nr_Tahioni6+1   
                                            if i8=='Frecv-CR':
                                                nr_FrCr6=nr_FrCr6+1 
                                            if i8=='SAUNA':
                                                nr_Sauna6=nr_Sauna6+1
                                                if nr_Tahioni6+nr_FrCr6+nr_Sauna6+nr_Ozon6<7:
                                                    ter6w.append(ttt1[0])
                                                else:
                                                    if len(ttt1)>1:
                                                        ter6w.append(ttt1[1])
                                            if i8=='BAIE OZON':
                                                nr_Ozon6=nr_Ozon6+1
                                                if nr_Tahioni6+nr_FrCr6+nr_Sauna6+nr_Ozon6<7:
                                                    ter6w.append(ttt1[0])
                                                else:
                                                    if len(ttt1)>1:
                                                        ter6w.append(ttt1[1])       
                                        if i7==7:
                                            ter7.append(ttt1[nri])
                                            if i8=='TAHION':
                                                nr_Tahioni7=nr_Tahioni7+1  
                                            if i8=='Frecv-CR':
                                                nr_FrCr7=nr_FrCr7+1
                                            if i8=='SAUNA':
                                                nr_Sauna7=nr_Sauna7+1
                                                if nr_Tahioni7+nr_FrCr7+nr_Sauna7+nr_Ozon7<7:
                                                    ter7w.append(ttt1[0])
                                                else:
                                                    if len(ttt1)>1:
                                                        ter7w.append(ttt1[1])
                                            if i8=='BAIE OZON':
                                                nr_Ozon7=nr_Ozon7+1
                                                if nr_Tahioni7+nr_FrCr7+nr_Sauna7+nr_Ozon7<7:
                                                    ter7w.append(ttt1[0])
                                                else:
                                                    if len(ttt1)>1:
                                                        ter7w.append(ttt1[1])    

                                        if i7==8:
                                            ter8.append(ttt1[nri])
                                            if i8=='TAHION':
                                                nr_Tahioni8=nr_Tahioni8+1       
                                            if i8=='Frecv-CR':
                                                nr_FrCr8=nr_FrCr8+1
                                            if i8=='SAUNA':
                                                nr_Sauna8=nr_Sauna8+1
                                                if nr_Tahioni8+nr_FrCr8+nr_Sauna8+nr_Ozon8<7:
                                                    ter8w.append(ttt1[0])
                                                else:
                                                    if len(ttt1)>1:
                                                        ter6w.append(ttt1[1])
                                            if i8=='BAIE OZON':
                                                nr_Ozon8=nr_Ozon8+1
                                                if nr_Tahioni8+nr_FrCr8+nr_Sauna8+nr_Ozon8<7:
                                                    ter8w.append(ttt1[0])
                                                else:
                                                    if len(ttt1)>1:
                                                        ter8w.append(ttt1[1])                
                                    else:
                                        matrix_TA[i7][i9]=i8+'-'+'fara terapeut'
                                        if i7==5:                                                    
                                            if i8=='TAHION':
                                                nr_Tahioni5=nr_Tahioni5+1
                                            if i8=='Frecv-CR':
                                                nr_FrCr5=nr_FrCr5+1
                                            if i8=='SAUNA':
                                                nr_Sauna5=nr_Sauna5+1
                                            if i8=='BAIE OZON':
                                                nr_Ozon5=nr_Ozon5+1        
                                        if i7==6:                                                    
                                            if i8=='TAHION':
                                                nr_Tahioni6=nr_Tahioni6+1
                                            if i8=='Frecv-CR':
                                                nr_FrCr6=nr_FrCr6+1
                                            if i8=='SAUNA':
                                                nr_Sauna6=nr_Sauna6+1
                                            if i8=='BAIE OZON':
                                                nr_Ozon6=nr_Ozon6+1        
                                        if i7==7:                                                    
                                            if i8=='TAHION':
                                                nr_Tahioni7=nr_Tahioni7+1              
                                            if i8=='Frecv-CR':
                                                nr_FrCr7=nr_FrCr7+1
                                            if i8=='SAUNA':
                                                nr_Sauna7=nr_Sauna7+1
                                            if i8=='BAIE OZON':
                                                nr_Ozon7=nr_Ozon7+1            
                                        if i7==8:
                                            if i8=='TAHION':
                                                nr_Tahioni8=nr_Tahioni8+1       
                                            if i8=='Frecv-CR':
                                                nr_FrCr8=nr_FrCr8+1
                                            if i8=='SAUNA':
                                                nr_Sauna8=nr_Sauna8+1
                                            if i8=='BAIE OZON':
                                                nr_Ozon8=nr_Ozon8+1

                                if i7==0:
                                    if i8=='VOCALE,RESPIRATII,CODUL V':
                                        matrix_TA[i7][i9]='VOC,RESP,CODUL V'+'-'+ter_dim[0]
                                if i7==2:
                                    if i8=='YOGA TERAPEUTICA':
                                        matrix_TA[i7][i9]='YOGA T'+'-'+ter_dim[0]
                                
                                if i7<=2:
                                    ttt2=ter_dim1[:]
                                if i7>2 and i7<5:
                                    ttt2=ter_dim[:]        
                                if i7==8:
                                    ttt2=ter_dup[:]
                                if i7<=4 or i7==8:
                                    if i8 in terapii_individuale:
                                        for i10 in eval(dictTI_ord[i8]):
                                            if (i10 not in arr_buffer)==True and i10 in ttt2:
                                                terap=i10
                                                arr_buffer.append(i10)
                                                if i7==8:
                                                    TercuTI8.append(i10)
                                                break
                                            else:
                                                terap='fara terapeut'
                                        matrix_TA[i7][i9]=dictTI_prescurtari[i8]+'-'+terap 
                            
                            if i9<=nr_pacienti_p_si_aP-1: #vreau doar pt Pp si Pa i9 pleaca de la 0 la 12
                                if i7==0:
                                    if matrix_TA[i7][i9]=='VOCALE,RESPIRATII,CODUL V':
                                        matrix_TA[i7][i9]='VOC,RESP,CODUL V'+'-'+ter_dim[0]
                                    if i9<nr_pacienti_p:
                                        if matrix_TA[i7][i9]=='-':
                                            if len(ter_dim1)>0:
                                                terap1=ter_dim1[0]
                                            else:
                                                terap1=ter_dim[0]    
                                            matrix_TA[i7][i9]='in camera-'+terap1

                                if i7==2:
                                    if matrix_TA[i7][i9]=='YOGA TERAPEUTICA':
                                        matrix_TA[i7][i9]='YOGA T'+'-'+ter_dim[0]
                                    if i9<nr_pacienti_p:
                                        if matrix_TA[i7][i9]=='-':
                                            if len(ter_dim1)>0:
                                                terap1=ter_dim1[0]
                                            else:
                                                terap1=ter_dim[0]    
                                            matrix_TA[i7][i9]='in camera-'+terap1



                            i9=i9+1
                    ####sfarsit cod4571 pt a aloca Aa terapeuti        
                    #inceput cod34 aloc ambulatorilor-ambulatori din linia 7 un terapeut si scad din contor_terapeuti1617 terapeutul    
                    for iii5 in range(nr_pacienti_p_si_aP,nr_pacienti):
                        if (matrix_TA[7][iii5] in terapii_individuale)==True:
                            ops=1
                            ti_pt_terapeut=matrix_TA[7][iii5]
                            lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[ti_pt_terapeut])
                            for i7 in lista_cu_terapeuti_ai_terapiei_ordonata:
                                if (i7 in ter_dup)==True:
                                    idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==i7][0]
                                    if (i7 in ter_dup)==True and contor_terapeuti1617[idx_terapeut1617]<1:
                                        matrix_TA[7][iii5]=dictTI_prescurtari[ti_pt_terapeut]+'-'+i7
                                        TIAa7.append(i7)
                                        ar_PpTi7[iii5]=i7
                                        idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==i7][0]
                                        contor_terapeuti1617[idx_terapeut1617]=contor_terapeuti1617[idx_terapeut1617]+1
                                        """if idx_terapeut1617==1 or idx_terapeut1617==2 or idx_terapeut1617==3:
                                            ocupat_masa_oleatie1617=ocupat_masa_oleatie1617+1
                                        if idx_terapeut1617==4 or idx_terapeut1617==5 or idx_terapeut1617==6 or idx_terapeut1617==7 or idx_terapeut1617==8:
                                            ocupat_masa_masaj1617=ocupat_masa_masaj1617+1"""
                                        break
                                    else:
                                        matrix_TA[7][iii5]=dictTI_prescurtari[ti_pt_terapeut]+'-'+'nu are'
                                        """if idx_terapeut1617==1 or idx_terapeut1617==2 or idx_terapeut1617==3:
                                            ocupat_masa_oleatie1617=ocupat_masa_oleatie1617+1
                                        if idx_terapeut1617==4 or idx_terapeut1617==5 or idx_terapeut1617==6 or idx_terapeut1617==7 or idx_terapeut1617==8:
                                            ocupat_masa_masaj1617=ocupat_masa_masaj1617+1"""
                                        
                    #sfarsit cod34 aloc ambulatorilor-ambulatori din linia 7 un terapeut si scad din contor_terapeuti1617 terapeutul 
                    arr_indexMTA5=[] #indecsii din matrix_TA5 care vor cobori in linia 6 plus cel care coboara in linia 7 (imparul)
                    ##inceput cod1 cobor din linia 5 in linia 7 Si aloc TERAPEUT!!! lista_indecsi_AP=[10, 'DDS MERIDIANE']vezi al2-lea if de mai jos AICI MUT IMPARUL(SAU NU, DACA AM 2n+1 TERAPII SI NU AM IN LINIA7 CU CINE)
                    if contor_t_individuala_1416%2>=3 and contor_t_individuala_1416%2==1 and len(lista_indecsi_AP)==3 and contor_t_individuala_1416PplusAP>0:
                        mutare_da_sau_nu57=1 # chiar daca este nr impar si am 2*n+1>=3 pacienti nu cobor nici un pacient sau ambulator-pacient pt ca nu am terapeut pt el in linia 7
                        mutare5775_imparul=2 #adica nu se muta!!
                        nr_terapeuti_necesari=nr_terapeuti_necesari+1        
                    if mutare_da_sau_nu57==0 and var_index_coboara_la_linia3==1 and len(lista_indecsi_AP)==2:
                        ti_ce_va_fi_mutata=lista_indecsi_AP[1]
                        lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[ti_ce_va_fi_mutata])#=['Mirela']
                        for i7 in lista_cu_terapeuti_ai_terapiei_ordonata:
                            if (i7 in ter_dup)==True:
                                idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==i7][0]
                            #contor_terapeuti1617[idx_terapeut1617]=contor_terapeuti1617[idx_terapeut1617]+1
                            if (i7 in ter_dup)==True and contor_terapeuti1617[idx_terapeut1617]<1:
                                terapeutul=i7
                                break
                            else:
                                terapeutul='nu are'
                        var1=matrix_TA[7][lista_indecsi_AP[0]]
                        matrix_TA[7][lista_indecsi_AP[0]]=dictTI_prescurtari[lista_indecsi_AP[1]]+'-'+terapeutul

                        
                        #matrix_TA[5][lista_indecsi_AP[0]]=var1
                        for i111 in ter_toti:
                            if (i111 not in ter5) or ter5.count(i111)<2:
                                terapeutul_2=i111
                                ter5.append(terapeutul_2)
                                break
                            else:
                                terapeutul_2='nu are'

                        for i111 in ter_toti:
                            if (i111 not in ter6) or ter6.count(i111)<2:
                                terapeutul_3=i111
                                ter6.append(terapeutul_3)
                                break
                            else:
                                terapeutul_2='nu are'
                        matrix_TA[5][lista_indecsi_AP[0]]='TAHION'+'-'+terapeutul_2
                        matrix_TA[6][lista_indecsi_AP[0]]='Frecv-CR'+'-'+terapeutul_3
                        if nr_zi1!=6 and nr_zi1!=7:
                            nr_Tahioni5=nr_Tahioni5+1
                            nr_FrCr6=nr_FrCr6+1
                        #arr_indexMTA5.append(lista_indecsi_AP[0])
                        ar_PpTi7[lista_indecsi_AP[0]]=terapeutul
 
                        idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==lista_indecsi_AP[1]][0]
                        terapii_individuale1623_scot_ambulatorii_ambulatori[idx]=terapii_individuale1623_scot_ambulatorii_ambulatori[idx]-1
                        if lista_indecsi_AP[0]>=nr_pacienti_p and lista_indecsi_AP[0]<nr_pacienti_p_si_aP and i7!='nu are':
                            terapii_individuale1416x2dupa[idx]=terapii_individuale1416x2dupa[idx]+1
                            if lista_indecsi_AP[1] not in TI_doar_pentru_pacienti and terapii_individuale1416x2dupa[idx]>0:
                                TI_doar_pentru_pacienti.append(lista_indecsi_AP[1])
                                            

                        if terapeutul!='nu are':
                            idx_terapeut1617=[i2 for i2, j2 in enumerate(ter_dup) if j2==terapeutul][0]
                            contor_terapeuti1617[idx_terapeut1617]=contor_terapeuti1617[idx_terapeut1617]+1
                        if idx==1 or idx==2 or idx==3:
                            ocupat_masa_oleatie1415=ocupat_masa_oleatie1415-1
                            ocupat_masa_oleatie1416=ocupat_masa_oleatie1416-1
                            ocupat_masa_oleatie1617=ocupat_masa_oleatie1617+1
                        if idx==4 or idx==5 or idx==6 or idx==7 or idx==8:
                            ocupat_masa_masaj1415=ocupat_masa_masaj1415-1
                            ocupat_masa_masaj1416=ocupat_masa_masaj1416-1
                            ocupat_masa_masaj1617=ocupat_masa_masaj1617+1

                        mutare5775_imparul=1 #adica se muta
                        
                    
                    ##sfarsit cod1 cobor din linia 5 in linia 7 Si aloc TERAPEUT!!! lista_indecsi_AP=[10, 'DDS MERIDIANE'] vezi if-ul de mai sus AICI AM MUTAT IMPARUL(SAU NU DACA AM 3 TERAPII SI NU AM IN LINIA7 CU CINE)
                    
                    
                    
                    ##inceput cod22 memorez in arrayul ar_PpT toti terapeutii din linia 5 si 6 care fac TI            
                    ar_PpTi5=[]            
                    for i7 in range(nr_pacienti):
                        ar_PpTi5.append(50)
                    if len(lista_indecsi_AP)==2:
                        ar_PpTi5[lista_indecsi_AP[0]]=49
                    ar_PpTi6=[]            
                    for i7 in range(nr_pacienti):
                        ar_PpTi6.append(50)
                    
                        
                    ##sfarsit cod22 memorez in arrayul ar_PpT toti terapeutii din linia 5 si 6 care fac TI  
                    ##inceput cod690 aloc ambulatorilorP si ambulatorilor-ambulatori un TERAPEUT pt terapia lor
                    for iii5 in range(nr_pacienti_p,nr_pacienti):
                        if (matrix_TA[5][iii5] in terapii_individuale)==True:
                            ti_pt_terapeut=matrix_TA[5][iii5]
                            lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[ti_pt_terapeut])
                            for i7 in lista_cu_terapeuti_ai_terapiei_ordonata:
                                if (i7 in ter_toti)==True:
                                    idx_terapeut1416=[i2 for i2, j2 in enumerate(ter_toti) if j2==i7][0]
                        
                                if iii5>nr_pacienti_p_si_aP-1:
                                    if (i7 in ter_toti)==True and contor_terapeuti1416[idx_terapeut1416]<1:
                                        terapeutul=i7
                                        break
                                else:
                                    terapeutul='nu are'    
                                if iii5<=nr_pacienti_p_si_aP-1:    
                                    if (i7 in ter_toti)==True and contor_terapeuti1416[idx_terapeut1416]<2:
                                        terapeutul=i7
                                        break
                                else:
                                    terapeutul='nu are'    



                                                            
                                            
                                        
                            matrix_TA[5][iii5]=dictTI_prescurtari[ti_pt_terapeut]+"-"+terapeutul
                            ar_PpTi5[iii5]=terapeutul
                            if iii5>nr_pacienti_p_si_aP-1 and terapeutul!='nu are':
                                TIAa5.append(terapeutul)

                            idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==ti_pt_terapeut][0]
                            if terapeutul!='nu are':
                                contor_terapeuti1416[idx_terapeut1416]=contor_terapeuti1416[idx_terapeut1416]+1
                                contor_terapeuti1415[idx_terapeut1416]=contor_terapeuti1415[idx_terapeut1416]+1
                    for iii5 in range(nr_pacienti_p,nr_pacienti):
                        if (matrix_TA[6][iii5] in terapii_individuale)==True:
                            ti_pt_terapeut=matrix_TA[6][iii5]
                            lista_cu_terapeuti_ai_terapiei_ordonata=eval(dictTI_ord[ti_pt_terapeut])
                            for i7 in lista_cu_terapeuti_ai_terapiei_ordonata:
                                if (i7 in ter_toti)==True:
                                    idx_terapeut1416=[i2 for i2, j2 in enumerate(ter_toti) if j2==i7][0]
                        
                                if (i7 in ter_toti)==True and contor_terapeuti1416[idx_terapeut1416]<2 and contor_terapeuti1516[idx_terapeut1416]<1:
                                    terapeutul1=i7
                                    
                                    break
                                else:
                                    terapeutul1='nu are'
                                    
                                            
                                        
                            matrix_TA[6][iii5]=dictTI_prescurtari[ti_pt_terapeut]+"-"+terapeutul1
                            if iii5>nr_pacienti_p_si_aP-1 and terapeutul1!='nu are':
                                TIAa6.append(terapeutul1)
                            #terapeutuli=db(db.terapeuti.nume==row).select()
                            if (terapeutul1!='nu are'):
                                ar_PpTi6[iii5]=terapeutul1
                            idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==ti_pt_terapeut][0]
                            if terapeutul1!='nu are':
                                contor_terapeuti1416[idx_terapeut1416]=contor_terapeuti1416[idx_terapeut1416]+1    
                                contor_terapeuti1516[idx_terapeut1416]=contor_terapeuti1516[idx_terapeut1416]+1
                    ##sfarsit cod690 aloc ambulatorilorP si ambulatorilor-ambulatori un TERAPEUT pt terapia lor
                    ##inceput cod70 refacere structura matrix_TA[6] si matrix_TA[7]  Ex: Matrix_TA[6]=['--' '--' 'PSIHO IND-nu are']  Matrix_TA[7]=['PSIHOTERAPIE INDIVIDUALA' '---' '---'] dadea o eroare la liniute -,---


                    i8=0
                    for i7 in matrix_TA[6]:
                        if i7=='-' or i7=='--' or i7=='---': 
                            matrix_TA[6][i8]='--'
                        i8=i8+1
                    i8=0
                    for i7 in matrix_TA[7]:
                        if i7=='-' or i7=='--' or i7=='---': 
                            matrix_TA[7][i8]='---'
                        i8=i8+1    
                    ##sfarsit cod70 refacere structura matrix_TA[6] si matrix_TA[7]  Ex: Matrix_TA[6]=['--' '--' 'PSIHO IND-nu are']  Matrix_TA[7]=['PSIHOTERAPIE INDIVIDUALA' '---' '---'] dadea o eroare la liniute -,--
            
                    #############################Inceput Cod133 alocare terapii si terapeuti doar PACIENTILOR din ar_pacienti
                    
                    ##inceput cod1a creez un array unde vor veni indecsii din matris_TA[5] doar ai pacientilor rezolvati pe care pas cu pas nu ii mai iau in calcul
                    ar_idx_verificati=[]
                    ar_idx_verificati_only=[]
                    ar_Pp=[] #este arrayul cu terapiile Pp daca se gasesc care vor figura in orar_p (deci este f important!!)
                    array1=[]
                    array2=[]
                    array3=[]
                    if nr_zi1!=6 and nr_zi1!=7:    
                        for i7 in range(nr_pacienti_p):
                            ar_idx_verificati.append(50)
                            ar_Pp.append(50)
                            
                        
                        if len(lista_indecsi_AP)==2 and lista_indecsi_AP[0]<nr_pacienti_p:
                            ar_idx_verificati[lista_indecsi_AP[0]]=lista_indecsi_AP[0]
                            ar_idx_verificati_only.append(lista_indecsi_AP[0])
                            ar_Pp[lista_indecsi_AP[0]]=lista_indecsi_AP[1]

                            
                        for i7 in range(nr_pacienti_p):
                            if matrix_TA[5][i7]=='-':
                                ar_idx_verificati[i7]=i7
                                ar_idx_verificati_only.append(i7)
                                matrix_TA[5][i7]='fara'
                                ar_Pp[i7]='fara'
                                

                        ##sfarsit cod1a creez un array unde vor veni indecsii din matris_TA[5] doar ai pacientilor rezolvati pe care pas cu pas nu ii mai iau in calcul Ex ar_idx_verificati_only=[6,8] si va tot creste..
                        ##inceput cod55 verific si scot din ter_toti terapeutii care au deja alocate 2 terapii de la 14-16
                        ter_toti_only=ter_toti[:]
                        i8=0
                        for i7 in contor_terapeuti1416:
                            if i7>1:
                                ter_toti_only.remove(ter_toti[i8])
                            i8=i8+1    
                        ##sfarsit cod55 verific si scot din ter_toti terapeutii care au deja alocate 2 terapii de la 14-16
                        ##inceput cod33(am pus la mana) verific daca mai am loc la mesele de oleatie si masaj si pun 0 posibilitatea de a face in Ex: terapii_individuale1416x2dupa=[2, 4, 4, 4, 0, 0, 0, 0, 0]
                        nu_fac_oleatie=0
                        nu_fac_masaj=0
                        if ocupat_masa_oleatie1416>3:
                            nu_fac_oleatie=1
                        if ocupat_masa_masaj1416>5:
                            nu_fac_masaj=1    
                        if nu_fac_oleatie==1:
                            for i7 in range(1,4):
                                terapii_individuale1416x2dupa[i7]=0
                        if nu_fac_masaj==1:
                            for i7 in range(4,9):
                                terapii_individuale1416x2dupa[i7]=0    
                        ##sfarsitt cod33(am pus la mana) verific daca mai am loc la mesele de oleatie si masaj si pun 0 posibilitatea de a face in Ex: terapii_individuale1416x2dupa=[2, 4, 4, 4, 0, 0, 0, 0, 0]
                        ##inceput cod44 sa vedem ce terapii disponibile am
                        terapii_individuale1416x2dupaa=terapii_individuale1416x2dupa[:]
                        ##sfarsit cod44 sa vedem ce terapii disponibile am
                        ##inceput cod80 mai fac o verificare prin intermediul lui ter_toti_only(pe care o sa operez) sa vad ce terapii mai raman pt fiecare pacient in ar_pacienti
                        i8=0
                        t1=0
                        ar_pacienti2=ar_pacienti[:]
                        #ar_pacienti2 = ar_pacienti.copy() #face ce face si linia de mai sus -sunt echivalente
                        for i7 in ar_pacienti:
                            if i8 not in ar_idx_verificati_only:
                                for i9 in i7:
                                    t1=0
                                    for i10 in ter_toti_only:
                                        if i10!='lipsa T dim' and i10!='lipsa T dup':
                                            row=(db(db.terapeuti.nume==i10).select().first()).ce_terapii_face
                                            if (i9 in row)==True:
                                                t1=1
                                                break
                                    if t1==0:
                                        #ar_pacienti2[i8].remove(i9)
                                        ar_pacienti2[i8] = [xer for xer in ar_pacienti2[i8] if xer != i9] #face ce face si linia de mai sus dar nu actioneaza si asupra originalului
                            i8=i8+1        

                        ##sfarsit cod80 mai fac o verificare prin intermediul lui ter_toti_only(pe care o sa operez) sa vad ce terapii mai raman pt fiecare pacient in ar_pacienti
                        
                        ########################inceput cod777 - aloc terapii si terapeuti fiecarui Pp.La sfarsit aceasta va fi realizata
                        for i77 in range(20):  #20 este ales arbitrar puteam sa pun si 100. Am pus mai mult pt a face bucla de suficiente ori 
                            array1=[]
                            array2=[]
                            array3=[]
                            i8=0
                            c1=0 # variabila pt a vedea daca i7 este sau nu in ar_idx_verificati_only. Are valoarea 1 daca nu este si 0 daca este. vezi mai jos cu 6 linii
                            ##inceput cod 221 pt a pune in matrice toti pacientii fara terapii
                            i8=0
                            for i7 in ar_pacienti:
                                if i8 not in ar_idx_verificati_only:
                                    if len(ar_pacienti2[i8])==0:
                                        matrix_TA[5][i8]='introdu terapeut'
                                        ar_idx_verificati[i8]=i8
                                        ar_idx_verificati_only.append(i8)

                                i8=i8+1                

                            ##sfarsit cod 221 pt a pune in matrice toti pacientii fara terapii
                            if len(ar_idx_verificati_only)<(nr_pacienti_p-1):#daca mai am cu cine sa compar, adica daca daca mai sunt macar 2 pacienti de rezolvat
                                for i7 in range(nr_pacienti_p):
                                    array1=[]
                                    if i7 not in ar_idx_verificati_only:
                                        c1=1
                                        array1.append(i7)#am adaugat indexul sa vad al catalea este in matrix_TA[5]
                                        if len(ar_pacienti2[i7])>0:
                                            idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==ar_pacienti2[i7][0]][0]
                                            array1.append(ar_pacienti2[i7][0]) #am adaugat terapia
                                        ###inceput cod adaug terapeutul
                                        
                                        for i9 in eval(dictTI_ord[ar_pacienti2[i7][0]]): # ma plimb in arrayul cu terapeuti ai acelei terapii si cum gasesc ies
                                            if i9 in ter_toti_only:
                                                array1.append(i9) # am adaugat si terapeutul
                                                break
                                        if len(array1)==2:
                                            array1.append('-fara terapeut')    
                                        ###sfarsit cod adaug terapeutul
                                        array1.append(len(ar_pacienti2[i7]))#am adaugat lungimea (nr de terapii pe care le are la dispozitie acel pacient)
                                        ### inceput cod verific daca acea terapie este importanta sau nu
                                        if array_datele_orar_p[-(nr_pacienti-i7)*19+2]!=None and len(array_datele_orar_p[-(nr_pacienti-i7)*19+2])==1:
                                            if array_datele_orar_p[-(nr_pacienti-i7)*19+2][0]==ar_pacienti2[i7][0]:
                                                array1.append('da')
                                            else:
                                                array1.append('nu')    
                                        else:
                                            array1.append('nu')        
                                        ### sfarsit cod verific daca acea terapie este importanta sau nu
                                        ###inceput cod verific  terapie de cate ori apare
                                        de_cate_ori_apare_terapia=0
                                        if array_datele_orar_p[-(nr_pacienti-i7)*19+4]!=None:
                                            for row in eval((array_datele_orar_p[-(nr_pacienti-i7)*19+4])[-1])[-1]:
                                                if row==ar_pacienti2[i7][0]:
                                                    de_cate_ori_apare_terapia=de_cate_ori_apare_terapia+1
                                        array1.append(de_cate_ori_apare_terapia) #am adaugat de cate ori este terapia respectiva facuta in trecut            
                                        ###sfarsit cod verific de cate ori apare
                                        ###inceput1 verific si adaug de cate zile este pacientul
                                        if array_datele_orar_p[-(nr_pacienti-i7)*19+4]!=None:
                                            array1.append((dataa-(eval(array_datele_orar_p[-(nr_pacienti-i7)*19+4][0]))[0]).days) #am adaugat de cate zile este pacientul
                                        else:
                                            array1.append(0)   
                                    else:
                                        c1=2         
                                        ###sfarsit1 verific si adaug de cate zile este pacientul
                                    if c1==1:
                                            
                                        if len(array2)==0:
                                            array2=array1[:]
                                        else: #incepe sa compari array1 cu array2
                                            if array1!=[]:
                                                array3=[]
                                                if array2[3]==1:
                                                    array3=array2[:]
                                                    break
                                                if array1[3]==1:
                                                    array3=array1[:]
                                                    break
                                                if array1[4]=='da' and array2[4]=='nu':
                                                    array3=array1[:]
                                                if array2[4]=='da' and array1[4]=='nu':    
                                                    array3=array2[:]
                                                if array1[4]=='nu' and array2[4]=='nu':
                                                    if array1[5]<array2[5]:
                                                        array3=array1[:]
                                                    if array1[5]>array2[5]:    
                                                        array3=array2[:]
                                                    if array1[5]==array2[5]:
                                                        if array1[3]>array2[3]:
                                                            array3=array2[:]
                                                        if array1[3]<array2[3]:
                                                            array3=array1[:]
                                                        if array1[3]==array2[3]:
                                                            if array2[6]<array1[6]:
                                                                array3=array1[:]
                                                            else:
                                                                array3=array2[:]
                                                if array1[4]=='da' and array2[4]=='da':        
                                                    if array1[5]<array2[5]:
                                                        array3=array1[:]
                                                    if array1[5]>array2[5]:    
                                                        array3=array2[:]
                                                    if array1[5]==array2[5]:
                                                        if array1[6]>array2[6]:
                                                            array3=array1[:]
                                                        if array1[6]<array2[6]:
                                                            array3=array2[:]
                                                        if array1[6]==array2[6]:
                                                            if array2[3]>array1[3]:
                                                                array3=array1[:]
                                                            else:
                                                                array3=array2[:]
                                                array2=array3[:]
                                            else:
                                                array2=array3[:]    
                                matrix_TA[5][array3[0]]=dictTI_prescurtari[array3[1]]+'-'+array3[2]
                                ar_Pp[array3[0]]=array3[1] 
                                ar_PpTi5[array3[0]]=array3[2]
                                if array3[2]!='-fara terapeut':
                                    ####inceput cod12 actualizez: terapeutii daca mai sunt dispo; mesele si terapiile daca se mai pot face...
                                    idx=[i2 for i2, j2 in enumerate(ter_toti) if j2==array3[2]][0]
                                    contor_terapeuti1416[idx]=contor_terapeuti1416[idx]+1
                                    contor_terapeuti1415[idx]=contor_terapeuti1415[idx]+1
                                    if contor_terapeuti1416[idx]==2:
                                        c2=1 #variabila de control
                                        ter_toti_only.remove(array3[2])

                                    ####sfarsit cod12 actualizez: terapeutii daca mai sunt dispo; mesele si terapiile daca se mai pot face...
                                ##inceput cod11 actualizez f. important ce Pp mai am de rezolvat
                                ar_idx_verificati[array3[0]]=array3[0]
                                ar_idx_verificati_only.append(array3[0])
                                ##sfarsit cod11 actualizez f. important ce Pp mai am de rezolvat
                                ##inceput cod80 mai fac o verificare prin intermediul lui ter_toti_only(pe care o sa operez) sa vad ce terapii mai raman pt fiecare pacient in ar_pacienti
                                i8=0
                                t1=0
                                
                                for i7 in ar_pacienti:
                                    if i8 not in ar_idx_verificati_only:
                                        for i9 in i7:
                                            t1=0
                                            for i10 in ter_toti_only:
                                                if i10!='lipsa T dim' and i10!='lipsa T dup':
                                                    row=(db(db.terapeuti.nume==i10).select().first()).ce_terapii_face
                                                    if (i9 in row)==True:
                                                        t1=1
                                                        break

                                            if t1==0:
                                                #ar_pacienti2[i8].remove(i9)
                                                ar_pacienti2[i8] = [xer for xer in ar_pacienti2[i8] if xer != i9] ##face ce face si linia de mai sus dar nu actioneaza si asupra originalului
                                    i8=i8+1        

                                ##sfarsit cod80 mai fac o verificare prin intermediul lui ter_toti_only(pe care o sa operez) sa vad ce terapii mai raman pt fiecare pacient in ar_pacienti    
                                ##inceput cod43 verific situatia meselor de masaj si daca nu mai am loc scot acele terapii
                                idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==array3[1]][0]
                                if idx==1 or idx==2 or idx==3:
                                    ocupat_masa_oleatie1415=ocupat_masa_oleatie1415+1
                                    ocupat_masa_oleatie1416=ocupat_masa_oleatie1416+1
                                    
                                if idx==4 or idx==5 or idx==6 or idx==7 or idx==8:
                                    ocupat_masa_masaj1415=ocupat_masa_masaj1415+1
                                    ocupat_masa_masaj1416=ocupat_masa_masaj1416+1

                                if ocupat_masa_masaj1416>=6:
                                    i8=0
                                    for i7 in ar_pacienti:
                                        if i8 not in ar_idx_verificati_only:
                                            for i9 in i7:
                                                idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==i9][0]
                                                if idx==4 or idx==5 or idx==6 or idx==7 or idx==8:
                                                    #ar_pacienti2[i8].remove(i9) 
                                                    ar_pacienti2[i8] = [xer for xer in ar_pacienti2[i8] if xer != i9] #face ce face si linia de mai sus dar nu actioneaza si asupra originalului
                                                
                                                                                    
                                        i8=i8+1    

                                if ocupat_masa_oleatie1416>=4:
                                    i8=0
                                    for i7 in ar_pacienti:
                                        if i8 not in ar_idx_verificati_only:
                                            for i9 in i7:
                                                idx=[i2 for i2, j2 in enumerate(terapii_individuale) if j2==i9][0]
                                                if idx==1 or idx==2 or idx==3:
                                                    #ar_pacienti2[i8].remove(i9) 
                                                    ar_pacienti2[i8] = [xer for xer in ar_pacienti2[i8] if xer != i9] #face ce face si linia de mai sus dar nu actioneaza si asupra originalului
                                                    i88.append(i8)    
                                                    i88.append(i9)    
                                                                                    
                                        i8=i8+1       

                                ##sfarsit cod43 verific situatia meselor de masaj si daca nu mai am loc scot acele terapii
                                ##inceput cod 221 pt a pune in matrice toti pacientii fara terapii
                                i8=0
                                for i7 in ar_pacienti:
                                    if i8 not in ar_idx_verificati_only:
                                        if len(ar_pacienti2[i8])==0:
                                            matrix_TA[5][i8]='introdu terapeut'
                                            ar_idx_verificati[i8]=i8
                                            ar_idx_verificati_only.append(i8)

                                    i8=i8+1                

                                ##sfarsit cod 221 pt a pune in matrice toti pacientii fara terapii





                        ##inceput cod81 pentru ultimul Pp sa ii stabilesc terapia si terapeutul
                        if 50 in ar_idx_verificati:
                            array3=[]
                            index_last_Pp = ar_idx_verificati.index(50)
                            array3.append(index_last_Pp)
                            array3.append(ar_pacienti2[index_last_Pp][0])
                            for i9 in eval(dictTI_ord[ar_pacienti2[index_last_Pp][0]]): # ma plimb in arrayul cu terapeuti ai acelei terapii si cum gasesc ies
                                if i9 in ter_toti_only:
                                    array3.append(i9) # am adaugat si terapeutul
                                    break
                            if len(array3)==2:
                                array3.append('-fara terapeut')
                            ar_Pp[array3[0]]=array3[1]
                            ar_PpTi5[array3[0]]=array3[2]
                            matrix_TA[5][array3[0]]=dictTI_prescurtari[array3[1]]+'-'+array3[2]
                            if array3[2]!='-fara terapeut':
                                ####inceput cod12 actualizez: terapeutii daca mai sunt dispo; mesele si terapiile daca se mai pot face...
                                idx=[i2 for i2, j2 in enumerate(ter_toti) if j2==array3[2]][0]
                                contor_terapeuti1416[idx]=contor_terapeuti1416[idx]+1
                                contor_terapeuti1415[idx]=contor_terapeuti1415[idx]+1
                                if contor_terapeuti1416[idx]==2:
                                    c2=1 #variabila de control
                                    ter_toti_only.remove(array3[2])

                                ####sfarsit cod12 actualizez: terapeutii daca mai sunt dispo; mesele si terapiile daca se mai pot face...
                            ar_idx_verificati[array3[0]]=array3[0]
                            ar_idx_verificati_only.append(array3[0])
                            
                            ##inceput cod80 mai fac o verificare prin intermediul lui ter_toti_only(pe care o sa operez) sa vad ce terapii mai raman pt fiecare pacient in ar_pacienti
                            i8=0
                            t1=0
                            
                            for i7 in ar_pacienti:
                                if i8 not in ar_idx_verificati_only:
                                    for i9 in i7:
                                        t1=0
                                        for i10 in ter_toti_only:
                                            if i10!='lipsa T dim' and i10!='lipsa T dup':
                                                row=(db(db.terapeuti.nume==i10).select().first()).ce_terapii_face
                                                if (i9 in row)==True:
                                                    t1=1
                                                    break

                                        if t1==0:
                                            #ar_pacienti2[i8].remove(i9)
                                            ar_pacienti2[i8] = [xer for xer in ar_pacienti2[i8] if xer != i9] #face ce face si linia de mai sus dar nu actioneaza si asupra originalului
                                i8=i8+1        
                        ##sfarsit cod80 mai fac o verificare prin intermediul lui ter_toti_only(pe care o sa operez) sa vad ce terapii mai raman pt fiecare pacient in ar_pacienti

                        ##sfarsit cod81 pentru ultimul Pp sa ii stabilesc terapia si terapeutul

                        
                                        
                        
                        
                        ########################sfarsit cod777

                        #############################Sfarsitt Cod133 alocare terapii si terapeuti doar PACIENTILOR din ar_pacienti
                            
                    
                    
                    

                        ###sfarsit44 cod mutare din linia 1 in linia 3
                        ###inceput cod142 mut jumatate TI ale (Pp+Pa) din linia 5 in linia 6 si pun TAHION SI FR-CR in liniile 5,6,7
                        ar_PpTi5doarT=[] #o sa pun in el din ar_PpTi5 doar terapeutii si elimin 'fara' sau 'introdu terapeut' sau 49 sau 50
                        for i7 in ar_PpTi5:
                            if i7 in ter_toti:
                                ar_PpTi5doarT.append(i7)
                        ar_PpTi5doarT2=[] # in acest array vor fi terapeutii care apar de 2 ori in linia 5si trebuie sa cobor unul in linia6 ['Mirela', 'Iulia', 'Mari', 'Lidia', 'Mihai']
                        for i7 in ar_PpTi5doarT:
                            nr=ar_PpTi5doarT.count(i7)
                            if nr==2:
                                if i7 not in ar_PpTi5doarT2:
                                    ar_PpTi5doarT2.append(i7)
                        
                        for i7 in ar_PpTi5doarT2:  #ar_PpTi5doarT2=['Nushu', 'Lidia']
                            i9=0
                            for i8 in ar_PpTi5:  #ar_PpTi5=['Nushu', 49, 'Lidia', 'Carla', 'Nushu']
                                if i9<nr_pacienti_p_si_aP:
                                    if i8==i7:
                                        arr_indexMTA5.append(i9)
                                    

                                        break            
                                i9=i9+1

                                
                        nrcaremaitrebuiecoborati=int((len(ar_PpTi5doarT)/2)-len(ar_PpTi5doarT2))
                        for i7 in range(nrcaremaitrebuiecoborati):
                            i9=0
                            for i8 in ar_PpTi5doarT:
                                if i8 not in ar_PpTi5doarT2:
                                    if len(lista_indecsi_AP)==2 and lista_indecsi_AP[0]!=i9:
                                        ar_PpTi5doarT2.append(i8)
                                        arr_indexMTA5.append(i9)
                                        break
                                    if len(lista_indecsi_AP)!=2:
                                        ar_PpTi5doarT2.append(i8)
                                        arr_indexMTA5.append(i9)
                                        break
                                i9=i9+1    
                        
                        
                        
                        ##inceput cod135 incep sa cobor si sa aloc
                        i8=0
                        i9=0
                        for i7 in matrix_TA[5]:
                            if i8 in arr_indexMTA5:#acestia sunt cei coboriti cu terapia individuala de pe linia 5 pe linia 6 -(jumate din total)
                                matrix_TA[6][i8]=i7
                                
                                for i112 in ter_toti:
                                    if (i112 not in ter5) or (ter5.count(i112)<2):
                                        terapeutul_3=i112
                                        #ter5.append(i112)
                                        break
                                    else:
                                        terapeutul_3='nu are'
                                for i113 in ter_dup:
                                    if (i113 not in ter7) or  (i113 not in ar_PpTi7 and (ter7.count(i113)<7)):
                                        terapeutul_4=i113
                                        #ter7.append(i113)
                                        break   
                                    elif (i113 not in ter7) or (ter7.count(i113)<2):
                                        terapeutul_4=i113
                                        #ter7.append(i113)
                                        break
                                    
                                    else:
                                        terapeutul_4='nu are'
                                
                                        



                                if i9%2==0:
                                    if nr_FrCr5<4:
                                        matrix_TA[5][i8]='Frecv-CR'+'-'+terapeutul_3
                                        nr_FrCr5=nr_FrCr5+1
                                        if terapeutul_3!='nu are':   
                                            ter5.append(terapeutul_3)
                                    if nr_Tahioni5<3:
                                        matrix_TA[7][i8]='TAHION'+'-'+terapeutul_4
                                        nr_Tahioni7=nr_Tahioni7+1
                                        if terapeutul_4!='nu are':
                                            ter7.append(terapeutul_4)
                                    
                                        
                                    
                                if i9%2==1:
                                    if nr_FrCr5<4:
                                        matrix_TA[7][i8]='Frecv-CR'+'-'+terapeutul_4
                                        nr_FrCr7=nr_FrCr7+1
                                        if terapeutul_4!='nu are':
                                            ter7.append(terapeutul_4)
                                    if nr_Tahioni5<3:        
                                        matrix_TA[5][i8]='TAHION'+'-'+terapeutul_3
                                        nr_Tahioni5=nr_Tahioni5+1
                                        if terapeutul_3!='nu are':
                                            ter5.append(terapeutul_3)
                                    
                                    
                                i9=i9+1

                            i8=i8+1
                        nr_tah_frcr5=nr_Tahioni5+nr_FrCr5
                        nr_tah_frcr6=nr_Tahioni6+nr_FrCr6
                        nr_tah_frcr7=nr_Tahioni7+nr_FrCr7
                        nr_tah_frcr8=nr_Tahioni8+nr_FrCr8
                        i8=0
                        i9=0
                        for i7 in matrix_TA[5]:#pun pt cei care nu au deloc TI in linia 5 si/sau 6,7,8 TAHION si FR-CR
                            if i8<nr_pacienti_p_si_aP and (matrix_TA[5][i8]=='fara' or matrix_TA[5][i8]=='-'):
                                if nr_tah_frcr5<7:#daca am tahion sau fr-cr disponibil

                                    for i112 in ter_toti:
                                        if (i112 not in ter5) or (ter5.count(i112)<2):
                                            terapeutul_5=i112
                                            ter5.append(i112)
                                            break
                                        else:
                                            terapeutul_5='nu are'

                                    for i112 in ter_toti:
                                        if (i112 not in ter6) or (ter6.count(i112)<2):
                                            terapeutul_6=i112
                                            #ter6.append(i112)
                                            break
                                        else:
                                            terapeutul_6='nu are'
                                    for i113 in ter_dup:
                                        if (i113 not in ter7) or  (i113 not in ar_PpTi7 and (ter7.count(i113)<7)):
                                            terapeutul_7=i113
                                            #ter7.append(i113)
                                            break   
                                        elif (i113 not in ter7) or (ter7.count(i113)<2):
                                            terapeutul_7=i113
                                            #ter7.append(i113)
                                            break
                                        else:
                                            terapeutul_7='nu are'
                                    for i113 in ter_dup:
                                        if (i113 not in ter8) or (ter8.count(i113)<7):
                                            terapeutul_8=i113
                                            #ter8.append(i113)
                                            break
                                        else:
                                            terapeutul_8='nu are'        

            
                                    if i9%2==0 and nr_FrCr5<4:

                                        matrix_TA[5][i8]='Frecv-CR'+'-'+terapeutul_5
                                        arr_indexMTA5.append(i8)
                                        nr_FrCr5=nr_FrCr5+1
                                        if terapeutul_5!='nu are':
                                            ter5.append(terapeutul_5)
                                            
                                        for i10 in range(6,9):
                                            if eval('nr_Tahioni'+str(i10))<3:
                                                matrix_TA[i10][i8]='TAHION'+'-'+eval('terapeutul_'+str(i10))
                                                if i10==6:
                                                    nr_Tahioni6=nr_Tahioni6+1
                                                if i10==7:
                                                    nr_Tahioni7=nr_Tahioni7+1
                                                if i10==8:    
                                                    nr_Tahioni8=nr_Tahioni8+1

                                                if eval('terapeutul_'+str(i10))!='nu are':
                                                    if i10==6:
                                                        ter6.append(terapeutul_6)
                                                    if i10==7:
                                                        ter7.append(terapeutul_7)    
                                                    if i10==8:
                                                        ter8.append(terapeutul_8)    
                                                
                                                break


                                    elif i9%2==0 and nr_Tahioni5<3:
                                        matrix_TA[5][i8]='TAHION'+'-'+terapeutul_5
                                        nr_Tahioni5=nr_Tahioni5+1
                                        arr_indexMTA5.append(i8)
                                        if terapeutul_5!='nu are':
                                            ter5.append(terapeutul_5)
                                        for i10 in range(6,9):
                                            if eval('nr_FrCr'+str(i10))<4:
                                                matrix_TA[i10][i8]='Frecv-CR'+'-'+eval('terapeutul_'+str(i10))
                                                if i10==6:
                                                    nr_FrCr6=nr_FrCr6+1
                                                if i10==7:
                                                    nr_FrCr7=nr_FrCr7+1
                                                if i10==8:    
                                                    nr_FrCr8=nr_FrCr8+1

                                                if eval('terapeutul_'+str(i10))!='nu are':
                                                    if i10==6:
                                                        ter6.append(terapeutul_6)
                                                    if i10==7:
                                                        ter7.append(terapeutul_7)    
                                                    if i10==8:
                                                        ter8.append(terapeutul_8)    
                                                
                                                break
                                                
                                                        
                                        
                                    if i9%2==1 and nr_Tahioni5<3:
                                        matrix_TA[5][i8]='TAHION'+'-'+terapeutul_5
                                        arr_indexMTA5.append(i8)
                                        nr_Tahioni5=nr_Tahioni5+1
                                        if terapeutul_5!='nu are':
                                            ter5.append(terapeutul_5)
                                        for i10 in range(6,9):
                                            if eval('nr_FrCr'+str(i10))<4:
                                                matrix_TA[i10][i8]='Frecv-CR'+'-'+eval('terapeutul_'+str(i10))
                                                if i10==6:
                                                    nr_FrCr6=nr_FrCr6+1
                                                if i10==7:
                                                    nr_FrCr7=nr_FrCr7+1
                                                if i10==8:    
                                                    nr_FrCr8=nr_FrCr8+1

                                                if eval('terapeutul_'+str(i10))!='nu are':
                                                    if i10==6:
                                                        ter6.append(terapeutul_6)
                                                    if i10==7:
                                                        ter7.append(terapeutul_7)    
                                                    if i10==8:
                                                        ter8.append(terapeutul_8)    
                                                
                                                break   
                                    elif i9%2==1 and nr_FrCr5<4:
                                        matrix_TA[5][i8]='Frecv-CR'+'-'+terapeutul_5
                                        arr_indexMTA5.append(i8)
                                        nr_FrCr5=nr_FrCr5+1
                                        if terapeutul_5!='nu are':
                                            ter5.append(terapeutul_5)
                                        for i10 in range(6,9):
                                            if eval('nr_Tahioni'+str(i10))<3:
                                                matrix_TA[i10][i8]='TAHION'+'-'+eval('terapeutul_'+str(i10))
                                                if i10==6:
                                                    nr_Tahioni6=nr_Tahioni6+1
                                                if i10==7:
                                                    nr_Tahioni7=nr_Tahioni7+1
                                                if i10==8:    
                                                    nr_Tahioni8=nr_Tahioni8+1

                                                if eval('terapeutul_'+str(i10))!='nu are':
                                                    if i10==6:
                                                        ter6.append(terapeutul_6)
                                                    if i10==7:
                                                        ter7.append(terapeutul_7)    
                                                    if i10==8:
                                                        ter8.append(terapeutul_8)    
                                                
                                                break
                                                    
                                    i9=i9+1
                                    
                            i8=i8+1



                        if len(lista_indecsi_AP)==2:
                            arr_indexMTA5.append(lista_indecsi_AP[0])
                        i8=0
                        for i7 in matrix_TA[5]:
                            if i8<nr_pacienti_p_si_aP:
                                if i8 not in arr_indexMTA5:
                                    #if matrix_TA[5][i8]!='fara' and matrix_TA[5][i8]!='introdu terapeut' and matrix_TA[5][i8]!='-':#adica cei din linia 5 care au TI si care nu se muta
                                    a=0
                                    for i112 in ter_toti:#stabilesc terapeutul din linia 6 disponibil
                                        if (i112 not in ter6) or (ter6.count(i112)<2):
                                            terapeutul_6=i112                                            
                                            break
                                        else:
                                            terapeutul_6='nu are'
                                    for i112 in ter_dup:#stabilesc terapeutul din linia 7 disponibil
                                        if (i112 not in ter7) or  (i112 not in ar_PpTi7 and (ter7.count(i112)<7)):
                                            terapeutul_7=i112
                                            #ter7.append(i113)
                                            break   
                                        elif (i112 not in ter7) or (ter7.count(i112)<2):
                                            terapeutul_7=i112                                            
                                            break
                                        else:
                                            terapeutul_7='nu are'
                                    for i112 in ter_dup:#stabilesc terapeutul din linia 8 disponibil
                                        if (i112 not in ter8) or (ter8.count(i112)<7):
                                            terapeutul_8=i112                                            
                                            break
                                        else:
                                            terapeutul_8='nu are'            
                                    if nr_Tahioni6<3:
                                        a=1
                                        matrix_TA[6][i8]='TAHION-'+terapeutul_6
                                        nr_Tahioni6=nr_Tahioni6+1
                                        if terapeutul_6!='nu are':
                                            ter6.append(terapeutul_6)
                                        if nr_FrCr7<4:
                                            matrix_TA[7][i8]='Frecv-CR-'+terapeutul_7
                                            nr_FrCr7=nr_FrCr7+1
                                            if terapeutul_7!='nu are':
                                                ter7.append(terapeutul_7)
                                            
                                        else:
                                            matrix_TA[8][i8]='Frecv-CR-'+terapeutul_8
                                            nr_FrCr8=nr_FrCr8+1
                                            if terapeutul_8!='nu are':
                                                ter8.append(terapeutul_8)   


                                        
                                    if a==0:
                                        if nr_FrCr6<4:
                                            a=2
                                            matrix_TA[6][i8]='Frecv-CR-'+terapeutul_6
                                            nr_FrCr6=nr_FrCr6+1
                                            if terapeutul_6!='nu are':
                                                ter6.append(terapeutul_6)
                                            if nr_Tahioni7<3:
                                                matrix_TA[7][i8]='TAHION-'+terapeutul_7
                                                nr_Tahioni7=nr_Tahioni7+1
                                                if terapeutul_7!='nu are':    
                                                    ter7.append(terapeutul_7)
                                            else:
                                                matrix_TA[8][i8]='Tahion-'+terapeutul_8
                                                ter8.append(terapeutul_8)
                                                if terapeutul_8!='nu are':
                                                    nr_Tahioni8=nr_Tahioni8+1
                                    if a==0:#aici ar trebui sa fac ceva daca nu am loc nici in linia 6 si nici in linia 7 nici de TAHION nici de FR-CR-las deocamdata asa
                                        pass

                                    #if matrix_TA[5][i8]=='fara' or matrix_TA[5][i8]=='-':#cei din linia 5 care nu au nimic


                                        
                                            
                            i8=i8+1    

                        ##sfarsit cod135 incep sa cobor si sa aloc


                        ###sfarsit cod142 mut jumatate TI ale (Pp+Pa) din linia 5 in linia 6 si pun TAHION SI FR-CR in liniile 5,6,7
                    ##inceput cod70 refacere structura matrix_TA[6] si matrix_TA[7]  Ex: Matrix_TA[6]=['--' '--' 'PSIHO IND-nu are']  Matrix_TA[7]=['PSIHOTERAPIE INDIVIDUALA' '---' '---'] dadea o eroare la liniute -,---

                    if nr_zi1==6 or nr_zi1==7:
                        i8=0
                        for i7 in matrix_TA[5]:
                            if i8<nr_pacienti_p_si_aP: 
                                matrix_TA[5][i8]='-'
                            i8=i8+1
                        i8=0
                        for i7 in matrix_TA[6]:
                            if i8<nr_pacienti_p_si_aP: 
                                matrix_TA[6][i8]='--'
                            i8=i8+1
                        i8=0
                        for i7 in matrix_TA[7]:
                            if i8<nr_pacienti_p_si_aP: 
                                matrix_TA[7][i8]='---'
                            i8=i8+1
                        i8=0
                        for i7 in matrix_TA[8]:
                            if i8<nr_pacienti_p_si_aP: 
                                matrix_TA[8][i8]='----'
                            i8=i8+1
                        i8=0       
                        ##sfarsit cod70 refacere structura matrix_TA[6] si matrix_TA[7]  Ex: Matrix_TA[6]=['--' '--' 'PSIHO IND-nu are']  Matrix_TA[7]=['PSIHOTERAPIE INDIVIDUALA' '---' '---'] dadea o eroare la liniute -,--
                        #########inceput cod457 pun la toti Pp si Pa pe liniile 5,6,7,8 SAUNA,OZON,TAHION,FR-CR
                        #aici ma joc de maine
                        ####inceput cod23 fac tabelul arr_osb1=[['SAUNA', 'BAIE OZON'], ['SAUNA', 'BAIE OZON'], ['BAIE OZON']..., [], []..]
                        arr_osb=[] # array cu SAUNA , BAIA DE OZON SI BICICLETA
                        arr_osb2=[]
                        for i7 in range(nr_pacienti_p_si_aP):
                            if (array_datele_orar_p[-(nr_pacienti-i7)*19+7])!=None:
                                arr_osb.append((array_datele_orar_p[-(nr_pacienti-i7)*19+7]))
                            else:
                                arr_osb.append([])
                        for i7 in range(len(arr_osb)):
                            arr_osb2.append([])
                        i9=0
                        for i7 in arr_osb:
                            if len(i7)>0:
                                if ('SAUNA' in i7)==True:
                                    arr_osb2[i9].append('SAUNA')
                                if ('BAIE OZON' in i7)==True:
                                    arr_osb2[i9].append('BAIE OZON')    
                            i9=i9+1
                        ####sfarsit cod23 fac tabelul arr_osb1=[['SAUNA', 'BAIE OZON'], ['SAUNA', 'BAIE OZON'], ['BAIE OZON']..., [], []..]
                        ###inceput cod11 verific ce s-a facut Sambata pt a face altceva Duminica la cei care au 2 terapii: BAIE OZON si SAUNA
                        varOsauS='aa'
                        if nr_zi1==7:
                            i9=0
                            arr_osb3=arr_osb2[:]
                            for i7 in arr_osb3:
                                if len(i7)==2:
                                    if (array_datele_orar_p[-(nr_pacienti-i9)*19+8])!=None:
                                        varOsauS=(eval(array_datele_orar_p[-(nr_pacienti-i9)*19+8][-1]))[-1][-1] #poate fi SAUNA sau BAIE OZON ce a fost Sambata
                                        #if varOsauS!=50:
                                        (arr_osb2[i9]).remove(varOsauS)
                                i9=i9+1
                        ###sfarsit cod11 verific ce s-a facut Sambata pt a face altceva Duminica la cei care au 2 terapii: BAIE OZON si SAUNA

                        arr_osb1=arr_osb2[:]
                        ###sfarsit cod11 verific ce s-a facut Sambata pt a face altceva Duminica la cei care au 2 terapii: BAIE OZON si SAUNA
                        ####inceput cod24 fac variabilele: nrp_faraosb,nrp_cuO,nrp_cuOS pt a vedea cati pacienti am cu BAIE OZON cu SAUNA, cu amandoua sau cu niciuna
                        nrp_faraosb=0 #numarul de pacienti care nu au nici BAIE OZON nici SAUNA
                        nrp_cuO=0 # numarul de pacienti care au BAIE OZON
                        nrp_cuS=0 # numarul de pacienti care au SAUNA
                        nrp_cuOS=0 # numarul de pacienti care au BAIE OZON si SAUNA
                        for i7 in arr_osb1:
                            if i7==[]:
                                nrp_faraosb=nrp_faraosb+1
                            if i7==['BAIE OZON']:
                                nrp_cuO=nrp_cuO+1
                            if i7==['SAUNA']:
                                nrp_cuS=nrp_cuS+1
                            if i7==['SAUNA','BAIE OZON']:            
                                nrp_cuOS=nrp_cuOS+1
                        nrp_cuO=nrp_cuO+nr_Ozon5+nr_Ozon6+nr_Ozon7
                        nrp_cuS=nrp_cuS+nr_Sauna5+nr_Sauna6+nr_Sauna7        
                        nr_totalOSB=nrp_cuO+nrp_cuS+nrp_cuOS#numarul total de pacienti cu  BAIE OZON ori SAUNA sau ambele
                        
                        ####sfarsit cod24 fac variabilele: nrp_faraosb,nrp_cuO,nrp_cuOS pt a vedea cati pacienti am cu BAIE OZON cu SAUNA, cu amandoua sau cu niciuna
                        ##inceput cod21 sa vad cate OS pun pe liniile 5,6,7
                        nr_pelinie=int(nr_totalOSB/3)
                        cate_liniiauinplus=nr_totalOSB%3
                        if cate_liniiauinplus!=0:
                            nr_pelinia5=nr_pelinie+1
                        if cate_liniiauinplus>1:                   
                            nr_pelinia6=nr_pelinie+1
                        else:
                            nr_pelinia6=nr_pelinie
                        nr_pelinia7=nr_pelinie
                        
                        ##sfarsit cod21 sa vad cate OS pun pe liniile 5,6,7
                        #########inceput cod434 pun in matrix_TA5 la toti Pp si Pa ozon sau sauna alternativ
                        i9=0
                        nrO=0
                        nrS=0
                        for i7 in arr_osb1:
                            if i9<nr_pacienti_p_si_aP:
                                if len(arr_osb1[i9])==1:
                                    matrix_TA[5][i9]=arr_osb1[i9][0]
                                    var1=arr_osb1[i9][0]
                                    if var1=='BAIE OZON':
                                        nrO=nrO+1
                                    else:
                                        nrS=nrS+1    
                            i9=i9+1
                        i9=0       
                        for i7 in arr_osb1:
                            if i9<nr_pacienti_p_si_aP:             
                                if len(arr_osb1[i9])==2:
                                    if nrO>=nrS:
                                        matrix_TA[5][i9]='SAUNA'
                                        nrS=nrS+1
                                    elif nrO<nrS:
                                        matrix_TA[5][i9]='BAIE OZON'
                                        nrO=nrO+1         
                            i9=i9+1        
                        #########sfarsit cod434 pun in matrix_TA5 la toti Pp si Pa ozon sau sauna alternativ

                        ##inceput cod89 cobor in liniile 6 si 7 ozon si sauna si aloc fr-cr si tahioni
                        mindecsirezolvati=[]
                        idxcineeinlinia8=[]
                        for i7 in range(nr_pacienti_p_si_aP):
                            mindecsirezolvati.append(50)
                        verificcaticobordinlinia5inlinia6=nr_pelinia6-nr_Ozon6-nr_Sauna6    
                        
                        for i10 in range(verificcaticobordinlinia5inlinia6):
                            i9=0
                            for i7 in matrix_TA[5]:
                                if i9<nr_pacienti_p_si_aP and verificcaticobordinlinia5inlinia6>0:
                                    if nr_Sauna6>=nr_Ozon6 and nr_Ozon6<2:
                                        if i7=='BAIE OZON':
                                            matrix_TA[6][i9]='BAIE OZON'
                                            nr_Ozon6=nr_Ozon6+1
                                            if nr_FrCr5<=nr_Tahioni5 and nr_FrCr5<4:
                                                matrix_TA[5][i9]=matrix_TA[5][i9]='Frecv-CR'
                                                nr_FrCr5=nr_FrCr5+1
                                                if nr_Tahioni7<3:
                                                    matrix_TA[7][i9]='TAHION'
                                                    nr_Tahioni7=nr_Tahioni7+1
                                                elif nr_Tahioni8<3:
                                                    matrix_TA[8][i9]='TAHION'
                                                    nr_Tahioni8=nr_Tahioni8+1
                                                    idxcineeinlinia8.append(i9)
                                                            
                                                                                
                                            elif nr_FrCr5>nr_Tahioni5 and nr_Tahioni5<3:
                                                matrix_TA[5][i9]=matrix_TA[5][i9]='TAHION'
                                                nr_Tahioni5=nr_Tahioni5+1
                                                if nr_FrCr7<4:
                                                    matrix_TA[7][i9]='Frecv-CR'
                                                    nr_FrCr7=nr_FrCr7+1
                                                elif nr_FrCr8<4:
                                                    matrix_TA[8][i9]='Frecv-CR'
                                                    nr_FrCr8=nr_FrCr8+1
                                                    idxcineeinlinia8.append(i9)
                                            mindecsirezolvati[i9]=i9
                                            verificcaticobordinlinia5inlinia6=verificcaticobordinlinia5inlinia6-1
                                            break
                                    elif nr_Sauna6<nr_Ozon6 and nr_Sauna6<2:
                                        if i7=='SAUNA':
                                            matrix_TA[6][i9]='SAUNA'
                                            nr_Sauna6=nr_Sauna6+1
                                            if nr_FrCr5<=nr_Tahioni5 and nr_FrCr5<4:
                                                matrix_TA[5][i9]=matrix_TA[5][i9]='Frecv-CR'
                                                nr_FrCr5=nr_FrCr5+1
                                                if nr_Tahioni7<3:
                                                    matrix_TA[7][i9]='TAHION'
                                                    nr_Tahioni7=nr_Tahioni7+1
                                                elif nr_Tahioni8<3:
                                                    matrix_TA[8][i9]='TAHION'
                                                    nr_Tahioni8=nr_Tahioni8+1
                                                    idxcineeinlinia8.append(i9)
                                                            
                                                                                
                                            elif nr_FrCr5>nr_Tahioni5 and nr_Tahioni5<3:
                                                matrix_TA[5][i9]=matrix_TA[5][i9]='TAHION'
                                                nr_Tahioni5=nr_Tahioni5+1
                                                if nr_FrCr7<4:
                                                    matrix_TA[7][i9]='Frecv-CR'
                                                    nr_FrCr7=nr_FrCr7+1
                                                elif nr_FrCr8<4:
                                                    matrix_TA[8][i9]='Frecv-CR'
                                                    nr_FrCr8=nr_FrCr8+1
                                                    idxcineeinlinia8.append(i9)
                                            mindecsirezolvati[i9]=i9  
                                            verificcaticobordinlinia5inlinia6=verificcaticobordinlinia5inlinia6-1
                                            break      
                                i9=i9+1
                            
                        ##sfarsit cod89 cobor in liniile 6 si 7 ozon si sauna si aloc fr-cr si tahioni

                        ##inceput cod899 cobor in liniile 6 si 7 ozon si sauna si aloc fr-cr si tahioni

                        
                        
                        verificcaticobordinlinia5inlinia7=nr_pelinia7-nr_Ozon7-nr_Sauna7    
                        i9=0
                        for i10 in range(verificcaticobordinlinia5inlinia7):
                            i9=0
                            for i7 in matrix_TA[5]:
                                if i9 not in mindecsirezolvati:
                                    if i9<nr_pacienti_p_si_aP and verificcaticobordinlinia5inlinia7>0:
                                        if nr_Sauna7>=nr_Ozon7 and nr_Ozon7<2:
                                            if i7=='BAIE OZON':
                                                matrix_TA[7][i9]='BAIE OZON'
                                                nr_Ozon7=nr_Ozon7+1
                                                if nr_FrCr5<=nr_Tahioni5 and nr_FrCr5<4:
                                                    matrix_TA[5][i9]=matrix_TA[5][i9]='Frecv-CR'
                                                    nr_FrCr5=nr_FrCr5+1
                                                    if nr_Tahioni6<3:
                                                        matrix_TA[6][i9]='TAHION'
                                                        nr_Tahioni6=nr_Tahioni6+1
                                                    elif nr_Tahioni8<3:
                                                        matrix_TA[8][i9]='TAHION'
                                                        nr_Tahioni8=nr_Tahioni8+1
                                                        idxcineeinlinia8.append(i9)
                                                                
                                                                                    
                                                elif nr_FrCr5>nr_Tahioni5 and nr_Tahioni5<3:
                                                    matrix_TA[5][i9]=matrix_TA[5][i9]='TAHION'
                                                    nr_Tahioni5=nr_Tahioni5+1
                                                    if nr_FrCr6<4:
                                                        matrix_TA[6][i9]='Frecv-CR'
                                                        nr_FrCr6=nr_FrCr6+1
                                                    elif nr_FrCr8<4:
                                                        matrix_TA[8][i9]='Frecv-CR'
                                                        nr_FrCr8=nr_FrCr8+1
                                                        idxcineeinlinia8.append(i9)
                                                mindecsirezolvati[i9]=i9
                                                verificcaticobordinlinia5inlinia7=verificcaticobordinlinia5inlinia7-1
                                                break
                                        elif nr_Sauna7<nr_Ozon7 and nr_Sauna7<2:
                                            if i7=='SAUNA':
                                                matrix_TA[7][i9]='SAUNA'
                                                nr_Sauna7=nr_Sauna7+1
                                                if nr_FrCr5<=nr_Tahioni5 and nr_FrCr5<4:
                                                    matrix_TA[5][i9]=matrix_TA[5][i9]='Frecv-CR'
                                                    nr_FrCr5=nr_FrCr5+1
                                                    if nr_Tahioni6<3:
                                                        matrix_TA[6][i9]='TAHION'
                                                        nr_Tahioni6=nr_Tahioni6+1
                                                    elif nr_Tahioni8<3:
                                                        matrix_TA[8][i9]='TAHION'
                                                        nr_Tahioni8=nr_Tahioni8+1
                                                        idxcineeinlinia8.append(i9)        
                                                                                    
                                                elif nr_FrCr5>nr_Tahioni5 and nr_Tahioni5<3:
                                                    matrix_TA[5][i9]=matrix_TA[5][i9]='TAHION'
                                                    nr_Tahioni5=nr_Tahioni5+1
                                                    if nr_FrCr6<4:
                                                        matrix_TA[6][i9]='Frecv-CR'
                                                        nr_FrCr6=nr_FrCr6+1
                                                    elif nr_FrCr8<4:
                                                        matrix_TA[8][i9]='Frecv-CR'
                                                        nr_FrCr8=nr_FrCr8+1
                                                        idxcineeinlinia8.append(i9)
                                                mindecsirezolvati[i9]=i9  
                                                verificcaticobordinlinia5inlinia7=verificcaticobordinlinia5inlinia7-1
                                                break      
                                i9=i9+1
                        ##sfarsit cod899 cobor in liniile 6 si 7 ozon si sauna si aloc fr-cr si tahioni
                        ##inceput cod8999 pun in liniile 6 si 7 si eventual 8 tahioni si fr-cr . Ramane pe loc sauna si baia ozon pe linia 5
                        i9=0
                        zz1=0
                        for i7 in matrix_TA[5]:
                            if i9<nr_pacienti_p_si_aP:
                                if i9 not in mindecsirezolvati:
                                    if i7=='BAIE OZON' or i7=='SAUNA':
                                        if nr_Tahioni6<nr_FrCr6 and nr_Tahioni6<3:
                                            matrix_TA[6][i9]='TAHION'
                                            nr_Tahioni6=nr_Tahioni6+1
                                            if nr_FrCr7<4:
                                                matrix_TA[7][i9]='Frecv-CR'
                                                nr_FrCr7=nr_FrCr7+1
                                            elif nr_FrCr8<4:
                                                matrix_TA[8][i9]='Frecv-CR'
                                                nr_FrCr8=nr_FrCr8+1
                                                idxcineeinlinia8.append(i9)    
                                            mindecsirezolvati[i9]=i9
                                        elif nr_Tahioni6<nr_FrCr6 and nr_FrCr6<4:
                                            matrix_TA[6][i9]='Frecv-CR'
                                            nr_FrCr6=nr_FrCr6+1
                                            if nr_Tahioni7<3:
                                                matrix_TA[7][i9]='TAHION'
                                                nr_Tahioni7=nr_Tahioni7+1
                                            elif nr_Tahioni8<3:
                                                matrix_TA[8][i9]='TAHION'
                                                nr_Tahioni8=nr_Tahioni8+1
                                                idxcineeinlinia8.append(i9)
                                            mindecsirezolvati[i9]=i9
                                        elif nr_Tahioni6>=nr_FrCr6 and nr_FrCr6<4:
                                            matrix_TA[6][i9]='Frecv-CR'
                                            nr_FrCr6=nr_FrCr6+1
                                            if nr_Tahioni7<3:
                                                matrix_TA[7][i9]='TAHION'
                                                nr_Tahioni7=nr_Tahioni7+1
                                            elif nr_Tahioni8<3:
                                                matrix_TA[8][i9]='TAHION'
                                                nr_Tahioni8=nr_Tahioni8+1
                                                idxcineeinlinia8.append(i9)
                                            mindecsirezolvati[i9]=i9    


                            i9=i9+1
                        ##sfarsit cod8999 pun in liniile 6 si 7 si eventual 8 tahioni si fr-cr . Ramane pe loc sauna si baia ozon pe linia 5
                        ##inceput cod347 incerc sa corectez daca se poate idxcineeinlinia8 sa vad daca pot sa-i pun doar pe liniile 5,6,7
                        for i7 in idxcineeinlinia8:
                            if matrix_TA[8][i7]=='TAHION':
                                if matrix_TA[5][i7]=='SAUNA' or matrix_TA[5][i7]=='BAIE OZON':
                                    if nr_Tahioni6<3 and nr_FrCr7<4:
                                        matrix_TA[8][i7]='----'
                                        nr_Tahioni8=nr_Tahioni8-1
                                        if matrix_TA[6][i7]=='Frecv-CR':
                                            nr_FrCr6=nr_FrCr6-1
                                        matrix_TA[6][i7]='TAHION'
                                        nr_Tahioni6=nr_Tahioni6+1
                                        if matrix_TA[7][i7]=='TAHION':
                                            nr_Tahioni7=nr_Tahioni7-1
                                        matrix_TA[7][i7]='Frecv-CR'
                                        nr_FrCr7=nr_FrCr7+1
                                elif matrix_TA[6][i7]=='SAUNA' or matrix_TA[6][i7]=='BAIE OZON':      
                                    if nr_Tahioni5<3 and nr_FrCr7<4:
                                        matrix_TA[8][i7]='----'
                                        nr_Tahioni8=nr_Tahioni8-1
                                        if matrix_TA[5][i7]=='Frecv-CR':
                                            nr_FrCr6=nr_FrCr6-1
                                        matrix_TA[5][i7]='TAHION'
                                        nr_Tahioni5=nr_Tahioni5+1
                                        if matrix_TA[7][i7]=='TAHION':
                                            nr_Tahioni7=nr_Tahioni7-1
                                        matrix_TA[7][i7]='Frecv-CR'
                                        nr_FrCr7=nr_FrCr7+1
                                elif matrix_TA[7][i7]=='SAUNA' or matrix_TA[7][i7]=='BAIE OZON':
                                    if nr_Tahioni5<3 and nr_FrCr6<4:
                                        matrix_TA[8][i7]='----'
                                        nr_Tahioni8=nr_Tahioni8-1
                                        if matrix_TA[5][i7]=='Frecv-CR':
                                            nr_FrCr5=nr_FrCr5-1
                                        matrix_TA[5][i7]='TAHION'
                                        nr_Tahioni5=nr_Tahioni5+1
                                        if matrix_TA[6][i7]=='TAHION':
                                            nr_Tahioni6=nr_Tahioni6-1
                                        matrix_TA[6][i7]='Frecv-CR'
                                        nr_FrCr6=nr_FrCr6+1
                                        
                            if matrix_TA[8][i7]=='Frecv-CR':
                                if matrix_TA[5][i7]=='SAUNA' or matrix_TA[5][i7]=='BAIE OZON':
                                    if nr_FrCr6<4 and nr_Tahioni7<3:
                                        matrix_TA[8][i7]='----'
                                        nr_FrCr8=nr_FrCr8-1
                                        if matrix_TA[6][i7]=='TAHION':
                                            nr_Tahioni6=nr_Tahioni6-1
                                        matrix_TA[6][i7]='Frecv-CR'
                                        nr_FrCr6=nr_FrCr6+1
                                        if matrix_TA[7][i7]=='Frecv-CR':
                                            nr_FrCr7=nr_FrCr7-1
                                        matrix_TA[7][i7]='TAHION'
                                        nr_Tahioni7=nr_Tahioni7+1
                                elif matrix_TA[6][i7]=='SAUNA' or matrix_TA[6][i7]=='BAIE OZON':      
                                    if nr_FrCr5<4 and nr_Tahioni7<3:
                                        matrix_TA[8][i7]='----'
                                        nr_FrCr8=nr_FrCr8-1
                                        if matrix_TA[5][i7]=='TAHION':
                                            nr_Tahioni6=nr_Tahioni6-1
                                        matrix_TA[5][i7]='Frecv-CR'
                                        nr_FrCr5=nr_FrCr5+1
                                        if matrix_TA[7][i7]=='Frecv-CR':
                                            nr_FrCr7=nr_FrCr7-1
                                        matrix_TA[7][i7]='TAHION'
                                        nr_Tahioni7=nr_Tahioni7+1
                                elif matrix_TA[7][i7]=='SAUNA' or matrix_TA[7][i7]=='BAIE OZON':
                                    if nr_FrCr5<4 and nr_Tahioni6<3:
                                        matrix_TA[8][i7]='----'
                                        nr_FrCr8=nr_FrCr8-1
                                        if matrix_TA[5][i7]=='TAHION':
                                            nr_Tahioni5=nr_Tahioni5-1
                                        matrix_TA[5][i7]='Frecv-CR'
                                        nr_FrCr5=nr_FrCr5+1
                                        if matrix_TA[6][i7]=='Frecv-CR':
                                            nr_FrCr6=nr_FrCr6-1
                                        matrix_TA[6][i7]='TAHION'
                                        nr_Tahioni6=nr_Tahioni6+1       
                            


                        ##sfarsit cod347 incerc sa corectez daca se poate idxcineeinlinia8 sa vad daca pot sa-i pun doar pe liniile 5,6,7
                        ##inceput cod90 pt a le pune FR-CR si TAHION Pp si Pa care nu au nici BAIE OZON nici SAUNA cei ramasi cu 50 in arrayul mindecsirezolvati
                        ## eventual o sa le pun data viitoare bicicleta
                        for i10 in range(nr_pacienti_p_si_aP):
                            i9=0
                            for i7 in mindecsirezolvati:
                                if i7==50:
                                    if nr_Tahioni5<3 or nr_FrCr5<4:
                                        if nr_Tahioni5<3:
                                            matrix_TA[5][i9]='TAHION'
                                            nr_Tahioni5=nr_Tahioni5+1
                                            if nr_FrCr6<4:
                                                matrix_TA[6][i9]='Frecv-CR'
                                                nr_FrCr6=nr_FrCr6+1
                                            elif nr_FrCr7<4:
                                                matrix_TA[7][i9]='Frecv-CR'
                                                nr_FrCr7=nr_FrCr7+1
                                            elif nr_FrCr8<4:
                                                matrix_TA[8][i9]='Frecv-CR'
                                                nr_FrCr8=nr_FrCr8+1
                                        elif nr_FrCr5<4:
                                            matrix_TA[5][i9]='Frecv-CR'
                                            nr_FrCr5=nr_FrCr5+1
                                            if nr_Tahioni6<3:
                                                matrix_TA[6][i9]='TAHION'
                                                nr_Tahioni6=nr_Tahioni6+1
                                            elif nr_Tahioni7<3:
                                                matrix_TA[7][i9]='TAHION'
                                                nr_Tahioni7=nr_Tahioni7+1
                                            elif nr_Tahioni8<3:
                                                matrix_TA[8][i9]='TAHION'
                                                nr_Tahioni8=nr_Tahioni8+1
                                        mindecsirezolvati[i9]=i9
                                        break
                                    elif nr_Tahioni6<3 or nr_FrCr6<4:
                                        if nr_Tahioni6<3:
                                            matrix_TA[6][i9]='TAHION'
                                            nr_Tahioni6=nr_Tahioni6+1
                                            if nr_FrCr7<4:
                                                matrix_TA[7][i9]='Frecv-CR'
                                                nr_FrCr7=nr_FrCr7+1
                                            elif nr_FrCr8<4:
                                                matrix_TA[8][i9]='Frecv-CR'
                                                nr_FrCr8=nr_FrCr8+1
                                            
                                        elif nr_FrCr6<4:
                                            matrix_TA[6][i9]='Frecv-CR'
                                            nr_FrCr6=nr_FrCr6+1
                                            if nr_Tahioni7<3:
                                                matrix_TA[7][i9]='TAHION'
                                                nr_Tahioni7=nr_Tahioni7+1
                                            elif nr_Tahioni8<3:
                                                matrix_TA[8][i9]='TAHION'
                                                nr_Tahioni8=nr_Tahioni8+1
                                        mindecsirezolvati[i9]=i9
                                        break
                                    elif nr_Tahioni7<3 or nr_FrCr7<4:
                                        if nr_Tahioni7<3:
                                            matrix_TA[7][i9]='TAHION'
                                            nr_Tahioni7=nr_Tahioni7+1
                                            if nr_FrCr8<4:
                                                matrix_TA[8][i9]='Frecv-CR'
                                                nr_FrCr8=nr_FrCr8+1
                                                                                    
                                        elif nr_FrCr7<4:
                                            matrix_TA[7][i9]='Frecv-CR'
                                            nr_FrCr7=nr_FrCr7+1
                                            if nr_Tahioni8<3:
                                                matrix_TA[8][i9]='TAHION'
                                                nr_Tahioni8=nr_Tahioni8+1
                                        mindecsirezolvati[i9]=i9
                                        break                
                                    elif nr_Tahioni8<3 or nr_FrCr8<4:
                                        if nr_Tahioni8<3:
                                            matrix_TA[8][i9]='TAHION'
                                            nr_Tahioni8=nr_Tahioni8+1
                                                                                                            
                                        elif nr_FrCr8<4:
                                            matrix_TA[8][i9]='Frecv-CR'
                                            nr_FrCr8=nr_FrCr8+1
                                        mindecsirezolvati[i9]=i9
                                        break
                                i9=i9+1    
                                
                        ##sfarsit cod90 pt a le pune FR-CR si TAHION Pp si Pa care nu au nici BAIE OZON nici SAUNA cei ramasi cu 50 in arrayul mindecsirezolvati
                        ##inceput11 cod pt a vedea daca in linia 5 sunt mai mult de 2 BAIE OZON sau SAUNA
                        i9=0
                        nrBo5=0
                        nrSa5=0
                        for i7 in matrix_TA[5]:
                            if matrix_TA[5][i9]=='BAIE OZON' or ((matrix_TA[5][i9].split("-"))[0])=='BAIE OZON':
                                nrBo5=nrBo5+1
                            if matrix_TA[5][i9]=='SAUNA' or ((matrix_TA[5][i9].split("-"))[0])=='SAUNA':
                                nrSa5=nrSa5+1    
                            i9=i9+1    
                        i9=0
                        nrBo6=0
                        nrSa6=0
                        for i7 in matrix_TA[6]:
                            if matrix_TA[6][i9]=='BAIE OZON' or ((matrix_TA[6][i9].split("-"))[0])=='BAIE OZON':
                                nrBo6=nrBo6+1
                            if matrix_TA[6][i9]=='SAUNA' or ((matrix_TA[6][i9].split("-"))[0])=='SAUNA':
                                nrSa6=nrSa6+1    
                            i9=i9+1
                        i9=0
                        nrBo7=0
                        nrSa7=0
                        for i7 in matrix_TA[7]:
                            if matrix_TA[7][i9]=='BAIE OZON' or ((matrix_TA[7][i9].split("-"))[0])=='BAIE OZON':
                                nrBo7=nrBo7+1
                            if matrix_TA[7][i9]=='SAUNA' or ((matrix_TA[7][i9].split("-"))[0])=='SAUNA':
                                nrSa7=nrSa7+1    
                            i9=i9+1        

                        ##sfarsit11 cod pt a vedea daca in linia 5 sunt mai mult de 2 BAIE OZON sau SAUNA
                        ##inceput113 cod pt a cobori din linia 5 daca sunt mai multe
                        for i10 in range(8): #7 este ales aleator
                            if nrBo5>2:
                                i9=0
                                for i7 in matrix_TA[5]:
                                    if i7=='BAIE OZON':
                                        if nrBo6<2:
                                            v1=matrix_TA[6][i9]
                                            if v1=='TAHION':
                                                if nr_Tahioni5<3:
                                                    matrix_TA[5][i9]='TAHION'
                                                    nr_Tahioni5=nr_Tahioni5+1
                                                    nr_Tahioni6=nr_Tahioni6-1
                                                    matrix_TA[6][i9]='BAIE OZON'
                                                    nrBo6=nrBo6+1
                                                    nrBo5=nrBo5-1
                                                    break
                                            elif v1=='Frecv-CR':
                                                if nr_FrCr5<4:
                                                    matrix_TA[5][i9]='Frecv-CR'
                                                    nr_FrCr5=nr_FrCr5+1
                                                    nr_FrCr6=nr_FrCr6-1
                                                    matrix_TA[6][i9]='BAIE OZON'
                                                    nrBo6=nrBo6+1
                                                    nrBo5=nrBo5-1
                                                    break        

                                        elif nrBo7<2:
                                            v1=matrix_TA[7][i9]
                                            if v1=='TAHION':
                                                if nr_Tahioni5<3:
                                                    matrix_TA[5][i9]='TAHION'
                                                    nr_Tahioni5=nr_Tahioni5+1
                                                    nr_Tahioni7=nr_Tahioni7-1
                                                    matrix_TA[7][i9]='BAIE OZON'
                                                    nrBo7=nrBo7+1
                                                    nrBo5=nrBo5-1
                                                    break
                                            elif v1=='Frecv-CR':
                                                if nr_FrCr5<4:
                                                    matrix_TA[5][i9]='Frecv-CR'
                                                    nr_FrCr5=nr_FrCr5+1
                                                    nr_FrCr7=nr_FrCr7-1
                                                    matrix_TA[7][i9]='BAIE OZON'
                                                    nrBo7=nrBo7+1
                                                    nrBo5=nrBo5-1
                                                    break            
                                    if i10==7 and nrBo5>2:
                                        i12=0
                                        for i11 in matrix_TA[5]:
                                            if i11=='BAIE OZON' and nrBo5>2:
                                                if matrix_TA[8][i12]=='----':
                                                    matrix_TA[8][i12]='BAIE OZON'
                                                else:
                                                    matrix_TA[4][i12]='BAIE OZON'    
                                                matrix_TA[5][i12]='-'
                                                nrBo5=nrBo5-1
                                                if nrBo5==2:
                                                    break
                                            i12=i12+1

                                    i9=i9+1    


                        ##sfarsit113 cod pt a cobori din linia 5 daca sunt mai multe
                        ##inceput113 cod pt a cobori din linia 5 daca sunt mai multe
                        for i10 in range(8): #7 este ales aleator
                            if nrSa5>2:
                                i9=0
                                for i7 in matrix_TA[5]:
                                    if i7=='SAUNA':
                                        if nrSa6<2:
                                            v1=matrix_TA[6][i9]
                                            if v1=='TAHION':
                                                if nr_Tahioni5<3:
                                                    matrix_TA[5][i9]='TAHION'
                                                    nr_Tahioni5=nr_Tahioni5+1
                                                    nr_Tahioni6=nr_Tahioni6-1
                                                    matrix_TA[6][i9]='SAUNA'
                                                    nrSa6=nrSa6+1
                                                    nrSa5=nrSa5-1
                                                    break
                                            elif v1=='Frecv-CR':
                                                if nr_FrCr5<4:
                                                    matrix_TA[5][i9]='Frecv-CR'
                                                    nr_FrCr5=nr_FrCr5+1
                                                    nr_FrCr6=nr_FrCr6-1
                                                    matrix_TA[6][i9]='SAUNA'
                                                    nrSa6=nrSa6+1
                                                    nrSa5=nrSa5-1
                                                    break        

                                        elif nrSa7<2:
                                            v1=matrix_TA[7][i9]
                                            if v1=='TAHION':
                                                if nr_Tahioni5<3:
                                                    matrix_TA[5][i9]='TAHION'
                                                    nr_Tahioni5=nr_Tahioni5+1
                                                    nr_Tahioni7=nr_Tahioni7-1
                                                    matrix_TA[7][i9]='SAUNA'
                                                    nrSa7=nrSa7+1
                                                    nrSa5=nrSa5-1
                                                    break
                                            elif v1=='Frecv-CR':
                                                if nr_FrCr5<4:
                                                    matrix_TA[5][i9]='Frecv-CR'
                                                    nr_FrCr5=nr_FrCr5+1
                                                    nr_FrCr7=nr_FrCr7-1
                                                    matrix_TA[7][i9]='SAUNA'
                                                    nrSa7=nrSa7+1
                                                    nrSa5=nrSa5-1
                                                    break            
                                    if i10==7 and nrSa5>2:
                                        i12=0
                                        for i11 in matrix_TA[5]:
                                            if i11=='SAUNA' and nrSa5>2:
                                                if matrix_TA[8][i12]=='----':
                                                    matrix_TA[8][i12]='SAUNA'
                                                else:
                                                    matrix_TA[4][i12]='SAUNA'    
                                                matrix_TA[5][i12]='-'
                                                nrSa5=nrSa5-1
                                                if nrSa5==2:
                                                    break
                                            i12=i12+1

                                    i9=i9+1    


                        ##sfarsit113 cod pt a cobori din linia 5 daca sunt mai multe
                        ##inceput cod44 numar terapeutii alocati pt Aa la Fr-Cr Tahion Ozon si Sauna
                        for i7 in range(nr_pacienti_p_si_aP,nr_pacienti):
                            pass 

                        ##inceput cod44 numar terapeutii alocati pt Aa la Fr-Cr Tahion Ozon si Sauna
                        
                        araytp5=[]
                        araytp6=[]
                        araytp7=[]
                        araytp8=[]
                        for i8 in range(5,9):
                            for i7 in range(nr_pacienti_p_si_aP,nr_pacienti):
                                if matrix_TA[i8][i7]!='-' and matrix_TA[i8][i7][0]!='--' and matrix_TA[i8][i7]!='---' and matrix_TA[i8][i7]!='----':
                                    if (matrix_TA[i8][i7].split("-")[0])=='BAIE OZON':
                                        if i8==5:
                                            araytp5.append(matrix_TA[i8][i7].split("-")[1])
                                        elif i8==6:
                                            araytp6.append(matrix_TA[i8][i7].split("-")[1])
                                        elif i8==7:
                                            araytp7.append(matrix_TA[i8][i7].split("-")[1])        
                                        elif i8==8:
                                            araytp8.append(matrix_TA[i8][i7].split("-")[1])    
                                    if (matrix_TA[i8][i7].split("-")[0])=='SAUNA':
                                        if i8==5:
                                            araytp5.append(matrix_TA[i8][i7].split("-")[1])
                                        elif i8==6:
                                            araytp6.append(matrix_TA[i8][i7].split("-")[1])
                                        elif i8==7:
                                            araytp7.append(matrix_TA[i8][i7].split("-")[1])        
                                        elif i8==8:
                                            araytp8.append(matrix_TA[i8][i7].split("-")[1])    
                                    if (matrix_TA[i8][i7].split("-")[0])=='TAHION':
                                        if i8==5:
                                            araytp5.append(matrix_TA[i8][i7].split("-")[1])
                                        elif i8==6:
                                            araytp6.append(matrix_TA[i8][i7].split("-")[1])
                                        elif i8==7:
                                            araytp7.append(matrix_TA[i8][i7].split("-")[1])        
                                        elif i8==8:
                                            araytp8.append(matrix_TA[i8][i7].split("-")[1])    
                                    if (matrix_TA[i8][i7].split("-")[0])=='Frecv':
                                        if i8==5:
                                            araytp5.append(matrix_TA[i8][i7].split("-")[2])
                                        elif i8==6:
                                            araytp6.append(matrix_TA[i8][i7].split("-")[2])
                                        elif i8==7:
                                            araytp7.append(matrix_TA[i8][i7].split("-")[2])        
                                        elif i8==8:
                                            araytp8.append(matrix_TA[i8][i7].split("-")[2])    
                        ##inceput cod44 numar terapeutii alocati pt Aa la Fr-Cr Tahion Ozon si Sauna
                        ##
                        ar_idx_verificati1=[]
                        ar_idx_verificati_only1=[]
                        ar_Pp1=[] #este arrayul cu terapiile Pp daca se gasesc care vor figura in orar_p (deci este f important!!)
                        
                        for i7 in range(nr_pacienti_p):
                            ar_idx_verificati1.append(50)
                            ar_Pp1.append(50)
                        i9=0    
                        for i7 in range(nr_pacienti_p):
                            if matrix_TA[5][i7]=='BAIE OZON':
                                ar_Pp1[i7]='BAIE OZON'
                            elif matrix_TA[6][i7]=='BAIE OZON':
                                ar_Pp1[i7]='BAIE OZON'
                            elif matrix_TA[7][i7]=='BAIE OZON':
                                ar_Pp1[i7]='BAIE OZON'
                            elif matrix_TA[5][i7]=='SAUNA':
                                ar_Pp1[i7]='SAUNA'
                            elif matrix_TA[6][i7]=='SAUNA':
                                ar_Pp1[i7]='SAUNA'                    
                            elif matrix_TA[7][i7]=='SAUNA':
                                ar_Pp1[i7]='SAUNA' 
                        ##



                        ##inceput cod137 aloc terapeuti pt toti Pp si Pa din liniile 5,6,7,8 pt OZON si SAUNA
                        for i7 in range(4,9):#acestea sunt liniile: matrix_TA[4],matrix_TA[5],matrix_TA[6],matrix_TA[7],matrix_TA[8]
                            for i8 in range(nr_pacienti_p_si_aP):
                                if i7==4:
                                    if matrix_TA[4][i8]=='BAIE OZON' or matrix_TA[4][i8]=='SAUNA':
                                        if len(ter_dim)>0:
                                            matrix_TA[4][i8]=matrix_TA[4][i8]+'-'+ter_dim[0]
                                        else:
                                            matrix_TA[4][i8]=matrix_TA[4][i8]+'-'+'fara terapeut'
                                if i7>4 and i7<7:
                                    if matrix_TA[i7][i8]!='-' and matrix_TA[i7][i8]!='--' and matrix_TA[i7][i8]!='---' and matrix_TA[i7][i8]!='----':
                                        v1=0
                                        if len(ter_dup)>0:
                                            for i9 in ter_dup:
                                                if i7==5:
                                                    if i9 in TIAa5:
                                                        if araytp5.count(i9)<2:
                                                            terapeutul=i9
                                                            araytp5.append(i9)
                                                            v1=1
                                                            break
                                                    elif i9 not in TIAa5:
                                                        if araytp5.count(i9)<6:
                                                            terapeutul=i9
                                                            araytp5.append(i9)
                                                            v1=1
                                                            break
                                                if i7==6:
                                                    if i9 in TIAa6:
                                                        if araytp6.count(i9)<2:
                                                            terapeutul=i9
                                                            araytp6.append(i9)
                                                            v1=1
                                                            break
                                                    elif i9 not in TIAa6:
                                                        if araytp6.count(i9)<6:
                                                            terapeutul=i9
                                                            araytp6.append(i9)
                                                            v1=1
                                                            break        
                                        if v1==0:
                                            if len(ter_toti)>0:
                                                for i9 in ter_toti:
                                                    if i7==5:
                                                        if i9 in TIAa5:
                                                            if araytp5.count(i9)<2:
                                                                terapeutul=i9
                                                                araytp5.append(i9)
                                                                v1=1
                                                                break
                                                        elif i9 not in TIAa5:
                                                            if araytp5.count(i9)<6:
                                                                terapeutul=i9
                                                                araytp5.append(i9)
                                                                v1=1
                                                                break
                                                    if i7==6:
                                                        if i9 in TIAa6:
                                                            if araytp6.count(i9)<2:
                                                                terapeutul=i9
                                                                araytp6.append(i9)
                                                                v1=1
                                                                break
                                                        elif i9 not in TIAa6:
                                                            if araytp6.count(i9)<6:
                                                                terapeutul=i9
                                                                araytp6.append(i9)
                                                                v1=1
                                                                break                    
                                        if v1==0:
                                            terapeutul='fara terapeut'
                                        matrix_TA[i7][i8]=matrix_TA[i7][i8]+'-'+terapeutul

                                if i7>6 and i7<9:
                                    if matrix_TA[i7][i8]!='-' and matrix_TA[i7][i8]!='--' and matrix_TA[i7][i8]!='---' and matrix_TA[i7][i8]!='----':
                                        v1=0
                                        if len(ter_dup)>0:
                                            for i9 in ter_dup:
                                                if i7==7:
                                                    if i9 in TIAa7:
                                                        if araytp7.count(i9)<2:
                                                            terapeutul=i9
                                                            araytp7.append(i9)
                                                            v1=1
                                                            break
                                                    elif i9 not in TIAa7:
                                                        if araytp7.count(i9)<6:
                                                            terapeutul=i9
                                                            araytp7.append(i9)
                                                            v1=1
                                                            break
                                                if i7==8:
                                                    if i9 in TIAa8:
                                                        if araytp8.count(i9)<2:
                                                            terapeutul=i9
                                                            araytp8.append(i9)
                                                            v1=1
                                                            break
                                                    elif i9 not in TIAa8:
                                                        if araytp8.count(i9)<6:
                                                            terapeutul=i9
                                                            araytp8.append(i9)
                                                            v1=1
                                                            break        
                                                           
                                        if v1==0:
                                            terapeutul='fara terapeut'
                                        matrix_TA[i7][i8]=matrix_TA[i7][i8]+'-'+terapeutul                                    



                        ##sfarsit cod137 aloc terapeuti pt toti Pp si Pa din liniile 5,6,7,8 pt OZON si SAUNA
                    #####inceput134 cod pt a pune in row.individuala_da istoria TI. 

                    if nr_zi1!=6 and nr_zi1!=7:
                        i7=0
                        for row in pacienti_all: # pun in arrayul array_pacienti toti pacientii din data respectiva
                            if row.p_or_a=='pacient':
                                array_TI=[]
                                array_TI1=[]
                                last_array=[]
                                last_array1=0
                                if row.individuala_da==None:
                                    array_TI1.append(delta_data_min)
                                    #array_TI1.append(['PSIHOTERAPIE INDIVIDUALA'])
                                    ar_buffer=[]
                                    ar_buffer.append(ar_Pp[i7])
                                    array_TI1.append(ar_buffer)
                                    array_TI.append(array_TI1)

                                else:
                                    array_TI1.append(delta_data_min)
                                    last_array = eval(row.individuala_da[-1])
                                    #last_array1=type(last_array)
                                    array_TI1.append(last_array[1])
                                    
                                    #array_TI1[1].append('SHIRODHARA (OLEATIE CAP)')
                                    array_TI1[1].append(ar_Pp[i7])
                                    array_TI = row.individuala_da

                                    array_TI.append(array_TI1)                       
                                row.update_record(individuala_da=array_TI)
                                #row.update_record(individuala_da=None)
                                i7=i7+1
                    #####sfarsit134 cod  pune in row.individuala_da istoria TI.
                    
                    ##inceput cod1112 pt a o pune Sambata doar BO daca am maxim 6 pacienti care fac terapiile de weekend
                    
                    if nr_zi1==6:

                        pune_sambata_bo=0
                        contor=0
                        amb=0
                        for i1 in range(5,8):
                            i8=0                            
                            for i2 in matrix_TA[i1]:
                                if len(i2)>5:
                                    if i2[0]+i2[1]+i2[2]+i2[3]=='BAIE' or i2[0]+i2[1]+i2[2]+i2[3]=='SAUN':
                                        contor=contor+1 
                                        
                                if i8 in range(nr_pacienti_p_si_aP,nr_pacienti):
                                    if len(i2)>5:
                                        if i2[0]+i2[1]+i2[2]+i2[3]=='SAUN':         
                                            amb+=1
                                            break
                                i8+=1
                        if contor<7 and amb==0:    
                            pune_sambata1 = pune_sambata(matrix_TA,array_datele_orar_p,nr_pacienti) #apeleaza functia pune_Oana careia ii trimite argumentul matrix_TA
                            matrix_TA=pune_sambata1['matrix_TA1']
                            pune_sambata_bo=1
                    ##sfarsit cod1112 pt a o pune Sambata BO daca am maxim 6 pacienti care fac terapiile de weekend
                    
                    ##inceput cod1113 pt a o pune Duminica doar SAUNA daca am maxim 6 pacienti care fac terapiile de weekend
                    pune_duminica_sa=0
                    if nr_zi1==7:
                        contor=0
                        amb=0
                        for i1 in range(5,8):
                            i8=0                            
                            for i2 in matrix_TA[i1]:
                                if len(i2)>5:
                                    if i2[0]+i2[1]+i2[2]+i2[3]=='BAIE' or i2[0]+i2[1]+i2[2]+i2[3]=='SAUN':
                                        contor=contor+1 
                                        
                                if i8 in range(nr_pacienti_p_si_aP,nr_pacienti):
                                    if len(i2)>5:
                                        if i2[0]+i2[1]+i2[2]+i2[3]=='BAIE':         
                                            amb+=1
                                            break
                                i8+=1
                        if contor<7 and amb==0 and pune_sambata_bo==1:    
                            pune_duminica1 = pune_duminica(matrix_TA,array_datele_orar_p,nr_pacienti) #apeleaza functia pune_Oana careia ii trimite argumentul matrix_TA
                            matrix_TA=pune_duminica1['matrix_TA1']
                            pune_duminica_sa=1
                    ##sfarsit cod1112 pt a o pune Sambata BO daca am maxim 6 pacienti care fac terapiile de weekend 

                    

                    
                    if nr_zi1==6 or nr_zi1==7:
                        i7=0
                        for row in pacienti_all: # pun in arrayul array_pacienti toti pacientii din data respectiva
                            if row.p_or_a=='pacient':
                                array_TI=[]
                                array_TI1=[]
                                last_array=[]
                                last_array1=0
                                if row.degrup_da==None:
                                    array_TI1.append(delta_data_min)
                                    #array_TI1.append(['PSIHOTERAPIE INDIVIDUALA'])
                                    ar_buffer=[]
                                    if pune_sambata_bo==0:
                                        ar_buffer.append(ar_Pp1[i7])
                                    if pune_sambata_bo==1 and nr_zi1==6:
                                        ar_buffer.append("BAIE OZON")
                                    array_TI1.append(ar_buffer)
                                    array_TI.append(array_TI1)

                                else:
                                    array_TI1.append(delta_data_min)
                                    last_array = eval(row.degrup_da[-1])
                                    #last_array1=type(last_array)
                                    array_TI1.append(last_array[1])
                                    
                                    #array_TI1[1].append('SHIRODHARA (OLEATIE CAP)')
                                    if pune_sambata_bo==0:
                                        array_TI1[1].append(ar_Pp1[i7])
                                    if pune_sambata_bo==1 and nr_zi1==6:
                                        array_TI1[1].append('BAIE OZON')    
                                    array_TI = row.degrup_da

                                    array_TI.append(array_TI1)                       
                                row.update_record(degrup_da=array_TI)
                                #row.update_record(degrup_da=None)
                                i7=i7+1
                    #####sfarsit134 cod pt a pune in row.degrup_da istoria TI. Deocamdata am copiat doar ce a fost in ziua precedenta la degrup_da. Urmeaza sa adaug TI din ziua aceasta.
                    
                    ##inceput cod111 pt a o pune pe Oana la Fr-Cr si Tahion Daca este prezenta
                    if ("Oana" in ter_dim)==True:
                        pune_Oana1 = pune_Oana(matrix_TA) #apeleaza functia pune_Oana careia ii trimite argumentul matrix_TA
                        matrix_TA=pune_Oana1['matrix_TA1']
                    ##sfarsit cod111 pt a o pune pe Oana la Fr-Cr si Tahion Daca este prezenta
                    
                    
                    
                    




                   
                    ################aici122 inceput se intoduc in toate liniile sablonului tot ce este in matrix_TA
                    i8=0
                    for i7 in matrix_TA[1]:
                        if i7=='VOCALE,RESPIRATII,CODUL V':
                            matrix_TA[1][i8]='-'
                        i8=i8+1    
                    for j77 in range(nr_pacienti):  #aici se intoduc in linia 1 a sablonului toti pacientii
                        zzzz= 'pacient_'+str(j77+1)
                        zzz = {'1':zzzz}
                        date_linia_6.update_record(**{zzz['1']:matrix_TA[0][j77]})
                        date_linia_7.update_record(**{zzz['1']:matrix_TA[1][j77]})
                        date_linia_8.update_record(**{zzz['1']:matrix_TA[2][j77]})
                        date_linia_9.update_record(**{zzz['1']:matrix_TA[3][j77]})
                        date_linia_10.update_record(**{zzz['1']:matrix_TA[4][j77]})
                        date_linia_12.update_record(**{zzz['1']:matrix_TA[5][j77]})
                        date_linia_14.update_record(**{zzz['1']:matrix_TA[6][j77]})
                        date_linia_16.update_record(**{zzz['1']:matrix_TA[7][j77]})
                        date_linia_18.update_record(**{zzz['1']:matrix_TA[8][j77]})

                    ###############aici122 sfarsit se intoduc in toate liniile sablonului tot ce este in matrix_TA

                    

                    ##inceput cod111 pt a pune terapiile de seara
                    for j in range(nr_pacienti):  
                        zzzz= 'pacient_'+str(j+1)
                        zzz = {'1':zzzz}
                        
                        jjj=0
                        var_tip_pacient='pacient'
                        var_ora_ambulatoriu=0
                        var_nr_ticameraseara=0

                        for jjj in range(3):
                            
                              

                            for row_p in pacienti_all:
                                ter_dup_primul=[]
                                if var_nr_ticameraseara<6:
                                    if len(ter_dup)>0:
                                        ter_dup_primul.append('-'+ter_dup[0])
                                    else:
                                        ter_dup_primul.append('-fara terapeut')    
                                elif var_nr_ticameraseara>=6 and var_nr_ticameraseara<12:
                                    if len(ter_dup)>1:
                                        ter_dup_primul.append('-'+ter_dup[1])
                                    else:
                                        ter_dup_primul.append('-fara terapeut')      
                                elif var_nr_ticameraseara>=12 and var_nr_ticameraseara<18:
                                    if len(ter_dup)>2:
                                        ter_dup_primul.append('-'+ter_dup[2]) 
                                    else:
                                        ter_dup_primul.append('-fara terapeut')
                                   

                                if row_p.p_or_a=='pacient' and jjj==0:
                                    
                                    ##inceput cod1 pt individ in camera
                                    if ('BAIE LOCALA' in row_p.individuala_camera)==True or ('CLISMA' in row_p.individuala_camera)==True or ('INHALATIE' in row_p.individuala_camera)==True or ('CATAPLASMA' in row_p.individuala_camera)==True or ('SUPOZITOR' in row_p.individuala_camera)==True:
                                        var_indiv_in_camera=row_p.individuala_camera+ter_dup_primul
                                        array_t_individuala.append(var_indiv_in_camera)
                                        var_nr_ticameraseara=var_nr_ticameraseara+1
                                    else:
                                        array_t_individuala.append('nu are terapii individuale')
                                    ##sfarsit cod1 pt individ in camera
                                    
                                if row_p.p_or_a=='ambulatoriu' and jjj==1 and (str(row_p.ora_in)=='7' and str(row_p.ora_out)=='23'):
                                        
                                    ##inceput cod2 pt individ in camera
                                    if ('BAIE LOCALA' in row_p.individuala_camera)==True or ('CLISMA' in row_p.individuala_camera)==True or ('INHALATIE' in row_p.individuala_camera)==True or ('CATAPLASMA' in row_p.individuala_camera)==True or ('SUPOZITOR' in row_p.individuala_camera)==True:
                                        var_indiv_in_camera=row_p.individuala_camera+ter_dup_primul
                                        array_t_individuala.append(var_indiv_in_camera)
                                        var_nr_ticameraseara=var_nr_ticameraseara+1
                                    else:    
                                        array_t_individuala.append('--')
                                    ##sfarsit cod2 pt individ in camera
                                    
                                if row_p.p_or_a=='ambulatoriu' and jjj==2 and (str(row_p.ora_in)!='7' or str(row_p.ora_out)!='23'):
                                    
                                    ##inceput cod2 pt individ in camera
                                    if ('BAIE LOCALA' in row_p.individuala_camera)==True or ('CLISMA' in row_p.individuala_camera)==True or ('INHALATIE' in row_p.individuala_camera)==True or ('CATAPLASMA' in row_p.individuala_camera)==True or ('SUPOZITOR' in row_p.individuala_camera)==True:
                                        var_indiv_in_camera=row_p.individuala_camera+ter_dup_primul
                                        array_t_individuala.append(var_indiv_in_camera)
                                        var_nr_ticameraseara=var_nr_ticameraseara+1
                                    else:    
                                        array_t_individuala.append('--')
                                    ##sfarsit cod2 pt individ in camera
                                    
                            var_ora_ambulatoriu=1
                            jjj=jjj+1 
                                
                        
                        ##inceput cod3 pt individ in camera
                        if type(array_t_individuala[j])!=str: #verific daca elementul din array este un string(nu are terapii individuale sau este un nou array['CLISMA','SUPOZITOR'])
                            date_linia_21.update_record(**{zzz['1']:', '.join(array_t_individuala[j])})
                        else:
                            date_linia_21.update_record(**{zzz['1']:array_t_individuala[j]})
                        
                        
                        #j=j+1
                    ##sfarsit cod111 pt a pune terapiile de seara    


                    
                else:
                    matrix_A=[]
                    matrix_A=np.array(matrix_A)    
                    matrix_TA=matrix_A.transpose()
            else:
                matrix_A=[]
                matrix_A=np.array(matrix_A)    
                matrix_TA=matrix_A.transpose()
            #if i==6:
                #break    

            del array_datele_orar_p[:]
            
            del array_yogaterapeutica[:]
            del array_codv[:]
            del array_t_individuala[:]
            i=i+1
            ###########sfarsit cod pt linia 6-saptamana curenta -Yoga Terapeutica
           
    redirect(URL('default','orar'))    
    





#########################inceput cod 12345:  se face grid-ul cu orarul pe data curenta  din tabela orar dataa 
    querry_orar_o_zi = db.orar.dataa == dataa
    fields_orar = [db.orar.dataa,db.orar.ora,db.orar.info_generale,db.orar.pacient_1,db.orar.pacient_2,db.orar.pacient_3,db.orar.pacient_4,db.orar.pacient_5,db.orar.pacient_6,db.orar.pacient_7,db.orar.pacient_8,db.orar.pacient_9,db.orar.pacient_10,db.orar.pacient_11,db.orar.pacient_12,db.orar.pacient_13,db.orar.pacient_14,db.orar.pacient_15,db.orar.pacient_16,db.orar.pacient_17,db.orar.pacient_18,db.orar.pacient_19,db.orar.pacient_20]

   
    header_or ={'orar.dataa':'Data astazi','orar.ora':'Ora si Data','orar.pacient_1' : 'Pacient_______________________________1','orar.pacient_2' : 'Pacient 2________________________________','orar.pacient_3' : 'Pacient 3________________________________','orar.pacient_4' : 'Pacient 4________________________________','orar.pacient_5' : 'Pacient 5________________________________','orar.pacient_6' : 'Pacient 6________________________________','orar.pacient_7' : 'Pacient 7_________________________________','orar.pacient_8' : 'Pacient 8________________________________','orar.pacient_9' : 'Pacient 9________________________________','orar.pacient_10' : 'Pacient 10________________________________','orar.pacient_11' : 'Pacient 11________________________________','orar.pacient_12' : 'Pacient 12________________________________','orar.pacient_13' : 'Pacient 13________________________________','orar.pacient_14' : 'Pacient14________________________________','orar.pacient_15' : 'Pacient 15________________________________','orar.pacient_16' : 'Pacient 16________________________________','orar.pacient_17' : 'Pacient 17________________________________','orar.pacient_18' : 'Pacient 18________________________________','orar.pacient_19' : 'Pacient 19________________________________','orar.pacient_20' : 'Pacient 20________________________________'}
    maxtextlengths_1 = {'orar.pacient_1':70,'orar.pacient_2':70,'orar.pacient_3':70,'orar.pacient_4':70,'orar.pacient_5':70,'orar.pacient_6':70,'orar.pacient_7':70,'orar.pacient_8':70,'orar.pacient_9':70,'orar.pacient_10':70,'orar.pacient_11':70,'orar.pacient_12':70,'orar.pacient_13':70,'orar.pacient_14':70,'orar.pacient_15':70,'orar.pacient_16':70,'orar.pacient_17':70,'orar.pacient_18':70,'orar.pacient_19':70,'orar.pacient_20':70} 
    grid_orar = SQLFORM.grid(querry_orar_o_zi,maxtextlengths=maxtextlengths_1,fields=fields_orar,headers=header_or,user_signature=False,csv=False,paginate=30,create=False,searchable=False,sortable=False,editable=False,deletable=False,details=False)
######################sfarsit cod 12345:  s-a facut grid-ul cu orarul pe data curenta din tabela orar dataa    
    
    return locals()

def orar1():
    data_azi = datetime.datetime.now().strftime("%d-%m-%Y") #este doar pt a imi afisa in View. Nu o folosesc in calcule 15-08-2020
    zile_sapt = {"Monday": 1,"Tuesday": 2,"Wednesday": 3,"Thursday": 4,"Friday": 5,"Saturday": 6,"Sunday": 7}
    #dataa = datetime.datetime.now().date() #aceasta o sa o folosesc in calcule
    dataa = datetime.date(2020, 8, 15) # subtitui dataa de mai sus cu aceasta pt teste
    nr_zi = (zile_sapt[dataa.strftime("%A")]) # aici imi da un integer a cata zi din saptamana este (in cazul nostru 6). Deci urmeaza sa generez programul pe 2 zile
    nr_copii_sablon = 8-nr_zi
    delta2= (dataa+datetime.timedelta(days=nr_copii_sablon-1)) # aceasta este ultima data (Duminica) ce va fi introdusa in tabela orar adica in exemplul nostru: 2020-08-16
    este_generat1 = db(db.orar).select(db.orar.dataa.max())[0] # aceste 2 linii imi dau data maxima din tabela orar
    este_generat = este_generat1['_extra']['MAX("orar"."dataa")'] # aceasta este data maxima din tabela orar
    nr_rec = db((db.orar.id>0)).count() # numarul de inregistrari din tabela orar
    data_sf = (db(db.orar_t).select().last()).dataa #aceasta este data ultima introdusa din programul terapeutilor pt a vedea pana la ce data pot genera orarul
    if data_sf>=delta2: #verific daca au fost introduse orarele terapeutilor si daca nu dau mesaj ca trebuie introduse acestea mai intai si abia apoi pot genera sabloanele
        if nr_rec == 0 or este_generat<=dataa: # verifica daca data maxima din orar este mai mica decat data curenta si atunci introduce maxim 7 sabloane
            response.flash = T("Am generat sabloanele pentru %s zile")%(nr_copii_sablon)
            row_sablon = db(db.orar_sablon).select()
            i=0
            delta1= (dataa+datetime.timedelta(days=i))
            while i<nr_copii_sablon: # aici am introdus 2 copii in orar
                for row_s in row_sablon:
                    db.orar.insert(**db.orar._filter_fields(row_s))
                    row_s.update_record(dataa=delta1)
                i=i+1
                delta1= (dataa+datetime.timedelta(days=i))
        else:
            response.flash = T("Sabloanele au fost deja generate!") 
    else:
        response.flash = T("Introdu mai intai orarul terapeutilor!")
########################################################################################### PANA aici am introdus cele maxim 7 sabloane pe saptamana in curs (deocamdata 2 pt ca am inceput Sambata)
    
    querry_orar_o_zi = db.orar.dataa == dataa
    fields_orar = [db.orar.dataa,db.orar.ora,db.orar.info_generale,db.orar.pacient_1,db.orar.pacient_2,db.orar.pacient_3,db.orar.pacient_4,db.orar.pacient_5,db.orar.pacient_6,db.orar.pacient_7,db.orar.pacient_8,db.orar.pacient_9,db.orar.pacient_10,db.orar.pacient_11,db.orar.pacient_12,db.orar.pacient_13,db.orar.pacient_14,db.orar.pacient_15,db.orar.pacient_16,db.orar.pacient_17,db.orar.pacient_18,db.orar.pacient_19,db.orar.pacient_20]

   
    header_or ={'orar.dataa':'Data astazi','orar.ora':'Ora si Data','orar.pacient_1' : 'Pacient_______________________________1','orar.pacient_2' : 'Pacient 2________________________________','orar.pacient_3' : 'Pacient 3________________________________','orar.pacient_4' : 'Pacient 4________________________________','orar.pacient_5' : 'Pacient 5________________________________','orar.pacient_6' : 'Pacient 6________________________________','orar.pacient_7' : 'Pacient 7________________________________','orar.pacient_8' : 'Pacient 8________________________________','orar.pacient_9' : 'Pacient 9________________________________','orar.pacient_10' : 'Pacient 10________________________________','orar.pacient_11' : 'Pacient 11________________________________','orar.pacient_12' : 'Pacient 12________________________________','orar.pacient_13' : 'Pacient 13________________________________','orar.pacient_14' : 'Pacient14________________________________','orar.pacient_15' : 'Pacient 15________________________________','orar.pacient_16' : 'Pacient 16________________________________','orar.pacient_17' : 'Pacient 17________________________________','orar.pacient_18' : 'Pacient 18________________________________','orar.pacient_19' : 'Pacient 19________________________________','orar.pacient_20' : 'Pacient 20________________________________'}
    grid_orar = SQLFORM.grid(querry_orar_o_zi,fields=fields_orar,headers=header_or,user_signature=False,csv=False,paginate=30,create=False,searchable=False,sortable=False,editable=False,deletable=False,details=False)
    
    
    data_sf = (db(db.orar_t).select().last()).dataa #aceasta este data ultima introdusa din programul terapeutilor pt a vedea pana la ce data pot genera orarul
    ver_int = db(db.orar_p.dataa==dataa).count()
    datele=[]
    if ver_int == 0:
        row_pacienti = db(db.pacienti.inceput_tt == dataa).select()
        for row in row_pacienti:
            db.orar_p.insert(dataa=row.inceput_tt,pacient=row.nume,pacient_id=row.id,camere=row.camere,terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,terapii_nu=row.terapii_necesare,cicluri=0,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out)



    grid = SQLFORM.grid(db.orar_p,user_signature=False,csv=False)
    form = SQLFORM.factory(Field('dataa','date',format=('%Y-%m-%d'),label='Data:'),Field('question', requires=IS_NOT_EMPTY()))
    fields_orar_sablon = [db.orar_sablon.dataa,db.orar_sablon.ora,db.orar_sablon.info_generale,db.orar_sablon.pacient_1,db.orar_sablon.pacient_2,db.orar_sablon.pacient_3,db.orar_sablon.pacient_4,db.orar_sablon.pacient_5,db.orar_sablon.pacient_6,db.orar_sablon.pacient_7,db.orar_sablon.pacient_8,db.orar_sablon.pacient_9,db.orar_sablon.pacient_10,db.orar_sablon.pacient_11,db.orar_sablon.pacient_12,db.orar_sablon.pacient_13,db.orar_sablon.pacient_14,db.orar_sablon.pacient_15,db.orar_sablon.pacient_16,db.orar_sablon.pacient_17,db.orar_sablon.pacient_18,db.orar_sablon.pacient_19,db.orar_sablon.pacient_20]

    header_o ={'orar_sablon.dataa':'Data astazi','orar_sablon.ora':'Ora si Data','orar_sablon.pacient_1' : 'Pacient_______________________________1','orar_sablon.pacient_2' : 'Pacient 2________________________________','orar_sablon.pacient_3' : 'Pacient 3________________________________','orar_sablon.pacient_4' : 'Pacient 4________________________________','orar_sablon.pacient_5' : 'Pacient 5________________________________','orar_sablon.pacient_6' : 'Pacient 6________________________________','orar_sablon.pacient_7' : 'Pacient 7________________________________','orar_sablon.pacient_8' : 'Pacient 8________________________________','orar_sablon.pacient_9' : 'Pacient 9________________________________','orar_sablon.pacient_10' : 'Pacient 10________________________________','orar_sablon.pacient_11' : 'Pacient 11________________________________','orar_sablon.pacient_12' : 'Pacient 12________________________________','orar_sablon.pacient_13' : 'Pacient 13________________________________','orar_sablon.pacient_14' : 'Pacient14________________________________','orar_sablon.pacient_15' : 'Pacient 15________________________________','orar_sablon.pacient_16' : 'Pacient 16________________________________','orar_sablon.pacient_17' : 'Pacient 17________________________________','orar_sablon.pacient_18' : 'Pacient 18________________________________','orar_sablon.pacient_19' : 'Pacient 19________________________________','orar_sablon.pacient_20' : 'Pacient 20________________________________'}    
    grid1 = SQLFORM.grid(db.orar_sablon,headers= header_o,fields = fields_orar_sablon,maxtextlengths={'orar_sablon.ora':30,'orar_sablon.info_generale':36,'orar_sablon.pacient_1':50},user_signature=False,csv=True,paginate=30,create=False,searchable=False)
    #form.element('textarea[_name=question]')['_style'] = 'width:150px;height:50px;'
    return locals()




def index():
    redirect(URL('default','orar'))
    grid = SQLFORM.grid(db.terapii,fields=[db.terapii.nume,db.terapii.tip,db.terapii.durata,db.terapii.cuplaj_cu,db.terapii.posibil_inainte_de,db.terapii.imposibil_inainte_de,db.terapii.posibil_dupa,db.terapii.imposibil_dupa,db.terapii.simultan_maxim,db.terapii.cand_se_poate,db.terapii.pauza_aceeasi_terapie,db.terapii.interval_inceput_ora,db.terapii.interval_inceput_minut,db.terapii.interval_sfarsit_ora,db.terapii.interval_sfarsit_minut,db.terapii.mai_multe_intervale,db.terapii.interval2_inceput_ora,db.terapii.interval2_inceput_minut,db.terapii.interval2_sfarsit_ora,db.terapii.interval2_sfarsit_minut,db.terapii.interval3_inceput_ora,db.terapii.interval3_inceput_minut,db.terapii.interval3_sfarsit_ora,db.terapii.interval3_sfarsit_minut,db.terapii.cine_face,db.terapii.cine_nu_face,db.terapii.weekend,db.terapii.Obs],user_signature=False,paginate=8,csv=False)
    
    return locals()

def terapii():
    
    grid = SQLFORM.grid(db.terapii,user_signature=False,paginate=8,csv=False)
    
    return locals()



def terapeuti():
    
    grid = SQLFORM.grid(db.terapeuti,fields=[db.terapeuti.nume,db.terapeuti.ce_terapii_face,db.terapeuti.ce_terapii_nu_face],maxtextlengths={'terapeuti.ce_terapii_face':400,'terapeuti.ce_terapii_nu_face':400},user_signature=False,paginate=10,csv=False)
    return locals()

def camere():
# grid = SQLFORM.grid(db.camere,headers={'camere.camera':'Camera','camere.pat':'Pat','camere.nr_maxim_locuri':'Nr maxim locuri','camere.nr_paturi_simple':'Nr paturi simple','camere.nr_paturi_duble':'Nr paturi #duble'},user_signature=False,paginate=10,csv=False)
    grid = SQLFORM.grid(db.camere,fields=[db.camere.camera,db.camere.pat,db.camere.max_locuri,db.camere.nr_paturi_simple,db.camere.nr_paturi_duble],user_signature=False,paginate=10,csv=False)
    
    return locals()


def ver_data(form): #in aceasta functie pot pune orice fel de conditii inainte de a valida un add record 
    id = form.vars.id
    inceput_tt = form.vars.inceput_tt
    sfarsit_tt = form.vars.sfarsit_tt
    cameree = form.vars.camere
    if inceput_tt>sfarsit_tt or camere == None or cameree==27:
        form.errors= True
    else:
        form.errors= False

def ver_data1(form): #in aceasta functie pot pune orice fel de conditii inainte de a valida un add record. aici la ambulatoriu verifica sa fie data de intrare= cu cea de iesire 
    id = form.vars.id

    inceput_tt = form.vars.inceput_tt
    sfarsit_tt = form.vars.sfarsit_tt
    
    #cameree = lambda form.vars.camere,r:'%s' % (r.camere.camera)
    cameree = form.vars.camere # pt camera 0-0 vine un integer 27
    if inceput_tt!=sfarsit_tt or camere == None or cameree!=27:
        form.errors= True
    else:
        form.errors= False
    


def xx(form): # aceasta functie se apeleaza cand sunt erori in formularul de completare. Aceasta functie se apeleaza si din  fct ver_data fiind apelata : form.errors= True
    response.flash = 'Eroare. Completeaza corect! '

def do_something(form): # de la pacienti vine aici si x=1
    id = form.vars.id
    camera1=form.vars.camere
    if camera1==None:
        db(db.pacienti.id == id).delete()
        session.flash = 'Introdu camera'
        redirect(URL('default','pacienti'))
    
    nume = form.vars.nume
    row = db(db.pacienti.id == id).select().first() # linia cu pacientul respectiv care a intrat deja in tabela
    session.flash = 'Reusit!'
    db.orar_p.insert(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,camere=row.camere)
    
    p_or_a = row.p_or_a
    
    if p_or_a=='pacient':
        x=1
        xupd=1
        redirect(URL('default','ad_terapii',vars=dict(id=id,xupd=xupd,nume=nume,x=x))) #,p_or_a=p_or_a))
    else:
        x=2
        xupd=2
        redirect(URL('default','ad_terapii',vars=dict(id=id,xupd=xupd,nume=nume,x=x))) #,p_or_a=p_or_a))
    
def do_something1(form): #de la ambulatoriu vine aici si x=2
    id = form.vars.id
    camera1=form.vars.camere
    if camera1==None:
        db(db.pacienti.id == id).delete()
        session.flash = 'Introdu camera'
        redirect(URL('default','ambulatoriu'))
    row = db(db.pacienti.id == id).select().first() # linia cu pacientul respectiv care a intrat deja in tabela
    session.flash = 'Reusit!'
    
    nume = form.vars.nume
    db.orar_p.insert(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,camere=row.camere)
    ora_incepere = form.vars.ora_in
    ora_sfarsit = form.vars.ora_out
    #p_or_a = form.vars.p_or_a
    x=2
    xupd=2
    redirect(URL('default','ad_terapii',vars=dict(id=id,nume=nume,x=x,xupd=xupd,ora_incepere=ora_incepere,ora_sfarsit=ora_sfarsit)))

def do_something2(form): #de la ad_terapii
    
    session.flash = 'Reusit!'
    id = form.vars.id
    nume = form.vars.nume
    #p_or_a = form.vars.p_or_a
    x=2
    redirect(URL('default','ad_terapii',vars=dict(id=id,nume=nume,x=x)))

def do_something3(form): # de la pacienti vine aici si x=1
    
    session.flash = 'Reusit!'
    id = form.vars.id
    nume = form.vars.nume
    row = db(db.pacienti.id == id).select().first() # linia cu pacientul respectiv care a intrat deja in tabela
    p_or_a = row.p_or_a
    
    if p_or_a=='pacient':
        x=1
        xupd=3 
        
        #rowupdt=db(db.pacienti.id==int(y['id1'])).select().first()
        rowupdt1=db(db.orar_p.pacient_id==int(id)).select().first()
        rowupdt1.update_record(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,camere=row.camere)
        
        redirect(URL('default','ad_terapii',vars=dict(id=id,nume=nume,x=x,xupd=xupd))) #,p_or_a=p_or_a))
    else:
        x=2
        xupd=4
        redirect(URL('default','ad_terapii',vars=dict(id=id,nume=nume,x=x,xupd=xupd))) #,p_or_a=p_or_a))

def do_something4(form): #de la ambulatoriu vine aici si x=2
    
    session.flash = 'Reusit!'
    id = form.vars.id
    nume = form.vars.nume
    ora_incepere = form.vars.ora_in
    ora_sfarsit = form.vars.ora_out
    #p_or_a = form.vars.p_or_a
    x=2
    xupd=4
    row = db(db.pacienti.id == id).select().first() # linia cu pacientul respectiv care a intrat deja in tabela
    rowupdt1=db(db.orar_p.pacient_id==id).select().first()
    rowupdt1.update_record(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,camere=row.camere,
    ora_in=row.ora_in,ora_out=row.ora_out)
    
    redirect(URL('default','ad_terapii',vars=dict(id=id,nume=nume,x=x,xupd=xupd,ora_incepere=ora_incepere,ora_sfarsit=ora_sfarsit)))
        


def on_sterg(table,id):
    db(db.orar_p.pacient_id ==  id).delete()
    
    
def pacienti():
    
    db.pacienti.inceput_ss.writable = False
    db.pacienti.inceput_ss.readable = False
    db.pacienti.sfarsit_ss.writable = False
    db.pacienti.sfarsit_ss.readable = False
    db.pacienti.ora_in.writable = False
    db.pacienti.ora_in.readable = False
    db.pacienti.ora_out.writable = False
    db.pacienti.ora_out.readable = False
    db.pacienti.terapii_necesare.writable = False
    #db.pacienti.terapii_necesare.readable = False
    db.pacienti.terapii_importante.writable = False
    #db.pacienti.terapii_importante.readable = False
    db.pacienti.p_or_a.default = 'pacient'
    db.pacienti.p_or_a.writable = False
    #db.pacienti.p_or_a.readable = False
    #abc=1
    callback = lambda *args: redirect(URL('default','pacienti'))
    querry = db.pacienti.id.belongs([0])
   
    grid = SQLFORM.grid(db.pacienti,orderby=~db.pacienti.inceput_tt,fields = [db.pacienti.camere,db.pacienti.nume,db.pacienti.din_localitatea,db.pacienti.inceput_tt,db.pacienti.sfarsit_tt,db.pacienti.terapii_necesare,db.pacienti.terapii_importante,db.pacienti.p_or_a],oncreate=do_something,onfailure=xx,onupdate=do_something3,onvalidation=ver_data,ondelete=on_sterg, user_signature=False,paginate=10,csv=False,editable=True)
#     grid = SQLFORM.grid(db.pacienti, fields = #[db.pacienti.camere,db.pacienti.nume,db.pacienti.din_localitatea,db.pacienti.inceput_t,db.pacienti.sfarsit_t,db.pacienti.inceput_s,db.pacienti.sfarsit_s],user_signature=False,paginate=10,csv=False) #este cu inceput/sfarsit cazare
    
    return locals()

def ambulatoriu():
    db.pacienti.inceput_ss.writable = False
    db.pacienti.inceput_ss.readable = False
    db.pacienti.sfarsit_ss.writable = False
    db.pacienti.sfarsit_ss.readable = False
    db.pacienti.terapii_necesare.writable = False
    #db.pacienti.terapii_necesare.readable = False
    db.pacienti.terapii_importante.writable = False
    #db.pacienti.terapii_importante.readable = False
    db.pacienti.p_or_a.writable = False
    #db.pacienti.p_or_a.readable = False
    db.pacienti.p_or_a.default = 'ambulatoriu'
    
    #row = db(db.camere.select(camere.id==27))
    #cam=row.camera
    #db.pacienti.camere.default = db(db.pacienti.camere == 27).select().first().camere
    db.pacienti.camere.default = 27
    callback = lambda *args: redirect(URL('default','pacienti'))
    querry = db.pacienti.id.belongs([0])
   
    grid = SQLFORM.grid(db.pacienti.p_or_a=='ambulatoriu',orderby=~db.pacienti.inceput_tt,fields = [db.pacienti.camere,db.pacienti.nume,db.pacienti.din_localitatea,db.pacienti.inceput_tt,db.pacienti.sfarsit_tt,db.pacienti.terapii_necesare,db.pacienti.p_or_a],oncreate=do_something1,onfailure=xx,onupdate=do_something4,onvalidation=ver_data1,ondelete=on_sterg,user_signature=False,paginate=10,csv=False,editable=True)
#     grid = SQLFORM.grid(db.pacienti, fields = #[db.pacienti.camere,db.pacienti.nume,db.pacienti.din_localitatea,db.pacienti.inceput_t,db.pacienti.sfarsit_t,db.pacienti.inceput_s,db.pacienti.sfarsit_s],user_signature=False,paginate=10,csv=False) #este cu inceput/sfarsit cazare
    return locals()


def ad_terapii(): #adauga terapii pentru pacienti dar si pentru ambulatoriu iar din functia mm, ma trimite in ad_terapii2
    
    y = request.vars
    x=y['x']# x=1 daca este pacient
    xupd=int(y['xupd']) # xupd=3 daca este pacient si vreau modificare si NU creare (este pt update)
    if int(x)==2:
        ora_incepere=y['ora_incepere']
        ora_sfarsit=y['ora_sfarsit']
    else:
        ora_incepere='100'
        ora_sfarsit='100'
    rows=db(db.terapii).select()
    pacientul_in_cauza = db(db.pacienti.id==int(y['id'])).select().first()
    form1 = SQLFORM.grid(db.terapii,fields=[db.terapii.nume,db.terapii.tip],csv=False,paginate=50,create=False,deletable=False,searchable=False,editable=False,details=False,
    user_signature=False,selectable = [('Adauga terapii',lambda ids :  redirect(URL('default', 'mm', vars=dict(id=ids,id1 = y['id'],titlu1 = y['nume'],tip1=y['tip1'],
    x=x,xupd=xupd,ora_incepere=ora_incepere,ora_sfarsit=ora_sfarsit))))])
    
    if form1.elements('th'): #acest if imi da posibilitatea sa selectez tot(checkbox-urile): ALL
            form1.elements('th')[0].append(SPAN('All', BR(), INPUT(_type='checkbox',
    _onclick="jQuery('input:checkbox').not(this).prop('checked', this.checked);"
    )))
   
    #selectable = [('button label1', lambda...), ('button label2', lambda ...)]    
    
    return locals()

def ad_terapii2(): #este pt a adauga terapiile imortante dupa ce adaug terapiile
    
    y = request.vars
    xupd=int(y['xupd'])
    
    film_id=int(y['film_id'])
    
    #form = SQLFORM.grid(db.terapii,fields=[db.terapii.nume,db.terapii.tip],csv=False,paginate=50,create=False,deletable=False,searchable=False,editable=False,details=False,user_signature=False,selectable = [('Adauga terapii',lambda ids: redirect(URL('default', 'mm1', vars=dict(id=ids,id1 = y['id'],titlu1 = y['nume'],tip1=y['tip1']))))])
    #form = SQLFORM.grid(db.terapii,fields=[db.terapii.nume,db.terapii.tip],csv=False,paginate=50,create=False,deletable=False,searchable=False,editable=False,details=False,user_signature=False,selectable = [('Adauga terapii',lambda f, v: SQLFORM.widgets.radio.widget(f, v, style='divs'))])
    rows=db(db.terapii).select()
    pacientul_in_cauza = db(db.pacienti.id==film_id).select().first()
    ######## cod de protectie: cand nu se pune nici o terapie individuala dupa ce se adauga terapiile nu se mai duce sa adauge terapie importanta pt ca nu are=> si incheie: redirect(URL('default','pacienti'))
    terapiile_necesare = pacientul_in_cauza.terapii_necesare #terapiile necesare din tabela pacienti
    len_terapiile_necesare = len(terapiile_necesare) # lungimea liststringului terapii-necesare
    i11=0
    i12=0 
    tab_ter_necesare_individuala=[]
    
    for i11 in range(len_terapiile_necesare):
        terapia_necesara = terapiile_necesare[i11]
        tip_terapia_necesara_gasita = db(db.terapii.nume == terapia_necesara).select().first().tip
        if tip_terapia_necesara_gasita== 'individuala':
            i12=1
    if i12==0:#se duce aici daca nu are nici o terapie individuala
        if xupd==1 or xupd==2:
            row = db(db.pacienti).select().last() #in aceasta linie si in cea de mai jos copii in tabela orar_p pacientul cu datele lui
        if xupd==3 or xupd==4:
            row = db(db.pacienti.id==film_id).select().first()  
             
        ##########inceput cod:12345
        terapiile_necesare = row.terapii_necesare #terapiile necesare din tabela pacienti
        len_terapiile_necesare = len(terapiile_necesare) # lungimea liststringului terapii-necesare
        i=0
        tab_ter_necesare_individuala=[]
        tab_ter_necesare_degrup=[]
        tab_ter_necesare_degrupd=[]
        tab_ter_necesare_individuala_camera=[]
        for i in range(len_terapiile_necesare):
            terapia_necesara = terapiile_necesare[i]
            tip_terapia_necesara_gasita = db(db.terapii.nume == terapia_necesara).select().first().tip
            if tip_terapia_necesara_gasita== 'de grup d':
                tab_ter_necesare_degrupd.append(terapia_necesara)
            if tip_terapia_necesara_gasita== 'individuala':
                tab_ter_necesare_individuala.append(terapia_necesara)
            if tip_terapia_necesara_gasita== 'de grup':
                tab_ter_necesare_degrup.append(terapia_necesara)
            if tip_terapia_necesara_gasita== 'individuala in camera':
                tab_ter_necesare_individuala_camera.append(terapia_necesara)    
            i=i+1
        if xupd==1 or xupd==2:    
            db.orar_p.insert(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,
            camere=row.camere,terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
            individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,
            degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,individuala_camera=tab_ter_necesare_individuala_camera)
            #redirect(URL('default', 'ad_actor',vars=dict(id1=film_id,xx=xx,titlu1=film_titlu,row1=row)))
            ##########sfarsit cod:12345
            
        if xupd==3 or xupd==4: 
            #rowupdt=db(db.pacienti.id==int(y['id1'])).select().first()
            rowupdt1=db(db.orar_p.pacient_id==film_id).select().first()
            rowupdt1.update_record(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,camere=row.camere,
            terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
            individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,
            individuala_camera=tab_ter_necesare_individuala_camera)
        #redirect(URL('default','ambulatoriu'))
        redirect(URL('default','pacienti'))  
    ########sfarsit cod de protectie: cand nu se pune nici o terapie individuala dupa ce se adauga terapiile nu se mai duce sa adauge terapie importanta pt ca nu are si incheie: redirect(URL('default','pacienti'))
    return locals()



def mm(): 
    y = request.vars # este un set de dictionare <Storage {'records': [], 'id': ['1', '2', '3', '4']}>
    
    ora_incepere=y['ora_incepere']
    ora_sfarsit=y['ora_sfarsit']
    z= y['id']#id-urile selecatate ex:['1', '2', '3', '4']
    film_id = int(y['id1'])
    xupd=int(y['xupd'])
    ver_list = isinstance(z, str)# verifica daca z este un string adica doar un element selectat=>True sau daca este o lista adica mai multe elemente selectate sau niciunul: =>False
    xpa=y['x']
    zz=y['nume']# are valoarea None => nu imi foloseste
    
    film_titlu = y['titlu1']
    tip_tip = y['tip1']
    if z!=None:
        if xupd==3 or xupd==4:
            db(db.pacienti.id == film_id).select().first().update_record(terapii_importante=None)
            db(db.orar_p.pacient_id == film_id).select().first().update_record(terapii_importante=None)
    ###verific daca se incadreaza in intervalul orar
    if xupd==1 or xupd==2: #sterg doar la adaugare NU si la update
        db(db.orar_p.pacient_id == int(film_id)).delete()
    if ((int(float(ora_incepere))!=7) or (int(float(ora_sfarsit))!=23)) and ora_incepere!='100':#adica este ambulator-ambulator
        if z==None:
            db(db.pacienti.id == int(film_id)).delete()
            session.flash = 'Nu ai introdus nici o terapie'
            redirect(URL('default','ambulatoriu'))
    
        z2=z     
        if type(z)==str:
            z1=z
            z=[]
            z.append(z1)
        yt_este=0
        voc_este=0
        contor_ter=0 # cate terapii individuale si aparate am
        control_fr=0
        key_sterge=0 #daca e 0 nu sterg daca e 1 sterg
        i10=0
        id_yt=(db(db.terapii.nume=='YOGA TERAPEUTICA').select().first()).id
        id_voc=(db(db.terapii.nume=='VOCALE').select().first()).id
        id_resp=(db(db.terapii.nume=='RESPIRATII').select().first()).id
        id_ps=(db(db.terapii.nume=='PSIHOTERAPIE DE GRUP (CODUL VINDECARII, IERTARE, MEDITATIE)').select().first()).id
        id_fr=(db(db.terapii.nume=='LAMPA FRECVENTE').select().first()).id
        id_cr=(db(db.terapii.nume=='CROMOTERAPIE').select().first()).id
        if (str(id_yt) in z)==True:
            yt_este=1
        if (str(id_voc) in z)==True or (str(id_resp) in z)==True or (str(id_ps) in z)==True:
            voc_este=2
        for i8 in z:
            i9=(db(db.terapii.id==int(i8)).select().first()).tip
            if i9=='individuala in camera':
                i10=1
            
            if (str(id_yt)!=i8) and (str(id_voc)!=i8) and (str(id_resp)!=i8) and (str(id_ps)!=i8) and i10!=1:
                contor_ter=contor_ter+1
                if (str(id_fr)==i8):
                    control_fr=1
                if (str(id_cr)==i8) and control_fr==1:    
                    contor_ter=contor_ter-1 #contor_ter spune cate terapii individuale si aparate am
            i10=0            
        key_ora_incepere=9-int(dict_ore_incepere[ora_incepere]) # imi da cate terapii pot face
        if (int(float(ora_incepere))>=12):
            key_valabilitate=key_ora_incepere-contor_ter
            if key_valabilitate<0:
                key_sterge=1
        if (int(float(ora_incepere))==7) or (int(float(ora_incepere))==9) or (int(float(ora_incepere))==10):
            key_valabilitate=key_ora_incepere-contor_ter-yt_este-voc_este # am posibilitatea la atatea terapii individuale si aparate
            if key_valabilitate<0:
                key_sterge=1
        if (int(float(ora_incepere))==11):
            key_valabilitate=key_ora_incepere-contor_ter-yt_este
            if key_valabilitate<0:
                key_sterge=1
        if key_sterge==1:
            db(db.pacienti.id == int(film_id)).delete()
            session.flash = 'Introdu cu atentie ora de inceput'
            #redirect(URL('default','test1',vars=dict(z=z,contor_ter=contor_ter,voc_este=voc_este,yt_este=yt_este,id_yt=id_yt,key_ora_incepere=key_ora_incepere,key_valabilitate=key_valabilitate)))
            redirect(URL('default','ambulatoriu'))
        if key_sterge==0:
            pass
        z=z2    
    else:
        pass
    ###sfarsit verific daca se incadreaza in intervalul orar
    if z==None:
        if xupd<3:
            db(db.pacienti.id == int(film_id)).delete()
            session.flash = 'Nu ai introdus nici o terapie'
            redirect(URL('default','pacienti'))
    if ver_list == False:
        if y['id']!=None:
            l = len(y['id'])
        else:
            l=0

        if l!=0:
            datele = []
            for i in range(l):
                datele.append (y['id'][i] ) 
            xx=[]
            querry=db.terapii.id.belongs(datele)
            form = SQLFORM.grid(querry) # grid doar cu id-urile selectate
            form1 = SQLFORM.grid(querry) # grid doar cu id-urile selectate
            xxx = db(db.terapii.id.belongs(datele)).select()  #inregistrarile id-urilor selectate
            for x in xxx:
                xx.append(x.nume) #pune in lista xx categoriile selectate ex: ['romantic', 'documentar', 'istoric', 'comedie']

            row = db(db.pacienti.id == film_id).select().first()
            db(db.pacienti.id == film_id).select().first().update_record(terapii_necesare=xx)
            
            #redirect(URL('default', 'ad_actor',vars=dict(id1=film_id,xx=xx,titlu1=film_titlu,row1=row)))
            if xpa=='1':

                redirect(URL('default','ad_terapii2',vars=dict(film_id=film_id,xupd=xupd,nume=film_titlu)))
            else:
                if xupd==1 or xupd==2:
                    row = db(db.pacienti).select().last() #in aceasta linie si in cea de mai jos copii in tabela orar_p pacientul cu datele lui
                if xupd==3 or xupd==4:
                    row = db(db.pacienti.id==film_id).select().first()
                ##########inceput cod:12345
                terapiile_necesare = row.terapii_necesare #terapiile necesare din tabela pacienti
                len_terapiile_necesare = len(terapiile_necesare) # lungimea liststringului terapii-necesare
                i=0
                tab_ter_necesare_individuala=[]
                tab_ter_necesare_degrup=[]
                tab_ter_necesare_degrupd=[]
                tab_ter_necesare_individuala_camera=[]
                for i in range(len_terapiile_necesare):
                    terapia_necesara = terapiile_necesare[i]
                    tip_terapia_necesara_gasita = db(db.terapii.nume == terapia_necesara).select().first().tip
                    if tip_terapia_necesara_gasita== 'de grup d':
                        tab_ter_necesare_degrupd.append(terapia_necesara)
                    if tip_terapia_necesara_gasita== 'individuala':
                        tab_ter_necesare_individuala.append(terapia_necesara)
                    if tip_terapia_necesara_gasita== 'de grup':
                        tab_ter_necesare_degrup.append(terapia_necesara)
                    if tip_terapia_necesara_gasita== 'individuala in camera':
                        tab_ter_necesare_individuala_camera.append(terapia_necesara)    
                    i=i+1
                if xupd==1 or xupd==2:    
                    db.orar_p.insert(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,
                    camere=row.camere,terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
                    individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,
                    degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,individuala_camera=tab_ter_necesare_individuala_camera)
                    #redirect(URL('default', 'ad_actor',vars=dict(id1=film_id,xx=xx,titlu1=film_titlu,row1=row)))
                    ##########sfarsit cod:12345
                    
                if xupd==3 or xupd==4:
                    #rowupdt=db(db.pacienti.id==int(y['id1'])).select().first()
                    rowupdt1=db(db.orar_p.pacient_id==film_id).select().first()
                    rowupdt1.update_record(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,camere=row.camere,
                    terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
                    individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,
                    individuala_camera=tab_ter_necesare_individuala_camera)
                    
                redirect(URL('default','ambulatoriu'))


                
        else:
            if xpa=='1':
                redirect(URL('default','ad_terapii2',vars=dict(film_id=film_id,xupd=xupd,nume=film_titlu)))
            else:
                if xupd==1 or xupd==2:
                    row = db(db.pacienti).select().last() #in aceasta linie si in cea de mai jos copii in tabela orar_p pacientul cu datele lui
                if xupd==3 or xupd==4:
                    row = db(db.pacienti.id==film_id).select().first()
                ##########inceput cod:12345
                terapiile_necesare = row.terapii_necesare #terapiile necesare din tabela pacienti
                len_terapiile_necesare = len(terapiile_necesare) # lungimea liststringului terapii-necesare
                i=0
                tab_ter_necesare_individuala=[]
                tab_ter_necesare_degrup=[]
                tab_ter_necesare_degrupd=[]
                tab_ter_necesare_individuala_camera=[]
                for i in range(len_terapiile_necesare):
                    terapia_necesara = terapiile_necesare[i]
                    tip_terapia_necesara_gasita = db(db.terapii.nume == terapia_necesara).select().first().tip
                    if tip_terapia_necesara_gasita== 'de grup d':
                        tab_ter_necesare_degrupd.append(terapia_necesara)
                    if tip_terapia_necesara_gasita== 'individuala':
                        tab_ter_necesare_individuala.append(terapia_necesara)
                    if tip_terapia_necesara_gasita== 'de grup':
                        tab_ter_necesare_degrup.append(terapia_necesara)
                    if tip_terapia_necesara_gasita== 'individuala in camera':
                        tab_ter_necesare_individuala_camera.append(terapia_necesara)    
                    i=i+1
                if xupd==1 or xupd==2:    
                    db.orar_p.insert(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,
                    camere=row.camere,terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
                    individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,
                    degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,individuala_camera=tab_ter_necesare_individuala_camera)
                    #redirect(URL('default', 'ad_actor',vars=dict(id1=film_id,xx=xx,titlu1=film_titlu,row1=row)))
                    ##########sfarsit cod:12345
                    
                if xupd==3 or xupd==4:
                    #rowupdt=db(db.pacienti.id==int(y['id1'])).select().first()
                    rowupdt1=db(db.orar_p.pacient_id==film_id).select().first()
                    rowupdt1.update_record(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,camere=row.camere,
                    terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
                    individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,
                    individuala_camera=tab_ter_necesare_individuala_camera)
                redirect(URL('default','ambulatoriu'))
                
    else:
        if y['id']!=None:
            l = 1
        else:
            l=0

        if l!=0:
            datele = []
            datele.append (y['id']) 
            xx=[]
            querry=db.terapii.id.belongs(datele)
            form = SQLFORM.grid(querry) # grid doar cu id-urile selectate
            form1 = SQLFORM.grid(querry) # grid doar cu id-urile selectate
            xxx = db(db.terapii.id.belongs(datele)).select()  #inregistrarile id-urilor selectate
            for x in xxx:
                xx.append(x.nume) #pune in lista xx categoriile selectate ex: ['romantic', 'documentar', 'istoric', 'comedie']

            row = db(db.pacienti.id == film_id).select().first()
            db(db.pacienti.id == film_id).select().first().update_record(terapii_necesare=xx)

            #redirect(URL('default', 'ad_actor',vars=dict(id1=film_id,xx=xx,titlu1=film_titlu,row1=row)))
            if xpa=='1':
                redirect(URL('default','ad_terapii2',vars=dict(film_id=film_id,xupd=xupd,nume=film_titlu)))
            else:
                if xupd==1 or xupd==2:
                    row = db(db.pacienti).select().last() #in aceasta linie si in cea de mai jos copii in tabela orar_p pacientul cu datele lui
                if xupd==3 or xupd==4:
                    row = db(db.pacienti.id==film_id).select().first()
                ##########inceput cod:12345
                terapiile_necesare = row.terapii_necesare #terapiile necesare din tabela pacienti
                len_terapiile_necesare = len(terapiile_necesare) # lungimea liststringului terapii-necesare
                i=0
                tab_ter_necesare_individuala=[]
                tab_ter_necesare_degrup=[]
                tab_ter_necesare_degrupd=[]
                tab_ter_necesare_individuala_camera=[]
                for i in range(len_terapiile_necesare):
                    terapia_necesara = terapiile_necesare[i]
                    tip_terapia_necesara_gasita = db(db.terapii.nume == terapia_necesara).select().first().tip
                    if tip_terapia_necesara_gasita== 'de grup d':
                        tab_ter_necesare_degrupd.append(terapia_necesara)
                    if tip_terapia_necesara_gasita== 'individuala':
                        tab_ter_necesare_individuala.append(terapia_necesara)
                    if tip_terapia_necesara_gasita== 'de grup':
                        tab_ter_necesare_degrup.append(terapia_necesara)
                    if tip_terapia_necesara_gasita== 'individuala in camera':
                        tab_ter_necesare_individuala_camera.append(terapia_necesara)    
                    i=i+1
                if xupd==1 or xupd==2:    
                    db.orar_p.insert(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,
                    camere=row.camere,terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
                    individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,
                    degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,individuala_camera=tab_ter_necesare_individuala_camera)
                    #redirect(URL('default', 'ad_actor',vars=dict(id1=film_id,xx=xx,titlu1=film_titlu,row1=row)))
                    ##########sfarsit cod:12345
                    
                if xupd==3 or xupd==4:
                    #rowupdt=db(db.pacienti.id==int(y['id1'])).select().first()
                    rowupdt1=db(db.orar_p.pacient_id==film_id).select().first()
                    rowupdt1.update_record(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,camere=row.camere,
                    terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
                    individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,
                    individuala_camera=tab_ter_necesare_individuala_camera)
                    
                redirect(URL('default','ambulatoriu'))
                
        else:
            if xpa=='1':
                redirect(URL('default','ad_terapii2',vars=dict(film_id=film_id,xupd=xupd,nume=film_titlu)))
            else:
                if xupd==1 or xupd==2:
                    row = db(db.pacienti).select().last() #in aceasta linie si in cea de mai jos copii in tabela orar_p pacientul cu datele lui
                if xupd==3 or xupd==4:
                    row = db(db.pacienti.id==film_id).select().first()
                ##########inceput cod:12345
                terapiile_necesare = row.terapii_necesare #terapiile necesare din tabela pacienti
                len_terapiile_necesare = len(terapiile_necesare) # lungimea liststringului terapii-necesare
                i=0
                tab_ter_necesare_individuala=[]
                tab_ter_necesare_degrup=[]
                tab_ter_necesare_degrupd=[]
                tab_ter_necesare_individuala_camera=[]
                for i in range(len_terapiile_necesare):
                    terapia_necesara = terapiile_necesare[i]
                    tip_terapia_necesara_gasita = db(db.terapii.nume == terapia_necesara).select().first().tip
                    if tip_terapia_necesara_gasita== 'de grup d':
                        tab_ter_necesare_degrupd.append(terapia_necesara)
                    if tip_terapia_necesara_gasita== 'individuala':
                        tab_ter_necesare_individuala.append(terapia_necesara)
                    if tip_terapia_necesara_gasita== 'de grup':
                        tab_ter_necesare_degrup.append(terapia_necesara)
                    if tip_terapia_necesara_gasita== 'individuala in camera':
                        tab_ter_necesare_individuala_camera.append(terapia_necesara)    
                    i=i+1
                if xupd==1 or xupd==2:    
                    db.orar_p.insert(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,
                    camere=row.camere,terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
                    individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,
                    degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,individuala_camera=tab_ter_necesare_individuala_camera)
                    #redirect(URL('default', 'ad_actor',vars=dict(id1=film_id,xx=xx,titlu1=film_titlu,row1=row)))
                    ##########sfarsit cod:12345
                    
                if xupd==3 or xupd==4:
                    #rowupdt=db(db.pacienti.id==int(y['id1'])).select().first()
                    rowupdt1=db(db.orar_p.pacient_id==film_id).select().first()
                    rowupdt1.update_record(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,camere=row.camere,
                    terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
                    individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,
                    individuala_camera=tab_ter_necesare_individuala_camera)
                redirect(URL('default','ambulatoriu'))
                
    return locals()

def mm1(): #COD INUTIL NU E FOLOSIT NICAIERI este pt a adauga terapiile importante dupa ce am adaugat terapiile
    y = request.vars # este un set de dictionare <Storage {'records': [], 'id': ['1', '2', '3', '4']}>
    z= y['id']#id-urile selecatate ex:['1', '2', '3', '4']
    zz=y['nume']# are valoarea None => nu imi foloseste
    film_id = y['id1']
    film_titlu = y['titlu1']
    tip_tip = y['tip1']
    ver_list = isinstance(z, str) # verifica daca z este un string adica doar un element selectat=>True sau daca este o lista adica mai multe elemente selectate sau niciunul: =>False
    if ver_list == False:
        if y['id']!=None:
            l = len(y['id'])
        else:
            l=0

        if l!=0:
            datele = []
            for i in range(l):
                datele.append (y['id'][i] ) 
            xx=[]
            querry=db.terapii.id.belongs(datele)
            form = SQLFORM.grid(querry) # grid doar cu id-urile selectate
            form1 = SQLFORM.grid(querry) # grid doar cu id-urile selectate
            xxx = db(db.terapii.id.belongs(datele)).select()  #inregistrarile id-urilor selectate
            for x in xxx:
                xx.append(x.nume) #pune in lista xx categoriile selectate ex: ['romantic', 'documentar', 'istoric', 'comedie']

            row = db(db.pacienti.id == film_id).select().first()
            db(db.pacienti.id == film_id).select().first().update_record(terapii_importante=xx)
            
            if xupd==1 or xupd==2:
                row = db(db.pacienti).select().last() #in aceasta linie si in cea de mai jos copii in tabela orar_p pacientul cu datele lui
            if xupd==3 or xupd==4:
                row = db(db.pacienti.id==int(y['id1'])).select().first()
            ##########inceput cod:12345
            terapiile_necesare = row.terapii_necesare #terapiile necesare din tabela pacienti
            len_terapiile_necesare = len(terapiile_necesare) # lungimea liststringului terapii-necesare
            i=0
            tab_ter_necesare_individuala=[]
            tab_ter_necesare_degrup=[]
            tab_ter_necesare_degrupd=[]
            tab_ter_necesare_individuala_camera=[]
            for i in range(len_terapiile_necesare):
                terapia_necesara = terapiile_necesare[i]
                tip_terapia_necesara_gasita = db(db.terapii.nume == terapia_necesara).select().first().tip
                if tip_terapia_necesara_gasita== 'de grup d':
                    tab_ter_necesare_degrupd.append(terapia_necesara)
                if tip_terapia_necesara_gasita== 'individuala':
                    tab_ter_necesare_individuala.append(terapia_necesara)
                if tip_terapia_necesara_gasita== 'de grup':
                    tab_ter_necesare_degrup.append(terapia_necesara)
                if tip_terapia_necesara_gasita== 'individuala in camera':
                    tab_ter_necesare_individuala_camera.append(terapia_necesara)    
                i=i+1
            if xupd==1 or xupd==2:    
                db.orar_p.insert(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,
                camere=row.camere,terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
                individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,
                degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,individuala_camera=tab_ter_necesare_individuala_camera)
                #redirect(URL('default', 'ad_actor',vars=dict(id1=film_id,xx=xx,titlu1=film_titlu,row1=row)))
                ##########sfarsit cod:12345
                
            if xupd==3 or xupd==4:
                rowupdt=db(db.pacienti.id==int(y['id1'])).select().first()
                rowupdt1=db(db.orar_p.pacient_id==int(y['id1'])).select().first()
                rowupdt1.update_record(dataa=row.inceput_tt)
                rowupdt1.update_record(sfarsit_tt=row.sfarsit_tt)
                rowupdt1.update_record(din_localitatea=row.din_localitatea)
                rowupdt1.update_record(pacient=row.nume)
                rowupdt1.update_record(pacient_id=row.id)
                rowupdt1.update_record(camere=row.camere)
                rowupdt1.update_record(terapii_necesare=row.terapii_necesare)
                rowupdt1.update_record(terapii_importante=row.terapii_importante)
                rowupdt1.update_record(p_or_a=row.p_or_a)
                rowupdt1.update_record(ora_in=row.ora_in)
                rowupdt1.update_record(ora_out=row.ora_out)
                rowupdt1.update_record(individuala_nu=tab_ter_necesare_individuala)
                rowupdt1.update_record(individuala_cicluri=0)
                rowupdt1.update_record(degrup_nu=tab_ter_necesare_degrup)
                rowupdt1.update_record(degrup_cicluri=0)
                rowupdt1.update_record(degrupd=tab_ter_necesare_degrupd)
                rowupdt1.update_record(individuala_camera=tab_ter_necesare_individuala_camera)
            redirect(URL('default','ambulatoriu'))
        else:
            row = db(db.pacienti).select().last() #in aceasta linie si in cea de mai jos copii in tabela orar_p pacientul cu datele lui
            ##########inceput cod:12345
            terapiile_necesare = row.terapii_necesare #terapiile necesare din tabela pacienti
            len_terapiile_necesare = len(terapiile_necesare) # lungimea liststringului terapii-necesare
            i=0
            tab_ter_necesare_individuala=[]
            tab_ter_necesare_degrup=[]
            tab_ter_necesare_degrupd=[]
            tab_ter_necesare_individuala_camera=[]
            for i in range(len_terapiile_necesare):
                terapia_necesara = terapiile_necesare[i]
                tip_terapia_necesara_gasita = db(db.terapii.nume == terapia_necesara).select().first().tip
                if tip_terapia_necesara_gasita== 'de grup d':
                    tab_ter_necesare_degrupd.append(terapia_necesara)
                if tip_terapia_necesara_gasita== 'individuala':
                    tab_ter_necesare_individuala.append(terapia_necesara)
                if tip_terapia_necesara_gasita== 'de grup':
                    tab_ter_necesare_degrup.append(terapia_necesara)
                if tip_terapia_necesara_gasita== 'individuala in camera':
                    tab_ter_necesare_individuala_camera.append(terapia_necesara)    
                i=i+1
            if xupd==1 or xupd==2:    
                db.orar_p.insert(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,
                camere=row.camere,terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
                individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,
                degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,individuala_camera=tab_ter_necesare_individuala_camera)
                #redirect(URL('default', 'ad_actor',vars=dict(id1=film_id,xx=xx,titlu1=film_titlu,row1=row)))
                ##########sfarsit cod:12345
                
            if xupd==3 or xupd==4:
                rowupdt=db(db.pacienti.id==int(y['id1'])).select().first()
                rowupdt1=db(db.orar_p.pacient_id==int(y['id1'])).select().first()
                rowupdt1.update_record(dataa=row.inceput_tt)
                rowupdt1.update_record(sfarsit_tt=row.sfarsit_tt)
                rowupdt1.update_record(din_localitatea=row.din_localitatea)
                rowupdt1.update_record(pacient=row.nume)
                rowupdt1.update_record(pacient_id=row.id)
                rowupdt1.update_record(camere=row.camere)
                rowupdt1.update_record(terapii_necesare=row.terapii_necesare)
                rowupdt1.update_record(terapii_importante=row.terapii_importante)
                rowupdt1.update_record(p_or_a=row.p_or_a)
                rowupdt1.update_record(ora_in=row.ora_in)
                rowupdt1.update_record(ora_out=row.ora_out)
                rowupdt1.update_record(individuala_nu=tab_ter_necesare_individuala)
                rowupdt1.update_record(individuala_cicluri=0)
                rowupdt1.update_record(degrup_nu=tab_ter_necesare_degrup)
                rowupdt1.update_record(degrup_cicluri=0)
                rowupdt1.update_record(degrupd=tab_ter_necesare_degrupd)
                rowupdt1.update_record(individuala_camera=tab_ter_necesare_individuala_camera)
            redirect(URL('default','ambulatoriu'))
            pass
    else:
        if y['id']!=None:
            l = 1
        else:
            l=0

        if l!=0:
            datele = []
            datele.append (y['id']) 
            xx=[]
            querry=db.terapii.id.belongs(datele)
            form = SQLFORM.grid(querry) # grid doar cu id-urile selectate
            form1 = SQLFORM.grid(querry) # grid doar cu id-urile selectate
            xxx = db(db.terapii.id.belongs(datele)).select()  #inregistrarile id-urilor selectate
            for x in xxx:
                xx.append(x.nume) #pune in lista xx categoriile selectate ex: ['romantic', 'documentar', 'istoric', 'comedie']

            row = db(db.pacienti.id == film_id).select().first()
            db(db.pacienti.id == film_id).select().first().update_record(terapii_importante=xx)
            row = db(db.pacienti).select().last() #in aceasta linie si in cea de mai jos copii in tabela orar_p pacientul cu datele lui
            #tab_terapii = row.terapii_necesare
            ##########inceput cod:12345
            terapiile_necesare = row.terapii_necesare #terapiile necesare din tabela pacienti
            len_terapiile_necesare = len(terapiile_necesare) # lungimea liststringului terapii-necesare
            i=0
            tab_ter_necesare_individuala=[]
            tab_ter_necesare_degrup=[]
            tab_ter_necesare_degrupd=[]
            tab_ter_necesare_individuala_camera=[]
            for i in range(len_terapiile_necesare):
                terapia_necesara = terapiile_necesare[i]
                tip_terapia_necesara_gasita = db(db.terapii.nume == terapia_necesara).select().first().tip
                if tip_terapia_necesara_gasita== 'de grup d':
                    tab_ter_necesare_degrupd.append(terapia_necesara)
                if tip_terapia_necesara_gasita== 'individuala':
                    tab_ter_necesare_individuala.append(terapia_necesara)
                if tip_terapia_necesara_gasita== 'de grup':
                    tab_ter_necesare_degrup.append(terapia_necesara)
                if tip_terapia_necesara_gasita== 'individuala in camera':
                    tab_ter_necesare_individuala_camera.append(terapia_necesara)    
                i=i+1
            if xupd==1 or xupd==2:    
                db.orar_p.insert(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,
                camere=row.camere,terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
                individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,
                degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,individuala_camera=tab_ter_necesare_individuala_camera)
                #redirect(URL('default', 'ad_actor',vars=dict(id1=film_id,xx=xx,titlu1=film_titlu,row1=row)))
                ##########sfarsit cod:12345
                
            if xupd==3 or xupd==4:
                rowupdt=db(db.pacienti.id==int(y['id1'])).select().first()
                rowupdt1=db(db.orar_p.pacient_id==int(y['id1'])).select().first()
                rowupdt1.update_record(dataa=row.inceput_tt)
                rowupdt1.update_record(sfarsit_tt=row.sfarsit_tt)
                rowupdt1.update_record(din_localitatea=row.din_localitatea)
                rowupdt1.update_record(pacient=row.nume)
                rowupdt1.update_record(pacient_id=row.id)
                rowupdt1.update_record(camere=row.camere)
                rowupdt1.update_record(terapii_necesare=row.terapii_necesare)
                rowupdt1.update_record(terapii_importante=row.terapii_importante)
                rowupdt1.update_record(p_or_a=row.p_or_a)
                rowupdt1.update_record(ora_in=row.ora_in)
                rowupdt1.update_record(ora_out=row.ora_out)
                rowupdt1.update_record(individuala_nu=tab_ter_necesare_individuala)
                rowupdt1.update_record(individuala_cicluri=0)
                rowupdt1.update_record(degrup_nu=tab_ter_necesare_degrup)
                rowupdt1.update_record(degrup_cicluri=0)
                rowupdt1.update_record(degrupd=tab_ter_necesare_degrupd)
                rowupdt1.update_record(individuala_camera=tab_ter_necesare_individuala_camera)
            redirect(URL('default','ambulatoriu'))
        else:
            redirect(URL('default', 'pacienti'))
            #redirect(URL('default', 'ad_actor',vars=dict(id1=film_id,titlu1=film_titlu)))
            pass
    return locals()

def mm2():
    do=request.vars['habits2']#MASAJ RELAXARE
    do1=request.vars['idul']# este none??
    xupd=int(request.vars['xupd1'])#este 3
    array_terapie_importanta=[]
    #film_id=int(do1)
    film_id=int(request.vars['film_id1']) #ESTE 208
    if do==None:
        pass
    else:
        array_terapie_importanta.append(do)
        row = db(db.pacienti.id == film_id).select().first()
        db(db.pacienti.id == film_id).select().first().update_record(terapii_importante=do)
    if xupd==1 or xupd==2:
        row = db(db.pacienti).select().last() #in aceasta linie si in cea de mai jos copii in tabela orar_p pacientul cu datele lui
    if xupd==3 or xupd==4:
        row = db(db.pacienti.id==film_id).select().first()    
    
    #tab_terapii = row.terapii_necesare
    ##########inceput cod:12345
    terapiile_necesare = row.terapii_necesare #terapiile necesare din tabela pacienti
    len_terapiile_necesare = len(terapiile_necesare) # lungimea liststringului terapii-necesare
    i=0
    tab_ter_necesare_individuala=[]
    tab_ter_necesare_degrup=[]
    tab_ter_necesare_degrupd=[]
    tab_ter_necesare_individuala_camera=[]
    for i in range(len_terapiile_necesare):
        terapia_necesara = terapiile_necesare[i]
        tip_terapia_necesara_gasita = db(db.terapii.nume == terapia_necesara).select().first().tip
        if tip_terapia_necesara_gasita== 'de grup d':
            tab_ter_necesare_degrupd.append(terapia_necesara)
        if tip_terapia_necesara_gasita== 'individuala':
            tab_ter_necesare_individuala.append(terapia_necesara)
        if tip_terapia_necesara_gasita== 'de grup':
            tab_ter_necesare_degrup.append(terapia_necesara)
        if tip_terapia_necesara_gasita== 'individuala in camera':
            tab_ter_necesare_individuala_camera.append(terapia_necesara)    
        i=i+1
    if xupd==1 or xupd==2:    
        db.orar_p.insert(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,camere=row.camere,terapii_necesare=row.terapii_necesare,
        terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,
        degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,individuala_camera=tab_ter_necesare_individuala_camera)
    if xupd==3 or xupd==4:
        #rowupdt=db(db.pacienti.id==int(y['id1'])).select().first()
        rowupdt1=db(db.orar_p.pacient_id==film_id).select().first()
        rowupdt1.update_record(dataa=row.inceput_tt,sfarsit_tt=row.sfarsit_tt,din_localitatea=row.din_localitatea,pacient=row.nume,pacient_id=row.id,camere=row.camere,
        terapii_necesare=row.terapii_necesare,terapii_importante=row.terapii_importante,p_or_a=row.p_or_a,ora_in=row.ora_in,ora_out=row.ora_out,
        individuala_nu=tab_ter_necesare_individuala,individuala_cicluri=0,degrup_nu=tab_ter_necesare_degrup,degrup_cicluri=0,degrupd=tab_ter_necesare_degrupd,
        individuala_camera=tab_ter_necesare_individuala_camera)    
    redirect(URL('default', 'pacienti'))
    return locals()

def orar_t():
    row=db(db.orar_t).select(db.orar_t.dataa.max())[0]
    row1 = row['_extra']['MAX("orar_t"."dataa")'] 
    data_ce_urmeaza= (row1+datetime.timedelta(days=1))
    if len(request.args)>1 and request.args[-2]=='new':
        response.flash=data_ce_urmeaza
    grid = SQLFORM.grid(db.orar_t,user_signature=False,csv=False,orderby=~db.orar_t.dataa,onvalidation=ver_data2,onfailure=xx,oncreate=do_something2,onupdate=do_something2)
    
    return locals()

def ver_data2(form):#in aceasta functie pot pune orice fel de conditii inainte de a valida un add record ziua urmatoare terapeuti
    dataa = form.vars.dataa
    controll = form.vars.control #valoarea checkboxului nevalidata=None
    len_tab = db(db.orar_t).count()# verific daca se afla vreo inregistrare in tabela, daca len_tab>0 se afla
    len1=0
    len1 = db(db.orar_t.dataa==dataa).count()#verific daca exista deja in tabela aceasta inregistrare-este pt update
    #len1=0
    if len1==0: #aici se adauga si pe else se face update
        if len_tab>0: #marimea tabelei
            row = db(db.orar_t).select().last()
            if (dataa+datetime.timedelta(days=-1))==row.dataa or controll != None:  #check-box-urile le verific cu None care inseamna neselectat
                form.errors= False
            else:
                form.errors= True
        else:
            form.errors= False
    else:
        if len_tab>0: #lungimea tabelei
            row = db(db.orar_t.dataa==dataa).select().first()
            if ((dataa+datetime.timedelta(days=0))==row.dataa or controll != None):  #check-box-urile le verific cu None care inseamna neselectat
                form.errors= False
            else:
                form.errors= True
        else:
            form.errors= False

def do_something2(form):
    session.flash = 'Reusit!'
    id = form.vars.id
    dataa = form.vars.dataa
    row = db(db.orar_t.id == id).select().first()
    if dataa==row.dataa:
        form.errors=False
        
    else:
        form.errors=True

             


def orar_sablon():
    fields_orar_sablon = [db.orar_sablon.ora,db.orar_sablon.info_generale,db.orar_sablon.pacient_1,db.orar_sablon.pacient_2,db.orar_sablon.pacient_3,db.orar_sablon.pacient_4,db.orar_sablon.pacient_5,db.orar_sablon.pacient_6,db.orar_sablon.pacient_7,db.orar_sablon.pacient_8,db.orar_sablon.pacient_9,db.orar_sablon.pacient_10,db.orar_sablon.pacient_11,db.orar_sablon.pacient_12,db.orar_sablon.pacient_13,db.orar_sablon.pacient_14,db.orar_sablon.pacient_15,db.orar_sablon.pacient_16,db.orar_sablon.pacient_17,db.orar_sablon.pacient_18,db.orar_sablon.pacient_19,db.orar_sablon.pacient_20]

    header_o ={'orar_sablon.ora':'Ora si Data','orar_sablon.pacient_1' : 'Pacient_______________________________1','orar_sablon.pacient_2' : 'Pacient 2________________________________','orar_sablon.pacient_3' : 'Pacient 3________________________________','orar_sablon.pacient_4' : 'Pacient 4________________________________','orar_sablon.pacient_5' : 'Pacient 5________________________________','orar_sablon.pacient_6' : 'Pacient 6________________________________','orar_sablon.pacient_7' : 'Pacient 7________________________________','orar_sablon.pacient_8' : 'Pacient 8________________________________','orar_sablon.pacient_9' : 'Pacient 9________________________________','orar_sablon.pacient_10' : 'Pacient 10________________________________','orar_sablon.pacient_11' : 'Pacient 11________________________________','orar_sablon.pacient_12' : 'Pacient 12________________________________','orar_sablon.pacient_13' : 'Pacient 13________________________________','orar_sablon.pacient_14' : 'Pacient14________________________________','orar_sablon.pacient_15' : 'Pacient 15________________________________','orar_sablon.pacient_16' : 'Pacient 16________________________________','orar_sablon.pacient_17' : 'Pacient 17________________________________','orar_sablon.pacient_18' : 'Pacient 18________________________________','orar_sablon.pacient_19' : 'Pacient 19________________________________','orar_sablon.pacient_20' : 'Pacient 20________________________________'}     
    grid = SQLFORM.grid(db.orar_sablon,headers= header_o,fields = fields_orar_sablon,maxtextlengths={'orar_sablon.ora':30,'orar_sablon.info_generale':36,'orar_sablon.pacient_1':50},user_signature=False,csv=True,paginate=30,create=False,searchable=False)
    #,<col id="orar_sablon-ora" data-column="1">
    return locals()
        

def useri():
    grid = SQLFORM.grid(db.auth_user,paginate=10,csv=False)
    return locals()

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


 ##### inceput11 cod pt a vedea terapiile posibile pe intervale de ore
def arrayuriterapii1(terapii_degrupd,terapii_individuale,ter_dim,terapii_aparate,terapii_ind_tot,ter_dim1,ter_toti,ter_dup):
    terapii_degrupd1714=[]
    i5=0
    for i2 in terapii_degrupd:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_dim1:
            if i4!='lipsa T dim':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break
        terapii_degrupd1714.append(i3)
        i5=i5+1
    
    #tab_terapii_individuale dimineata Ex: terapii_individuale714=[0, 5, 5, 5, 3, 0, 5, 0, 1]
    terapii_individuale714=[]   #Ex: terapii_individuale714=[0, 5, 5, 5, 3, 0, 5, 0, 1]
    i5=0
    for i2 in terapii_individuale:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_dim:
            if i4!='lipsa T dim':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break
        terapii_individuale714.append(i3)
        i5=i5+1

    terapii_aparate714=[]
    i5=0
    for i2 in terapii_aparate:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_dim:
            if i4!='lipsa T dim':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break    
        terapii_aparate714.append(i3)
        i5=i5+1
    terapii_individuale_tot714=[]
    i5=0
    for i2 in terapii_ind_tot:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_dim:
            if i4!='lipsa T dim':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break         
        terapii_individuale_tot714.append(i3)
        i5=i5+1



    terapii_individuale1714=[]
    i5=0
    for i2 in terapii_individuale:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_dim1:
            if i4!='lipsa T dim':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break
        terapii_individuale1714.append(i3)
        i5=i5+1
    terapii_aparate1714=[]
    i5=0
    for i2 in terapii_aparate:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_dim1:
            if i4!='lipsa T dim':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break    
        terapii_aparate1714.append(i3)
        i5=i5+1
    terapii_individuale_tot1714=[]
    i5=0
    for i2 in terapii_ind_tot:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_dim1:
            if i4!='lipsa T dim':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break    
        terapii_individuale_tot1714.append(i3)
        i5=i5+1  
    #sfarsit tab_terapii_individuale dimineata     
    #inceput creare tab toti pt terapiile de dimineata in intervalul 14-16
    terapii_degrupd1416=[]
    i5=0
    for i2 in terapii_degrupd:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_toti:
            if i4!='lipsa T dim' and i4!='lipsa T dup':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break
        terapii_degrupd1416.append(i3)
        i5=i5+1
    #sfarsit creare tab toti pt terapiile de dimineata in intervalul 14-16    
    # inceputtab_terapii_individuale toti 14-16.15 Ex: terapii_individuale714=[0, 5, 5, 5, 3, 0, 5, 0, 1]
    terapii_individuale1416=[]
    i5=0
    for i2 in terapii_individuale:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_toti:
            if i4!='lipsa T dim' and i4!='lipsa T dup':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break    
        terapii_individuale1416.append(i3)
        i5=i5+1
    terapii_aparate1416=[]
    i5=0
    for i2 in terapii_aparate:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_toti:
            if i4!='lipsa T dim' and i4!='lipsa T dup':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break    
        terapii_aparate1416.append(i3)
        i5=i5+1
    terapii_individuale_tot1416=[]
    i5=0
    for i2 in terapii_ind_tot:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_toti:
            if i4!='lipsa T dim' and i4!='lipsa T dup':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break    
        terapii_individuale_tot1416.append(i3)
        i5=i5+1

    # sfarsitttab_terapii_individuale toti 14-16.15
    terapii_degrupd1623=[]
    i5=0
    for i2 in terapii_degrupd:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_dup:
            if i4!='lipsa T dup':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break
        terapii_degrupd1623.append(i3)
        i5=i5+1
    # inceputtab_terapii_individuale toti 16.15-23 Ex: terapii_individuale1623=[0, 5, 5, 5, 3, 0, 5, 0, 1]
    terapii_individuale1623=[]
    i5=0
    for i2 in terapii_individuale:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_dup:
            if i4!='lipsa T dup':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break
        terapii_individuale1623.append(i3)
        i5=i5+1
    terapii_aparate1623=[]
    i5=0
    for i2 in terapii_aparate:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_dup:
            if i4!='lipsa T dup':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break
        terapii_aparate1623.append(i3)
        i5=i5+1
    
    
    
    terapii_individuale_tot1623=[]
    i5=0
    for i2 in terapii_ind_tot:
        i3=0
        i6=int((db(db.terapii.nume==i2).select().first()).simultan_maxim)
        for i4 in ter_dup:
            if i4!='lipsa T dup':
                row=db(db.terapeuti.nume==i4).select().first()
                if (i2 in row.ce_terapii_face)==True:
                    i3=i3+1
                if i3>=i6:
                    break
        terapii_individuale_tot1623.append(i3)
        i5=i5+1
    return locals()
    # sfarsitttab_terapii_individuale toti 14-16.15
    ##
    ##### sfarsit11 cod pt a vedea terapiile posibile pe intervale de ore
def arraypacienti1(pacienti_all,delta_data_min):
    ##inceput cod: pun in array-urile array_pacienti  pacientii din ziua respectiva, primii pacientii si apoi ambulatorii si in array_id_orar_p id-urile lor
    array_pacienti = []
    array_datele_orar_p=[]
    array_pacientii=[]#
    array_pacienti_ambulatoriu=[]
    array_pacienti_p_si_aP=[]
    array_pacienti_p=[]
    array_pacienti_aP=[]
    array_pacienti_a=[]
    jj=0
    nr_pacienti_pacienti=0# pt a stabili cati pacienti-pacienti sunt in ziua respectiva si cati pacienti ambulatoriu Ex: 6 cu 4
    nr_pacienti_ambulatoriu=0 # pt a stabili cati pacienti-pacienti sunt in ziua respectiva si cati pacienti ambulatoriu Ex: 6 cu 4
    for jj in range (3): # pun in arrayul array_pacienti toti pacientii din data respectiva
        for row in pacienti_all: # pun in arrayul array_pacienti toti pacientii din data respectiva
            if row.p_or_a=='pacient' and jj==0:
                
                #####inceput134 cod pt a pune in row.individuala_da istoria TI. Deocamdata am copiat doar ce a fost in ziua precedenta la individuala_da. Urmeaza sa adaug TI din ziua aceasta.
                
                


                #row.update_record(individuala_da=None)
                #####sfarsit134 cod pt a pune in row.individuala_da istoria TI. Deocamdata am copiat doar ce a fost in ziua precedenta la individuala_da. Urmeaza sa adaug TI din ziua aceasta.
                
                
                array_pacienti.append(row.pacient+' '+row.camere.camera+'-'+row.camere.pat)
                array_pacientii.append(row.pacient)
                array_pacienti_p_si_aP.append(row.pacient)
                array_pacienti_p.append(row.pacient)
                ##inceputcod132 pun in array toate datele despre pacientii inclusiv ambulatorii din ziua respectiva din tabela orar_p
                array_datele_orar_p.append(row.id) #0
                array_datele_orar_p.append(row.terapii_necesare) #1
                array_datele_orar_p.append(row.terapii_importante) #2
                array_datele_orar_p.append(row.individuala_nu) #3
                array_datele_orar_p.append(row.individuala_da) #4
                array_datele_orar_p.append(row.individuala_precedente) #5
                array_datele_orar_p.append(row.individuala_cicluri) #6
                array_datele_orar_p.append(row.degrup_nu) #7
                array_datele_orar_p.append(row.degrup_da) #8
                array_datele_orar_p.append(row.degrup_precedente) #9
                array_datele_orar_p.append(row.degrup_cicluri) #10
                array_datele_orar_p.append(row.degrupd) #11
                array_datele_orar_p.append(row.degrupd_da) #12
                array_datele_orar_p.append(row.individuala_camera) #13
                array_datele_orar_p.append(row.individuala_da) #14
                array_datele_orar_p.append(row.p_or_a)
                array_datele_orar_p.append('pacientt')
                array_datele_orar_p.append(row.ora_in)
                array_datele_orar_p.append(row.ora_out)
                ##sfarsitcod132 pun in array toate datele despre pacientii din ziua inclusiv ambulatorii respectiva din tabela orar_p
                nr_pacienti_pacienti=nr_pacienti_pacienti+1 # pt a stabili cati pacienti-pacienti sunt in ziua respectiva si cati pacienti ambulatoriu Ex: 6 cu 4
            if row.p_or_a=='ambulatoriu' and jj==1 and (str(row.ora_in)=='7' and str(row.ora_out)=='23'): 
                array_pacienti.append(row.pacient+'-'+'ambulatoriuP')
                array_pacientii.append(row.pacient)
                array_pacienti_ambulatoriu.append(row.pacient)
                array_pacienti_p_si_aP.append(row.pacient)
                array_pacienti_aP.append(row.pacient)
                ##inceputcod132 pun in array toate datele despre pacientii din ziua respectiva din tabela orar_p
                array_datele_orar_p.append(row.id)
                array_datele_orar_p.append(row.terapii_necesare)
                array_datele_orar_p.append(row.terapii_importante)
                array_datele_orar_p.append(row.individuala_nu)
                array_datele_orar_p.append(row.individuala_da)
                array_datele_orar_p.append(row.individuala_precedente)
                array_datele_orar_p.append(row.individuala_cicluri)
                array_datele_orar_p.append(row.degrup_nu)
                array_datele_orar_p.append(row.degrup_da)
                array_datele_orar_p.append(row.degrup_precedente)
                array_datele_orar_p.append(row.degrup_cicluri)
                array_datele_orar_p.append(row.degrupd)
                array_datele_orar_p.append(row.degrupd_da)
                array_datele_orar_p.append(row.individuala_camera)
                array_datele_orar_p.append(row.individuala_da)
                array_datele_orar_p.append(row.p_or_a)
                if str(row.ora_in)=='7' and str(row.ora_out)=='23':
                    array_datele_orar_p.append('ambulatoriup')
                else:
                    array_datele_orar_p.append('ambulatoriua')
                array_datele_orar_p.append(row.ora_in)
                array_datele_orar_p.append(row.ora_out)
                ##sfarsitcod132 pun in array toate datele despre pacientii din ziua respectiva din tabela orar_p
                nr_pacienti_ambulatoriu=nr_pacienti_ambulatoriu+1 # pt a stabili cati pacienti-pacienti sunt in ziua respectiva si cati pacienti ambulatoriu Ex: 6 cu 4
            if row.p_or_a=='ambulatoriu' and jj==2 and (str(row.ora_in)!='7' or str(row.ora_out)!='23'): 
                array_pacienti.append(row.pacient+'-'+'ambulatoriu')
                array_pacientii.append(row.pacient)
                array_pacienti_ambulatoriu.append(row.pacient)
                array_pacienti_a.append(row.pacient)
                ##inceputcod132 pun in array toate datele despre pacientii din ziua respectiva din tabela orar_p
                array_datele_orar_p.append(row.id)
                array_datele_orar_p.append(row.terapii_necesare)
                array_datele_orar_p.append(row.terapii_importante)
                array_datele_orar_p.append(row.individuala_nu)
                array_datele_orar_p.append(row.individuala_da)
                array_datele_orar_p.append(row.individuala_precedente)
                array_datele_orar_p.append(row.individuala_cicluri)
                array_datele_orar_p.append(row.degrup_nu)
                array_datele_orar_p.append(row.degrup_da)
                array_datele_orar_p.append(row.degrup_precedente)
                array_datele_orar_p.append(row.degrup_cicluri)
                array_datele_orar_p.append(row.degrupd)
                array_datele_orar_p.append(row.degrupd_da)
                array_datele_orar_p.append(row.individuala_camera)
                array_datele_orar_p.append(row.individuala_da)
                array_datele_orar_p.append(row.p_or_a)
                if str(row.ora_in)=='7' and str(row.ora_out)=='23':
                    array_datele_orar_p.append('ambulatoriup')
                else:
                    array_datele_orar_p.append('ambulatoriua')
                array_datele_orar_p.append(row.ora_in)
                array_datele_orar_p.append(row.ora_out)
                ##sfarsitcod132 pun in array toate datele despre pacientii din ziua respectiva din tabela orar_p
                nr_pacienti_ambulatoriu=nr_pacienti_ambulatoriu+1 # pt a stabili cati pacienti-pacienti sunt in ziua respectiva si cati pacienti ambulatoriu Ex: 6 cu 4
        jj=jj+1

        ##sfarsit cod: pun in array-urile array_pacienti  pacientii din ziua respectiva, primii pacientii si apoi ambulatorii si in array_id_orar_p id-urile lor
    return locals()
def arrayuri_terapeuti1(delta_data_min):             
    ###inceput cod1347 pt a pune in array-uri terapeutii:toti,toti fara principali,dim,dup,nu
    #if delta_data_min in db.orar_t.dataa:
    row_terapeuti_ziua_respectiva = db(db.orar_t.dataa==delta_data_min).select().first()
    

    array_terapeuti_ziua_respectiva=[] #array_terapeuti_ziua_respectiva=['Catalin', '7-16', 'Mirela', '14-23', 'Mari', '7-16', 'Lidia', 'all', 'Carmen', '14-23', 'Iulia', '7-16', 'Mihai', 'all']
    ter_toti=[]
    ter_nu=[]
    #ziua_are_terapeuti=0
    if row_terapeuti_ziua_respectiva.terapeut_dim!=None:
        array_terapeuti_ziua_respectiva.append(row_terapeuti_ziua_respectiva.terapeut_dim) #Ex: array_terapeuti_ziua_respectiva=['Catalin', '7-16', 'Mirela', '14-23', 'Mari', '7-16']
        array_terapeuti_ziua_respectiva.append('7-16')
        ter_toti.append(row_terapeuti_ziua_respectiva.terapeut_dim) #ter_toti=['Catalin', 'Mirela', 'Mari', 'Lidia', 'Carmen', 'Iulia', 'Mihai']
        ziua_are_terapeuti=0
    else:
        array_terapeuti_ziua_respectiva.append('lipsa T dim')
        array_terapeuti_ziua_respectiva.append('7-16')
        ter_toti.append('lipsa T dim')
        ziua_are_terapeuti=1

    if row_terapeuti_ziua_respectiva.terapeut_dup!=None:
        array_terapeuti_ziua_respectiva.append(row_terapeuti_ziua_respectiva.terapeut_dup)
        array_terapeuti_ziua_respectiva.append('14-23')
        ter_toti.append(row_terapeuti_ziua_respectiva.terapeut_dup)
        seara_are_terapeuti=0
    else:
        array_terapeuti_ziua_respectiva.append('lipsa T dup')
        array_terapeuti_ziua_respectiva.append('14-23')   
        ter_toti.append('lipsa T dup') #ter_toti=['Catalin', 'Mirela', 'Mari', 'Lidia', 'Carmen', 'Iulia', 'Mihai']
        seara_are_terapeuti=1
    #if ziua_are_terapeuti==0 and seara_are_terapeuti==0:    
    for ii in range(7):
        disp_z="dispo"+str(ii+1)
        ter_z="terapeut_"+str(ii+1)
        var1=row_terapeuti_ziua_respectiva(disp_z)
        var2=row_terapeuti_ziua_respectiva(ter_z)
        if var1!=None and var1!='nu':
            array_terapeuti_ziua_respectiva.append(var2)
            array_terapeuti_ziua_respectiva.append(var1)
            ter_toti.append(var2) # toti terapeutii de dimineata si dupamiaza inclusiv cei principali   ter_toti=['Catalin', 'Mirela', 'Mari', 'Lidia', 'Carmen', 'Iulia', 'Mihai']
        elif var1!=None and var1=='nu':
            ter_nu.append(var2)


    idx_terapeuti_dim=[i2 for i2, j2 in enumerate(array_terapeuti_ziua_respectiva) if j2=='7-16' or j2=='all']
    idx_terapeuti_dup=[i2 for i2, j2 in enumerate(array_terapeuti_ziua_respectiva) if j2=='14-23' or j2=='all']
    #idx_terapeuti_nu=[i2 for i2, j2 in enumerate(ter_nu1) if type(j2)=='str']
    ter_dim=[]        # toti terapeutii de dimineata inclusiv cel principal  ['Catalin', 'Mari', 'Lidia', 'Iulia', 'Mihai']
    ter_dup=[]        # toti terapeutii de dupamiaza inclusiv cel principal  ['Mirela', 'Lidia', 'Carmen', 'Mihai']
    ter_dim1=[]       # doar terapeutii secundari de dimineata ['Mari', 'Lidia', 'Iulia', 'Mihai']
    ter_dup1=[]       # doar terapeutii secundari de dupamiaza  ['Lidia', 'Carmen', 'Mihai']
    for i2 in idx_terapeuti_dim:
        ter_dim.append( array_terapeuti_ziua_respectiva[i2-1])
    for i2 in idx_terapeuti_dup:
        ter_dup.append(array_terapeuti_ziua_respectiva[i2-1])
    for i2 in ter_dim:
        ter_dim1.append(i2)
    for i2 in ter_dup:
        ter_dup1.append(i2)
    if len(ter_dim1)>0:    
        ter_dim1.pop(0)
    if len(ter_dup1)>0:    
        ter_dup1.pop(0)
    return locals()
    ###sfarsit cod1347 pt a pune in array-ul array_terapeuti_ziua_respectiva terapeutii cu intervalul in care lucreaza:['Catalin','7-16','Mari','14-23','Lidia','all',etc]
def pune_Oana(matrix_TA1):
    #if ("Oana" in ter_dim)==True:
    lenm=len(matrix_TA1[0])
    for i1 in range(7):
        i3=0
        contor=0
        for i2 in matrix_TA1[i1]:
            if contor<6:
                if len(i2)>5:
                    if i2[0]+i2[1]+i2[2]+i2[3]+i2[4]=='Frecv':
                        matrix_TA1[i1][i3]='Frecv-CR-Oana'
                        contor=contor+1
                    if i2[0]+i2[1]+i2[2]+i2[3]+i2[4]=='CROMO':
                        matrix_TA1[i1][i3]='CROMO-Oana'
                        contor=contor+1
                    if i2[0]+i2[1]+i2[2]+i2[3]+i2[4]=='LAMPA':
                        matrix_TA1[i1][i3]='Frecv-Oana'
                        contor=contor+1    
                    if i2[0]+i2[1]+i2[2]+i2[3]+i2[4]+i2[5]=='TAHION':
                        matrix_TA1[i1][i3]='TAHION-Oana'
                        contor=contor+1    
                i3=i3+1
                if i3>=lenm:
                    break
            else:
                break    
                    
    return locals()

def pune_sambata(matrix_TA1,array_datele_orar_p,nr_pacienti):
    i10=0
    for i1 in range(5,8):
        i3=0
        for i2 in matrix_TA1[i1]:
            pozitia = i10%(len(matrix_TA1[i1]))
            if len(i2)>5:
                if i2[0]+i2[1]+i2[2]+i2[3]=='SAUN':
                    if (array_datele_orar_p[-(nr_pacienti-pozitia)*19+1])!=None:
                        if ('BAIE OZON' in (array_datele_orar_p[-(nr_pacienti-pozitia)*19+1]))==True:
                            i4=(i2.split("-"))[1]
                            matrix_TA1[i1][i3]='BAIE OZON'+'-'+i4
                        else:
                            i4=(i2.split("-"))[1]
                            matrix_TA1[i1][i3]='FARA BAIE OZON'+'-'+i4   
            i3+=1            
            i10+=1
    return locals()

def pune_duminica(matrix_TA1,array_datele_orar_p,nr_pacienti):
    i10=0
    for i1 in range(5,8):
        i3=0
        for i2 in matrix_TA1[i1]:
            pozitia = i10%(len(matrix_TA1[i1]))
            if len(i2)>5:
                if i2[0]+i2[1]+i2[2]+i2[3]=='BAIE':
                    if (array_datele_orar_p[-(nr_pacienti-pozitia)*19+1])!=None:
                        if ('SAUNA' in (array_datele_orar_p[-(nr_pacienti-pozitia)*19+1]))==True:
                            i4=(i2.split("-"))[1]
                            matrix_TA1[i1][i3]='SAUNA'+'-'+i4
                    if ((array_datele_orar_p[-(nr_pacienti-pozitia)*19+4]))==None:
                        pass
                           
            i3+=1            
            i10+=1
    return locals()  