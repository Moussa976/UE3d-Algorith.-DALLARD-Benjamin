import streamlit as st
import pandas as pd
import numpy as np
import os
#Mon répertoire local
#st.write(os.getcwd())


def main():
	""" Explorateur des jeux de données """
	st.title("Explorateur des jeux de données")
	st.subheader("Exploration des données")

	def file_selector(folder_path='.\mesdatasets'):
        # Liste des fichiers csv dans le répertoire mesdatesets
		filenames = os.listdir(folder_path)
		selected_filename = st.selectbox("Séléctionner un fichier de données",filenames)
        
		return os.path.join(folder_path,selected_filename) # Construction de noms de chemins

    # Le fichier sélectionné
	filename = file_selector()
    # Message qui informe le fichier sélectionné
	st.info("Vous avez sélectionné {}".format(filename))

    # On charge le ficher
	data = pd.read_csv(filename)

	#* Afficher le dataset chargé suivant un nombre de ligne entrées par l’utilisateur
	if st.checkbox("Afficher le dataset :"):
		number = st.number_input("Choisir le nombre de ligne")
		st.write(data.head(number))

	#* Afficher le nom des colonnes du dataset 
	if st.checkbox("Afficher les noms des colonnes"):
		st.write(data.columns)

	#* Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées 


	#* La shape du dataset, par lignes et par colonnes


	#* Afficher les statistiques descriptives du dataset


	#* Afficher plusieurs type de graphique dans une partie visualisation avec notamment : 
	#	* Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés)
	#   * Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis)
	#​
	#* Sélectionner le type de graphique à tracer

	#* Sélectionner des colonnes dans le jeux de données afin de générer le graphique
	#* (bonus)À noter que suivant certain jeux de données il y aura des graphiques qui n’auront pas de sens capturez les dans des exceptions ��
    

if __name__ == '__main__':
    main()
    
# # st.title('Bonjour')

# DATA_URL = ('netflix_titles.csv')

# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     return data

# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Chargement des données...')
# # Load 10,000 rows of data into the dataframe.
# data = load_data(10000)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text('Chargement des données ... terminé!')

# st.write(data)
