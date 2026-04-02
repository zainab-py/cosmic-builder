import streamlit as st
import plotly.graph_objects as go
import numpy as np
from style import cosmic_style
from ai_module import generate_planet_description

# --- PAGE CONFIG ---
st.set_page_config(page_title="Build a Planet", page_icon="🪐", layout="wide")

# --- LOAD STYLE ---
st.markdown(cosmic_style(), unsafe_allow_html=True)

# --- TITLE ---
st.title("🪐 Build Your Own Planet")
st.markdown("Design your dream planet — rings, moons, colors, and all. Then hit **Build Planet** to bring it to life in 3D!")

# --- SIDEBAR INPUTS ---
st.sidebar.header("Planet Customization")
planet_name = st.sidebar.text_input("Planet Name", "Zynara")
radius = st.sidebar.slider("Planet Radius", 0.5, 5.0, 2.0)
color = st.sidebar.color_picker("Planet Color", "#3498db")
has_rings = st.sidebar.checkbox("Has Rings?", True)
ring_thickness = st.sidebar.slider("Ring Thickness", 0.05, 0.5, 0.1)
num_moons = st.sidebar.slider("Number of Moons", 0, 5, 2)
rotation_speed = st.sidebar.slider("Rotation Speed", 0.1, 2.0, 1.0)
show_orbit = st.sidebar.checkbox("Show Orbit Path", False)
ai_description = st.sidebar.checkbox("Generate AI Description", False)

def darken_color(hex_color, factor=0.4):
    """Return a darker shade of the given hex color."""
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    dark_rgb = tuple(int(c * factor) for c in rgb)
    return '#{:02x}{:02x}{:02x}'.format(*dark_rgb)


# --- BUTTON ---
build = st.sidebar.button("🚀 Build Planet")

# --- VISUALIZATION ---
if build:
    st.subheader("Your Planet Visualization 🌌")

    # Planet sphere
    phi, theta = np.mgrid[0:np.pi:100j, 0:2*np.pi:100j]
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)

    # Create a color gradient (like stripes)
    stripe_pattern = np.sin(8 * phi)  # 8 stripes across latitude
    dark_color = darken_color(color, 0.3)
    colorscale = [[0, dark_color], [1, color]] # gradient effect using user color

    planet_surface = go.Surface(
        x=x,
        y=y,
        z=z,
        surfacecolor=stripe_pattern,
        colorscale=colorscale,
        cmin=-1, cmax=1,
        showscale=False,
        opacity=1,
    )

    fig = go.Figure(data=[planet_surface])

    # Add rings if user selected
    if has_rings:
        ring_r_inner = 1.3
        ring_r_outer = 2.2
        ring_theta = np.linspace(0, 2 * np.pi, 200)
        ring_r = np.linspace(ring_r_inner, ring_r_outer, 20)
        ring_r, ring_theta = np.meshgrid(ring_r, ring_theta)

        ring_x = ring_r * np.cos(ring_theta)
        ring_y = ring_r * np.sin(ring_theta)
        ring_z = np.zeros_like(ring_x)  # same plane as equator

        ring_surface = go.Surface(
            x=ring_x,
            y=ring_y,
            z=ring_z,
            colorscale=[[0, 'rgba(200,200,200,0.4)'], [1, 'rgba(255,255,255,0.1)']],
            showscale=False,
            opacity=0.7,
        )
        fig.add_trace(ring_surface)

    fig.update_layout(
        template="plotly_dark",
        margin=dict(l=0, r=0, t=0, b=0),
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode="data",
            bgcolor="black"
        )
    )
        # Moons
    for i in range(num_moons):
        moon_r = radius * 0.3
        angle = i * (2 * np.pi / max(num_moons, 1))
        moon_x = (radius * 2.5) * np.cos(angle)
        moon_y = (radius * 2.5) * np.sin(angle)
        moon_z = 0

        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        xm = moon_r * np.cos(u) * np.sin(v) + moon_x
        ym = moon_r * np.sin(u) * np.sin(v) + moon_y
        zm = moon_r * np.cos(v) + moon_z

        fig.add_trace(go.Surface(x=xm, y=ym, z=zm, colorscale='Greys', showscale=False))

    # Orbit
    if show_orbit:
        orbit_t = np.linspace(0, 2*np.pi, 200)
        orbit_x = (radius * 2.5) * np.cos(orbit_t)
        orbit_y = (radius * 2.5) * np.sin(orbit_t)
        orbit_z = np.zeros(orbit_t.shape)
        fig.add_trace(go.Scatter3d(x=orbit_x, y=orbit_y, z=orbit_z, mode='lines', line=dict(color='white', width=1)))

    st.plotly_chart(fig, use_container_width=True)
    
    

    # Optional AI description
    if ai_description:
        st.markdown("### 🧠 AI Planet Description")
        desc = generate_planet_description(planet_name, radius, color, num_moons, has_rings)
        st.info(desc)
