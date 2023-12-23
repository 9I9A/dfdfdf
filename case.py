#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('menu.csv')
#Гипотеза 1
print('Завтрак имеет большее кол во полезных веществ по сравнению с Рыбой и Курицей')

healthier = df.groupby(by = 'Category')['Sugars'].mean()
sug_break = healthier['Breakfast']
sug_chic = healthier['Chicken & Fish']
healthier1 = df.groupby(by = 'Category')['Vitamin A (% Daily Value)'].mean()
vita_break = healthier1['Breakfast']
vita_chic = healthier1['Chicken & Fish']
print('Витамины А в завтраках', round(vita_break,2),'Витамины А в Рыбе и Курице', round(vita_chic, 2))
healthier2 = df.groupby(by = 'Category')['Vitamin C (% Daily Value)'].mean()
vitc_break = healthier2['Breakfast']
vitc_chic = healthier2['Chicken & Fish']
print('Витамины C в завтраках', round(vitc_break,2),'Витамины C в Рыбе и Курице', round(vitc_chic, 2))
print('Гипотеза опровергнута')
s = pd.Series(data=[sug_break, sug_chic, vita_break, vita_chic, vitc_break, vitc_chic], index = ['Завтраки', 'Курица и Рыба', 'Затраки', 'Курица и Рыба', 'Завтраки', 'Курица и Рыба', ])
s.plot(kind = 'bar')
plt.show()



#Гипотеза 2
print('Холестерина содержится больше чем протеина в напитках')

mcdon = df.groupby(by = 'Category')['Cholesterol'].mean()
chol_dr = mcdon['Coffee & Tea']
chol_dr2 = mcdon['Smoothies & Shakes']
print('Холестерина в напитках:', 'в горячих напитках:', round(chol_dr, 2), 'в молочных напитках:', round(chol_dr2, 2))
mcdon2 = df.groupby(by = 'Category')['Protein'].mean()
pr_dr = mcdon2['Coffee & Tea']
pr_dr2 = mcdon2['Smoothies & Shakes']
print('Протеина в напитках:', 'в горячих напитках:', round(pr_dr, 2), 'в молочных напитках:', round(pr_dr2, 2))
print('Гипотеза подтверждена')
#s = pd.Series(data=[chol_dr, chol_dr2, pr_dr, pr_dr2], index = ['Холестерин в горячих напитках', 'Холестерин в молочных напитках', 'Протеин в горячих напитках', 'Протеин в молочных напитках'])
#s.plot(kind='pie')
#plt.show()



