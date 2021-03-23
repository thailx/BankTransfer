import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("D:\PycharmProjects\pythonProject\S2_DataFile.csv")

# Convert datetime
df['TRAN_TIME'] = pd.to_datetime(df['TRAN_TIME'], format='%d/%m/%Y %H:%M')

# Check values
mask = df['AMOUNT'] > 0
df = df[mask]

df['TRAN_HOUR'] = df['TRAN_TIME'].dt.strftime('%H')

# 1.Bieu do pie ve ty le so tien giao dich tren cac kenh
sum_AMT_byChannel = df.groupby(['CHANNEL_ID'])['AMOUNT'].sum().reset_index(name='SUM_AMT_BY_CHN')
print(sum_AMT_byChannel)

df_plot = sum_AMT_byChannel
df_plot = df_plot.set_index('CHANNEL_ID')
print(df_plot)
plot = df_plot.plot.pie(y='SUM_AMT_BY_CHN', subplots=True, figsize=(8, 8))

plt.title("DOANH SỐ GIAO DỊCH THEO KÊNH")
plt.ylabel("")
plt.show()

# 2.Bieu do doanh va so luong giao dich tren cac kenh giao dich
count_byChannel = df.groupby(['CHANNEL_ID']).size().reset_index(name='COUNTS')
print(count_byChannel)
df_plot2 = sum_AMT_byChannel.merge(count_byChannel, on=['CHANNEL_ID'])
print(df_plot2)
df_plot2 = df_plot2.set_index('CHANNEL_ID')
print(df_plot2)

# Quy đổi dữ liệu Doanh số về phần trăm để biểu diễn tính tương quan của dữ liệu
max_amt = df_plot2['SUM_AMT_BY_CHN'].max()
df_plot2['%_DOANHSO'] = df_plot2['SUM_AMT_BY_CHN'] * 100 / max_amt
# Quy đổi dữ liệu Số lượng giao dịch về phần trăm để biểu diễn tính tương quan của dữ liệu
max_count = df_plot2['COUNTS'].max()
df_plot2['%_SOLUONG'] = df_plot2['COUNTS'] * 100 / max_count
print(df_plot2)

df_plot2.plot.bar(y=['%_SOLUONG', '%_DOANHSO'])
plt.title("Tỷ lệ doanh số và số lượng giao dịch theo các kênh", fontsize=22)
plt.ylabel('tỷ lệ %')
plt.xticks(rotation=0)
plt.show()

# 3.Số lieu giao dich trung binh trong tung gio trong ngay
count_byChannel = df.groupby(['CHANNEL_ID']).size().reset_index(name='COUNTS')
print(count_byChannel)
df_plot2 = sum_AMT_byChannel.merge(count_byChannel, on=['CHANNEL_ID'])
print(df_plot2)
df_plot2 = df_plot2.set_index('CHANNEL_ID')
print(df_plot2)

# Quy đổi dữ liệu Doanh số về phần trăm để biểu diễn tính tương quan của dữ liệu
max_amt = df_plot2['SUM_AMT_BY_CHN'].max()
df_plot2['%_DOANHSO'] = df_plot2['SUM_AMT_BY_CHN'] * 100 / max_amt
# Quy đổi dữ liệu Số lượng giao dịch về phần trăm để biểu diễn tính tương quan của dữ liệu
max_count = df_plot2['COUNTS'].max()
df_plot2['%_SOLUONG'] = df_plot2['COUNTS'] * 100 / max_count
print(df_plot2)

df_plot2.plot.bar(y=['%_SOLUONG', '%_DOANHSO'])
plt.title("Tỷ lệ doanh số và số lượng giao dịch theo các kênh", fontsize=22)
plt.ylabel('tỷ lệ %')
plt.xticks(rotation=0)
plt.show()
df.to_csv('DB_Bank.csv')
