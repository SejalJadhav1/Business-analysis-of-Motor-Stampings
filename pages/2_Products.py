import pandas as pd
import streamlit as st
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Products"
)

data = pd.read_excel("bdm_alpha.xlsx")
data_pie = pd.read_excel("data_pie.xlsx")
st.subheader("About the Company's Products")

tab1, tab3, tab4= st.tabs(["Product Wise Sales", "Winter Sales", "Outliers"])

with tab1:
    st.write('''The company produces around twenty-one products ranging from sizes 73 x 38mm which is the smallest size product and 222 x 120 mm which is the largest size.
             These products are coded as A-T, A being the smallest size and T being the largest size as shown in the table for easy understanding while reading and for visualization.   
''')

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        horizontal_spacing = 0.01)

    fig.add_trace(go.Pie(labels=['F', 'M', 'C', 'E'], values=[1200, 989, 811.2, 760.0], name="2", scalegroup="one",
                         textinfo="label+value"),
                  1, 1)

    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

    fig.add_trace(go.Pie(labels=data_pie["Size"], values=data_pie["Profit"], name="1", scalegroup="one",
                         textinfo='percent+label'),
                  1, 2)

    fig.update_traces(textfont_size=15,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))

    fig.update_traces(hole=.3, hoverinfo="label+percent+name")

    fig.update_layout(
        title="Products Sales",
        font_family="Courier New",
        font_color="white",
        title_font_family="Bahnschrift Light",
        title_font_color="black",
        legend_title_font_color="green"
    )
    fig.update_layout(showlegend=False)
    fig.update_layout(height=370, width=600)

    st.write(fig)

    st.info('''The cumulative Profits incurred by the products in the month of October, November and December 2021
     was seen the least for D which was around 0.835% of the total profits (around Rs 9000). The maximum profit producing product was F which was around 13.5% of the total profit. 

F product can be considered in the small size product group. The group which has less profit as compared to other products since it has high production cost. But even after it being from the group of low profit producing products, it has the highest profit in these three months, and that is because of the demand or the amount of quantity demanded was highest for F by the clients. Therefore, more the sales of the product F result in more profit production by it. And hence the reason. ''')


with tab3:
    fig = px.scatter(data, x=data["Date"], y=data["Quantity Sold Kgs"],
                     size=data["Quantity Sold Kgs"], color="Quantity Sold Kgs",
                     title="Sales in Winter",
                     labels=dict(x="Date", y="Quantity Sold kgs"),
                     text=data.Size)
    fig.update_xaxes(title_font_family="Candara Light")
    fig.update_yaxes(title_font_family="Candara Light")

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Bahnschrift Light",
        title_font_color="black",
        legend_title_font_color="green"
    )
    st.write(fig)

    st.info('''
    According to the data analysed for the quantities sold in the month of October, November, and December it can be incurred that as the months go by the quantity of the products demanded increase. 

    During the winter season many companies demand for motors for manufacturing of Fans, Air Conditioners, Blowers, Exhausts, Coolers. 
    During summers all these products are in immense demand to be bought by the customers. Therefore, the companies begin the manufacturing process in the season of winter and keeps it fresh and ready till summers.   

    Further on during the summers the motors are used for manufacturing of water pumps which are then widely demanded during the rainy season.

    As a result, Light Motor Works has majority of their quantity being demanded and sold in the season of Winters and Summers. ''')

with tab4:

    fig = px.box(data, x="Size", y="Quantity Sold Kgs", color="Size",
                 title="Outlier detection for different Sizes")

    fig.add_annotation(x="F", y=323,
                       text="F (323 kgs)",
                       showarrow=True,
                       arrowhead=1)

    fig.add_annotation(x="E", y=198,
                       text="E (198 kgs)",
                       showarrow=True,
                       arrowhead=1)

    fig.add_annotation(x="M", y=397,
                       text="M (397 kgs)",
                       showarrow=True,
                       arrowhead=1)

    fig.add_annotation(x="K", y=295,
                       text="K (295 kgs)",
                       showarrow=True,
                       arrowhead=1)

    fig.add_annotation(x="B", y=147,
                       text="B (147 kgs)",
                       showarrow=True,
                       arrowhead=1)

    fig.add_annotation(x="R", y=263,
                       text="R (263 kgs)",
                       showarrow=True,
                       arrowhead=1)

    fig.update_xaxes(title="Product", title_font_family="Candara Light")
    fig.update_yaxes(title_font_family="Candara Light")

    fig.update_layout(
        font_family="Courier New",
        font_color="white",
        title_font_family="Bahnschrift Light",
        title_font_color="black",
        legend_title_font_color="green"
    )
    fig.update_xaxes(categoryorder='category ascending')

    fig.update_layout(showlegend=False)

    st.write(fig)

    st.info('''Outliers detected for the products B, E, F, K, M, R clearly tells that the demand for any specific product is not constant and can fluctuate according to season and client’s need. 

The highest quantity order was for product F and M in the consecutive last three months of 2021. 
''')

