import streamlit as st

st.ttlie("Bağlantı Güvenliği Kontrol Aracı")

st.html(
    '<p>Naber Cınım<p>'
)

url = st.text_input(" ")

if url.startswith("https"):
    st.text("Bağlantınız Güvenli:Bilgileriniz (örneğin şifreler veya kredi kartı numaraları) bu siteye gönderilirken gizli olur.")
elif url.startswith("http"):
    st.text("Bağlantınız Güvenli Değil:Bilgileriniz (örneğin şifreler veya kredi kartı numaraları gibi) bu siteye gönderilirken gizlenmez")
else:
    st.text ("Lütfen URL'yi kırpmadan giriniz!")
