import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Personal Finance Tracker",
    page_icon="💰",
    layout="wide"
)

# Judul aplikasi
st.title("💰 Personal Finance Tracker")
st.write("Aplikasi sederhana untuk mengelola keuangan pribadi.")

st.divider()

# Dashboard ringkasan
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Pemasukan", "Rp 5.000.000")

with col2:
    st.metric("Total Pengeluaran", "Rp 2.000.000")

with col3:
    st.metric("Saldo Saat Ini", "Rp 3.000.000")

st.divider()

st.subheader("📝 Tambah Transaksi")

nama = st.text_input("Nama Transaksi")
jumlah = st.number_input(
    "Jumlah (Rp)",
    min_value=0,
    step=1000
)

jenis = st.selectbox(
    "Jenis Transaksi",
    ["Pemasukan", "Pengeluaran"]
)

if st.button("Simpan Transaksi"):
    if nama and jumlah > 0:
        st.success(f"Transaksi '{nama}' berhasil dicatat!")
    else:
        st.warning("Mohon isi nama dan jumlah transaksi.")