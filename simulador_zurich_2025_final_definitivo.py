
import streamlit as st

def format_currency(value):
    return "${:,.2f}".format(value)

st.set_page_config(page_title="Simulador Bonos Zurich 2025", layout="centered")

st.markdown("<h1 style='text-align: center;'>Simulador de Bonos</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Zurich 2025</h2>", unsafe_allow_html=True)

nombre_agente = st.text_input("Nombre del agente")

if nombre_agente:
    plan = st.selectbox("Selecciona el plan:", ["IMPULZA", "CIZ"])
    
    ramos_impulza = ["Auto", "Daños"]
    ramos_ciz = ["Auto"]

    if plan == "IMPULZA":
        ramo = st.selectbox("Selecciona el ramo:", ramos_impulza)
    else:
        ramo = st.selectbox("Selecciona el ramo:", ramos_ciz)

    total_bono = 0
    resultados = []
    datos_ingresados = []

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
        resultados.append(f"Bono Auto: {porcentaje*100:.2f}% → {format_currency(monto)} → {comentario}")

    elif plan == "IMPULZA" and ramo == "Daños":
        canal = st.radio("¿Por dónde emite?", ["Portal", "Mesa de trámites"])
        pol = st.number_input("Pólizas pagadas mensuales (Daños)", min_value=0)
        if canal == "Portal":
            if pol >= 5:
                porcentaje = 0.07
                comentario = "✅ Emitiste 5+ pólizas vía Portal. Aplica bono del 7%."
            elif pol >= 3:
                porcentaje = 0.06
                comentario = "✅ Emitiste 3-4 pólizas vía Portal. Aplica bono del 6%."
            elif pol >= 1:
                porcentaje = 0.03
                comentario = "✅ Emitiste al menos una póliza vía Portal. Aplica bono del 3%."
            else:
                porcentaje = 0
                comentario = "❌ Se requiere mínimo una póliza para aplicar bono."
        else:
            if pol >= 5:
                porcentaje = 0.06
                comentario = "✅ Emitiste 5+ pólizas vía Mesa de trámites. Aplica bono del 6%."
            elif pol >= 3:
                porcentaje = 0.05
                comentario = "✅ Emitiste 3-4 pólizas vía Mesa de trámites. Aplica bono del 5%."
            elif pol >= 1:
                porcentaje = 0.03
                comentario = "✅ Emitiste al menos una póliza vía Mesa. Aplica bono del 3%."
            else:
                porcentaje = 0
                comentario = "❌ Se requiere mínimo una póliza para aplicar bono."
        monto = pol * 1000 * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Pólizas: {pol} / Canal: {canal}")
        resultados.append(f"Bono Daños: {porcentaje*100:.2f}% → {format_currency(monto)} → {comentario}")

    elif plan == "CIZ" and ramo == "Auto":
        prima = st.number_input("Prima mensual Auto", min_value=0.0)
        sin = st.number_input("Siniestralidad (%)", min_value=0.0, max_value=100.0)
        if sin <= 65:
            if prima >= 100_000:
                porcentaje = 0.055
                comentario = "✅ Prima alta y siniestralidad ≤ 65%. Aplica bono del 5.5%."
            elif prima >= 50_000:
                porcentaje = 0.045
                comentario = "✅ Prima media y siniestralidad ≤ 65%. Aplica bono del 4.5%."
            elif prima >= 20_000:
                porcentaje = 0.035
                comentario = "✅ Prima mínima cumplida. Aplica bono del 3.5%."
            else:
                porcentaje = 0
                comentario = "❌ Prima insuficiente. Mínimo requerido: 20,000."
        else:
            porcentaje = 0
            comentario = f"❌ Siniestralidad ({sin:.2f}%) supera el máximo permitido (65%)."
        monto = prima * porcentaje
        total_bono += monto
        datos_ingresados.append(f"Prima: {format_currency(prima)} / Siniestralidad: {sin:.2f}%")
        resultados.append(f"Bono Auto CIZ: {porcentaje*100:.2f}% → {format_currency(monto)} → {comentario}")

    if resultados and st.button("Calcular Bonos"):
        st.markdown(f"### 🧾 Resultado para {nombre_agente}")
        st.markdown("#### 📊 Datos Ingresados:")
        for dato in datos_ingresados:
            st.markdown(f"- {dato}")
        st.markdown("#### 💵 Resultados de Bono:")
        for r in resultados:
            st.markdown(f"- {r}")
        st.markdown("#### 🧮 Total del Bono:")
        st.markdown(f"- {format_currency(total_bono)}")
        st.markdown("<p style='text-align: center; color: gray;'>Aplican restricciones y condiciones conforme al cuaderno oficial de Zurich Seguros 2025.</p>", unsafe_allow_html=True)
