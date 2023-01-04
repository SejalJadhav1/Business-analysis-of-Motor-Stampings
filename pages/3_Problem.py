import streamlit as st
import plotly
import openpyxl
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Problem"
)

data = pd.read_excel("bdm_line_graph.xlsx")

st.subheader("About the Business Problem")

tab1, tab2  = st.tabs(["Business Problem", "More Details" ])

with tab1:
    st.write('''Another insight into the business which was analysed are the differences in profit and cost incurred by different products of the company. 

The analysis is specifically evaluated for the products A, B, C, D which fall in small size products group, and the products R, Q, S, T which fall in the large size products group.

Whenever an order is placed by a client it is always in the unit kilograms. For example, a client may order for 10 kilograms
     of size A and 10 kilograms of size R. Now, a size A weighs around 3gm. In order to produce size A which will be total of 1000 gm which is 
     1 kilogram the company has to manufacture at least 250 motor stampings of size A. Now, if the company has order of 10kg of size A it will
      add up to manufacturing 250 multiplied by 10 which will be 2500 products of size A to be manufactured. 
      
Similarly, the job gets quicker, and easier when it comes to the larger size products. As mentioned above now if we consider a client’s order of 10 kg of size R we can say that a size R weighs around 55gm. Therefore, to manufacture a 1 kg of product we will be needing around 17 motors to be produced. As, a result if we do the calculations for 10kgs of client’s order by multiplying 10 with 17 its results in production of 170 motor stampings of size R. 
''')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Size"], y=data["Number of products"], name="Number of products"))
    fig.add_trace(go.Scatter(x=data["Size"], y=data["Quantity Sold gms"], name="Quantity Sold Kgs"))

    fig.update_xaxes(categoryorder='category ascending')

    fig.update_layout(colorway=['#3A01DF', '#DF0101', "#FA5858"])

    fig.update_xaxes(title="Product", title_font_family="Candara Light")
    fig.update_yaxes(title="Number of Products & Qunatity sold (gms)", title_font_family="Candara Light")

    fig.update_layout(
        title="Time Consuming Products",
        font_family="Courier New",
        font_color="black",
        title_font_family="Bahnschrift Light",
        title_font_color="black",
        legend_title_font_color="green"
    )

    st.write(fig)
    st.info('''
There's an exponential decrease in the number of products produced for different small and large size. 

In the graph above there is an evident decrease in the number of products manufactured as the size of the product starts increasing. Therefore, it is very clear that there’s an inverse relationship between the number of products to be manufactured and the size of the product. 
''')

with tab2:
    st.write('''The discussion of inverse relationship between the size of the product and the number of products to be manufactured does not end there. This inverse relationship furthermore also has affected the cost of production for the company. 

The company majorly uses labour work along with machines to manufacture the products. There’s absence of any automatic motor stamping manufacturing machine in the company. Machines are used to punch down the metal shapes of desired shape from the metal sheets. The operation of this task requires a labourer. 

The stacking of these shapes on one another to generate a final product requires another labourer. Basically, the business of the company is labour oriented and dependent. 

Therefore, more the products to be manufactured for an ordered size more is the labour work which corresponds to increase in the production cost of the product. 
''')
    fig = go.Figure()
    fig.add_trace(go.Histogram(histfunc="sum", x=data["Size"], y=data["Profit"], name="Sum of Profit"))
    fig.add_trace(
        go.Histogram(histfunc="sum", x=data["Size"], y=data["labor cost (per kg)"], name="Sum of Labour Cost"))

    fig.update_xaxes(categoryorder='category ascending')
    fig.update_layout(
        bargap=0.2, colorway=["#31B404", '#82FA58', "#FA5858"])

    fig.update_xaxes(title="Product", title_font_family="Candara Light")
    fig.update_yaxes(title="Sum", title_font_family="Candara Light")


    fig.add_annotation(x="M", y=1210,
                       text="(The products are in ascending order of their size starting from A)",
                       showarrow=False,
                       arrowhead=1)

    fig.add_annotation(x="B", y=900,
                       text="Profit=Cost"
                       ,
                       showarrow=True,
                       arrowhead=1)

    fig.add_annotation(x="O", y=900,
                       text="Profit>Cost",
                       showarrow=True,
                       arrowhead=1)
    fig.update_layout(height=500, width=800)
    fig.update_layout(
        title="Profit Efficient Products",
        font_family="Courier New",
        font_color="white",
        title_font_family="Bahnschrift Light",
        title_font_color="black",
        legend_title_font_color="green"
    )

    st.write(fig)

    st.info('''Graph inference shows that the company continues to manufacture and sell small size products even with a less profit margin as compared to the large size products. ''')
    st.write('''Another reason why the company has continued to manufacture the small size products is due to its demand in the market.
     The owner of the company in his statement said that “we are small scale motor stamping manufacturing company. 
     The clients who approach us are also from a similar background like ours. 
     The client companies can be from a fan manufacturing background, Pump manufacturing background etc. 
     Manufacturing of these products requires small size motors only. 
     As a result, even with low profit margin we must give the market what it demands.”''')
