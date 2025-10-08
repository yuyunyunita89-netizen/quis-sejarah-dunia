import streamlit as st
import random

# Set judul halaman
st.set_page_config(page_title="Kuis Sejarah", layout="centered")
st.title("📜 Kuis Sejarah Dunia")

# Daftar soal
soal = [
    {"soal": "Siapa yang memimpin pasukan Mongol?", 
     "option": ["Genghis Khan", "Alexander Agung", "Napoleon Bonaparte", "Julius Caesar"], 
     "jawaban": 0},
    
    {"soal": "Perang Dunia II terjadi pada tahun?", 
     "option": ["1939-1945", "1914-1918", "1945-1950", "1950-1955"], 
     "jawaban": 0},
    
    {"soal": "Siapa yang menemukan Amerika?", 
     "option": ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "Amerigo Vespucci"], 
     "jawaban": 0},
]

# Acak urutan soal hanya sekali saat sesi dimulai
if "soal_diacak" not in st.session_state:
    st.session_state.soal_diacak = random.sample(soal, len(soal))
    st.session_state.skor = 0
    st.session_state.soal_ke = 0
    st.session_state.selesai = False

# Fungsi untuk reset kuis
def reset_kuis():
    st.session_state.soal_diacak = random.sample(soal, len(soal))
    st.session_state.skor = 0
    st.session_state.soal_ke = 0
    st.session_state.selesai = False

# Tampilkan kuis jika belum selesai
if not st.session_state.selesai:
    s = st.session_state.soal_diacak[st.session_state.soal_ke]
    st.subheader(f"Soal {st.session_state.soal_ke + 1} dari {len(soal)}")
    st.write(s["soal"])
    jawaban_user = st.radio("Pilih jawaban kamu:", s["option"], key=st.session_state.soal_ke)

    if st.button("Submit Jawaban"):
        if s["option"].index(jawaban_user) == s["jawaban"]:
            st.success("✅ Jawaban benar!")
            st.session_state.skor += 1
        else:
            st.error(f"❌ Jawaban salah. Jawaban yang benar adalah **{s['option'][s['jawaban']]}**")
        
        st.session_state.soal_ke += 1

        if st.session_state.soal_ke >= len(soal):
            st.session_state.selesai = True

        st.experimental_rerun()

else:
    st.success(f"🎉 Kuis selesai! Skor akhir kamu: **{st.session_state.skor} / {len(soal)}**")
    if st.button("Ulangi Kuis"):
        reset_kuis()
        st.experimental_rerun()
