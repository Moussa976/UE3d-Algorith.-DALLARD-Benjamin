import streamlit as st
import pandas as pd
import numpy as np
import os
#Mon répertoire local
#st.write(os.getcwd())

import seaborn as sns

import matplotlib.pyplot as plt 
%matplotlib inline


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
	if st.checkbox("Afficher le dataset"):
		number = st.number_input("Choisir le nombre de ligne")
		st.dataframe(data.head(number))

	#* Afficher le nom des colonnes du dataset 
	if st.checkbox("Afficher les noms des colonnes"):
		st.write(data.columns)

	#* Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées 
	if st.checkbox("Sélectionner les colonnes à afficher"):
		lescolonnes = data.columns.tolist()
		colonne_selectionnee = st.multiselect("Sélection(s) : ",lescolonnes)
		new_data = data[colonne_selectionnee]
		st.dataframe(new_data)

	#* La shape du dataset, par lignes et par colonnes
	if st.checkbox("La shape du dataset"):
		data_dim = st.radio("Afficher la dimension par ",("Lignes","Colonnes"))
		if data_dim == 'Lignes':
			st.text("Nombre de lignes")
			st.write(data.shape[0])
		elif data_dim == 'Colonnes':
			st.text("Nombre de colonnes")
			st.write(data.shape[1])
		else:
			st.write(data.shape)

	#* Afficher les statistiques descriptives du dataset
	if st.checkbox("Les statistiques descriptives du dataset"):
		st.write(data.describe().T)

	#* Afficher plusieurs type de graphique dans une partie visualisation avec notamment : 
	#	* Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés)
	if st.checkbox("Corrélation avec Seaborn"):
		st.write(sns.heatmap(data.corr(),annot=True))
		st.pyplot()
	#   * Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis)
	if st.checkbox("Graphique des comptes de valeur"):
		st.text("Comptes de valeur par cible")
		all_columns_names = data.columns.tolist()
		premiere_col = st.selectbox("Première colonne à GroupBy",all_columns_names)
		selected_columns_names = st.multiselect("Colonne(s) à sélectionner",all_columns_names)
		if st.button("Graphique"):
			st.text("Générer un Graphique")
			if selected_columns_names:
				vc_plot = data.groupby(premiere_col)[selected_columns_names].count()
			else:
				vc_plot = data.iloc[:,-1].value_counts()
			st.write(vc_plot.plot(kind="bar"))
			st.pyplot()
	#​
	#* Sélectionner le type de graphique à tracer
	all_columns_names = data.columns.tolist()
	type_of_plot = st.selectbox("Sélectionnez le type de graphique",["area","bar","line","hist","box","kde"])
	selected_columns_names = st.multiselect("Sélectionnez les colonnes à tracer",all_columns_names)
	#* Sélectionner des colonnes dans le jeux de données afin de générer le graphique
	if st.button("Généré un graphique"):
		st.success("Génération d'un tracé personnalisable de {} pour {}".format(type_of_plot,selected_columns_names))

		# Graphique par Streamlit
		if type_of_plot == 'area':
			cust_data = data[selected_columns_names]
			st.area_chart(cust_data)

		elif type_of_plot == 'bar':
			cust_data = data[selected_columns_names]
			st.bar_chart(cust_data)

		elif type_of_plot == 'line':
			cust_data = data[selected_columns_names]
			st.line_chart(cust_data)

		# Graphique personnalisé
		elif type_of_plot:
			cust_plot= data[selected_columns_names].plot(kind=type_of_plot)
			st.write(cust_plot)
			st.pyplot()
	#* (bonus)À noter que suivant certain jeux de données il y aura des graphiques qui n’auront pas de sens capturez les dans des exceptions
 

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
