
# 3. COURSECON International Summer Seminars - 2023 July & August

# Genç Ekonomistler Kulübü

# Lecture: Dr. Şule Batbaylı / Uludag University

# Create (Applied) : Yasin Tosun / Siegen University 

####################### #######################################
## APPLIED PROBLEM SETS
####################### #######################################

# 1. Trade Deficit (Ticaret Açığı) & Trade Surplus (Ticaret Fazlası)

export_total = 500 # İhracat
import_total = 700 # ithalat

trade_balance = export_total - import_total

if trade_balance < 0 :
    print("Trade balance: ",abs(trade_balance), "(Ticaret Açığı)")
elif trade_balance > 0 :
    print("Trade Balance: ", abs(trade_balance), "(Ticaret Fazlası)")
else:
    print("Trade Balance: 0")

# 2. Ticaret / GSYIH Oranı

exports = 250 
imports = 200
GDP = 1000
trade_to_GDP_ratio = (exports + imports) / GDP
print("Trade-to-GDP Ratio: ", trade_to_GDP_ratio)

# 3. Mutlak Üstünlükler Teorisi

class Country:
    def __init__(self, name, cotton_cost):
        self.name = name
        self.cotton_cost = cotton_cost

# İki ülkeyi temsil eden nesneleri oluşturalım
country1 = Country("Ülke A", 20) #Ülke A nın pamuk maliyeti
country2 = Country("Ülke B", 15) # Ülke B nin pamuk maliyeti

# Maliyetleri karşılaştırarak mutalk üstünlükleri belirleyeim
if country1.cotton_cost < country2.cotton_cost :
    print(f"{country1.name}, pamuk üretiminde mutlak üstünlüğe sahiptir.")
elif country1.cotton_cost > country2.cotton_cost :
    print(f"{country2.name}, pamuk üretiminde mutlak üstünlüğe sahiptir.")
else:
    print("Her ülkede aynı maliyetle pamuk üretrebilmektedir")



# 4. Karşılaştırmalı Üartünlükler

class Country:
    def __init__(self, name, wheat_cost, rice_cost):
        self.name = name
        self.wheat_cost = wheat_cost
        self.rice_cost = rice_cost

# İki ülkeyi temsil eden nesneleri oluşturalım
country1 = Country("Ülke A", 2, 4)
country2 = Country("Ülke B", 3, 2)

# Buğday üretimini karşılaştırdık
if country1.wheat_cost < country2.wheat_cost:
    wheat_comparative_advantage = country1.name
elif country1.wheat_cost > country2.wheat_cost:
    wheat_comparative_advantage = country2.name
else:
    wheat_comparative_advantage = "Her iki ülkede aynı fırsat maliyetine sahiptir."


# Pirinç üretimini karşılaştırdık
if country1.rice_cost < country2.rice_cost:
    rice_comparative_advantage = country1.name
elif country1.rice_cost > country2.rice_cost:
    rice_comparative_advantage = country2.name
else:
    rice_comparative_advantage = "Her iki ülkede aynı fırsat maliyetine sahiptir."

# Sonuçlar
print("Buğday üretimi için mutlak üstünlük:{}".format(wheat_comparative_advantage))
print("Pirinç üretimi için mutlak üstünlük:{}".format(rice_comparative_advantage))

# 5. Balance Payment (Ödemeler Dengeleri)

import numpy as np
import matplotlib.pyplot as plt

# İhracat ve İthalat verileri
yıllar = [2016, 2017, 2018, 2019, 2020]
ithalat = [500,550,600,560,700]
ihracat = [400,450,500,550,600]

# Ticaret Dengesini hesapalam
ticaret_dengesi = np.subtract(ihracat,ithalat)

# Grafiğini çizdirme

plt.plot(yıllar, ticaret_dengesi)
plt.xlabel('Yıllar')
plt.ylabel('Ticaret Dengesi (Milyar Dolar')
plt.title('Ülkenin Mal Ticareti Dengesi')
plt.grid(True)
plt.show()


# 6. Current Account Balance 

import numpy as np
import matplotlib.pyplot as plt

# Yıllar
yıllar = [2016, 2017,2018,2019,2020]

# Kalemler
ticaret_dengesi =[100,120,150,130,140]
hizmet_dengesi = [-50, -60, -70, -80, -90]
gelir_dengesi = [-20, -30, -40, -50, -60]
transfer_dengesi = [-20, -10, -10, -15, -20]

# cari hesap dengesi
cari_hesap_dengesi = np.add(np.add(ticaret_dengesi, hizmet_dengesi),np.add(gelir_dengesi,transfer_dengesi))

# grafik
plt.plot(yıllar, cari_hesap_dengesi)
plt.xlabel('Yıllar')
plt.ylabel('Cari Hesap Dengesi (Milyar Dolar')
plt.title('Cari Hesap Dengesi')
plt.grid(True)
plt.show()


















