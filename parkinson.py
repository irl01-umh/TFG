# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:54:30 2024

@author: Inma Ramírez
"""

import pandas as pd

#Carga de train_peptides.csv, train_proteins.csv y train_clinical_data.csv
train_peptides = pd.read_csv('train_peptides.csv')
train_peptides

train_proteins = pd.read_csv('train_proteins.csv')
train_proteins

train_clinical_data = pd.read_csv('train_clinical_data.csv')
train_clinical_data

supplemental_clinical_data = pd.read_csv('supplemental_clinical_data.csv')
supplemental_clinical_data


# train_peptides.csv x train_clinical_data.csv

#frecuencia de patient_id
frecuencia_pep_patientid = train_peptides['patient_id'].value_counts()
print(frecuencia_pep_patientid)

frecuencia_clinic_patientid = train_clinical_data['patient_id'].value_counts()
print(frecuencia_clinic_patientid)

#datos ordenados
train_peptides_ordenado =  train_peptides['patient_id'].sort_values()
print(train_peptides_ordenado)

train_clinical_ordenado =  train_clinical_data['patient_id'].sort_values()
print(train_clinical_ordenado)


#frecuencia de visit_id
frecuencia_pep_visitid = train_peptides['visit_id'].value_counts()
print(frecuencia_pep_visitid)

frecuencia_clinic_visitid = train_clinical_data['visit_id'].value_counts()
print(frecuencia_clinic_visitid)

#datos ordenados
train_peptides_ordenado_visit =  train_peptides['visit_id'].sort_values()
print(train_peptides_ordenado_visit)

train_clinical_ordenado_visit =  train_clinical_data['visit_id'].sort_values()
print(train_clinical_ordenado_visit)




# train_proteins.csv x train_clinical_data.csv

#frecuencia de patient_id
frecuencia_prot_patientid = train_proteins['patient_id'].value_counts()
print(frecuencia_prot_patientid)

frecuencia_clinic_patientid = train_clinical_data['patient_id'].value_counts()
print(frecuencia_clinic_patientid)

#datos ordenados
train_proteins_ordenado =  train_proteins['patient_id'].sort_values()
print(train_proteins_ordenado)

train_clinical_ordenado =  train_clinical_data['patient_id'].sort_values()
print(train_clinical_ordenado)


#frecuencia de visit_id
frecuencia_prot_visitid = train_proteins['visit_id'].value_counts()
print(frecuencia_prot_visitid)
  
frecuencia_clinic_visitid = train_clinical_data['visit_id'].value_counts()
print(frecuencia_clinic_visitid)

#datos ordenados
train_proteins_ordenado_visit =  train_proteins['visit_id'].sort_values()
print(train_proteins_ordenado_visit)

train_clinical_ordenado_visit =  train_clinical_data['visit_id'].sort_values()
print(train_clinical_ordenado_visit)




#frecuencias de Uniprot


frecuencia_peptidesUniProt = train_peptides['UniProt'].value_counts()
print(frecuencia_peptidesUniProt)

frecuencia_proteinsUniProt = train_proteins['UniProt'].value_counts()
print(frecuencia_proteinsUniProt)


#frecuencia_peptidesUniProt_ordenado = train_peptides['UniProt'].sort_values()
#print(frecuencia_peptidesUniProt_ordenado)

#frecuencia_proteinsUniProt_ordenado = train_proteins['UniProt'].sort_values()
#print(frecuencia_proteinsUniProt_ordenado)




#frecuencia de Peptides 

def depurador(cadena):
    import re
    return re.sub(r'\([^)]*\)', '', cadena)

train_peptides['Peptide'] = train_peptides['Peptide'].apply(depurador)

#datos actualizados
print(train_peptides)

frecuencia_peptides_peptides=train_peptides['Peptide'].value_counts()
print(frecuencia_peptides_peptides)

#frecuencia agrupados por Uniprot

frecuencia_conjunta = train_peptides.groupby(['Peptide', 'UniProt']).size().reset_index(name='frecuencia')
print(frecuencia_conjunta)


# NPX x UniProt

frecuencia_NPX_UniProt = train_proteins.groupby(['UniProt', 'NPX']).size().reset_index(name='frecuencia')
print(frecuencia_NPX_UniProt)







# train_clinical_data.csv y supplemental_clinical_data.csv

faltantes_updrs_4 = train_clinical_data['updrs_4'].isnull().sum().sum()
print("Total de valores faltantes updrs_4:", faltantes_updrs_4)

faltantes_upd23b = train_clinical_data['upd23b_clinical_state_on_medication'].isnull().sum().sum()
print("Total de valores faltantes upd23b:", faltantes_upd23b)



faltantes_updrs_4 = supplemental_clinical_data['updrs_4'].isnull().sum().sum()
print("Total de valores faltantes updrs_4:", faltantes_updrs_4)


faltantes_upd23b = supplemental_clinical_data['upd23b_clinical_state_on_medication'].isnull().sum().sum()
print("Total de valores faltantes upd23b:", faltantes_upd23b)


#train_Clinical_Data

registros_por_paciente= train_clinical_data['patient_id'].value_counts()
print(registros_por_paciente)

pacientes_faltantes_updrs_4 = train_clinical_data.groupby(['patient_id', 'updrs_4']).size().reset_index(name='frecuencia')
print(pacientes_faltantes_updrs_4)

pacientes_faltantes_upd23b = train_clinical_data.groupby(['patient_id', 'upd23b_clinical_state_on_medication']).size().reset_index(name='frecuencia')
print(pacientes_faltantes_upd23b)

#supplemetal_clinical_Data

registros_por_paciente_S= supplemental_clinical_data['patient_id'].value_counts()
print(registros_por_paciente_S)

pacientes_faltantes_updrs_4_S =supplemental_clinical_data.groupby(['patient_id', 'updrs_4']).size().reset_index(name='frecuencia')
print(pacientes_faltantes_updrs_4_S)

pacientes_faltantes_upd23b_S = supplemental_clinical_data.groupby(['patient_id', 'upd23b_clinical_state_on_medication']).size().reset_index(name='frecuencia')
print(pacientes_faltantes_upd23b_S)

#visitas por paciente

visitas_paciente=train_clinical_data.groupby(['patient_id', 'visit_id']).size().reset_index(name='frecuencia')
print(visitas_paciente) #108

visitas_paciente_s=supplemental_clinical_data.groupby(['patient_id', 'visit_id']).size().reset_index(name='frecuencia')
print(visitas_paciente_s) 