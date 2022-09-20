from promo_scheduling.entity import Mechanic, Partner, Promotion, SystemSettings
import pandas as pd
from google.cloud import bigquery

system_settings = SystemSettings(min_duration=3)

project = "dotzcloud-datalabs-datascience"
dataset_id = "DATA_SCIENCE_TEMP"
table_id = "OTIMIZADOR_DADOS"

# partners_names=['AMAZON','Magazine Luiza.com','Americanas.com','Submarino']
# # ['AMAZON','Americanas.com','Magazine Luiza.com','Netshoes','Casas Bahia','Submarino','Shop Time','RENNER','Ponto Frio','EXTRA.COM']
# partners_availability=[7,7,7,7]
# mechanics_names=[['DZ_2','DZ_3','DZ_4','DZ_5'],
#                  ['DZ_8','DZ_9','DZ_10','DZ_11','DZ_12'],
#                  ['DZ_14','DZ_15','DZ_16','DZ_17','DZ_18','DZ_19','DZ_20']]
# mechanics_availability=[28,4,4]

partners_names=['AMAZON','Americanas.com','Magazine Luiza.com','Submarino']
# ['AMAZON','Americanas.com','Magazine Luiza.com','Netshoes','Casas Bahia','Submarino','Shop Time','RENNER','Ponto Frio','EXTRA.COM']
partners_availability=[7,7,7,7]
mechanics_names=[['DZ_2','DZ_3','DZ_4'],
                 ['DZ_10','DZ_11','DZ_12'],
                 ['DZ_14','DZ_15','DZ_16','DZ_17','DZ_18','DZ_19','DZ_20']]
mechanics_availability=[28,3,0]

client = bigquery.Client()
dataset_ref = bigquery.DatasetReference(project, dataset_id)
table_ref = dataset_ref.table(table_id)
table = client.get_table(table_ref)
df = client.list_rows(table).to_dataframe()

def productivity_base(df,partners_names,mechanics_names):
    df_filter=df.loc[(df['NomeParceiro']==partners_names)&(df['PromoAjust'].isin(mechanics_names))]
    if df_filter['DistinctDays'].sum()==0:
        result=0
    else:
        result = df_filter['Clientes'].sum()/df_filter['DistinctDays'].sum()
    return result    

mechanic_a = Mechanic(mechanics_names[0],mechanics_availability[0])
mechanic_b = Mechanic(mechanics_names[1],mechanics_availability[1])
mechanic_c = Mechanic(mechanics_names[2],mechanics_availability[2])

partner_a = Partner(partners_names[0], partners_availability[0])
partner_b = Partner(partners_names[1], partners_availability[1])
partner_c = Partner(partners_names[2], partners_availability[2])
partner_d = Partner(partners_names[3], partners_availability[3])

partner_a_jobs = [
    Promotion(
        partner=partner_a,
        mechanic=mechanic_a,
        productivity_ref=productivity_base(df,
            partners_names=partners_names[0],mechanics_names=mechanics_names[0])
    ),
    Promotion(
        partner=partner_a,
        mechanic=mechanic_b,
        productivity_ref=productivity_base(df,
            partners_names=partners_names[0],mechanics_names=mechanics_names[1])
    ),
    Promotion(
        partner=partner_a,
        mechanic=mechanic_c,
        productivity_ref=productivity_base(df,
            partners_names=partners_names[0],mechanics_names=mechanics_names[2])
    )
]

partner_b_jobs = [
    Promotion(
        partner=partner_b,
        mechanic=mechanic_a,
        productivity_ref=productivity_base(df,
            partners_names=partners_names[1],mechanics_names=mechanics_names[0])
    ),
    Promotion(
        partner=partner_b,
        mechanic=mechanic_b,
        productivity_ref=productivity_base(df,
            partners_names=partners_names[1],mechanics_names=mechanics_names[1])
    ),
    Promotion(
        partner=partner_b,
        mechanic=mechanic_c,
        productivity_ref=productivity_base(df,
            partners_names=partners_names[1],mechanics_names=mechanics_names[2])
    )
]

partner_c_jobs = [
    Promotion(
        partner=partner_c,
        mechanic=mechanic_a,
        productivity_ref=productivity_base(df,
            partners_names=partners_names[2],mechanics_names=mechanics_names[0])
    ),
    Promotion(
        partner=partner_c,
        mechanic=mechanic_b,
        productivity_ref=productivity_base(df,
            partners_names=partners_names[2],mechanics_names=mechanics_names[1])
    ),
    Promotion(
        partner=partner_c,
        mechanic=mechanic_c,
        productivity_ref=productivity_base(df,
            partners_names=partners_names[2],mechanics_names=mechanics_names[2])
    )
]

partner_d_jobs = [
    Promotion(
        partner=partner_d,
        mechanic=mechanic_a,
        productivity_ref=productivity_base(df,
            partners_names=partners_names[3],mechanics_names=mechanics_names[0])
    ),
    Promotion(
        partner=partner_d,
        mechanic=mechanic_b,
        productivity_ref=productivity_base(df,
            partners_names=partners_names[3],mechanics_names=mechanics_names[1])
    ),
    Promotion(
        partner=partner_d,
        mechanic=mechanic_c,
        productivity_ref=productivity_base(df,
            partners_names=partners_names[3],mechanics_names=mechanics_names[2])
    )
]

possible_promotions = [*partner_a_jobs, *partner_b_jobs, *partner_c_jobs, *partner_d_jobs]
partners = [partner_a, partner_b, partner_c, partner_d]
mechanics = [mechanic_a, mechanic_b, mechanic_c]
