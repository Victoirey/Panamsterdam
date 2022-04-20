import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from scipy import stats
from PIL import Image
import streamlit.components.v1 as components


st.set_page_config(page_title="#panamsterdam", page_icon=":bike:", layout="wide")

#image = Image.open(r'C:\Users\Administrateur\Documents\GitHub\Final_Project\Streamlit\Panamsterdam.png')
#st.image(image, use_column_width=True, width=500)



###############################################################################
############### SIDEBAR #######################################################
###############################################################################
st.sidebar.subheader("The bike revolution in Paris \n en route to #panamsterdam")
page1 = "Executive summary"
page2 = "Infrastructure overview"
page3 = "Traffic overview"
page4 = "Accident overview"
page5 = "Correlation between variables"
page6 = "Users' perception"
page7 = "Is Paris municipality giving itself the means to achieve its ambitions?"

pages = [page1, page2, page3, page4, page5, page6, page7]
select_page = st.sidebar.radio("", pages)

st.sidebar.write(" ") 
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")

st.sidebar.write("Olivier Masson " "\n" "[Linkedin](https://www.linkedin.com/in/oliviermasson/) "
"\n\n" "Victoire Rey " "\n" "[Linkedin](https://www.linkedin.com/in/victoire-rey/) "
"\n\n" "Final Project - Data Analytics Bootcamp" "\n\n" "Apr-22")


###############################################################################
############### PAGE 1 - EXECUTIVE SUMMARY ####################################
###############################################################################
if select_page == page1:
    st.markdown(
    "<h1 style='text-align: center'>"
    "<strong>The bike revolution in Paris (2018-2024):</strong>"
    "<br><span style='font-size: smaller'>en route to #panamsterdam</span>"
    "</h1>", unsafe_allow_html=True)
    st.subheader("Executive summary")
    st.markdown("[PENDING]")


###############################################################################
############### PAGE 2 - INFRASTRUCTURE OVERVIEW ##############################
###############################################################################
elif select_page == page2:
    st.subheader("Infrastructure overview")
#Cycling path map  
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650476924834' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cy&#47;CyclingpathsParis&#47;Tableaudebord1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CyclingpathsParis&#47;Tableaudebord1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cy&#47;CyclingpathsParis&#47;Tableaudebord1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650476924834');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='700px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='700px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                              width=1000, height=500)
    st.markdown("[PENDING]")
#Cycling paths
    image = Image.open("images/Cycling_paths.PNG")
    st.image(image, width =800)
    st.markdown("[PENDING]")



###############################################################################
############### PAGE 3 - TRAFFIC OVERVIEW #####################################
###############################################################################
elif select_page == page3:
    st.subheader("Traffic overview")
#Active counter in the Paris area
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650484554609' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 5 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord5&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CompteursVeloParis&#47;Tableaudebord5' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord5&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650484554609');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                          width=1000, height=550)
    st.markdown("[PENDING]")
    
#Dynamic traffic map 
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650486407825' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 7 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;47&#47;47Y4FD3M2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;47Y4FD3M2' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;47&#47;47Y4FD3M2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650486407825');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='900px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='900px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                          width=1000, height=500)
    st.markdown("[PENDING]")
    
#Monthly trend over 4 years + projection
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650488523264' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 6 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord6&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CompteursVeloParis&#47;Tableaudebord6' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord6&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650488523264');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                          width=1000, height=550)
    st.markdown("[PENDING]")

#Traffic per weekday
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650487201987' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 8 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord8&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CompteursVeloParis&#47;Tableaudebord8' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord8&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650487201987');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                          width=1000, height=550)
    st.markdown("[PENDING]")
    
#Intraday peak hours
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650487767872' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 9 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord9&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CompteursVeloParis&#47;Tableaudebord9' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord9&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650487767872');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                          width=1000, height=550)
    st.markdown("[PENDING]")

#Direction of commute
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650489048774' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 11 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord11&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CompteursVeloParis&#47;Tableaudebord11' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord11&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650489048774');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                      width=1000, height=850)
    st.markdown("[PENDING]")

#Top 20 counters
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650488339997' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 10 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord10&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CompteursVeloParis&#47;Tableaudebord10' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord10&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650488339997');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                          width=1000, height=550)
    st.markdown("[PENDING]")


###############################################################################
############### PAGE 4 - ACCIDENT OVERVIEW ####################################
###############################################################################
elif select_page == page4:
    st.subheader("Accident overview")
#Accident map     
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650490210397' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ac&#47;Accidents2017-2020&#47;Tableaudebord1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Accidents2017-2020&#47;Tableaudebord1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ac&#47;Accidents2017-2020&#47;Tableaudebord1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650490210397');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='627px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                          width=1000, height=700)
    st.markdown("[PENDING]")
    
#Bike accidents peak hours
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650491643702' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 4 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord4&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CompteursVeloParis&#47;Tableaudebord4' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;CompteursVeloParis&#47;Tableaudebord4&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650491643702');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                              width=1000, height=450)
    st.markdown("[PENDING]")
    
#Bike accident saisonnality
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650490462260' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ac&#47;Accidents2017-2020&#47;Tableaudebord2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Accidents2017-2020&#47;Tableaudebord2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ac&#47;Accidents2017-2020&#47;Tableaudebord2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650490462260');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='627px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                              width=1000, height=700)

##    
    st.components.v1.html("""""", 
                              width=1000, height=450)      
    
    
###############################################################################
############### PAGE 5 - CORRELATIONS #########################################
###############################################################################
elif select_page == page5:
#Trend accidents vs traffic
    st.subheader("Correlation between traffic, accidents & weather")
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650491248212' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ac&#47;AccidentsvTraffic&#47;Tableaudebord1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='AccidentsvTraffic&#47;Tableaudebord1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ac&#47;AccidentsvTraffic&#47;Tableaudebord1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650491248212');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='627px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                          width=1000, height=650)
    st.markdown("[PENDING]")

#Trend accidents vs weather
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650491330902' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ac&#47;AccidentsvTraffic&#47;Tableaudebord2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='AccidentsvTraffic&#47;Tableaudebord2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ac&#47;AccidentsvTraffic&#47;Tableaudebord2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650491330902');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='627px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                          width=1000, height=650)
    st.markdown("[PENDING]")

#Trend traffic vs weather
    st.components.v1.html("""<div class='tableauPlaceholder' id='viz1650491400274' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 3 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ac&#47;AccidentsvTraffic&#47;Tableaudebord3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='AccidentsvTraffic&#47;Tableaudebord3' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ac&#47;AccidentsvTraffic&#47;Tableaudebord3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650491400274');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='627px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""", 
                          width=1000, height=650)
    st.markdown("[PENDING]")
    
    
###############################################################################
############### PAGE 6 - USERS' PERCEPTION ####################################
###############################################################################
elif select_page == page6:
    st.subheader("Users' perception")
    st.markdown("[PENDING]")
    
    
###############################################################################
############### PAGE 7 - CONCLUSIONS OF PROJECT ###############################
###############################################################################
elif select_page == page7:
    st.subheader("Is Paris municipality giving itself the means to achieve its ambitions?")
    st.markdown("[PENDING]")


    st.components.v1.html("""""", 
                          width=1000, height=550)


# =============================================================================
# def main():
#     html_temp = """<div class='tableauPlaceholder' id='viz1650476924834' style='position: relative'><noscript><a href='#'><img alt='Tableau de bord 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cy&#47;CyclingpathsParis&#47;Tableaudebord1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CyclingpathsParis&#47;Tableaudebord1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cy&#47;CyclingpathsParis&#47;Tableaudebord1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650476924834');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='700px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='700px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
#     components.html(html_temp, width=1000, height=800)
#     if __name__ == "__main__":    
#         main()
# =============================================================================


# =============================================================================
# def main():
#     html_temp = """<div class='tableauPlaceholder' id='viz1650302350918' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;Panamsterdam_accidents2017_2020&#47;Bikeaccidentstrend&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Panamsterdam_accidents2017_2020&#47;Bikeaccidentstrend' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;Panamsterdam_accidents2017_2020&#47;Bikeaccidentstrend&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650302350918');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
#     components.html(html_temp, width=1000, height=500)
# if __name__ == "__main__":    
#     main()
# =============================================================================
