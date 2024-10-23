import streamlit as st

st.set_page_config(page_title="Benim Başlığım", page_icon="🧮")

st.title("Bağlantı Güvenliği Kontrol Aracı")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

url = st.text_input(" ")

if url.startswith("https"):
    st.text("Bağlantınız Güvenli:Bilgileriniz (örneğin şifreler veya kredi kartı numaraları) bu siteye gönderilirken gizli olur.")
elif url.startswith("http"):
    st.text("Bağlantınız Güvenli Değil:Bilgileriniz (örneğin şifreler veya kredi kartı numaraları gibi) bu siteye gönderilirken gizlenmez")
else:
    st.text ("Lütfen URL'yi kırpmadan giriniz!")
