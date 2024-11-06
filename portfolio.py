import streamlit as st
from PIL import Image
import base64
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Portfolio d'Axel Stoltz", layout="wide")

# Fonction pour encoder l'image en base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Charger et encoder l'image
background_image = get_base64_image("Asset/background.png")

# Ajouter l'image de fond uniquement pour le header
st.markdown(
    f"""
    <style>
    .header-section {{
        background-image: url("data:image/jpeg;base64,{background_image}");
        background-size: cover;
        background-position: center;
        padding: 50px 0;
    }}
    .header-text {{
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        padding-left: 3%;
    }}
    .header-name {{
        font-size: 60px;
        font-weight: bold;
        color: white;
        margin-bottom: 0px;
    }}
    .header-title {{
        font-size: 24px;
        font-weight: 400;
        color: white;
        margin-top: -5px;
    }}
    .header-info {{
        font-size: 20px;
        color: white;
    }}
    .header-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
    }}
    </style>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <div class="header-section">
        <div class="header-row">
            <div class="header-text">
                <div class="header-name">Axel Stoltz</div>
                <div class="header-title">Data Scientist / Engineering Student</div>
            </div>
            <div style="color:white; font-weight:800;" class="header-info">
                📧 axel.stoltz@efrei.net | 
                🔗 <a style="text-decoration:none; color:white; font-weight:800;" href="https://www.linkedin.com/in/axel-stoltz/" target="_blank">LinkedIn</a> | 
                📅 <a style="text-decoration:none; color:white; font-weight:800; margin-right:3%;" href="https://calendly.com/axel-stoltz-efrei/meet-me" target="_blank">Meet me</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .nav-bar {
        display: flex;
        justify-content: space-around;
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .nav-item {
        font-size: 18px;
        font-weight: bold;
        color: #3e64ff;
        text-decoration: none;
        margin: 0 10px;
    }
    .nav-item:hover {
        color: #ff5722;
    }
    </style>
    """, unsafe_allow_html=True
)


if 'selection' not in st.session_state:
    st.session_state.selection = "💻 Cool Projects"  

col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 3])

with col1:
    if st.button("📝 My Resume"):
        st.session_state.selection = "📝 My Resume"
with col2:
    if st.button("💻 Cool Projects"):
        st.session_state.selection = "💻 Cool Projects"
with col3:
    if st.button("📰 Fresh News"):
        st.session_state.selection = "📰 Fresh News"
with col4:
    if st.button("👤 Know Me Better"):
        st.session_state.selection = "👤 Know Me Better"
with col5:
    st.write("")

if st.session_state.selection == "📝 My Resume":
    st.header("Resume")
    st.write("")
    st.write("")
    colA,colB = st.columns([4,1])
    with colA:
        st.subheader("🤓 Education")
        st.write("")

        education = [
        {"logo": "Asset/logo_efrei.svg", "school": "Engineering Degree Data & AI, **Efrei Paris Panthéon-Assas University**", "dates": ":grey[***2024 - présent***]"},
        {"logo": "Asset/logo_apu.png", "school": "Abroad Study Semester, **Asia Pacific University**", "dates": ":grey[***Aug 2023 - Dec 2023***]"},
        {"logo": "Asset/logo_efrei.svg", "school": "Bachelor Degree Computer Science, **Efrei Paris Panthéon-Assas University**", "dates": ":grey[***Aug 2021 - Jul 2024***]"}
        ]   

        for entry in education:
            col0, col1, col2, col3 = st.columns([0.2,1, 5, 2])  
            with col0:
                st.write("")
            with col1:
                st.image(entry['logo'], width=80) 

            with col2:
                st.write(entry["school"])

            with col3:
                st.write(entry["dates"])


        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.subheader("💼 Experiences")
        st.write("")
        
        work = [
        {"logo": "Asset/logo_coca.svg","width": 80, "school": "Ambassador @Paris 2024 Olympics, **The Coca-Cola Company**", "dates": ":grey[***Jul 2024 - Aug 2024***]"},
        {"logo": "Asset/logo_hdor.jpg", "width": 80, "school": "Sales assistant in jeweller's, **Histoire d'Or**", "dates": ":grey[***Jan 2023 - Jan 2023***]"},
        ]   

        for entry in work:
            col0, col1, col2, col3 = st.columns([0.2,1, 5, 2])  
            with col0:
                st.write("")
            with col1:
                st.image(entry['logo'], width=entry['width'])  

            with col2:
                st.write(entry["school"])

            with col3:
                st.write(entry["dates"])


        st.write("")
        st.write("")
        st.download_button(
            label="📥 Download my resume",
            data=open("Asset/CV.pdf", "rb").read(),
            file_name="CV_Axel_Stoltz.pdf",
            mime="application/pdf"
        )

    
    
    with colB:
        st.subheader("🛠️ Hard Skills")
        st.write("""
        👨‍💻 **Coding** : Python, SQL, PL/SQL  
                  
        🛠️ **Frameworks & Libraries** : Pandas, NumPy, scikit-learn, Streamlit, Folium, PyTorch, TensorFlow  
                  
        🧠 **Knowledge** : Machine Learning Models, Data Visualization, Maths for Data Science
        """)

        st.subheader("✨ Soft Skills")
        st.write("""
        💪 Leadership and team player  
                 
        ⏳ Autonomous  
                 
        🎨 Creativity  
                 
        🤔 Problem solving  
                 
        🤑 Entrepreneurial spirit  
                 
                 """)


elif st.session_state.selection  == "💻 Cool Projects":
    st.header("Projects 🚀")
    
    projects = [
        {
            "title": "🚲 Velib Visualization",
            "description": "Velib data visualization"
        },
        {
            "title": "📃 P'AItent",
            "description": "Patent Classification Using CPC Codes and Machine Learning"
        },
        {
            "title": "📱 PhindH",
            "description": "Student Networking App for University Students"
        }
    ]
    
    project_titles = [project["title"] for project in projects]
    selected_project = st.selectbox("Select a project:", project_titles)
    
    for project in projects:
        if project["title"] == selected_project:
            st.header(f"{project['title']}")
            st.write(f"**Description**: {project['description']}")

    if selected_project == "🚲 Velib Visualization":

        st.write("""
            As a regular user of the Velib service in Paris, I've often noticed that the experience doesn't always meet my expectations. Stations can sometimes be overcrowded or, conversely, completely empty, making it frustrating to rent a bike. Intrigued by these fluctuations, I decided to conduct my own investigation.

            My curiosity led me to explore data about the Velib system, and I found a very interesting dataset on [data.gouv.fr](https://www.data.gouv.fr/en/datasets/velib-velos-et-bornes-disponibilite-temps-reel/). I downloaded the data covering the period from Thursday, October 18 to Sunday, October 20, to capture a representative window of usage patterns over a weekend.

            This project aims to analyze the major trends in bike and station availability, hoping to gain a better understanding of how this urban mobility system actually functions. By examining this data, I aim to highlight areas for improvement and contribute to a smoother user experience for all cycling enthusiasts in Paris.  
                  
                 

        """)
        st.write("")
        st.write("")

        files = ['thu-10h.csv','thu-12h.csv','thu-16h.csv','thu-19h.csv','thu-22h.csv']

        df_list = [pd.read_csv(f'Data/thu-17/{file}', delimiter=';') for file in files]
        df_thursday = pd.concat(df_list, ignore_index=True)
        df_thursday = df_thursday.sort_values('stationcode')
        df_thursday.reset_index(drop=True, inplace=True)

        st.write(df_thursday.head())

        feature_options = [
            "name",
            "ebike",
            "duedate",
            "capacity",
            "is_renting",
            "mechanical",
            "stationcode",
            "is_installed",
            "is_returning",
            "coordonnees_geo",
            "numbikesavailable",
            "numdocksavailable",
            "code_insee_commune",
            "nom_arrondissement_communes"
        ]
        
        selected_feature = st.selectbox("Select a feature to learn more about:", feature_options)

        feature_explanations = {
            "name": "The name of the bike station",
            "ebike": "# of ebike per station",
            "duedate": "The date and time when the data was recorded, providing a temporal context for the availability of bikes.",
            "capacity": "The total number of bike docks available at the station, reflecting the station's overall capacity for bike storage.",
            "is_renting": "A boolean value indicating whether the station is currently open for bike rentals.",
            "mechanical": "# of mechanical bikes per station",
            "stationcode": "A unique identifier for the station, which helps in referencing and tracking specific locations in the dataset.",
            "is_installed": "A boolean value indicating whether the bike station is physically installed and operational.",
            "is_returning": "A boolean value indicating whether the station is open for bike returns, allowing users to drop off bikes at that location.",
            "coordonnees_geo": "The geographic coordinates (latitude and longitude) of the station, useful for mapping and spatial analysis.",
            "numbikesavailable": "The number of bikes currently available for rent at the station, indicating its usability at a given time.",
            "numdocksavailable": "The number of empty docks available at the station, showing how many bikes can be returned there.",
            "code_insee_commune": "A unique code assigned to the municipality for statistical purposes, often used in administrative and demographic analyses.",
            "nom_arrondissement_communes": "The name of the arrondissement (district) or municipality where the bike station is located, providing a local context."
        }

        st.write(f"**{selected_feature.capitalize()}**: {feature_explanations[selected_feature]}")

        st.header("Visualizations 📊")

        visualization_options = [
            "Top 10 Municipalities with the Most Stations",
            "Bikes Distribution",
            "Hourly Availability",
            "Station Map",
            "Station Density Map",
            "Bikes Availability Map",
            "Ebike rate",
        ]

        selected_visualization = st.selectbox("Select a visualization:", visualization_options)

        if selected_visualization == "Top 10 Municipalities with the Most Stations":
            st.subheader("Top 10 Municipalities with the Most Stations")
            st.components.v1.html(open('top_cities_graph.html', 'r').read(), height=600)
            st.subheader("Analysis")
            st.write("""
            This visualization highlights the top 10 municipalities with the highest number of bike-sharing stations. 
            It helps identify areas with high bike-sharing infrastructure, which could correlate with greater usage or demand.
            """)

        elif selected_visualization == "Bikes Distribution":
            st.subheader("Bikes Distribution")
            st.components.v1.html(open('rate_bike.html', 'r').read(), height=600)
            st.write("""
            The Bikes Distribution visualization provides insight into how bikes are spread across different stations. 
            Analyzing this distribution can help detect areas where there might be an imbalance in bike availability, 
            either excess or scarcity, and optimize redistribution efforts.
            """)

        elif selected_visualization == "Hourly Availability":
            day_options = ["Thursday, October 18, 2024", "Friday, October 19, 2024", "Saturday, October 20, 2024"]
            selected_day = st.radio("Select a day for hourly availability:", day_options)

            if selected_day == "Thursday, October 18, 2024":
                st.subheader("Hourly Availability on Thursday, October 18, 2024 (Rainy)")
                st.components.v1.html(open('dispo_jeudi.html', 'r').read(), height=600)
                

            elif selected_day == "Friday, October 19, 2024":
                st.subheader("Hourly Availability on Friday, October 19, 2024 (Sunny/Cloudy)")
                st.components.v1.html(open('dispo_vendredi.html', 'r').read(), height=600)
                

            elif selected_day == "Saturday, October 20, 2024":
                st.subheader("Hourly Availability on Saturday, October 20, 2024 (Sunny)")
                st.components.v1.html(open('dispo_samedi.html', 'r').read(), height=600)

            st.subheader("Analysis")
            st.write("""
            This visualization shows the availability of bikes at different times throughout the selected day. 
            It is useful for identifying patterns in bike availability across different hours, which can indicate peak times of usage 
            or potential shortages during specific periods of the day.
            """)

        elif selected_visualization == "Station Map":
            st.subheader("Station Map")
            with open('carte_stations_paris_cluster.html', 'r', encoding='utf-8') as f:
                map_html = f.read()
            st.components.v1.html(map_html, height=600)
            st.subheader("Analysis")
            st.write("""
            The Station Map allows you to visually explore the locations of bike-sharing stations across the city. 
            This can highlight areas with good coverage as well as potential gaps in the network, where adding new stations 
            might improve accessibility.
            """)

        elif selected_visualization == "Station Density Map":
            st.subheader("Station Density Map")
            with open('carte_densite2.html', 'r', encoding='utf-8') as f:
                map_html = f.read()
            st.components.v1.html(map_html, height=600)
            st.subheader("Analysis")
            st.write("""
            The Station Density Map focuses on the density of bike-sharing stations in different parts of the city. 
            Areas with high density are often better served, while low-density areas may require additional infrastructure 
            to meet potential demand.
            """)

        elif selected_visualization == "Bikes Availability Map":
            st.subheader("Bikes Availability Map")

            # Sélecteur de jour
            day_options = ["Thursday", "Friday", "Saturday"]
            selected_day = st.selectbox("Select a day:", day_options)

            # Sélecteur de plage horaire
            if selected_day == "Thursday":
                time_labels = ['8-12h', '12-16h', '16-20h', '20-24h']
            else:
                time_labels = ['1-8h', '8-10h', '10-12h', '12-17h', '17-20h', '20-24']

            selected_time_range = st.selectbox("Select a time range:", time_labels)

            if selected_day == "Thursday":
                file_name = f'carte_interactive_thu_{selected_time_range}.html'
            elif selected_day == "Friday":
                file_name = f'carte_interactive_fri_{selected_time_range}.html'
            else:  
                file_name = f'carte_interactive_sat_{selected_time_range}.html'

            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    map_html = f.read()
                st.components.v1.html(map_html, height=600)
            except FileNotFoundError:
                st.error("The selected map is not available.")
        
            st.subheader("Analysis")
            st.write("""
            The Bikes Availability Map shows the number of bikes available at each station during the selected time range.
            It helps to understand how bike availability fluctuates over time and across locations, providing insights for 
            resource allocation and user behavior patterns.
            """)

        elif selected_visualization == "Ebike rate":
            st.subheader("Ebike rate")
            st.components.v1.html(open('proportion_ebike.html', 'r').read(), height=600)
            with open('carte_top_10_ebike.html', 'r', encoding='utf-8') as f:
                map_html = f.read()
            st.subheader("Top 30 ebike stations")
            st.components.v1.html(map_html, height=600)
            st.subheader("Analysis")
            st.write("""
            This plot shows the number of stations in relation to the e-bike rate per station.

            Electric Vélibs are clearly in high demand and short supply! Riders are far more likely to find a station stocked with traditional, mechanical Vélibs than with electric ones. This scarcity of e-bikes could contribute to frustration among users who prefer a quicker, less strenuous ride, especially during peak hours or for longer commutes. The distribution also suggests potential imbalances in the fleet's availability, which might be worth addressing to enhance user satisfaction and meet the growing preference for e-bikes            
            """)
                
                



elif st.session_state.selection == "📰 Fresh News":
    st.header("News 🌍")
    st.markdown(
        """
        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7238853163775070210" 
                height="1425" width="1000" 
                frameborder="0" 
                allowfullscreen="" 
                title="Post intégré"></iframe>
        """,
        unsafe_allow_html=True
    )

elif st.session_state.selection == "👤 Know Me Better":
    st.header("About Me 😊")
    st.write("""
    Passionné par la data et l'innovation, je m'engage à utiliser la technologie pour résoudre des problèmes complexes et améliorer la vie des gens.
    """)

# Footer
st.write("---")
