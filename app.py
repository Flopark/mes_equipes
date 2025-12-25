# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 00:04:15 2025

@author: march
"""
import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="Générateur d'Équipes", page_icon="🎲")

# --- STYLISATION CSS ---
st.markdown("""
<style>
    .team-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        border: 1px solid #e0e0e0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
    }
    .team-label {
        color: #888888;
        font-size: 0.75rem;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: block;
        margin-bottom: 5px;
    }
    .team-name {
        color: #1E1E1E;
        font-size: 1.4rem;
        font-weight: 700;
    }
    .separator {
        color: #FF4B4B; /* Couleur rouge Streamlit */
        font-size: 1.5rem;
        font-weight: 300;
        margin: 0 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIQUE DE L'APPLICATION ---
st.title("🎲 Tirage au sort des équipes Tyler")

# Listes de base
g1 = ['Aglaé', 'Camille', 'Florian', 'Nathan', 'William']
g2 = ['Mamy', 'Sophie', 'Patrick', 'Kevin', 'Masako']

if st.button('🚀 Lancer le mélange'):
    # Mélange aléatoire des deux listes
    random.shuffle(g1)
    random.shuffle(g2)
    
    st.write("---")
    
    # Création des colonnes pour un affichage propre (optionnel)
    # Ici on affiche une carte par ligne pour bien voir le "&"
    for i, (p1, p2) in enumerate(zip(g1, g2), 1):
        st.markdown(f"""
            <div class="team-card">
                <span class="team-label">ÉQUIPE {i}</span>
                <span class="team-name">{p1}</span>
                <span class="separator">&</span>
                <span class="team-name">{p2}</span>
            </div>
        """, unsafe_allow_html=True)
else:
    st.info("Cliquez sur le bouton pour générer les duos !")
