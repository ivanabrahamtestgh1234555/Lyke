import streamlit as st

# 1. Configuración de la página (debe ser el primer comando)
st.set_page_config(page_title="Lyke - Corporativo", page_icon="🏢", layout="wide")

# 2. Menú de navegación en la barra lateral
st.sidebar.title("LYKE")
st.sidebar.markdown("---")
menu = ["Inicio", "Nosotros", "Servicios"]
eleccion = st.sidebar.radio("Navegación", menu)

st.sidebar.markdown("---")
st.sidebar.info("© 2026 Lyke. Todos los derechos reservados.")

# ----------------------------------------
# PÁGINA DE INICIO
# ----------------------------------------
if eleccion == "Inicio":
    st.title("Bienvenido a Lyke 🚀")
    st.markdown("### Innovación, tecnología y soluciones empresariales a tu medida.")
    st.write("Transformamos tus ideas en realidades corporativas con un enfoque ágil y moderno.")
    
    st.divider()
    
    # Sistema de columnas para crear un diseño atractivo
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("#### Lleva tu empresa al siguiente nivel")
        st.write("A diferencia de las agencias tradicionales, en Lyke construimos soluciones tecnológicas que escalan contigo. Lo que significa que ahorrarás tiempo y dinero a largo plazo.")
        
        # Botón decorativo
        if st.button("Ver Nuestros Servicios", type="primary"):
            st.success("👈 Selecciona 'Servicios' en el menú lateral izquierdo para ver más.")
            
    with col2:
        # Cargamos una imagen desde la web para ilustrar
        st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80", use_column_width=True)

# ----------------------------------------
# PÁGINA DE NOSOTROS
# ----------------------------------------
elif eleccion == "Nosotros":
    st.title("Sobre Lyke 🏢")
    st.write("Somos una empresa dedicada a impulsar el éxito de nuestros clientes a través de estrategias innovadoras.")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.header("🎯 Nuestra Misión")
        st.info("Proveer soluciones tecnológicas y corporativas de primer nivel que optimicen el flujo de trabajo de las empresas del mañana.")
    
    with col2:
        st.header("👁️ Nuestra Visión")
        st.success("Ser líderes en el mercado global, reconocidos por nuestra excelencia, adaptabilidad y compromiso con nuestros usuarios.")

# ----------------------------------------
# PÁGINA DE SERVICIOS
# ----------------------------------------
elif eleccion == "Servicios":
    st.title("Nuestros Servicios 💼")
    st.write("Diseñados para optimizar cada área de tu negocio.")
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📊 Consultoría Estratégica")
        st.write("Optimizamos tus procesos y te guiamos en la toma de decisiones tecnológicas. Tomamos decisiones basadas en métricas reales.")
        
    with col2:
        st.subheader("💻 Desarrollo Web")
        st.write("Creamos aplicaciones y sitios web a medida. De este modo, tus clientes disfrutarán de la mejor experiencia digital.")
        
    with col3:
        st.subheader("🎧 Soporte Corporativo")
        st.write("Te acompañamos 24/7 para garantizar que tu negocio nunca se detenga con un mantenimiento técnico continuo.")
