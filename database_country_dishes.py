# database_country_dishes.py - Base de connaissances étendue

CUISINES = {
    "Français": [
        "Algérienne", "Marocaine", "Tunisienne", "Française", "Italienne", "Japonaise", 
        "Indienne", "Mexicaine", "Libanaise", "Espagnole", "Grecque", "Turque", 
        "Thaïlandaise", "Chinoise", "Vietnamienne", "Coréenne", "Américaine", "Brésilienne", 
        "Péruvienne", "Sénégalaise", "Égyptienne", "Iranienne", "Portugaise", "Russe", 
        "Allemande", "Éthiopienne", "Indonésienne", "Suisse", "Argentine", "Anglaise"
    ],
    "English": [
        "Algerian", "Moroccan", "Tunisian", "French", "Italian", "Japanese", 
        "Indian", "Mexican", "Lebanese", "Spanish", "Greek", "Turkish", 
        "Thai", "Chinese", "Vietnamese", "Korean", "American", "Brazilian", 
        "Peruvian", "Senegalese", "Egyptian", "Iranian", "Portuguese", "Russian", 
        "German", "Ethiopian", "Indonesian", "Swiss", "Argentine", "English"
    ]
}

# database_country_dishes.py

COUNTRY_SPECIFIC_KEYWORDS = {
    "Algérienne 🇩🇿": ["Couscous", "Chorba Frik", "Rechta", "Tajine Zitoun", "Bourek", "Mthewed", "Chakhchoukha"],
    "Marocaine 🇲🇦": ["Tagine", "Couscous royal", "Pastilla", "Harira", "Rfissa", "Tanjia"],
    "Tunisienne 🇹🇳": ["Lablabi", "Couscous au poisson", "Brik", "Osh el bulbul", "Kafteji", "Ojja"],
    "Française 🇫🇷": ["Bœuf Bourguignon", "Ratatouille", "Coq au vin", "Blanquette de veau", "Cassoulet", "Magret de canard"],
    "Italienne 🇮🇹": ["Risotto", "Pasta Carbonara", "Lasagne", "Osso Buco", "Gnocchi", "Saltimbocca"],
    "Japonaise 🇯🇵": ["Sushi", "Ramen", "Tempura", "Teriyaki", "Okonomiyaki", "Miso Soup", "Takoyaki"],
    "Indienne 🇮🇳": ["Butter Chicken", "Biryani", "Palak Paneer", "Tikka Masala", "Dhokla", "Naan"],
    "Mexicaine 🇲🇽": ["Tacos al Pastor", "Mole Poblano", "Enchiladas", "Chiles en Nogada", "Guacamole", "Quesadilla"],
    "Libanaise 🇱🇧": ["Hummus", "Tabbouleh", "Kibbeh", "Baba Ganoush", "Falafel", "Shawarma"],
    "Espagnole 🇪🇸": ["Paella", "Gazpacho", "Tortilla de patatas", "Patatas Bravas", "Pisto"],
    "Grecque 🇬🇷": ["Moussaka", "Souvlaki", "Spanakopita", "Tzatziki", "Gemista"],
    "Turque 🇹🇷": ["Kebab", "Baklava", "Pide", "Lahmacun", "Kofte", "Dolma"],
    "Thaïlandaise 🇹🇭": ["Pad Thai", "Tom Yum", "Green Curry", "Som Tum", "Massaman Curry"],
    "Chinoise 🇨🇳": ["Dim Sum", "Peking Duck", "Mapo Tofu", "Kung Pao Chicken", "Wonton"],
    "Vietnamienne 🇻🇳": ["Pho", "Banh Mi", "Spring Rolls", "Bun Cha", "Bo Bun"],
    "Coréenne 🇰🇷": ["Bibimbap", "Kimchi", "Bulgogi", "Japchae", "Korean Fried Chicken"],
    "Américaine 🇺🇸": ["Burger", "Clam Chowder", "BBQ Ribs", "Mac and Cheese", "Buffalo Wings"],
    "Brésilienne 🇧🇷": ["Feijoada", "Pão de Queijo", "Coxinha", "Moqueca", "Brigadeiro"],
    "Péruvienne 🇵🇪": ["Ceviche", "Lomo Saltado", "Aji de Gallina", "Causa Rellena"],
    "Sénégalaise 🇸🇳": ["Thieboudienne", "Yassa au poulet", "Mafé", "Pastels"],
    "Égyptienne 🇪🇬": ["Koshary", "Molokhia", "Ful Medames", "Mahshi"],
    "Iranienne 🇮🇷": ["Ghormeh Sabzi", "Fesenjan", "Tahdig", "Kabab Koobideh"],
    "Portugaise 🇵🇹": ["Bacalhau", "Pastel de Nata", "Caldo Verde", "Frango Piri-Piri"],
    "Russe 🇷🇺": ["Borscht", "Beef Stroganoff", "Pelmeni", "Blini", "Syrniki"],
    "Allemande 🇩🇪": ["Sauerkraut", "Schnitzel", "Currywurst", "Pretzel", "Sauerbraten"],
    "Éthiopienne 🇪🇹": ["Injera", "Doro Wat", "Kitfo", "Shiro"],
    "Indonésienne 🇮🇩": ["Nasi Goreng", "Satay", "Gado-Gado", "Rendang"],
    "Suisse 🇨🇭": ["Fondue", "Raclette", "Rösti", "Zürcher Geschnetzeltes"],
    "Argentine 🇦🇷": ["Asado", "Empanadas", "Chimichurri", "Milanesa"],
    "Anglaise 🇬🇧": ["Fish and Chips", "Shepherd's Pie", "Sunday Roast", "Beef Wellington"]
}