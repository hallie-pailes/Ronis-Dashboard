'''
#for order count
april_days = []
april_orders = []
for i in range(len(april_rows)):
    x = april_rows[i][5]
    #print(x)
    result = x.split("-")
    day = int(result[0])
    order = int(result[1])
    #print(day, " ", order)
    april_days += [day]
    april_orders += [order]
april_order_count = 1
for i in range(len(april_days)-1):
    if (april_orders[i+1] != april_orders[i]):
        april_order_count += 1
print(april_order_count)

#for time
april_hours = []
april_time = {'00' : 0, '01' : 0, '02' : 0, '03' : 0, '04' : 0, '05' : 0, '06' : 0, '07' : 0, '08' : 0, '09' : 0, '10' : 0, '11' : 0, '12' : 0, '13' : 0, '14' : 0, '15' : 0, '16' : 0, '17' : 0, '18' : 0, '19' : 0, '20' : 0, '21' : 0, '22' : 0, '23' : 0, '24' : 0}
for i in range(len(april_rows)):
    x = april_rows[i][1]
    result = x.split(" ") #[date, time]
    #print(result)
    time = result[1].split(":") #[hour, minute, second]
    april_hours += [time[0]]
    #print(time)
hour_count = 1
for i in range(len(april_rows)-1):
    if ((april_hours[i+1] == april_hours[i]) & ((april_orders[i+1] != april_orders[i]))):
        #hour_count += 1
        if (april_time[april_hours[i]] == 0):
            april_time[april_hours[i]] += 2
        else:
            april_time[april_hours[i]] += 1
    #april_time[april_hours[i]] = hour_count
print (april_time)
print (april_time['11'] + april_time['12'] + april_time['13'] + april_time['14'] + april_time['15'] + april_time['16'] + april_time['17'] + april_time['18'] + april_time['19'] + april_time['20'] + april_time['21'] + april_time['22'])


#may - 31
may_rows = [list(row) for row in mayFile.values]

may_days = []
may_orders = []
for i in range(len(may_rows)):
    x = may_rows[i][5]
    result = x.split("-")
    day = int(result[0])
    order = int(result[1])
    may_days += [day]
    may_orders += [order]
may_order_count = 1
for i in range(len(may_days)-1):
    if (may_orders[i+1] != may_orders[i]):
        may_order_count += 1
print(may_order_count)

#june - 30
june_rows = [list(row) for row in juneFile.values]

june_days = []
june_orders = []
for i in range(len(june_rows)):
    x = june_rows[i][5]
    result = x.split("-")
    day = int(result[0])
    order = int(result[1])
    june_days += [day]
    june_orders += [order]
june_order_count = 1
for i in range(len(june_days)-1):
    if (june_orders[i+1] != june_orders[i]):
        june_order_count += 1
print(june_order_count)
#july - 31
july_rows = [list(row) for row in julyFile.values]

july_days = []
july_orders = []
for i in range(len(july_rows)):
    x = july_rows[i][5]
    result = x.split("-")
    day = int(result[0])
    order = int(result[1])
    july_days += [day]
    july_orders += [order]
july_order_count = 1
for i in range(len(july_days)-1):
    if (july_orders[i+1] != july_orders[i]):
        july_order_count += 1
print(july_order_count)
#august - 31
august_rows = [list(row) for row in augustFile.values]

august_days = []
august_orders = []
for i in range(len(august_rows)):
    x = august_rows[i][5]
    result = x.split("-")
    day = int(result[0])
    order = int(result[1])
    august_days += [day]
    august_orders += [order]
august_order_count = 1
for i in range(len(august_days)-1):
    if (august_orders[i+1] != august_orders[i]):
        august_order_count += 1
print(august_order_count)
#september - 30
september_rows = [list(row) for row in septemberFile.values]

september_days = []
september_orders = []
for i in range(len(september_rows)):
    x = september_rows[i][5]
    result = x.split("-")
    day = int(result[0])
    order = int(result[1])
    september_days += [day]
    september_orders += [order]
september_order_count = 1
for i in range(len(september_days)-1):
    if (september_orders[i+1] != september_orders[i]):
        september_order_count += 1
print(september_order_count)
#october - 31
october_rows = [list(row) for row in octoberFile.values]

october_days = []
october_orders = []
for i in range(len(october_rows)):
    x = october_rows[i][5]
    result = x.split("-")
    day = int(result[0])
    order = int(result[1])
    october_days += [day]
    october_orders += [order]
october_order_count = 1
for i in range(len(october_days)-1):
    if (october_orders[i+1] != october_orders[i]):
        october_order_count += 1
print(october_order_count)
'''

'''
# Step 1: Load Data
data = pd.read_csv('april_2024.csv')
data['Sent Date'] = pd.to_datetime(data['Sent Date'])
data['Month'] = data['Sent Date'].dt.month
data['Day'] = data['Sent Date'].dt.day

# Step 2: Create an Interactive Plot (Example: Orders by Day)
fig = px.bar(data, x='Day', title="Orders by Day of the Month", color='Month')

# Step 3: Add Streamlit Widgets (Dropdown)
selected_month = st.selectbox('Select Month', options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Step 4: Filter Data Based on Selected Month
filtered_data = data[data['Month'] == selected_month]
fig_filtered = px.bar(filtered_data, x='Day', title=f"Orders for Month {selected_month}")

# Step 5: Display Graph and Text
st.title("Roni's Mac Bar - Interactive Dashboard")
st.write(f"Showing orders for the selected month ({selected_month})")
st.plotly_chart(fig_filtered) '''

# Plot the sales by day of the week
'''total_days.plot(kind='bar', color='skyblue')
plt.title("Sales by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Order Count")
#plt.show()'''

'''plt.plot(x, y)
plt.ylim(0, 5000)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Order ID")'''