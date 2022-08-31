from promo_scheduling.entity import Mechanic, Partner, Promotion, SystemSettings
import pandas as pd
from google.cloud import bigquery

client = bigquery.Client()
project = "dotzcloud-datalabs-datascience"
dataset_id = "DATA_SCIENCE_TEMP"

dataset_ref = bigquery.DatasetReference(project, dataset_id)
table_ref = dataset_ref.table("OTIMIZADOR_DADOS")
table = client.get_table(table_ref)

df = client.list_rows(table).to_dataframe()

# Productivity
partners_names=['AMAZON','Magazine Luiza.com','Americanas.com','Submarino']
partners=['amzn','mglu','amer','subm']
mechanics=['DZ_2','DZ_4','DZ_8']

dic={}
for p in partners:
    for m in mechanics:
        index=partners.index(p)
        dic[p+'_'+m]=0 if pd.isna(df.loc[(df['NomeParceiro']==partners_names[index])&(df['PromoAjust'] == m)]['CliePorDia'].mean()) \
                       else df.loc[(df['NomeParceiro'] == partners_names[index])&(df['PromoAjust'] == m)]['CliePorDia'].mean()

system_settings = SystemSettings(min_duration=3)

dz_2 = Mechanic('DZ2', 28)
dz_4 = Mechanic('DZ4', 4)
dz_8 = Mechanic('DZ8', 2)

amzn = Partner('Amazon', 7)
mglu = Partner('Magalu', 7)
amer = Partner('Americanas', 7)
subm = Partner('Submarino', 7)

amzn_jobs = [
    Promotion(
        partner=amzn,
        mechanic=dz_2,
        productivity_ref=dic['amzn_DZ_2']
    ),
    Promotion(
        partner=amzn,
        mechanic=dz_4,
        productivity_ref=dic['amzn_DZ_4']
    ),
    Promotion(
        partner=amzn,
        mechanic=dz_8,
        productivity_ref=dic['amzn_DZ_8']
    )
]

mglu_jobs = [
    Promotion(
        partner=mglu,
        mechanic=dz_2,
        productivity_ref=dic['mglu_DZ_2']
    ),
    Promotion(
        partner=mglu,
        mechanic=dz_4,
        productivity_ref=dic['mglu_DZ_4']
    ),
    Promotion(
        partner=mglu,
        mechanic=dz_8,
        productivity_ref=dic['mglu_DZ_8']
    )
]

amer_jobs = [
    Promotion(
        partner=amer,
        mechanic=dz_2,
        productivity_ref=dic['amer_DZ_2']
    ),
    Promotion(
        partner=amer,
        mechanic=dz_4,
        productivity_ref=dic['amer_DZ_4']
    ),
    Promotion(
        partner=amer,
        mechanic=dz_8,
        productivity_ref=dic['amer_DZ_8']
    )
]

subm_jobs = [
    Promotion(
        partner=subm,
        mechanic=dz_2,
        productivity_ref=dic['subm_DZ_2']
    ),
    Promotion(
        partner=subm,
        mechanic=dz_4,
        productivity_ref=dic['subm_DZ_4']
    ),
    Promotion(
        partner=subm,
        mechanic=dz_8,
        productivity_ref=dic['subm_DZ_8']
    )
]

possible_promotions = [*amzn_jobs, *mglu_jobs, *amer_jobs] #, *subm_jobs]
partners = [amzn, mglu, amer]  # , subm]
mechanics = [dz_2, dz_4, dz_8]
