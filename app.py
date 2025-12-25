# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 00:04:15 2025

@author: march
"""
import streamlit as st
import random
import time

# Configuration de la page
st.set_page_config(page_title="Générateur d'Équipes Tyler", page_icon="🎄")

# --- STYLISATION CSS AVANCÉE ---
st.markdown("""
<style>
    /* Animation d'apparition douce */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .team-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: center;
        /* Application de l'animation */
        animation: fadeInUp 0.6s ease-out forwards;
    }

    .team-label {
        color: #0056b3;
        font-size: 0.8rem;
        font-weight: bold;
        text-transform: uppercase;
        display: block;
        margin-bottom: 8px;
    }

    .team-name {
        color: #1E1E1E;
        font-size: 1.5rem;
        font-weight: 800;
    }

    .separator {
        color: #0056b3; 
        font-size: 1.6rem;
        font-weight: 300;
        margin: 0 15px;
        font-style: italic;
    }

    
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3em;
        background-color: #0056b3;
        color: white;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(255,75,75,0.3);
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIQUE ---
st.title("🎄 Tirage au sort des équipes Tyler")
st.write("Appuie c'est tout beau !")

g1 = ['Aglaé', 'Camille', 'Florian', 'Nathan', 'William']
g2 = ['Mamy', 'Sophie', 'Patrick', 'Kevin', 'Masako']

if st.button('🚀 TAP TAP TAPPPP !'):
    
    # 1. Animation de "réflexion"
    with st.spinner('🎲 Mélange en cours...'):
        # On simule un temps de calcul pour le suspense
        time.sleep(1.5)
        random.shuffle(g1)
        random.shuffle(g2)

    st.success("Tirage terminé !")
    time.sleep(0.6)
    st.write("---")

    # 2. Affichage séquentiel pour un effet visuel
    for i, (p1, p2) in enumerate(zip(g1, g2), 1):
        # On ajoute un micro-délai pour que les cartes apparaissent l'une après l'autre
        
        st.markdown(f"""
            <div class="team-card">
                <span class="team-label">❄️ EQUIPE N°{i} ❄️</span>
                <span class="team-name">⛄{p1}</span>
                <span class="separator"> & </span>
                <span class="team-name">{p2}⛄</span>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(0.6) 
        
    st.markdown(f"""
            <div class="team-card">
                <span class="team-label">❄️ EQUIPE N°6 v❄️</span>
                <span class="team-name">⛄ Thor </span>
                <span class="separator"> & </span>
                <span class="team-name"> Luffy ⛄</span>
            </div>
        """, unsafe_allow_html=True)
    time.sleep(1) 
    # 3. Célébration finale
    st.snow()

else:
    # État initial
    st.info("Joyeux Noël !")










