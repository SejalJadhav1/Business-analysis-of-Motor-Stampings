import streamlit as st
import pandas as pd
import pip
pip.main(["install", "plotly"])
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Recommendations"
)

st.subheader("Recommendations to the Company")

tab1, tab2  = st.tabs(["Recommendation", "Solution Table" ])
with tab1:
    st.write('''The solution for this problem would be to minimize the labour cost. The labour cost can be minimized by substituting the labourers with an automatic metal stamping machine. 

Basically, as mentioned above the conventional method for object stamping is manual, it is very time consuming and in non-automatic form. Continuous stamping or printing results in hand fatigue requires lots of efforts and affects the accuracy to result 

So, the manual method must be replaced by PLC Automation. Automatic stamping of object has received significant attention because automatic stamping is reliable and reproducible. This not only reduce manual effort but also gives more time for marketing also prevent danger which might occur when human being works in hazardous environment. Automation greatly improves the profit and productivity; it is very scalable.

Now, for Light Metal Works, if they decide to invest in Automatic stamping machines it gets a little trickier to accept the investment. Because the company then will have to make investment in buying around 20 machines for the company’s 20 different product sizes. 

Each machine will only stamp one specific size. The smallest size machine costs around 15 Lakhs. Larger the product size huger will be the machine and more will be its price. Not only that, but also the electricity cost increases with the machine size. The manager also informed that they order metal sheets pieces instead of an entire metal sheet coil. 

When asked the reason the manager responded by saying that “metal sheets are affordable and does the job. The coil on the other hand is expensive. The coil is the optimal metal sheet which is made to be used in automatic machines unless like ours. The metal sheets from the coil used in the automatic machines punches down the shape only in places where it has been engineered to. There is an immense amount of wastage and scrap which are the borders of the sheet which is then produced. This wastage is manageable and can be minimized in the manual machines. The laborers can move the sheets from under the machines and punch it on the places where they want. This results in the entire sheet being punched into feasible sizes.”

Even if the company buys the machines, it is a small-scale business and does not have sales as much as what the machines will produce in a single day. 

The company manufactures products only after they receive orders from the clients. That is, they produce fresh products and deliver it as soon as possible. If the company starts manufacturing products with the help of machines, they will need to store the extra products in a store house with least moisture, as the metal starts rusting if not stored appropriately. The company again must then invest to get store rooms.  

The labour cost with all these step ups decreases. The efficiency of the company to manufacture the products with minimum faults increase too. But, buying twenty machines is not the optimal approach for a small-scale business-like Light Metal Works. 

The optimal approach is to buy machines only for small size products, and using labour force for manufacturing large size products with the company’s old manual motor stamping machines. This will both substitute the immense time consumed to manufacture small size products, also reducing labour cost, and improving the product quality and optimality.

''')

data = pd.read_excel("bdm_alpha.xlsx", sheet_name="Sheet3")

with tab2:
    st.info('''The investment to buy size B and C automatic stamping machines can be made as they are the most small-size demanded product by the market. 
''')
    st.table(data)
    
hide_st_style = """
             <style>
             #MainMenu {visibility: hidden;}
             footer {visibility: hidden;}
             header {visibility: hidden;}
             </style>
             """
st.markdown(hide_st_style, unsafe_allow_html=True)
