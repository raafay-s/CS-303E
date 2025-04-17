# Assignment: HW2
# File: Prefixes.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course: CS303E
#
# Date: 01/26/2025
# Description of Program: This program calculates & displays the percentage difference between decimal & binary prefixes

# Decimal and binary values
kilo = 10**3
mega = 10**6
giga = 10**9
tera = 10**12
peta = 10**15
exa = 10**18
zetta = 10**21
yotta = 10**24

kibi = 2**10
mebi = 2**20
gibi = 2**30
tebi = 2**40
pebi = 2**50
exbi = 2**60
zebi = 2**70
yobi = 2**80

# Calculating the percentage differences
kilo_kibi_diff = ((kibi - kilo) / kilo) * 100
mega_mebi_diff = ((mebi - mega) / mega) * 100
giga_gibi_diff = ((gibi - giga) / giga) * 100
tera_tebi_diff = ((tebi - tera) / tera) * 100
peta_pebi_diff = ((pebi - peta) / peta) * 100
exa_exbi_diff = ((exbi - exa) / exa) * 100
zetta_zebi_diff = ((zebi - zetta) / zetta) * 100
yotta_yobi_diff = ((yobi - yotta) / yotta) * 100

# Code for printing the table
print()
print(format("Dec/Bin", "20s") + format("diff", ">5s") + "%")
print("--------------------------")
print(format("kilo/kibi", "20s") + format(kilo_kibi_diff, "5.2f") + "%")
print(format("mega/mebi", "20s") + format(mega_mebi_diff, "5.2f") + "%")
print(format("giga/gibi", "20s") + format(giga_gibi_diff, "5.2f") + "%")
print(format("tera/tibi", "20s") + format(tera_tebi_diff, "5.2f") + "%")
print(format("peta/pebi", "20s") + format(peta_pebi_diff, "5.2f") + "%")
print(format("exa/exbi", "20s") + format(exa_exbi_diff, "5.2f") + "%")
print(format("zetta/zebi", "20s") + format(zetta_zebi_diff, "5.2f") + "%")
print(format("yotta/yobi", "20s") + format(yotta_yobi_diff, "5.2f") + "%")