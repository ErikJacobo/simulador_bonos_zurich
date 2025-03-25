import streamlit as st

def format_currency(value):
    return "${:,.2f}".format(value)

st.set_page_config(page_title="Simulador Bonos Zurich 2025", layout="centered")

st.title("Simulador de Bonos Zurich 2025")

plan = st.selectbox("Selecciona el plan:", ["IMPULZA", "CIZ"])
agente = st.text_input("Nombre del agente")

total_bono = 0
resultados = []

def calcular_impulza():
    global total_bono
    st.subheader("IMPULZA - Bonos por ramo")

    # Auto Individual
    pol_auto = st.number_input("Pólizas pagadas mensuales (Auto)", min_value=0, step=1)
    if pol_auto >= 5:
        bono = 0.05
        comentario = "✅ 5% por 5+ pólizas"
    elif pol_auto >= 3:
        bono = 0.04
        comentario = "✅ 4% por 3-4 pólizas"
    elif pol_auto >= 1:
        bono = 0.03
        comentario = "✅ 3% por 1-2 pólizas"
    else:
        bono = 0
        comentario = "❌ No aplica bono"
    monto = pol_auto * 1000 * bono
    total_bono += monto
    resultados.append(f"**Auto:** {format_currency(monto)} ({bono*100:.1f}%) - {comentario}")

    # Flotillas
    pol_flot = st.number_input("Pólizas pagadas mensuales (Flotillas)", min_value=0, step=1)
    if pol_flot >= 7:
        bono = 0.035
        comentario = "✅ 3.5% por 7+ pólizas"
    elif pol_flot >= 5:
        bono = 0.025
        comentario = "✅ 2.5% por 5-6 pólizas"
    elif pol_flot >= 3:
        bono = 0.015
        comentario = "✅ 1.5% por 3-4 pólizas"
    else:
        bono = 0
        comentario = "❌ No aplica bono"
    monto = pol_flot * 1000 * bono
    total_bono += monto
    resultados.append(f"**Flotillas:** {format_currency(monto)} ({bono*100:.1f}%) - {comentario}")

    # Daños
    canal = st.radio("¿Por dónde emite Daños?", ["Portal", "Mesa"])
    pol_daños = st.number_input("Pólizas pagadas mensuales (Daños)", min_value=0, step=1)
    if pol_daños >= 5:
        bono = 0.07
    elif pol_daños >= 3:
        bono = 0.06
    elif pol_daños >= 1:
        bono = 0.03
    else:
        bono = 0
    comentario = f"{'✅' if bono else '❌'} {'Aplica' if bono else 'No aplica'} bono"
    monto = pol_daños * 1000 * bono
    total_bono += monto
    resultados.append(f"**Daños ({canal}):** {format_currency(monto)} ({bono*100:.1f}%) - {comentario}")

    # Vida + GMM
    pol_vida_gmm = st.number_input("Pólizas acumulables Vida + GMM", min_value=0, step=1)
    if pol_vida_gmm >= 11:
        bono = 0.08
        comentario = "✅ 3% GMM + 5% Vida"
    elif pol_vida_gmm >= 4:
        bono = 0.06
        comentario = "✅ 2% GMM + 4% Vida"
    elif pol_vida_gmm >= 1:
        bono = 0.04
        comentario = "✅ 1% GMM + 3% Vida"
    else:
        bono = 0
        comentario = "❌ No aplica bono"
    monto = pol_vida_gmm * 1000 * bono
    total_bono += monto
    resultados.append(f"**Vida + GMM:** {format_currency(monto)} ({bono*100:.1f}%) - {comentario}")

    # Accidentes Personales
    prima_acc = st.number_input("Prima mensual Accidentes Personales", min_value=0, step=1000)
    if prima_acc >= 1_000_000:
        bono = 0.12
    elif prima_acc >= 400_000:
        bono = 0.08
    elif prima_acc >= 45_000:
        bono = 0.04
    else:
        bono = 0
    comentario = f"{'✅' if bono else '❌'} {'Aplica' if bono else 'No aplica'} bono"
    monto = prima_acc * bono
    total_bono += monto
    resultados.append(f"**Accidentes Personales:** {format_currency(monto)} ({bono*100:.1f}%) - {comentario}")

    # Universal Assistance
    prima_usd = st.number_input("Prima mensual Universal Assistance (USD)", min_value=0, step=100)
    if prima_usd >= 8500:
        bono = 0.10
    elif prima_usd >= 4000:
        bono = 0.07
    elif prima_usd >= 2000:
        bono = 0.05
    else:
        bono = 0
    comentario = f"{'✅' if bono else '❌'} {'Aplica' if bono else 'No aplica'} bono"
    monto = prima_usd * bono
    total_bono += monto
    resultados.append(f"**Universal Assistance:** {format_currency(monto)} ({bono*100:.1f}%) - {comentario}")

def calcular_ciz():
    global total_bono
    st.subheader("CIZ - Bonos por ramo")

    prima_auto = st.number_input("Prima mensual Auto", min_value=0, step=1000)
    sin_auto = st.slider("Siniestralidad Auto (%)", 0, 100)
    if sin_auto <= 65:
        if prima_auto >= 100_000:
            bono = 0.055
        elif prima_auto >= 50_000:
            bono = 0.045
        elif prima_auto >= 20_000:
            bono = 0.035
        else:
            bono = 0
    else:
        bono = 0
    comentario = f"{'✅' if bono else '❌'} {'Aplica' if bono else 'No aplica'} bono"
    monto = prima_auto * bono
    total_bono += monto
    resultados.append(f"**Auto CIZ:** {format_currency(monto)} ({bono*100:.1f}%) - {comentario}")



    # Flotillas
    prima_flot = st.number_input("Prima mensual Flotillas", min_value=0, step=1000)
    sin_flot = st.slider("Siniestralidad Flotillas (%)", 0, 100)
    if sin_flot <= 65:
        if prima_flot >= 150_000:
            bono = 0.045
        elif prima_flot >= 100_000:
            bono = 0.035
        elif prima_flot >= 30_000:
            bono = 0.025
        else:
            bono = 0
    else:
        bono = 0
    comentario = f"{'✅' if bono else '❌'} {'Aplica' if bono else 'No aplica'} bono"
    monto = prima_flot * bono
    total_bono += monto
    resultados.append(f"**Flotillas CIZ:** {format_currency(monto)} ({bono*100:.1f}%) - {comentario}")

    # Daños
    canal = st.radio("¿Por dónde emite Daños?", ["Portal", "Mesa de trámites"])
    prima_daños = st.number_input("Prima mensual Daños", min_value=0, step=1000)
    sin_daños = st.slider("Siniestralidad Daños (%)", 0, 100)
    bono = 0
    if canal == "Portal":
        if prima_daños >= 80_000:
            bono = 0.06
        elif prima_daños >= 40_000:
            bono = 0.05
        elif prima_daños >= 15_000:
            bono = 0.03
    else:  # Mesa de trámites
        if sin_daños <= 40:
            if prima_daños >= 100_000:
                bono = 0.06
            elif prima_daños >= 50_000:
                bono = 0.05
    comentario = f"{'✅' if bono else '❌'} {'Aplica' if bono else 'No aplica'} bono"
    monto = prima_daños * bono
    total_bono += monto
    resultados.append(f"**Daños CIZ ({canal}):** {format_currency(monto)} ({bono*100:.1f}%) - {comentario}")

    # Vida y GMM nuevos
    prima_vida = st.number_input("Prima nueva Vida", min_value=0, step=1000)
    prima_gmm = st.number_input("Prima nueva GMM", min_value=0, step=1000)

    if prima_vida >= 6_000_000:
        bono_vida = 0.06
    elif prima_vida >= 2_500_000:
        bono_vida = 0.05
    elif prima_vida >= 500_000:
        bono_vida = 0.04
    elif prima_vida >= 50_000:
        bono_vida = 0.03
    else:
        bono_vida = 0
    monto_vida = prima_vida * bono_vida
    total_bono += monto_vida
    resultados.append(f"**Vida nueva:** {format_currency(monto_vida)} ({bono_vida*100:.1f}%)")

    if prima_gmm >= 6_000_000:
        bono_gmm = 0.03
    elif prima_gmm >= 2_500_000:
        bono_gmm = 0.02
    elif prima_gmm >= 500_000:
        bono_gmm = 0.01
    else:
        bono_gmm = 0
    monto_gmm = prima_gmm * bono_gmm
    total_bono += monto_gmm
    resultados.append(f"**GMM nuevo:** {format_currency(monto_gmm)} ({bono_gmm*100:.1f}%)")

    # Conservación y rentabilidad
    cons_vida = st.slider("Conservación cartera Vida (%)", 0, 100)
    sin_vida = st.slider("Siniestralidad cartera Vida (%)", 0, 100)
    if cons_vida >= 90 and sin_vida <= 60:
        bono_cons_vida = 0.025
    elif cons_vida >= 80 and sin_vida <= 89.99:
        bono_cons_vida = 0.015
    else:
        bono_cons_vida = 0
    monto_cons_vida = prima_vida * bono_cons_vida
    total_bono += monto_cons_vida
    resultados.append(f"**Bono conservación Vida:** {format_currency(monto_cons_vida)} ({bono_cons_vida*100:.1f}%)")

    cons_gmm = st.slider("Conservación cartera GMM (%)", 0, 100)
    sin_gmm = st.slider("Siniestralidad cartera GMM (%)", 0, 100)
    if cons_gmm >= 90 and sin_gmm <= 60:
        bono_cons_gmm = 0.025
    elif cons_gmm >= 80 and sin_gmm <= 89.99:
        bono_cons_gmm = 0.015
    else:
        bono_cons_gmm = 0
    monto_cons_gmm = prima_gmm * bono_cons_gmm
    total_bono += monto_cons_gmm
    resultados.append(f"**Bono conservación GMM:** {format_currency(monto_cons_gmm)} ({bono_cons_gmm*100:.1f}%)")


if st.button("Calcular Bonos"):
    if plan == "IMPULZA":
        calcular_impulza()
    elif plan == "CIZ":
        calcular_ciz()

    st.markdown("### Resultados")
    for r in resultados:
        st.markdown(f"- {r}")
    st.markdown(f"### Total bono estimado: **{format_currency(total_bono)}**")
