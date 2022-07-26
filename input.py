from promo_scheduling.entity import Mechanic, Partner, Promotion, SystemSettings

system_settings = SystemSettings(min_duration=3)

dz_1 = Mechanic('DZ1', 28)
dz_4 = Mechanic('DZ4', 4)
dz_8 = Mechanic('DZ8', 2)

amz = Partner('Amazon', 7)
nike = Partner('Nike', 7)
acom = Partner('Americanas', 7)
suba = Partner('Submarino', 7)

amz_jobs = [
    Promotion(
        partner=amz,
        mechanic=dz_1,
        productivity_ref=1000
    ),
    Promotion(
        partner=amz,
        mechanic=dz_4,
        productivity_ref=3000
    ),
    Promotion(
        partner=amz,
        mechanic=dz_8,
        productivity_ref=5000
    )
]

nike_jobs = [
    Promotion(
        partner=nike,
        mechanic=dz_1,
        productivity_ref=2000
    ),
    Promotion(
        partner=nike,
        mechanic=dz_4,
        productivity_ref=5000
    ),
    Promotion(
        partner=nike,
        mechanic=dz_8,
        productivity_ref=6000
    )
]

acom_jobs = [
    Promotion(
        partner=acom,
        mechanic=dz_1,
        productivity_ref=5000
    ),
    Promotion(
        partner=acom,
        mechanic=dz_4,
        productivity_ref=10000
    ),
    Promotion(
        partner=acom,
        mechanic=dz_8,
        productivity_ref=15000
    )
]

suba_jobs = [
    Promotion(
        partner=suba,
        mechanic=dz_1,
        productivity_ref=5000
    ),
    Promotion(
        partner=suba,
        mechanic=dz_4,
        productivity_ref=10000
    ),
    Promotion(
        partner=suba,
        mechanic=dz_8,
        productivity_ref=15000
    )
]

possible_promotions = [*amz_jobs, *nike_jobs, *acom_jobs]  # , *suba_jobs]
partners = [amz, nike, acom]  # , suba]
mechanics = [dz_1, dz_4, dz_8]
