# -*- coding: utf-8 -*-
"""
show the pre-made mp4s in a simple streamlit app
"""

import streamlit as st

video_links = {
    2017: 'https://github.com/user-attachments/assets/a6ac2564-d2ab-4b8f-867e-52ce1e93fc53',
    2018: 'https://github.com/user-attachments/assets/49a3a011-f1fe-4c40-b1c6-c00703f95b31',
    2019: 'https://github.com/user-attachments/assets/5b7237d6-93ab-495c-aaab-de264388b231',
    2020: 'https://github.com/user-attachments/assets/46d96a19-f7b0-4c7d-93ea-8b09c8b2830f',
    2021: 'https://github.com/user-attachments/assets/0e548c67-43a6-4c99-bbe6-582dfd3d4331',
    2022: 'https://github.com/user-attachments/assets/734ba483-0b94-4981-a575-42e08cf2af4f',
    2023: 'https://github.com/user-attachments/assets/6305acd2-9f2f-46b4-8fdb-7457cc68f02c',
    2024: 'https://github.com/user-attachments/assets/52c265c7-fa57-40c0-bd12-3c55231220d7',
    2025: 'https://github.com/user-attachments/assets/6c9ebbab-7446-4b66-8ea3-3b0fdde3b0b2',
}

st.title("Ruska weather replay")
year = st.selectbox("Select edition:", list(range(2017, 2026)))
st.video(video_links[year])
    
st.markdown("""
    <p style='font-size:12px; color:gray;'>Weather reanalysis source: Copernicus Climate Change Service (C3S), Climate Data Store, (2023): ERA5 hourly data on single levels from 1940 to present. DOI: 10.24381/cds.adbb2d47</p>
    <p style='font-size:12px; color:gray;'>Basemap: Natural Earth (naturalearthdata.com)</p>
    """,
    unsafe_allow_html=True
)


