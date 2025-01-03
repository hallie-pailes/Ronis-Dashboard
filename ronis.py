import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

import streamlit as st
import plotly.express as px
#from prophet import Prophet
#run using streamlit run ronis.py

aprilFile = pd.read_csv('april_2024.csv')
mayFile = pd.read_csv('may_2024.csv')
juneFile = pd.read_csv('june_2024.csv', encoding='latin-1') #this one had some sort of issue when reading, but encoding='latin-1' fixes it
julyFile = pd.read_csv('july_2024.csv')
augustFile = pd.read_csv('august_2024.csv')
septemberFile = pd.read_csv('september_2024.csv')
octoberFile = pd.read_csv('october_2024.csv')

#Order # - indx 0 	Sent Date - indx 1	Modifier - indx 2	Option Group Name - indx 3 	Parent Menu Selection - indx 4 	Order ID - indx 5 
#april_rows = [list(row) for row in aprilFile.values]
#print(april_rows)

#   APRIL
# Total orders:
aprilFile['Sent Date'] = pd.to_datetime(aprilFile['Sent Date']) #to_datetime changes it to a format where we can read the day, month, and year by using pandas day month and year keywords
total_orders_april = aprilFile['Order ID'].nunique() #.nunique() returns the number of unique values in a series, so this will give us the total number of orders

# Monthly Data:
#Add day month and hour properties to our file
aprilFile['Day'] = aprilFile['Sent Date'].dt.dayofweek  #.dayofweek gets the number of the day of the week with 0 = Monday -> 6 = Sunday, need .dt in front because that is how we access those time/date properties of our datetimelike values
aprilFile['Hour'] = aprilFile['Sent Date'].dt.hour #.hout gets the hour 

april_days = aprilFile.groupby('Day')['Order ID'].nunique() #.groupby groups the data by Day, then we can use ['Order ID'].nunique() to get the number of orders for each day
#print(april_days)
april_hours = aprilFile.groupby('Hour')['Order ID'].nunique()

# Most Popular:
april_popular = aprilFile['Parent Menu Selection'].value_counts() #.value_counts computes a histogram of a 1D array of values - so it will count the number of times each menu item appears
#print(april_popular)
april_modifiers = aprilFile['Modifier'].value_counts()
#print(april_modifiers)

#   MAY
# Total orders:
mayFile['Sent Date'] = pd.to_datetime(mayFile['Sent Date']) 
total_orders_may = mayFile['Order ID'].nunique() 

# Date Data:
mayFile['Day'] = mayFile['Sent Date'].dt.dayofweek  
mayFile['Hour'] = mayFile['Sent Date'].dt.hour 

may_days = mayFile.groupby('Day')['Order ID'].nunique()
may_hours = mayFile.groupby('Hour')['Order ID'].nunique()

# Most Popular
may_popular = mayFile['Parent Menu Selection'].value_counts() 
may_modifiers = mayFile['Modifier'].value_counts()

#   JUNE
# Total orders:
juneFile['Sent Date'] = pd.to_datetime(juneFile['Sent Date'])
total_orders_june = juneFile['Order ID'].nunique()

# Date Data:
juneFile['Day'] = juneFile['Sent Date'].dt.dayofweek
juneFile['Hour'] = juneFile['Sent Date'].dt.hour

june_days = juneFile.groupby('Day')['Order ID'].nunique()
june_hours = juneFile.groupby('Hour')['Order ID'].nunique()

# Most Popular
june_popular = juneFile['Parent Menu Selection'].value_counts() 
june_modifiers = juneFile['Modifier'].value_counts()

#   JULY
# Total orders:
julyFile['Sent Date'] = pd.to_datetime(julyFile['Sent Date'])
total_orders_july = julyFile['Order ID'].nunique()

# Date Data:
julyFile['Day'] = julyFile['Sent Date'].dt.dayofweek
julyFile['Hour'] = julyFile['Sent Date'].dt.hour

july_days = julyFile.groupby('Day')['Order ID'].nunique()
july_hours = julyFile.groupby('Hour')['Order ID'].nunique()

# Most Popular
july_popular = julyFile['Parent Menu Selection'].value_counts() 
july_modifiers = julyFile['Modifier'].value_counts()

#   AUGUST
# Total orders:
augustFile['Sent Date'] = pd.to_datetime(augustFile['Sent Date'])
total_orders_august = augustFile['Order ID'].nunique()

# Date Data:
augustFile['Day'] = augustFile['Sent Date'].dt.dayofweek
augustFile['Hour'] = augustFile['Sent Date'].dt.hour

august_days = augustFile.groupby('Day')['Order ID'].nunique()
august_hours = augustFile.groupby('Hour')['Order ID'].nunique()

# Most Popular
august_popular = augustFile['Parent Menu Selection'].value_counts() 
august_modifiers = augustFile['Modifier'].value_counts()

#   SEPTEMBER
# Total orders:
septemberFile['Sent Date'] = pd.to_datetime(septemberFile['Sent Date'])
total_orders_september = septemberFile['Order ID'].nunique()

# Date Data:
septemberFile['Day'] = septemberFile['Sent Date'].dt.dayofweek
septemberFile['Hour'] = septemberFile['Sent Date'].dt.hour

september_days = septemberFile.groupby('Day')['Order ID'].nunique()
september_hours = septemberFile.groupby('Hour')['Order ID'].nunique()

# Most Popular
september_popular = septemberFile['Parent Menu Selection'].value_counts() 
september_modifiers = septemberFile['Modifier'].value_counts()

#   OCTOBER
# Total orders:
octoberFile['Sent Date'] = pd.to_datetime(octoberFile['Sent Date'])
total_orders_october = octoberFile['Order ID'].nunique()

# Date Data:
octoberFile['Day'] = octoberFile['Sent Date'].dt.dayofweek
octoberFile['Hour'] = octoberFile['Sent Date'].dt.hour

october_days = octoberFile.groupby('Day')['Order ID'].nunique()
october_hours = octoberFile.groupby('Hour')['Order ID'].nunique()

# Most Popular
october_popular = octoberFile['Parent Menu Selection'].value_counts() 
october_modifiers = octoberFile['Modifier'].value_counts()

#   ALL
# Total Time
total_days = april_days + may_days + june_days + july_days + august_days + september_days + october_days

total_days.index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Output the results to check:
print(f"Total Orders in April: {total_orders_april}")
print(f"Total Orders in May: {total_orders_may}")
print(f"Total Orders in June: {total_orders_june}")
print(f"Total Orders in July: {total_orders_july}")
print(f"Total Orders in August: {total_orders_august}")
print(f"Total Orders in September: {total_orders_september}")
print(f"Total Orders in October: {total_orders_october}")

#print(aprilFile)

x = np.array(["April", "May", "June", "July", "August", "September", "October"])
y = np.array([total_orders_april, total_orders_may, total_orders_june, total_orders_july, total_orders_august, total_orders_september, total_orders_october])
col1, col2, col3 = st.columns([1, 2.7, 1.3], vertical_alignment="center")  # [1, 3, 1] defines relative column widths
with col2:
    st.image("ronis2.png", use_container_width=True)
    #st.header("- Interactive Dashboard - ")
st.markdown('<div style="text-align: center"><h1> Interactive Dashboard </h1></div>', unsafe_allow_html=True)

#Monthly sales graph
monthly_sales = np.array([total_orders_april, total_orders_may, total_orders_june, total_orders_july, total_orders_august, total_orders_september, total_orders_october])
months = np.array(["April", "May", "June", "July", "August", "September", "October"])

fig = px.line(x=x, y=y, title = "Monthly Sales", labels = {'x': "Month", 'y':"Order Count"}, markers = True, color_discrete_sequence = ["orange"])
#fig.show()
st.plotly_chart(fig)

selected_month = st.selectbox('Select Month', options=["April", "May", "June", "July", "August", "September", "October"])

if selected_month == "April":
    orders_by_day = april_days
    orders_by_hour = april_hours
    popular_items = april_popular 
    prev_month_orders = 0 
    curr_month_total = total_orders_april
elif selected_month == "May":
    orders_by_day = may_days
    orders_by_hour = may_hours
    popular_items = may_popular
    prev_month_orders = total_orders_april
    curr_month_total = total_orders_may
elif selected_month == "June":
    orders_by_day = june_days
    orders_by_hour = june_hours
    popular_items = june_popular
    prev_month_orders = total_orders_may
    curr_month_total = total_orders_june
elif selected_month == "July":
    orders_by_day = july_days
    orders_by_hour = july_hours
    popular_items = july_popular
    prev_month_orders = total_orders_june
    curr_month_total = total_orders_july
elif selected_month == "August":
    orders_by_day = august_days
    orders_by_hour = august_hours
    popular_items = august_popular
    prev_month_orders = total_orders_july
    curr_month_total = total_orders_august
elif selected_month == "September":
    orders_by_day = september_days
    orders_by_hour = september_hours
    popular_items = september_popular
    prev_month_orders = total_orders_august
    curr_month_total = total_orders_september
elif selected_month == "October":
    orders_by_day = october_days
    orders_by_hour = october_hours
    popular_items = october_popular
    prev_month_orders = total_orders_september
    curr_month_total = total_orders_october

#Plot by day depending on month selected
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
fig_day = px.bar(orders_by_day, x=days_of_week, y=orders_by_day.values, title=f"Orders by Day of the Week ({selected_month})",labels = {'x': "Day", 'y':"Order Count"}, color_discrete_sequence = ["orange"])
st.plotly_chart(fig_day)

left_column, right_column = st.columns(2)

with left_column:
    #calculate the change in orders between the selected month and the previous month - KPI Metric?
    if prev_month_orders > 0:
        change_in_orders = curr_month_total - prev_month_orders
        change_percent = (change_in_orders / prev_month_orders) * 100
    else:
        change_in_orders = curr_month_total
        change_percent = None

    if change_percent is not None:
        if change_in_orders >= 0:
            st.metric(label=f"Change in Orders ({selected_month})", value=f"{change_in_orders}", delta=f"+{change_percent:.2f}%", delta_color="normal") #use st.metric() to display change in orders
        else:
            st.metric(label=f"Change in Orders ({selected_month})", value=f"{change_in_orders}", delta=f"{change_percent:.2f}%", delta_color="normal")
    else:
        #case where theres no change_percent, like for the first month
        st.metric(label=f"Change in Orders ({selected_month})", value=f"{change_in_orders}", delta="N/A", delta_color="off")

with right_column:
    #Top 5 most popular for that month
    st.subheader(f"Most Popular Menu Items in {selected_month.capitalize()}")
    st.write(popular_items.head()) #.head() gives first 5 rows (default)

# 3. **Order Trends by Time of Day**
time_of_day_orders = orders_by_hour.reset_index()
fig_time_of_day = px.line(time_of_day_orders, x='Hour', y='Order ID', title=f"Orders by Hour in {selected_month}", labels={'Order ID': 'Total Orders', 'Hour': 'Hour of the Day'}, color_discrete_sequence = ["orange"])
fig_time_of_day.update_xaxes(range=[8, 23])
st.plotly_chart(fig_time_of_day)
#fig_time_of_day.update_xaxes(range=[9, 23])
#fig_time_of_day.update_layout(xaxis_range=[9, 23])

print(april_popular)
fig_pie = px.pie(juneFile, names='Modifier', title="Sales by Menu Item")
st.plotly_chart(fig_pie)
