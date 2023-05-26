import pandas as pd
from pandas import to_datetime
from pandas.plotting import register_matplotlib_converters
import numpy as np
from pathlib import Path
import base64
from datetime import date, datetime


from PIL import Image
import streamlit as st

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from htbuilder import HtmlElement, div, hr, a, p, img, styles
from htbuilder.units import percent, px
import seaborn as sns
import matplotlib.pyplot as plt
from altair_saver import save

register_matplotlib_converters()



sns.set(style="whitegrid")
pd.set_option('display.max_rows', 15)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
st.set_option('deprecation.showPyplotGlobalUse', False)


st.set_page_config(
    page_title="Seedeos Report", layout="wide", page_icon="./images/flask.png"
)

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded



def main():
    def _max_width_():
        max_width_str = f"max-width: 1000px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>
        """,
            unsafe_allow_html=True,
        )


    # Hide the Streamlit header and footer
    def hide_header_footer():
        hide_streamlit_style = """
                    <style>
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # increases the width of the text and tables/figures
    _max_width_()

    # hide the footer
    hide_header_footer()

image_edhec = Image.open('images/idehos.png')
st.image(image_edhec, width=400)

st.sidebar.header("Setup Report Parameters")
st.sidebar.markdown("---")


text_input = st.sidebar.text_input(
        "Enter Company ID 👇","1678979336218x396548994896559500"
    )

start_date = st.sidebar.date_input(
        "Select start date",
        date(2022, 1, 1),
        min_value=datetime.strptime("2022-01-01", "%Y-%m-%d"),
        max_value=datetime.now(),
    )

st.sidebar.number_input("Select min completion time:",1,10)


# List of Vovici items used for the 9 items of the MSP9
items_msp25 = ["MSP1", "MSP2", "MSP3", "MSP4", "MSP5", "MSP6", "MSP7", "MSP8", "MSP9"]
select_msp25 = st.sidebar.multiselect("Select your MSP you want to include: ", items_msp25, items_msp25)
# list of Vovici items used for the 10 items of the K10
items_K10 = ["K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9", "K10"]
select_K10 = st.sidebar.multiselect("Select your K you want to include: ", items_K10, items_K10)

# List of Vovici items used for the 56 items of the SP28
# Assigning values to the list facteurs and items_sp28
items_sp28 = ["Parti1", "RecoEff2", "Lati2", "ChargeM1", "Adapt2", "RecoEff1", "Incerti2", "SoutSup2", "Harcel1", "Adapt1",
              "Perspect2", "SoutColl2", "Perspect1", "Penib1", "Chang1", "Lati1", "Equilib2", "mgmt2", "Util2", "RecoRes2",
              "ChargeM2", "Harcel2", "Exig1", "Interet1", "Util1", "QualitSup2", "Penib2", "Interet2", "Ethic2", "Exig2",
              "mgmt1", "DevComp2", "ChargePres2", "Iniq1", "QualitColl2", "Chang2", "ChargePres1", "Equilib1", "Adequa2",
              "DevComp1", "Clart2", "Adequa1", "Clart1", "RecoRes1", "SoutSup1", "QualitColl1", "Previ2", "Ethic1",
              "Incerti1", "Parti2" , "QualitSup1", "SoutColl1", "Previ1",
              "Contrad2", "Iniq2", "Contrad1", ]
select_sp28 = st.sidebar.multiselect("Select your SP28 you want to include: ", items_sp28, items_sp28)


facteurs = ["f01chargeP", "f02chargeM", "f03adequa", "f04penib", "f05equilib", "f06contrad", "f07previ", "f08adapt",
            "f09lati", "f10parti", "f11devcomp", "f12perspct", "f13qualsup", "f14qualcol", "f15soutcol", "f16soutsup",
            "f17recoeff", "f18recores", "f19exig", "f20ethic", "f21interet", "f22util", "f23incerti", "f24chang",
            "f25iniq", "f26Clart", "f27harcel", "f28mgmt"]
select_facteurs = st.sidebar.multiselect("Select your facteurs you want to include: ", facteurs, facteurs)

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.write("### Step 00: Process ⚙️")

st.write("### Step 01: Upload Data 💽")

import streamlit as st

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)


st.write("### Step 02: Select Direction of Questions ➡️")

st.write("You can now edit the column 'sens' in the dataset ✍🏻:")

df_questions = pd.read_excel("datasets/questions.xlsx")
#st.dataframe(df_questions)
edited_df = st.experimental_data_editor(df_questions)

#st.write("### Step 01: Change of Scale: ")
#st.write("transformation des notes de 1 ‡ 6 en notes de 0 ‡ 5")



df_final = pd.read_excel("datasets/df_final_final.xlsx")
df_final_v2 = df_final.loc[:, ~df_final.columns.str.contains('^Unnamed')]
st.dataframe(df_final_v2.head(5))




st.write(" ")
st.write("### Step 03: Generate Simple Visuals: ")
image_simple = Image.open('images/bar-chart.png')
st.image(image_simple, width=80)
st.write(" ")

participation1 = Image.open('images/participation1.png')
st.image(participation1, width=800)

participation2 = Image.open('images/participation2.png')
st.image(participation2, width=800)

participation4 = Image.open('images/participation4.png')
st.image(participation4, width=800)

participation5 = Image.open('images/participation5.png')
st.image(participation5, width=800)

participation6 = Image.open('images/participation6.png')
st.image(participation6, width=800)



st.write(" ")
st.write("### Step 04: Stress Visuals: ")
image_stat = Image.open('images/curve.png')
st.image(image_stat, width=80)
st.write(" ")




stress2 = Image.open('images/stress2.png')
st.image(stress2, width=800)

stress3 = Image.open('images/stress3.png')
st.image(stress3, width=800)

stress4 = Image.open('images/stress4.png')
st.image(stress4, width=800)

stress5 = Image.open('images/stress5.png')
st.image(stress5, width=800)


stress6 = Image.open('images/stress6.png')
st.image(stress6, width=800)


stress7 = Image.open('images/stress7.png')
st.image(stress7, width=800)




st.write(" ")
st.write("### Step 05: Motivational Visuals: ")
image_motiv = Image.open('images/reward.png')
st.image(image_motiv, width=80)
st.write(" ")



st.write(" ")
st.write("### Step 06: Risk Visuals: ")
image_risk = Image.open('images/brain.png')
st.image(image_risk, width=80)
st.write(" ")


option1 = st.selectbox(
    'Which segmentation do you want ?',
    ['Direction', 'Site', 'Ancienneté','Contrat','Responsabilité',"Type d'activité","Statut professionnel"])

list_option2 = list(set(df_final[option1]))
option2 = st.selectbox('Which element ?',list_option2)

#st.write('You selected:', option2)

df_scores4 = df_final.copy()
df_scores_filtered = df_scores4[df_scores4[option1] == option2].reset_index(drop=True)





list_facteurs = ["f01chargeP","f02chargeM","f03adequa",
"f04penib","f05equilib","f06contrad","f07previ","f08adapt","f09lati",
"f10parti","f11devcomp","f12perspct","f13qualsup",
"f14qualcol","f15soutcol","f16soutsup",
"f17recoeff","f18recores","f19exig","f20ethic",
"f21interet","f22util","f23incerti","f24chang","f25iniq","f26Clart","f27harcel",
"f28mgmt"]


list_facteurs_values = ["Charge de travail et pression temporelle",
"Charge mentale",
"Adéquation Objectifs/Ressources",
"Pénibilité physique & environnementale",
"Equilibre vie professionnelle - vie privée",
"Demandes contradictoires",
"Prévisibilité de la charge",
"Adaptation",
"Latitude décisionnelle",
"Participation aux décisions",
"Développement des compétences",
"Perspectives d'Evolution",
"Qualité des relations avec les supérieurs",
"Qualité des relations avec les collègues",
"Soutien des collègues",
"Soutien des supérieurs",
"Reconnaissance des efforts",
"Reconnaissance des résultats",
"Exigences émotionnelles",
"Souffrance éthique",
"Intérêt intrinsèque de la tâche",
"Utilité du travail",
"Incertitude sur l'avenir",
"Conduite du changement",
"Iniquité de traitement",
"Clarté des rôles",
"Harcélement & menaces",
"Management"]









list_categories = ["Intensité du travail"]*6 +["Autonomie & contrôle au travail"]*6+["Rapports & soutiens sociaux"]*6+["Sens du travail"]*4+["Situation de travail"]*6

list_average = []
for j in list_facteurs:
  list_average.append(np.round(df_scores_filtered[j].mean(),1))


df_facteurs = pd.DataFrame(
    {'Catégories': list_categories,
     'Facteurs': list_facteurs_values,
     'Exposition sur 100': list_average,

    })
list_cons = []
for i in list_facteurs:
    #X = df_scores_cdi[["k10tot","msp9tot","k10sq","msp9sq"]]
    #y = df_scores_cdi[i]
    #model = LinearRegression()
    #model.fit(X, y)
    
    X = df_scores_filtered[["k10tot","msp9tot","k10sq","msp9sq"]].values
    y = df_scores_filtered[i]
    x_values = X
    y_values = y
    #define our polynomial model, with whatever degree we want
    degree=2

    # PolynomialFeatures will create a new matrix consisting of all polynomial combinations 
    # of the features with a degree less than or equal to the degree we just gave the model (2)
    poly_model = PolynomialFeatures(degree=degree)

    # transform out polynomial features
    poly_x_values = poly_model.fit_transform(x_values)

    # let's fit the model
    poly_model.fit(poly_x_values, y_values)

    # we use linear regression as a base!!! ** sometimes misunderstood **
    regression_model = LinearRegression()

    regression_model.fit(poly_x_values, y_values)

    y_pred = regression_model.predict(poly_x_values)
    r_squared = regression_model.score(poly_x_values, y_values)

    #view R-squared value
    print(r_squared)
    list_cons.append(r_squared)
df_facteurs['Conséquence en %'] = list_cons
df_facteurs['Conséquence en %'] = np.round(df_facteurs['Conséquence en %']*100,2)
df_facteurs['Niveau de Risque'] = np.round(df_facteurs['Conséquence en %']/100 * df_facteurs['Exposition sur 100'],2)
df_scores_man = df_facteurs.copy()
#df_scores_plus20 = df_scores_plus20.sort_values(by="Niveau de Risque",ascending=False)
st.dataframe(df_scores_man)





st.write(" ")
st.write("### Step 07: Khi Square: ")
image_edhec = Image.open('images/chalkboard.png')
st.image(image_edhec, width=80)
st.write(" ")


option3 = st.selectbox(
    'Which segmentation do you want for KHI ?',
    ['Direction', 'Site', 'Ancienneté','Contrat','Responsabilité',"Type d'activité","Statut professionnel"])

list_option4 = list(set(df_final[option3]))
option4 = st.selectbox('Which element for KHI ?',list_option4)


df_scores4 = df_final.copy()
df_scores_filtered_2 = df_scores4[df_scores4[option3] == option4].reset_index(drop=True)

from scipy.stats import chi2_contingency
# create contingency table
cont_table = pd.crosstab(df_scores_filtered_2["Type d'activité"], df_scores_filtered_2['binstress'])

# perform chi-squared test
chi2, p, dof, expected = chi2_contingency(cont_table)

# print results
st.write("Chi-squared test statistic:", chi2)
st.write("p-value:", p)
st.write("Degrees of freedom:", dof)
print("Expected frequencies:\n", expected)
if p <= 0.05:
    st.write('Relation significative entre cette variable et le taux d\'hyperstress.')
elif p <= 0.1:
    st.write('Tendance')
else:
    st.write('Relation non significative entre cette variable et le taux d\'hyperstress.')




st.markdown("### Congrats you made it 🎉")





if __name__=='__main__':
    main()

st.markdown(" ")
st.markdown("### 👨🏼‍💻 **App Contributors:** ")
st.image(['images/gaetan.png'], width=100,caption=["Gaëtan Brison"])

st.markdown(f"####  Link to Project Website [here]({'https://seedeos.com/'}) 🚀 ")
st.markdown(f"####  Feel free to contribute to the app and give a ⭐️")


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;background - color: white}
     .stApp { bottom: 80px; }
    </style>
    """
    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1,

    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def footer2():
    myargs = [
        " Made by ",
        link("https://seedeos.com/", "Seedeos"),
        "👨🏼‍💻"
    ]
    layout(*myargs)


#if __name__ == "__main__":
#    footer2()