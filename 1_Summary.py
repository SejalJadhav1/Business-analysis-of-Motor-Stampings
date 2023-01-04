import streamlit as st
import pandas as pd
import openpyxl

st.set_page_config(
    page_title=" Summary"
)

st.header("Motor Stampings Business Analysis")

data = pd.read_excel("bdm_alpha.xlsx")

tab1, tab2 , tab3 = st.tabs(["Summary", "Data" , "Encoded Sizes"])

with tab1:
   st.markdown(''' 
   Light Metal Works is a B2B motor stamping maufacturing business located in Kurla, Mumbai, 
   Maharashtra.They have been manufacturing the product from past 25 years.
   
   It was established in 1998 by Mr. Hussain Indorewala in a 300sq feet area 
   which has now been expanded to 1800sq feet. Mr. Hussain, the proprietor,began
   with a team of two people and only one client. He now has ten people working 
   under him and a client pool of 20.The team of ten consists of a production 
   manager, an office manager, seven laborers and the owner.
   
   They produce motor stampings of different sizes. The size ranges from 73mm to 300mm. 
   Company's production margin is high and product selling price low which helps engage 
   customers at the door and make them stand out from their competitors. The company
   use word-of-mouth as their marketing strategy. There are many other firms which also
   manufacture similar products. This brings the market of motor stamping production under
   perfect competition.  
  
   The smallest size is 73 x 38mm (A) while the biggest size being 222 x 120mm (T). These products are sold in kgs. The selling price of all size products is same. 
The company begins manufacturing the products once the client deal is confirmed. They produce fresh products every day. And deliver the orders within the ordered week. 
For a 1kg order the company must manufacture approximately around 250 to 275 motor stampings for the smaller sizes which weighs around 3grams to 4grams each. Whereas, for the bigger sizes the company must manufacture approximately around 17 to 18 motor stampings which weighs around 55grams to 60grams each. 

The insights of this business tell us that the major problem of the company lies in the small size motor stampings which are almost 20% of the company’s total production. These small size products take more time to produce as there are a greater number of products to be produced per kg than the large size motor stampings. 
The labors in the company are paid per day. Therefore, the more the time is consumed in making the products the more the production cost. Increase in production time caused by the small size products results in the increase of labor cost. 
And, as mentioned earlier all the products are sold at same price. Therefore, the profits incurred by the large size product is more than that of the small size products. Causing the small size products to be least profit producing products. 

After conversing with the manager of the company on why to continue selling small size products if they are the least profit producing ones, he responded saying that, “we cannot be choosy about the products we want to produce and not produce. Here the competition is extremely high. Everyone wants to pull each other down by selling everything the clients demand for, and sometimes at a rate lower than the market rate. If we discontinue to produce small size products it may result in losing our clients to our competitors as the clients choose to order at a company where everything is available in one place.” 
Therefore, even if it means manufacturing products at minimum profit margin the company continues to do so to compete their competitors and not lose their clients
   
   Company’s last three 2021 months sales consist of around 18748kgs corresponding to around
   8 lakhs company’s 3 months profit. 
   
   The company’s future plan is to step into another manufacturing business which is rotor dye
   casting. The process to launch the new company has already been commenced. This company expects
   to provide services of the same by the end of 2022. The owner’s dream is to be the market leader
   and envisions to expand the same in the upcoming years.''')

with tab2:
   st.caption("Raw data(Sep2021, Oct2021, Nov2021) collected from the company")
   st.dataframe(data)

with tab3:
   st.caption("(A being the smallest size and T being the largest size)")
   product_data = pd.read_excel("bdm_alpha.xlsx", sheet_name="Sheet2")
   st.table(product_data)

