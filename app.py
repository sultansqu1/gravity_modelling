import streamlit as st
from plotly import graph_objects as go 
import numpy as np

st.set_page_config(
    page_title="Gravity modeling",
    page_icon="*",
    layout="wide",
    initial_sidebar_state="expanded",
)

hide_streamlit_style= """
  <style>
  # mainmenu {visibility:hidden;}
  footer {visibility: hidden;}
  footer after {
  content:'created by Sultan';
  display: block;
  position: relative;
  # background-color: red;
  padding: 5px;
  top: 2px
  </style>
  """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
plotly_config = {
  'displaylogo': False,

}
with st.sidebar:
    st.title("Body 1")
    depth = st.slider("Depth", 2, 100, 50, key="Depth")
    distance = st.slider("distance", -300, 300, -100, key="distance")
    deltap = st.slider("Deltan P", -20.0, 20.0, 4.0, key="deltap")
    radius = st.slider("Radius", 1, 30, 10, key="radius")

    st.title("Body 2")
    depth2 = st.slider("Depth", 2, 100, 50, key="Depth2")
    distance2 = st.slider("distance", -300, 300, -100, key="distance2")
    deltap2 = st.slider("Deltan P", -20.0, 20.0, 4.0, key="deltap2")
    radius2 = st.slider("Radius", 1, 30, 10, key="radius2")

st.title("Gravity Modeling")
fig = go.Figure()
#Body 1
fig.add_shape(
   type ="circle",
   xref="x",
   yref="y",
   x0=distance - radius,
   y0=depth - radius, 
   x1=distance + radius, 
   y1 = depth + radius,
   line_color= "lightSeaGreen",
   fillcolor="PaleTurquoise",
   name="Body 1")

#Body 2
fig.add_shape(
   type = "circle",
   xref="x",
   yref="y",
   x0=distance2 - radius2,
   y0=depth2 - radius2, 
   x1=distance2 + radius2, 
   y1=depth2 + radius2,
   line_color= "lightSeaGreen",
   fillcolor="Grean",
   name="Body 2"
)  

fig.add_annotation(
   x=distance,
   y=depth,
   text="Sphere 1",
   showarrow=True,
   arrowhead=1,
   ax=40+radius,
   ay=-radius-40,
)
fig.add_annotation(
   x=distance2,
   y=depth2,
   text="Sphere 1",
   showarrow=True,
   arrowhead=1,
   ax=40+radius2,
   ay=-radius2-40,
)

fig.update_layout(
    title="Body 1and Body 2",
    xaxis_title ="Distance",
    yaxis_title ="Depth",
    font=dict(
        family="courier New, monospace",
        size=18,
        color='#7f7f7f'
    
    )
)

   

fig.update_xaes(range=[-300, 300])
fig.update_yaxes(range=[130, -30])

fig.update_yaxes(scaleanchor="x", scaleratio=1)

fig.update_layout(
    legend_title_text='Bodies',

)
st.plotly_chart(fig, config=plotly_config, use_container_width=True)

fig2=go.figure()
x= np.linspace(-300, 300, 2000)
deltag1=[0.0000000000667 * (4/3 * np.pi *radius**3 *
                            deltap * depth)/ ((x_i-distance) **2 + depth ** 2) ** (3/2) ]
deltag2=[0.0000000000667 * (4/3 * np.pi *radius2**3 *
                            deltap2 * depth2)/ ((x_i-distance2) **2 + depth2 ** 2) ** (3/2) ]
deltag=[deltag1_i + deltag2_i for deltag1_i, deltag2_i in zip(deltag1, deltag2)]

fig2.add_trace(go.scatter(x=x, y=deltag, mode='lines', name='Gravity response'))

fig2.update_layout(
    title='Gravity response of body 1 and body 2',
    xaxis_title="Distance",
    yaxis_title="Delta g",
    font=dict(
    family="Courier New, monospace",
    size=18,
    color="#7f7f7f"
    )

)

fig2.update_xaxes(range=[-300, 300])
st.plotly_chart(fig2, config=plotly_config, use_container_width=True)
