import streamlit as st
import requests

st.set_page_config(page_title='Credit Scoring App', layout='centered')

st.title('CREDIT RISK SCORRING')

with st.form('credit_form'):
    st.header('Data Diri Nasabah')

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox('Jenis Kelamin', ['M', 'F'])
        children = st.number_input('Jumlah Anak', min_value=0, step=1, value=0)
        education = st.selectbox(
            'Pendidikan Terakhir',
            [
                'Secondary / secondary special',
                'Higher education',
                'Incomplete higher',
                'Lower secondary',
                'Academic degree'
            ]
        )

    with col2:
        income_type = st.selectbox(
            'Tipe Pekerjaan',
            [
                'Working',
                'State servant',
                'Commercial associate',
                'Pensioner',
                'Unemployed',
                'Student',
                'Businessman'
            ]
        )
        region_rating = st.slider('Rating Wilayah(1=Kota Besar, 3=Pelosok)', 1, 3, 2)

    
    st.header('Data Finansial Nasabah')

    col3, col4 = st.columns(2)

    with col3:
        income = st.number_input('Pendapatan Tahunan (Rupiah)', min_value=0.0, value=100000000.0, step=1000000.0)
        annuity = st.number_input('Angsuran Kredit (Rupiah)', min_value=0.0, value=500000.0, step=100000.0)

    with col4:
        credit_amount = st.number_input('Jumlah Kredit (Rupiah)', min_value=0.0, value=2000000.0, step=100000.0)
        goods_price = st.number_input('Harga Barang (Jika Kredit Barang)', min_value=0.0, value=2500000.0, step=100000.0)

    st.header('Aset dan Skor Eksternal')

    col5, col6 = st.columns(2)

    with col5:
        own_car = st.selectbox('Punya Mobil?', ['Y', 'N'])
        own_realty = st.selectbox('Punya Rumah?',['Y', 'N'])

    with col6:
        ext_source_2 = st.slider('Skor Kredit Eksternal (Simulasi SLIK)', 0.0, 1.0, 0.5)

    submitted = st.form_submit_button('Prediksi Risiko Kredit')

if submitted:
    payload = {
        'CODE_GENDER': gender,
        'ONT_CHILDREN': int(children),
        'EXT_SOURCE_2': ext_source_2,
        'AMT_INCOME_TOTAL': float(income),
        'AMT_CREDIT': float(credit_amount),
        'AMT_ANNUITY': float(annuity),
        'FLAG_OWN_CAR': own_car,
        'FLAG_OWN_REALTY': own_realty,
        'AMT_GOODS_PRICE': float(goods_price),
        'NAME_INCOME_TYPE': income_type,
        'NAME_EDUCATION_TYPE': education,
        'REGION_RATING_CLIENT': int(region_rating),
    }

    try:
        api_url = 'http://127.0.0.1:8000/predict'
        
        with st.spinner('Sedang menghitung risiko . . .'):
            response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            result = response.json()

            st.divider()

            status = result['status']
            score = result['risk_score'] * 100

            if status == 'DISETUJUI':
                st.success(f'✅ **KEPUTUSAN: {status}**')
                st.balloons()
            else:
                st.error(f'❌ **KEPUTUSAN: {status}**')

            st.info(f'Skor Risiko Kredit: **{score:.2f}%**')

            st.progress(result['risk_score'], text='Level Risiko')

            if result['risk_score'] > 0.5:
                st.warning('Nasabah ini memiliki risiko tinggi. Disarankan untuk meminta jaminan tambahan atau menolak pengajuan.')
            else: st.write('Nasabah tergolong aman')

        else:
            st.error(f'gagal menghubungi API. Error: {response.text}')

    except Exception as e:
        st.error(f'Koneksi ERROR: {e}')