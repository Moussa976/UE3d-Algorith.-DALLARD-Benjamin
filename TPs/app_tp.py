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
	# Affichage du dataset
	if st.checkbox("Afficher le dataset :"):
		number = st.number_input("Choisir le nombre de ligne")

		st.write(data.head(number))

    

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
