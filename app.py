import streamlit as st
import pandas as pd

from PIL import Image

df=pd.read_csv("tested.csv")
df2=df.sample(n=8, random_state=1)
def main():
        nombre=st.text_input("Introduce tu nombre:")
        st.write(nombre)

        #área de texto
        mensaje=st.text_area("Introduce tu mensaje:", height=100)
        st.write(mensaje)
        st.title("Curso de Streamlit")
        st.header("Encabezado")
        nombre="Manoli"
        st.text(f"Hola {nombre}, soy yo")
        st.markdown("### Esto es Markdown")
        st.success("Exito")
        st.warning("Esto es una advertencia")
        st.info("Esto es información")
        st.error("Esto es un error")
        st.write("Texto normal")
        st.write("## Esto es un texto markdown")
        st.write(1+2)

        st.image("https://picsum.photos/800")
        st.header("Dataframe:")
        st.dataframe(df)
        #st.dataframe(df2.style.highlight_max(axis=0)) # que muestre de forma destacada el máximo
        # Mostrar un json
        st.json({"clave": "valor"})

        #Caja de selección: Selectbox
        opcion=st.selectbox(
                'Elige tu fruta favorita',
                ['Manzana','Naranja','Platano','Fresa']
        )
        st.write(f'Tu fruta favorita es: {opcion}')

        #Multiselección: multiselect
        opciones=st.multiselect(
                'Elige tus colores favoritos',
                ['Rojo','Naranja','Verde','Amarillo']
        )
        st.write(f'Tus colores favoritos son: {opciones}')

        #slider (para números)
        edad=st.slider(
                'Selecciona tu edad',
                min_value=0,
                max_value=100,
                value=25, # valor inicial
                step=1
        )
        st.write('tu edad es:',edad)

        #Select slider (para categorias)
        nivel=st.select_slider(
                'Selecciona tu nivel de satisfacción',
                options=['Muy bajo','Bajo','Medio','Alto','Muy Alto'],
                value='Medio'
        )
        st.write('Tu nivel de satisfacción es:', nivel)

        numero = st.number_input("Introduce un número",1,25, step=1)
        st.write(numero)

        cita=st.date_input("Selecciona una fecha")
        st.write(cita)

        hora=st.time_input("Selecciona una hora")
        st.write(hora)

        # Seleccionar un color
        color=st.color_picker("Selecciona un color")
        st.write(color)




if __name__ == '__main__':
        main()
