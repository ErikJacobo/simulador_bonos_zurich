# --- Simulador Zurich 2025 ---
import streamlit as st

def format_currency(value):
    return "${:,.2f}".format(value)

st.set_page_config(page_title="Simulador Bonos Zurich 2025", layout="centered")
st.markdown("<h1 style='text-align: center;'>Simulador de Bonos</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Zurich 2025</h2>", unsafe_allow_html=True)

# Campo inicial: Nombre del agente
nombre_agente = st.text_input("Nombre del agente")

if nombre_agente:
    # Selector de plan
    plan = st.selectbox("Selecciona el plan:", ["IMPULZA", "CIZ"])

    # Selector de ramo según el plan
    ramos_impulza = ["Auto", "Flotillas", "Daños", "Vida + GMM", "Accidentes Personales", "Universal Assistance"]
    ramos_ciz = ["Auto", "Flotillas", "Daños", "Vida", "GMM", "Conservación"]

    ramo = st.selectbox("Selecciona el ramo:", ramos_impulza if plan == "IMPULZA" else ramos_ciz)

    total_bono = 0
    resultados = []
    datos_ingresados = []

    # Lógica por plan y ramo
    if plan == "IMPULZA" and ramo == "Auto":
        pol = st.number_input("Pólizas pagadas mensuales (Auto)", min_value=0)
        if pol >= 5:
            porcentaje = 0.05
            comentario = f"✅ Emitiste {pol} pólizas. Superas el mínimo de 5 para el 5%."
        elif pol >= 3:
            porcentaje = 0.04
            comentario = f"✅ Emitiste {pol} pólizas. En el rango de 3-4, aplica bono del 4%."
        elif pol >= 1:
            porcentaje = 0.03
            comentario = f"✅ Emitiste al menos una póliza. Aplica bono del 3%."
        else:
            porcentaje = 0
            comentario = "❌ No emitiste pólizas. Se requiere mínimo una para aplicar bono."
        monto = pol * 1000 * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Pólizas emitidas: {pol}")
        resultados.append(("Bono Auto", porcentaje, monto, comentario))

    if resultados and st.button("Calcular Bonos"):
        st.markdown(f"### 🧾 Resultado para {nombre_agente}")
        st.markdown("#### 📊 Datos Ingresados:")
        for dato in datos_ingresados:
            st.markdown(f"- {dato}")

        st.markdown("#### 💵 Resultados de Bono:")
        for nombre_bono, porcentaje, monto, comentario in resultados:
            st.markdown(f"""
                <div style='margin-bottom: 10px;'>
                    <strong>{nombre_bono}:</strong><br>
                    Porcentaje aplicado: <code>{porcentaje*100:.2f}%</code><br>
                    Monto ganado: <code>{format_currency(monto)}</code><br>
                    Explicación: {comentario}
                </div>
            """, unsafe_allow_html=True)

        st.markdown("#### 🧮 Total del Bono:")
        st.markdown(f"<code>{format_currency(total_bono)}</code>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: gray;'>Aplican restricciones y condiciones conforme al cuaderno oficial de Zurich Seguros 2025.</p>", unsafe_allow_html=True)
    elif plan == "IMPULZA" and ramo == "Flotillas":
        pol = st.number_input("Pólizas pagadas mensuales (Flotillas)", min_value=0)
        if pol >= 7:
            porcentaje = 0.035
            comentario = "✅ Emitiste 7 o más pólizas. Aplica bono del 3.5%."
        elif pol >= 5:
            porcentaje = 0.025
            comentario = "✅ Emitiste entre 5 y 6 pólizas. Aplica bono del 2.5%."
        elif pol >= 3:
            porcentaje = 0.015
            comentario = "✅ Emitiste entre 3 y 4 pólizas. Aplica bono del 1.5%."
        else:
            porcentaje = 0
            comentario = "❌ Emitiste menos de 3 pólizas. No aplica bono."
        monto = pol * 1000 * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Pólizas Flotillas: {pol}")
        resultados.append(("Bono Flotillas", porcentaje, monto, comentario))
    elif plan == "IMPULZA" and ramo == "Daños":
        canal = st.radio("¿Por dónde emite?", ["Portal", "Mesa de trámites"])
        pol = st.number_input("Pólizas pagadas mensuales (Daños)", min_value=0)
        if canal == "Portal":
            if pol >= 5:
                porcentaje = 0.07
                comentario = "✅ Emitiste 5 o más pólizas por Portal. Aplica bono del 7%."
            elif pol >= 3:
                porcentaje = 0.06
                comentario = "✅ Emitiste entre 3 y 4 pólizas por Portal. Aplica bono del 6%."
            elif pol >= 1:
                porcentaje = 0.03
                comentario = "✅ Emitiste al menos 1 póliza por Portal. Aplica bono del 3%."
            else:
                porcentaje = 0
                comentario = "❌ No emitiste pólizas por Portal. No aplica bono."
        else:
            if pol >= 5:
                porcentaje = 0.06
                comentario = "✅ Emitiste 5 o más pólizas por Mesa de trámites. Aplica bono del 6%."
            elif pol >= 3:
                porcentaje = 0.05
                comentario = "✅ Emitiste entre 3 y 4 pólizas por Mesa de trámites. Aplica bono del 5%."
            elif pol >= 1:
                porcentaje = 0.03
                comentario = "✅ Emitiste al menos 1 póliza por Mesa de trámites. Aplica bono del 3%."
            else:
                porcentaje = 0
                comentario = "❌ No emitiste pólizas por Mesa de trámites. No aplica bono."
        monto = pol * 1000 * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Pólizas Daños: {pol} / Canal: {canal}")
        resultados.append(("Bono Daños", porcentaje, monto, comentario))
    elif plan == "IMPULZA" and ramo == "Vida + GMM":
        pol = st.number_input("Pólizas acumuladas (Vida + GMM)", min_value=0)
        if pol >= 11:
            porcentaje = 0.08
            comentario = "✅ Emitiste 11 o más pólizas. Aplica bono combinado: 3% GMM + 5% Vida (Total 8%)."
        elif pol >= 4:
            porcentaje = 0.06
            comentario = "✅ Emitiste entre 4 y 10 pólizas. Aplica bono combinado: 2% GMM + 4% Vida (Total 6%)."
        elif pol >= 1:
            porcentaje = 0.04
            comentario = "✅ Emitiste entre 1 y 3 pólizas. Aplica bono combinado: 1% GMM + 3% Vida (Total 4%)."
        else:
            porcentaje = 0
            comentario = "❌ No emitiste pólizas acumuladas. Mínimo 1 para aplicar bono."
        monto = pol * 1000 * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Pólizas Vida + GMM acumuladas: {pol}")
        resultados.append(("Bono Vida + GMM", porcentaje, monto, comentario))
    elif plan == "IMPULZA" and ramo == "Accidentes Personales":
        prima = st.number_input("Prima mensual acumulada (Accidentes)", min_value=0.0)
        if prima >= 1_000_000:
            porcentaje = 0.12
            comentario = "✅ Prima ≥ $1,000,000. Aplica bono del 12%."
        elif prima >= 400_000:
            porcentaje = 0.08
            comentario = "✅ Prima entre $400,000 y $999,999. Aplica bono del 8%."
        elif prima >= 45_000:
            porcentaje = 0.04
            comentario = "✅ Prima entre $45,000 y $399,999. Aplica bono del 4%."
        else:
            porcentaje = 0
            comentario = "❌ Prima insuficiente. Mínimo $45,000 para aplicar bono."
        monto = prima * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Prima mensual: {format_currency(prima)}")
        resultados.append(("Bono Accidentes", porcentaje, monto, comentario))
    elif plan == "IMPULZA" and ramo == "Universal Assistance":
        prima = st.number_input("Prima mensual en USD (Universal Assistance)", min_value=0.0)
        if prima >= 8500:
            porcentaje = 0.10
            comentario = "✅ Prima ≥ $8,500 USD. Aplica bono del 10%."
        elif prima >= 4000:
            porcentaje = 0.07
            comentario = "✅ Prima entre $4,000 y $8,499 USD. Aplica bono del 7%."
        elif prima >= 2000:
            porcentaje = 0.05
            comentario = "✅ Prima entre $2,000 y $3,999 USD. Aplica bono del 5%."
        else:
            porcentaje = 0
            comentario = "❌ Prima insuficiente. Mínimo $2,000 USD para aplicar bono."
        monto = prima * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Prima mensual (USD): {format_currency(prima)}")
        resultados.append(("Bono Universal Assistance", porcentaje, monto, comentario))
    elif plan == "CIZ" and ramo == "Auto":
        prima = st.number_input("Prima mensual Autos (CIZ)", min_value=0.0)
        sin = st.number_input("Siniestralidad Autos (%)", min_value=0.0, max_value=100.0)
        if sin <= 65:
            if prima >= 100_000:
                porcentaje = 0.055
                comentario = "✅ Prima ≥ $100,000 y siniestralidad ≤ 65%. Aplica bono del 5.5%."
            elif prima >= 50_000:
                porcentaje = 0.045
                comentario = "✅ Prima entre $50,000 y $99,999. Aplica bono del 4.5%."
            elif prima >= 20_000:
                porcentaje = 0.035
                comentario = "✅ Prima entre $20,000 y $49,999. Aplica bono del 3.5%."
            else:
                porcentaje = 0
                comentario = "❌ Prima menor a $20,000. No aplica bono."
        else:
            porcentaje = 0
            comentario = f"❌ Siniestralidad de {sin:.2f}% excede el máximo permitido (65%)."
        monto = prima * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Prima Autos: {format_currency(prima)} / Siniestralidad: {sin:.2f}%")
        resultados.append(("Bono Auto CIZ", porcentaje, monto, comentario))
    elif plan == "CIZ" and ramo == "Flotillas":
        prima = st.number_input("Prima mensual Flotillas (CIZ)", min_value=0.0)
        sin = st.number_input("Siniestralidad Flotillas (%)", min_value=0.0, max_value=100.0)
        if sin <= 65:
            if prima >= 100_000:
                porcentaje = 0.045
                comentario = "✅ Prima ≥ $100,000 y siniestralidad aceptable. Aplica bono del 4.5%."
            elif prima >= 50_000:
                porcentaje = 0.035
                comentario = "✅ Prima entre $50,000 y $99,999. Aplica bono del 3.5%."
            elif prima >= 20_000:
                porcentaje = 0.025
                comentario = "✅ Prima entre $20,000 y $49,999. Aplica bono del 2.5%."
            else:
                porcentaje = 0
                comentario = "❌ Prima menor a $20,000. No aplica bono."
        else:
            porcentaje = 0
            comentario = f"❌ Siniestralidad de {sin:.2f}% excede el límite permitido (65%)."
        monto = prima * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Prima Flotillas: {format_currency(prima)} / Siniestralidad: {sin:.2f}%")
        resultados.append(("Bono Flotillas CIZ", porcentaje, monto, comentario))
    elif plan == "CIZ" and ramo == "Daños":
        prima = st.number_input("Prima mensual Daños (CIZ)", min_value=0.0)
        sin = st.number_input("Siniestralidad Daños (%)", min_value=0.0, max_value=100.0)
        if sin <= 60:
            if prima >= 100_000:
                porcentaje = 0.06
                comentario = "✅ Prima ≥ $100,000 y siniestralidad ≤ 60%. Aplica bono del 6%."
            elif prima >= 50_000:
                porcentaje = 0.04
                comentario = "✅ Prima entre $50,000 y $99,999. Aplica bono del 4%."
            elif prima >= 20_000:
                porcentaje = 0.02
                comentario = "✅ Prima entre $20,000 y $49,999. Aplica bono del 2%."
            else:
                porcentaje = 0
                comentario = "❌ Prima menor a $20,000. No aplica bono."
        else:
            porcentaje = 0
            comentario = f"❌ Siniestralidad de {sin:.2f}% excede el máximo de 60%."
        monto = prima * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Prima Daños: {format_currency(prima)} / Siniestralidad: {sin:.2f}%")
        resultados.append(("Bono Daños CIZ", porcentaje, monto, comentario))
    elif plan == "CIZ" and ramo == "Vida":
        primas = st.number_input("Primas pagadas mensuales (Vida)", min_value=0.0)
        if primas >= 50_000:
            porcentaje = 0.06
            comentario = "✅ Primas ≥ $50,000. Aplica bono del 6%."
        elif primas >= 30_000:
            porcentaje = 0.04
            comentario = "✅ Primas entre $30,000 y $49,999. Aplica bono del 4%."
        elif primas >= 10_000:
            porcentaje = 0.02
            comentario = "✅ Primas entre $10,000 y $29,999. Aplica bono del 2%."
        else:
            porcentaje = 0
            comentario = "❌ Primas insuficientes. No aplica bono."
        monto = primas * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Primas Vida: {format_currency(primas)}")
        resultados.append(("Bono Vida CIZ", porcentaje, monto, comentario))
    elif plan == "CIZ" and ramo == "GMM":
        primas = st.number_input("Primas pagadas mensuales (GMM)", min_value=0.0)
        if primas >= 50_000:
            porcentaje = 0.05
            comentario = "✅ Primas ≥ $50,000. Aplica bono del 5%."
        elif primas >= 30_000:
            porcentaje = 0.03
            comentario = "✅ Primas entre $30,000 y $49,999. Aplica bono del 3%."
        elif primas >= 10_000:
            porcentaje = 0.01
            comentario = "✅ Primas entre $10,000 y $29,999. Aplica bono del 1%."
        else:
            porcentaje = 0
            comentario = "❌ Primas insuficientes. No aplica bono."
        monto = primas * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Primas GMM: {format_currency(primas)}")
        resultados.append(("Bono GMM CIZ", porcentaje, monto, comentario))
    elif plan == "CIZ" and ramo == "Conservación":
        cartera = st.number_input("Cartera conservada anual (CIZ)", min_value=0.0)
        if cartera >= 200_000:
            porcentaje = 0.04
            comentario = "✅ Conservación ≥ $200,000. Aplica bono del 4%."
        elif cartera >= 100_000:
            porcentaje = 0.03
            comentario = "✅ Conservación entre $100,000 y $199,999. Aplica bono del 3%."
        elif cartera >= 50_000:
            porcentaje = 0.02
            comentario = "✅ Conservación entre $50,000 y $99,999. Aplica bono del 2%."
        else:
            porcentaje = 0
            comentario = "❌ Conservación insuficiente. No aplica bono."
        monto = cartera * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Cartera conservada: {format_currency(cartera)}")
        resultados.append(("Bono Conservación CIZ", porcentaje, monto, comentario))
