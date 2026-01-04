<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Entraînement Vocabulaire CréaFrench</title>
    <style>
        :root { --primary: #3498db; --success: #2ecc71; --danger: #e74c3c; --bg: #121212; --card: #1e1e1e; --accent: #f1c40f; }
        body { background-color: var(--bg); color: white; font-family: 'Segoe UI', sans-serif; margin: 0; }
        #container { width: 95%; max-width: 1100px; margin: 40px auto; text-align: center; }
        .selector-container { background: var(--card); padding: 25px; border-radius: 12px; margin-bottom: 30px; border: 1px solid #333; }
        select { padding: 12px; background: #333; color: white; border-radius: 6px; border: 1px solid var(--primary); font-size: 16px; width: 300px; cursor: pointer; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
        .set-card { background: var(--card); padding: 20px; border-radius: 12px; border: 1px solid #333; transition: 0.3s; }
        .set-card:hover { border-color: var(--primary); transform: translateY(-3px); }
        .btn { background: var(--primary); color: white; border: none; padding: 12px; border-radius: 6px; cursor: pointer; font-size: 15px; width: 100%; margin-top: 10px; transition: 0.3s; font-weight: bold; }
        .btn-secondary { background: #555; }
        .screen { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: var(--bg); z-index: 100; justify-content: center; align-items: center; flex-direction: column; }
        #word-display { font-size: 60px; font-weight: bold; margin: 40px 0; color: var(--accent); padding: 0 20px; text-align: center; }
        #timer-container { width: 70%; height: 12px; background: #333; border-radius: 6px; margin: 20px auto; overflow: hidden; }
        #timer-bar { width: 100%; height: 100%; background: var(--success); transition: width 1s linear; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 10px; border: 1px solid #444; text-align: left; }
        .scroll-area { width: 90%; max-height: 70vh; overflow-y: auto; background: #1e1e1e; padding: 20px; border-radius: 10px; }
        input[type="text"] { background: #333; color: white; border: 1px solid #555; padding: 8px; width: 90%; border-radius: 4px; }
    </style>
</head>
<body>

<div id="container">
    <h1>Entraînement Vocabulaire CréaFrench</h1>
    <div class="selector-container">
        <label>Choisir le Thème :</label>
        <select id="theme-select" onchange="genererSeries(this.value)">
            <option value="">-- Maak een keuze --</option>
            <option value="13">Thème 13 : La Gastronomie</option>
            <option value="14">Thème 14 : L'Art et la Culture</option>
            <option value="15">Thème 15 : Voyage en France</option>
        </select>
    </div>
    <div class="grid" id="set-grid"></div>
</div>

<div id="edit-screen" class="screen">
    <h2 id="edit-title">Modifier la Série</h2>
    <div class="scroll-area"><table id="edit-table"><thead><tr><th>NL</th><th>FR</th><th>Action</th></tr></thead><tbody id="edit-body"></tbody></table></div>
    <button class="btn" onclick="sauvegarderEtDemarrer()" style="width:300px; margin-top:20px;">🚀 Enregistrer et Commencer</button>
</div>

<div id="exercise" class="screen">
    <div id="info-header" style="font-size: 1.2rem; color: #aaa;"></div>
    <div id="timer-container"><div id="timer-bar"></div></div>
    <div id="word-display">Chargement...</div>
    <button class="btn" style="width:140px; background:var(--danger);" onclick="location.reload()">Arrêter</button>
</div>

<div id="result" class="screen">
    <h2 style="color: var(--success);">Série terminée !</h2>
    <div class="scroll-area"><table><thead><tr><th>NL</th><th>FR</th></tr></thead><tbody id="res-body"></tbody></table></div>
    <button class="btn" style="margin-top: 20px; width:250px;" onclick="location.reload()">Retour au menu</button>
</div>

<script>
const listeVocabulaire = [
    // --- GASTRONOMIE ---
    {t:13, nl:"de maaltijden", fr:"les repas"}, {t:13, nl:"eten / vreten", fr:"manger / bouffer"}, {t:13, nl:"drinken", fr:"boire"}, {t:13, nl:"proeven", fr:"goûter"}, {t:13, nl:"fijnproeven", fr:"déguster"}, {t:13, nl:"het ontbijt", fr:"le petit-déjeuner"}, {t:13, nl:"de brunch", fr:"le brunch"}, {t:13, nl:"middagmaal / lunch", fr:"le déjeuner / le lunch"}, {t:13, nl:"het avondmaal", fr:"le dîner / le souper (BE)"}, {t:13, nl:"het aperitief", fr:"l'apéritif (m.)"}, {t:13, nl:"de hapjes", fr:"les amuse-bouche / zakouskis"}, {t:13, nl:"het voorgerecht", fr:"l'entrée (f.)"}, {t:13, nl:"de soep", fr:"la soupe / le potage"}, {t:13, nl:"het (hoofd)gerecht", fr:"le plat (principal)"}, {t:13, nl:"het dessert", fr:"le dessert"}, {t:13, nl:"koken", fr:"faire la cuisine"}, {t:13, nl:"de maaltijd klaarmaken", fr:"préparer le repas"}, {t:13, nl:"een recept", fr:"une recette"}, {t:13, nl:"fruit/groenten afspoelen", fr:"rincer les fruits et légumes"}, {t:13, nl:"schillen", fr:"éplucher"}, {t:13, nl:"snijden / hakken", fr:"couper (en morceaux)"}, {t:13, nl:"fijnhakken", fr:"émincer"}, {t:13, nl:"biefstuk bakken", fr:"cuire un steak"}, {t:13, nl:"mengen", fr:"mélanger"}, {t:13, nl:"roeren", fr:"remuer"}, {t:13, nl:"alleseter", fr:"omnivore"}, {t:13, nl:"flexitariër", fr:"flexitarien"}, {t:13, nl:"vegetariër", fr:"végétarien"}, {t:13, nl:"veganist", fr:"végan / végétalien"}, {t:13, nl:"glutenvrij dieet", fr:"le régime sans gluten"}, {t:13, nl:"het bestek", fr:"les couverts"}, {t:13, nl:"een mes", fr:"un couteau"}, {t:13, nl:"een vork", fr:"une fourchette"}, {t:13, nl:"een lepel", fr:"une cuillère"}, {t:13, nl:"een bord", fr:"une assiette"}, {t:13, nl:"een kom", fr:"un bol"}, {t:13, nl:"kookpot", fr:"une casserole"}, {t:13, nl:"pan", fr:"une poêle"}, {t:13, nl:"citroen", fr:"le citron"}, {t:13, nl:"appel", fr:"la pomme"}, {t:13, nl:"wortel", fr:"une carotte"}, {t:13, nl:"tomaat", fr:"une tomate"}, {t:13, nl:"look", fr:"l'ail (m.)"},

    // --- L'ART ET LA CULTURE ---
    {t:14, nl:"de lezer", fr:"le lecteur"}, {t:14, nl:"het boek", fr:"le bouquin / le livre"}, {t:14, nl:"pocketboek", fr:"le livre de poche"}, {t:14, nl:"de roman", fr:"le roman"}, {t:14, nl:"kortverhaal", fr:"la nouvelle"}, {t:14, nl:"stripverhaal", fr:"la bande dessinée"}, {t:14, nl:"hoofdstuk", fr:"le chapitre"}, {t:14, nl:"held(in)", fr:"le héros / l'héroïne"}, {t:14, nl:"hoofdpersonage", fr:"le protagoniste"}, {t:14, nl:"schrijver", fr:"un écrivain / auteur"}, {t:14, nl:"boekhandel", fr:"une librairie"}, {t:14, nl:"uitgeverij", fr:"une maison d'édition"}, {t:14, nl:"intrige / plot", fr:"l'intrigue (f.)"}, {t:14, nl:"ontknoping", fr:"le dénouement"}, {t:14, nl:"foto", fr:"la photo"}, {t:14, nl:"fotograaf", fr:"le photographe"}, {t:14, nl:"camera", fr:"la caméra"}, {t:14, nl:"voorstelling", fr:"une représentation"}, {t:14, nl:"opera", fr:"l'opéra"}, {t:14, nl:"musical", fr:"une comédie musicale"}, {t:14, nl:"festival", fr:"un festival"}, {t:14, nl:"toneelstuk", fr:"la pièce de théâtre"}, {t:14, nl:"acteur", fr:"un comédien / acteur"}, {t:14, nl:"hoofdrol", fr:"le rôle principal"}, {t:14, nl:"het podium", fr:"la scène"}, {t:14, nl:"decor", fr:"le decor"}, {t:14, nl:"coulissen", fr:"les coulisses"}, {t:14, nl:"regisseur", fr:"un réalisateur"}, {t:14, nl:"scenario", fr:"le scénario"}, {t:14, nl:"ondertiteling", fr:"le sous-titrage"}, {t:14, nl:"tekenfilm", fr:"le dessin-animé"}, {t:14, nl:"animatiefilm", fr:"le film d'animation"}, {t:14, nl:"thriller", fr:"le thriller"}, {t:14, nl:"blockbuster", fr:"le film à succès"}, {t:14, nl:"schilder", fr:"un peintre"}, {t:14, nl:"beeldhouwer", fr:"un sculpteur"}, {t:14, nl:"architectuur", fr:"l'architecture (f.)"},

    // --- VOYAGE EN FRANCE ---
    {t:15, nl:"Frankrijk", fr:"l'Hexagone (m.)"}, {t:15, nl:"streek / regio", fr:"la région"}, {t:15, nl:"departement", fr:"le département"}, {t:15, nl:"platteland", fr:"la campagne"}, {t:15, nl:"de grens", fr:"la frontière"}, {t:15, nl:"de toerist", fr:"le touriste"}, {t:15, nl:"bureau voor toerisme", fr:"l'office du tourisme"}, {t:15, nl:"zich informeren", fr:"se renseigner"}, {t:15, nl:"verblijf organiseren", fr:"organiser un séjour"}, {t:15, nl:"georganiseerde reis", fr:"un voyage organisé"}, {t:15, nl:"route / traject", fr:"un itinéraire"}, {t:15, nl:"rondreis", fr:"un circuit"}, {t:15, nl:"reservatie maken", fr:"faire une réservation"}, {t:15, nl:"accommodatie", fr:"l'hébergement (m.)"}, {t:15, nl:"lokale specialiteiten", fr:"les spécialités locales"}, {t:15, nl:"historisch monument", fr:"le monument historique"}, {t:15, nl:"kasteel", fr:"le château"}, {t:15, nl:"wijngaard", fr:"le vignoble"}, {t:15, nl:"cultureel erfgoed", fr:"le patrimoine culturel"}, {t:15, nl:"bekend / beroemd", fr:"connu / célèbre"}, {t:15, nl:"trekpleister", fr:"le pôle d'attraction"}, {t:15, nl:"klimaat", fr:"le climat"}, {t:15, nl:"bewolkte lucht", fr:"le ciel nuageux"}, {t:15, nl:"zonnig", fr:"ensoleillé"}, {t:15, nl:"regenbui", fr:"une averse"}, {t:15, nl:"opklaringen", fr:"les éclaircies"}, {t:15, nl:"sneeuw", fr:"la neige"}, {t:15, nl:"dicht bij", fr:"(tout) près de"}, {t:15, nl:"in de omgeving van", fr:"dans les alentours de"}, {t:15, nl:"landschap", fr:"le paysage"}, {t:15, nl:"het zicht", fr:"la vue"}, {t:15, nl:"plantengroei", fr:"la végétation"}, {t:15, nl:"bos", fr:"la forêt"}, {t:15, nl:"pijnbomen", fr:"les pins"}, {t:15, nl:"vallei", fr:"une vallée"}, {t:15, nl:"heuvel", fr:"une colline"}, {t:15, nl:"berg", fr:"une montagne"}, {t:15, nl:"meer", fr:"un lac"}, {t:15, nl:"stroom", fr:"un fleuve"}, {t:15, nl:"oceaan", fr:"l'océan"}, {t:15, nl:"kust", fr:"la côte / le littoral"}, {t:15, nl:"klif / rotswand", fr:"la falaise"}, {t:15, nl:"pittoresk", fr:"pittoresque"}
];

let toutesLesSeries = [];
let indexSerieActuelle = 0, indexMotActuel = 0, tempsRestant = 8, intervalle;

function genererSeries(numTheme) {
    const grille = document.getElementById('set-grid');
    grille.innerHTML = '';
    if (!numTheme) return;
    const vocab = listeVocabulaire.filter(m => m.t == numTheme);
    toutesLesSeries = [];
    for (let i = 0; i < Math.ceil(vocab.length / 9); i++) {
        toutesLesSeries.push(vocab.slice(i * 9, (i * 9) + 14));
    }
    toutesLesSeries.forEach((serie, i) => {
        const carte = document.createElement('div');
        carte.className = 'set-card';
        carte.innerHTML = `<h3>Série ${i+1}</h3><button class="btn" onclick="demarrerSerie(${i})">🚀 Commencer</button><button class="btn btn-secondary" onclick="ouvrirEdition(${i})">📝 Liste</button>`;
        grille.appendChild(carte);
    });
}

function demarrerSerie(idx) {
    indexSerieActuelle = idx; indexMotActuel = 0;
    document.getElementById('container').style.display = 'none';
    document.getElementById('exercise').style.display = 'flex';
    motSuivant();
}

function motSuivant() {
    const serie = toutesLesSeries[indexSerieActuelle];
    if (indexMotActuel >= serie.length) { afficherResultats(); return; }
    tempsRestant = 8;
    document.getElementById('word-display').innerText = serie[indexMotActuel].nl;
    document.getElementById('info-header').innerText = `Mot ${indexMotActuel+1}/${serie.length}`;
    if (intervalle) clearInterval(intervalle);
    intervalle = setInterval(() => {
        tempsRestant--;
        document.getElementById('timer-bar').style.width = (tempsRestant/8*100)+'%';
        if (tempsRestant <= 0) { indexMotActuel++; motSuivant(); }
    }, 1000);
}

function afficherResultats() {
    clearInterval(intervalle);
    document.getElementById('exercise').style.display = 'none';
    document.getElementById('result').style.display = 'flex';
    document.getElementById('res-body').innerHTML = toutesLesSeries[indexSerieActuelle].map(m => `<tr><td>${m.nl}</td><td>${m.fr}</td></tr>`).join('');
}

function ouvrirEdition(idx) {
    indexSerieActuelle = idx;
    const corps = document.getElementById('edit-body');
    corps.innerHTML = toutesLesSeries[idx].map(m => `<tr><td><input type="text" value="${m.nl}"></td><td><input type="text" value="${m.fr}"></td><td>✖</td></tr>`).join('');
    document.getElementById('edit-screen').style.display = 'flex';
}

function sauvegarderEtDemarrer() {
    document.getElementById('edit-screen').style.display = 'none';
    demarrerSerie(indexSerieActuelle);
}
</script>
</body>
</html>