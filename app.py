import streamlit as st
import time

# Modules personnalisés
from search_engine import get_automated_context
from brain import rank_best_recipes
from model import generate_recipe_stream
from database_country_dishes import CUISINES, COUNTRY_SPECIFIC_KEYWORDS
from Ingredients import INGREDIENTS, ALLERGIES_LIST

# --- OPTIMISATION CACHE ---
@st.cache_data(show_spinner=False)
def cached_search(query):
    return get_automated_context(query)

@st.cache_data(show_spinner=False)
def cached_ranking(query, data):
    return rank_best_recipes(query, data)

st.set_page_config(page_title="Maison SLIMANI", page_icon="🍳")


# --- DESIGN HAUTE COUTURE (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Cinzel:wght@400;500;600;700&display=swap');
    
    .stApp { 
        background-color: #1a1a1a; 
        background-image: radial-gradient(ellipse at top, rgba(212, 175, 55, 0.03) 0%, transparent 50%);
    }
    .block-container { padding-top: 2rem; }
    
    /* 1. TITRE MAISON SLIMANI : Centré et Blanc */
    .signature-title { 
        font-family: 'Cinzel', serif; 
        color: #FFFFFF !important; 
        text-align: center; 
        font-size: 3.2rem; 
        font-weight: 500; 
        letter-spacing: 8px; 
        margin-bottom: 8px;
        text-shadow: 0 2px 20px rgba(212, 175, 55, 0.15);
        position: relative;
    }
    .signature-title::after {
        content: '';
        display: block;
        width: 60px;
        height: 1px;
        background: linear-gradient(90deg, transparent, #D4AF37, transparent);
        margin: 20px auto 0;
    }
    
    /* 2. SOUS-TITRE : Élégance raffinée */
    .subtitle { 
        text-align: center; 
        color: #D4AF37; 
        font-family: 'Cormorant Garamond', serif;
        font-size: 0.95rem; 
        letter-spacing: 6px; 
        text-transform: uppercase; 
        margin-bottom: 50px; 
        width: 100%;
        font-weight: 400;
        opacity: 0.9;
        text-shadow: 0 0 30px rgba(212, 175, 55, 0.2);
    }

    [data-testid="stSidebar"] { 
        background: linear-gradient(180deg, #1c1c1c 0%, #141414 100%) !important; 
        border-right: 1px solid rgba(212, 175, 55, 0.3);
        box-shadow: 4px 0 30px rgba(0, 0, 0, 0.5);
    }
    .sidebar-logo-container { 
        text-align: center; 
        margin-top: 50px; 
        margin-bottom: 60px; 
    }
    .sidebar-logo { 
        display: inline-block; 
        color: #D4AF37; 
        font-family: 'Cinzel', serif;
        font-size: 1.6rem; 
        font-weight: 500; 
        padding: 18px 35px; 
        border: 1px solid rgba(212, 175, 55, 0.6); 
        background: linear-gradient(145deg, #0d0d0d, #1a1a1a);
        letter-spacing: 4px;
        box-shadow: 
            0 4px 20px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(212, 175, 55, 0.1);
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    .sidebar-logo:hover {
        border-color: #D4AF37;
        box-shadow: 
            0 8px 40px rgba(212, 175, 55, 0.15),
            inset 0 1px 0 rgba(212, 175, 55, 0.2);
        transform: translateY(-2px);
    }
    [data-testid="stSidebar"] label p { 
        color: #f5f5f5 !important; 
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.05rem;
        letter-spacing: 1px;
    }
    div.stRadio > div[role="radiogroup"] > label > div:first-child { 
        border: 1px solid rgba(212, 175, 55, 0.5) !important; 
        background-color: transparent !important;
        transition: all 0.3s ease;
    }
    div.stRadio > div[role="radiogroup"] > label:hover > div:first-child { 
        border-color: #D4AF37 !important;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
    }
    div.stRadio > div[role="radiogroup"] > label[data-checked="true"] > div:first-child > div { 
        background-color: #D4AF37 !important;
        box-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
    }
    
    h3 { 
        color: #1a1a1a !important; 
        font-family: 'Cinzel', serif;
        font-size: 1rem !important; 
        font-weight: 500;
        border-left: 3px solid #D4AF37; 
        padding-left: 20px; 
        background: linear-gradient(90deg, #fdfbf7 0%, #f8f6f0 100%); 
        padding-top: 12px; 
        padding-bottom: 12px; 
        margin-top: 30px !important;
        letter-spacing: 2px;
        box-shadow: 0 2px 15px rgba(0, 0, 0, 0.08);
    }
    
    div.stButton > button { 
        background: linear-gradient(145deg, #1a1a1a, #2a2a2a); 
        color: #D4AF37 !important; 
        border: 1px solid rgba(212, 175, 55, 0.5); 
        width: 100%; 
        height: 4.5em; 
        font-family: 'Cinzel', serif;
        font-weight: 500; 
        font-size: 0.85rem;
        letter-spacing: 3px; 
        border-radius: 0; 
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
    }
    div.stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.1), transparent);
        transition: left 0.6s ease;
    }
    div.stButton > button:hover::before {
        left: 100%;
    }
    div.stButton > button:hover { 
        border-color: #D4AF37; 
        color: #FFFFFF !important; 
        transform: translateY(-3px);
        box-shadow: 
            0 8px 30px rgba(0, 0, 0, 0.4),
            0 0 20px rgba(212, 175, 55, 0.15);
    }
    
    .prestige-signature { 
        color: #FFFFFF !important; 
        font-family: 'Cormorant Garamond', serif;
        font-weight: 500; 
        font-size: 1.15rem; 
        font-style: italic;
        margin-top: 50px; 
        letter-spacing: 2px; 
        border-top: 1px solid rgba(212, 175, 55, 0.4); 
        padding-top: 30px; 
        text-align: center;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    .prestige-sep { 
        color: #D4AF37; 
        margin: 0 15px;
        font-weight: 300;
        opacity: 0.8;
    }
    #MainMenu, header, footer {visibility: hidden;}

    /* 3. SIGNATURE SIDEBAR : Élégance discrète */
    .user-signature { 
        color: #FFFFFF !important; 
        font-family: 'Cormorant Garamond', serif;
        font-size: 0.85rem; 
        text-align: center; 
        margin-top: 60px; 
        opacity: 0.6;
        letter-spacing: 1px;
        white-space: nowrap;
        transition: opacity 0.3s ease;
    }
    .user-signature:hover {
        opacity: 0.9;
    }
    
    /* Scrollbar personnalisée */
    ::-webkit-scrollbar {
        width: 6px;
    }
    ::-webkit-scrollbar-track {
        background: #1a1a1a;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #D4AF37 0%, #a08930 100%);
        border-radius: 3px;
    }
    </style>
    """, unsafe_allow_html=True)


# --- DICTIONNAIRES DE TRADUCTION ---
FILTER_LABELS = {
    "Français": {
        "prot": "Protéines & Viandes", "fec": "Bases & Féculents", "leg": "Légumes Spécifiques", 
        "herb": "Herbes Fraîches", "epi": "Épices du Monde", "aut": "Produits Laitiers & fruits secs",
        "sauce": "Sauces & Condiments", "fruit": "Fruits du Verger",
        "world": "Cuisine du Monde", "serv": "Type de Service", "all": "Allergies à exclure", 
        "wish": "Note particulière pour le Chef", "place": "Ex: Texture fondante...", 
        "serv_list": ["Entrée", "Plat Principal", "Dessert"]
    },
    "English": {
        "prot": "Protein", "fec": "Starch", "leg": "Vegetables", 
        "herb": "Herbs", "epi": "Spices", "aut": "Others", 
        "sauce": "Sauces", "fruit": "Fruits",
        "world": "World Cuisine", "serv": "Service Type", "all": "Allergies to exclude", 
        "wish": "Special note for the Chef", "place": "Ex: Melting texture...", 
        "serv_list": ["Appetizer", "Main Course", "Dessert"]
    }
}

TRANS = {
    "Français": {
        "main_title": "Maison SLIMANI", "sub": "Haute Gastronomie Numérique",
        "btn": "DÉCOUVRIR LA CRÉATION", "status": "Le Chef compose votre menu...",
        "sec_ing": "Sélection du Marché", "caption": "Conçu & Développé par Houda SLIMANI",
        "time": "Temps", "ing_title": "Ingrédients", "inst_title": "Instructions", "pres_title": "Présentation",
        "copy_btn": " Copier la recette",
        "step1": "La Mise en place et Bases Maison",
        "step2": "Le Coeur du Plat",
        "step3": "L'Accompagnement",
        "step4": "Le Jus de Cuisine",
        "step5": "Le Dressage Signature"
    },
    "English": {
        "main_title": "Maison SLIMANI", "sub": "Digital Fine Dining",
        "btn": "DISCOVER THE CREATION", "status": "Chef is composing your menu...",
        "sec_ing": "Market Selection", "caption": "Designed & Developed by Houda SLIMANI",
        "time": "Time", "ing_title": "Ingredients", "inst_title": "Instructions", "pres_title": "Presentation",
        "copy_btn": " Copy the recipe",
        "step1": "Mise en place & Home-made Bases",
        "step2": "The Heart of the Dish",
        "step3": "The Side & Garnish",
        "step4": "The Culinary Jus",
        "step5": "The Signature Plating"
    }
}

# --- SIDEBAR ---
with st.sidebar:
    if 'current_lang' not in st.session_state: 
        st.session_state.current_lang = "Français"
    
    lang_titles = {"Français": "SÉLECTION LANGUE", "English": "LANGUAGE SELECTION"}
    
    langue = st.radio(lang_titles[st.session_state.current_lang], ["Français", "English"], 
                      index=["Français", "English"].index(st.session_state.current_lang))
    st.session_state.current_lang = langue
    t = TRANS[langue]
    fl = FILTER_LABELS[langue]

    st.markdown("<br>" * 12, unsafe_allow_html=True) 
    
    st.markdown("<div class='sidebar-logo-container'><div class='sidebar-logo'>M.S</div></div>", unsafe_allow_html=True)
    
    # AJOUT DE TA SIGNATURE ICI DANS LA SIDEBAR
    st.sidebar.markdown('<p class="user-signature">Conçu & Développé par Houda SLIMANI</p>', unsafe_allow_html=True)

# --- TITRES D'ACCUEIL ---
st.markdown(f"<div class='signature-title'>{t['main_title']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle'>{t['sub']}</div>", unsafe_allow_html=True)

# --- FORMULAIRE ---
st.subheader(t["sec_ing"])
c1, c2, c3, c4 = st.columns(4)
with c1:
    proteine = st.selectbox(fl["prot"], INGREDIENTS[langue].get(fl["prot"], ["Error"]))
    feculent = st.selectbox(fl["fec"], INGREDIENTS[langue].get(fl["fec"], ["Error"]))
with c2:
    legumes = st.multiselect(fl["leg"], INGREDIENTS[langue].get(fl["leg"], []))
    herbes = st.multiselect(fl["herb"], INGREDIENTS[langue].get(fl["herb"], []))
with c3:
    epices = st.multiselect(fl["epi"], INGREDIENTS[langue].get(fl["epi"], []))
    autres = st.multiselect(fl["aut"], INGREDIENTS[langue].get(fl["aut"], []))
with c4:
    sauces = st.multiselect(fl["sauce"], INGREDIENTS[langue].get(fl["sauce"], []))
    fruits = st.multiselect(fl["fruit"], INGREDIENTS[langue].get(fl["fruit"], []))

w1, w2 = st.columns(2)
with w1: cuisine_choisie = st.selectbox(fl["world"], CUISINES[langue])
with w2: type_plat = st.selectbox(fl["serv"], fl["serv_list"])

allergies = st.multiselect(fl["all"], ALLERGIES_LIST[langue])
user_wish = st.text_input(fl["wish"], placeholder=fl["place"])

# --- GÉNÉRATION ---
if st.button(t["btn"]):
    t_start = time.time()
    with st.status(t["status"]) as status:
        
        def clean_list(l): return ", ".join(l) if l else "Aucun"
        cultural_hint = COUNTRY_SPECIFIC_KEYWORDS.get(cuisine_choisie, "")

        #  DÉTECTION DU DOMAINE (CUISINE vs PÂTISSERIE)
        is_dessert = type_plat in ["Dessert", "تحلية"]
        
        #  PROMPT GÉNÉRATEUR ADAPTÉ POUR AUTONOMIE TOTALE
        if is_dessert:
            domain_rules = f"""
            RÈGLES D'OR DU CHEF PÂTISSIER SLIMANI :
            1. TOUT EST FAIT MAISON : Si le plat nécessite une pâte (feuilletée, brisée, sablée), une crème ou un insert, donne impérativement la méthode de fabrication complète de cette base. Interdiction de dire "utiliser une pâte du commerce".
            2. INTERDICTION FORMELLE : Pas d'huile d'olive, pas d'ail, pas d'oignons. On utilise du beurre AOP, de la crème, des gousses de vanille.
            3. TECHNIQUE DE PÂTISSERIE : Parle de tempérage, de foisonnement, de sablage, de caramélisation à sec, d'infusion à froid.
            4. PRÉCISION : Les quantités doivent être millimétrées (grammages précis).
            """
            structure_steps = f"""
            1. **{t['step1']}** : (Méthode complète pour fabriquer la pâte ou l'appareil de base)
            2. **{t['step2']}** : (Création de la crème, mousse ou ganache technique)
            3. **{t['step3']}** : (Assemblage technique et maîtrise des températures)
            4. **{t['step4']}** : (Finition, glaçage ou décor au cornet)
            5. **{t['step5']}** : (Présentation moderne et épurée)
            """
        else:
            domain_rules = f"""
            RÈGLES D'OR DU CHEF DE CUISINE SLIMANI :
            1. BASES AROMATIQUES OBLIGATOIRES : Utilise impérativement ail, échalotes, oignons, mirepoix, herbes pour construire le jus.
            2. TOUT EST FAIT MAISON : Si le plat nécessite une pâte (ex: Vol-au-vent) ou un fond (veau, volaille), donne la méthode de fabrication complète.
            3. TECHNIQUE SALÉE : Parle de réaction de Maillard, déglaçage au vin ou vinaigre, réduction, montage au beurre, repos de la viande.
            4. ACCOMPAGNEMENT : Propose une garniture complète (légumes glacés, purées soyeuses, céréales).
            """
            structure_steps = f"""
            1. **{t['step1']}** : (Préparation des légumes ET méthode pour le fond ou la pâte maison)
            2. **{t['step2']}** : (Cuisson technique de la protéine principale)
            3. **{t['step3']}** : (Préparation de la garniture associée)
            4. **{t['step4']}** : (Déglaçage et réduction des sucs pour un jus court)
            5. **{t['step5']}** : (Présentation digne d'une étoile Michelin)
            """

        query = f"""
        En tant que Chef Exécutif de la Maison SLIMANI, crée une recette de HAUTE GASTRONOMIE REELLE de A à Z pour un(e) {type_plat}.
        CULTURE : {cuisine_choisie} ({cultural_hint}).
        
        {domain_rules}
        
        PANIER D'INGRÉDIENTS :
        - Protéine : {proteine} | Féculent : {feculent}
        - Fruits : {clean_list(fruits)} | Légumes : {clean_list(legumes)}
        - Aromates/Condiments : {clean_list(herbes)}, {clean_list(epices)}, {clean_list(sauces)}
        
        ALLERGIES (INTERDIT) : {clean_list(allergies)}
        Note spéciale du client : {user_wish}
        """

        system_prompt = f"""
        Tu es le Chef Exécutif de la Maison SLIMANI. Ton style est celui d'un expert passionné qui ne triche jamais sur les bases.
        - Langue : {langue} EXCLUSIVEMENT.
        - Ton : Technique, précis, luxueux. Utilise le vocabulaire de métier approprié.
        - RÈGLE CRITIQUE : Ne suggère JAMAIS d'ingrédients préparés. Si tu mentionnes une pâte feuilletée, tu DOIS expliquer comment la faire (détrempe et tourage). Si c'est un fond de veau, explique la torréfaction des os.
        - Structure de la réponse :
        
        # **[NOM DU PLAT GASTRONOMIQUE]**
        ### **{t['pres_title']}**
        (Vision du Chef sur le mariage des saveurs et l'intention culinaire.)
        
        ### **{t['time']}**
        {"* **Preparation:** XX min | **Cooking:** XX min" if langue == "English" else 
         "* **Préparation :** XX min | **Cuisson :** XX min"}
        
        ### **{t['ing_title']}**
        (Liste exhaustive incluant TOUS les ingrédients pour les bases maison.)
        
        ### **{t['inst_title']}**
        {structure_steps}
        """

        raw_web_data = cached_search(query)
        context_refined = cached_ranking(query, raw_web_data)
        
        vitesse = round(time.time() - t_start, 2)
        status.update(label=f"Création prête en {vitesse}s", state="complete")

    st.markdown("---")
    placeholder = st.empty()
    full_recipe = ""
    
    for chunk in generate_recipe_stream(query, system_prompt=system_prompt):
        full_recipe += chunk
        placeholder.markdown(full_recipe + "▌")
    
    sig_html = f"<div class='prestige-signature'>MAISON SLIMANI <span class='prestige-sep'>|</span> L'Excellence Culinaire par Houda Slimani</div>"
    placeholder.markdown(f"{full_recipe}\n\n{sig_html}", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    #  COPIE DISCRÈTE (Traduit automatiquement)
    with st.expander(t['copy_btn']):
        st.code(full_recipe, language=None)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander(" Architecture & Intelligence System"):
        st.markdown(f"""
        **Spécifications du Système**
        * **Modèle** : Gemini 3 Flash (LLM Haute Performance)
        * **Vitesse d'inférence** : `{vitesse}s`
        * **Orchestration** : Python Framework By Houda Slimani
        """)

# --- SIGNATURE FINALE ---
st.markdown("<br><center><small style='color:#ccc;'>Maison SLIMANI © 2026</small></center>", unsafe_allow_html=True)