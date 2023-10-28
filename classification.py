#kütüphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri yükleme
veriler = pd.read_csv('veriler.txt')

print(veriler)

#veri ön işleme
boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy','kilo']]
print(boykilo)

x=10