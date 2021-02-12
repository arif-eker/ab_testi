#
#
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
from scipy.stats import shapiro

# Test Grubu (max bidding)
test_group = pd.read_excel("data/ab_testing_data.xlsx", sheet_name="Test Group")
test_group.head()

# Kontrol Grubu (avg bidding)
control_group = pd.read_excel("data/ab_testing_data.xlsx", sheet_name="Control Group")
control_group.head()


test_purchase = test_group[["Purchase"]]
control_purchase = control_group[["Purchase"]]

test_purchase.head()
control_purchase.head()


# Varsayım Kontrolleri

# 1 - Normallik Dağılım Varsayımı
# 2 - Varyans Homojenliği

# Normallik Varsayımı

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:... sağlanmamaktadır.

# p - value < ise 0.05'ten HO RED.
# p - value < değilse 0.05 H0 REDDEDİLEMEZ.


test_purchase.shape[0]
control_purchase.shape[0]

shapiro(test_purchase["Purchase"])[1] < 0.05  # H0 Reddedilemez
shapiro(test_purchase["Purchase"])[1]

shapiro(control_purchase["Purchase"])[1] < 0.05  # H0 Reddedilemez



# Varyans Homojenliği

# H0: Varyanslar homojendir
# H1: Varyanslar homojen değildir

# p - value < ise 0.05'ten HO RED.
# p - value < değilse 0.05 H0 REDDEDILEMEZ.

stats.levene(control_purchase["Purchase"], test_purchase["Purchase"])[1] < 0.05  # H0 Reddedilemez



# 1.1 Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test)
test_istatistigi, pvalue = stats.ttest_ind(control_purchase["Purchase"],
                                           test_purchase["Purchase"],
                                           equal_var=True)

print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))


# H0: M1 = M2 (... iki grup ortalamaları arasında ist ol.anl.fark yoktur.)
# H1: M1 != M2 (...vardır)

# p-value < ise 0.05 'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.

# Bu durumda H0 reddedilemez. Yani iki grup arasında istatistiksel olarak anlamlı bir fark yoktur.