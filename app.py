from flask import Flask, render_template, request

app = Flask(__name__)

PLATOS = [
    {
        "nombre": "Carpaccio de atun rojo",
        "descripcion": "Atun de almadraba, aceite de trufa y alcaparras fritas",
        "detalle": "Atun rojo de almadraba salvaje cortado a cuchillo, marinado 4 horas en AOVE y citricos. Terminado con laminas de trufa negra fresca, alcaparras fritas y sal de Maldon.",
        "precio": "18 EUR",
        "categoria": "entrante",
        "alergenos": "Pescado · Alcaparras · Frutos secos traza",
        "imagen": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600&q=80",
    },
    {
        "nombre": "Gazpacho de temporada",
        "descripcion": "Tomate de rama, pepino, pimiento verde y AOVE",
        "detalle": "Elaborado diariamente con tomate de rama de Almeria, pepino de huerta, pimiento verde italiano y un fondo de ajo negro. Servido muy frio con picatostes de pan de masa madre.",
        "precio": "12 EUR",
        "categoria": "entrante",
        "alergenos": "Gluten (picatostes) · Sin lacteos",
        "imagen": "https://images.unsplash.com/photo-1547592180-85f173990554?w=600&q=80",
    },
    {
        "nombre": "Croquetas de jamon iberico",
        "descripcion": "Bechamel artesanal con jamon de bellota D.O. Guijuelo",
        "detalle": "Bechamel elaborada a mano durante 40 minutos con jamon iberico de bellota D.O. Guijuelo 100%. Rebozado triple con panko japones para una corteza de maxima finura.",
        "precio": "14 EUR",
        "categoria": "entrante",
        "alergenos": "Gluten · Lacteos · Huevo",
        "imagen": "https://images.unsplash.com/photo-1599490659213-e2b9527bd087?w=600&q=80",
    },
    {
        "nombre": "Chuleton de buey a la brasa",
        "descripcion": "1 kg de buey gallego madurado 45 dias, sal Maldon y chimichurri",
        "detalle": "Buey gallego certificado con 45 dias de maduracion en camara propia. Cocinado sobre brasa de encina a 800 C, reposo obligatorio de 8 minutos. Acompanado de patatas confitadas y pimientos del padron.",
        "precio": "68 EUR",
        "categoria": "principal",
        "alergenos": "Sin gluten · Sin lacteos",
        "imagen": "https://images.unsplash.com/photo-1600891964599-f61ba0e24092?w=600&q=80",
    },
    {
        "nombre": "Lubina a la sal",
        "descripcion": "Lubina salvaje entera, costra de sal marina y hierbas del Mediterraneo",
        "detalle": "Lubina salvaje del Atlantico (1,2 kg) envuelta en costra de sal marina gruesa con estragón, hinojo y piel de limon. Horneada 22 minutos. Desmigada en sala frente al comensal.",
        "precio": "42 EUR",
        "categoria": "principal",
        "alergenos": "Pescado · Sin gluten",
        "imagen": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=600&q=80",
    },
    {
        "nombre": "Pasta fresca al tartufo",
        "descripcion": "Tagliolini caseros, mantequilla de trufa negra y parmesano 36 meses",
        "detalle": "Pasta fresca elaborada cada manana con semola de grano duro y yema de huevo ecologico. Salteada en mantequilla de trufa negra Perigord y parmesano Reggiano afinado 36 meses.",
        "precio": "28 EUR",
        "categoria": "principal",
        "alergenos": "Gluten · Huevo · Lacteos",
        "imagen": "https://images.unsplash.com/photo-1555949258-eb67b1ef0ceb?w=600&q=80",
    },
    {
        "nombre": "Coulant de chocolate negro",
        "descripcion": "Corazon fundente de Valrhona 70%, helado de vainilla de Madagascar",
        "detalle": "Masa de chocolate Valrhona Grand Cru 70% con corazon liquido de ganache caliente. Horneado al momento, servido con helado artesanal de vainilla Bourbon de Madagascar y polvo de oro comestible.",
        "precio": "10 EUR",
        "categoria": "postre",
        "alergenos": "Gluten · Huevo · Lacteos · Frutos secos traza",
        "imagen": "https://images.unsplash.com/photo-1624353365286-3f8d62daad51?w=600&q=80",
    },
    {
        "nombre": "Tarta de queso vasca",
        "descripcion": "Textura cremosa, quemado al horno, mermelada de frutos rojos",
        "detalle": "Queso cremoso de produccion local, horneado a alta temperatura hasta obtener el exterior tostado caracteristico. Acompanada de mermelada artesanal de fresas y frambuesas de temporada.",
        "precio": "9 EUR",
        "categoria": "postre",
        "alergenos": "Lacteos · Huevo · Sin gluten",
        "imagen": "https://images.unsplash.com/photo-1567327613485-fbc7bf616560?w=600&q=80",
    },
    {
        "nombre": "Seleccion del sumiller",
        "descripcion": "Vino de la casa, tinto o blanco de produccion local",
        "detalle": "Rotacion semanal de vinos de bodegas con las que mantenemos relacion directa. El sumiller selecciona el maridaje perfecto para tu menu. Disponible por copa o botella.",
        "precio": "6 EUR / copa",
        "categoria": "bebida",
        "alergenos": "Sulfitos",
        "imagen": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=600&q=80",
    },
    {
        "nombre": "Agua mineral",
        "descripcion": "Con o sin gas, botella 75 cl",
        "detalle": "Agua de manantial de los Pirineos, disponible con o sin gas. Servida en botella de cristal retornable a temperatura optima de consumo.",
        "precio": "3 EUR",
        "categoria": "bebida",
        "alergenos": "Sin alergenos",
        "imagen": "https://images.unsplash.com/photo-1548839140-29a749e1cf4d?w=600&q=80",
    },
]


@app.route("/")
def index():
    return render_template("index.html", active="inicio")


@app.route("/menu")
def menu():
    return render_template("menu.html", active="menu", platos=PLATOS)


@app.route("/galeria")
def galeria():
    return render_template("galeria.html", active="galeria")


@app.route("/reservas", methods=["GET", "POST"])
def reservas():
    mensaje = None
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        fecha  = request.form.get("fecha",  "").strip()
        hora   = request.form.get("hora",   "").strip()
        if nombre and fecha and hora:
            mensaje = f"Reserva confirmada para {nombre} el {fecha} a las {hora}. Te escribiremos pronto."
        else:
            mensaje = "Por favor completa todos los campos obligatorios."
    return render_template("reservas.html", active="reservas", mensaje=mensaje)


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    mensaje = None
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        if nombre:
            mensaje = f"Gracias, {nombre}. Hemos recibido tu mensaje y te responderemos en breve."
        else:
            mensaje = "Por favor completa todos los campos obligatorios."
    return render_template("contacto.html", active="contacto", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
