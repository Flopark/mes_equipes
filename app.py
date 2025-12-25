# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 00:04:15 2025

@author: march
"""
import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="Générateur d'Équipes", page_icon="🎲")

# Style personnalisé pour faire de "belles cartes"
st.markdown("""
    <style>
    .team-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        border-left: 5px solid #4A90E2;
        margin-bottom: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        font-family: sans-serif;
    }
    .team-name { color: #1f77b4; font-weight: bold; font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True) # <-- C'est ici que j'ai corrigé "html"

st.title("🎲 Tirage au sort des équipes Tyler")

# Listes de base
g1 = ['Aglaé', 'Camille', 'Florian', 'Nathan', 'William']
g2 = ['Mamy', 'Sophie', 'Patrick', 'Kevin', 'Masako']

if st.button('🚀 Lancer le mélange'):
    # Mélange aléatoire
    random.shuffle(g1)
    random.shuffle(g2)
    
    for i, (p1, p2) in enumerate(zip(g1, g2), 1):
        st.markdown(f"""
            <div class="team-card">
                <span style="color:gray; font-size:0.8rem;">ÉQUIPE {i}</span><br>
                <span class="team-name">{p1}</span> <span class="separator">&</span> <span class="team-name">{p2}</span>
            </div>
        """, unsafe_allow_html=True) # <-- Corrigé ici aussi
else:

    st.info("Clique sur le bouton pour générer les binômes.")


