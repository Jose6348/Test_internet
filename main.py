import streamlit as st
import speedtest

st.set_page_config(page_title="Teste de Velocidade de Internet", page_icon="📶", layout="centered")

def main():
    st.markdown(
        """
        <style>
        .title {
            font-size: 2.5em;
            font-weight: bold;
            color: #4A90E2;
            text-align: center;
            margin-bottom: 20px;
        }
        .subtitle {
            font-size: 1.2em;
            color: #7F8C8D;
            text-align: center;
            margin-bottom: 30px;
        }
        .metric {
            font-size: 1.5em;
            font-weight: bold;
            color: #2C3E50;
            margin-top: 10px;
        }
        .footer {
            font-size: 0.9em;
            color: #95A5A6;
            text-align: center;
            margin-top: 40px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="title">🚀 Teste de Velocidade de Internet</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Verifique a velocidade da sua conexão de forma rápida e fácil!</div>', unsafe_allow_html=True)

    if st.button("🔍 Iniciar Teste"):
        with st.spinner("🕒 Analisando a sua conexão..."):
            s = speedtest.Speedtest()
            s.get_best_server()
            download_speed = s.download() / 1_000_000  
            upload_speed = s.upload() / 1_000_000  
            results = s.results.dict()

            st.markdown("""
                <div style="display: flex; justify-content: space-around; margin-top: 20px;">
                    <div style="background-color: #EAF2F8; padding: 20px; border-radius: 10px; width: 30%; text-align: center;">
                        <h3 style="color: #2980B9;">🔻 Download</h3>
                        <p class="metric">{:.2f} Mbps</p>
                    </div>
                    <div style="background-color: #EAF2F8; padding: 20px; border-radius: 10px; width: 30%; text-align: center;">
                        <h3 style="color: #27AE60;">🔺 Upload</h3>
                        <p class="metric">{:.2f} Mbps</p>
                    </div>
                    <div style="background-color: #EAF2F8; padding: 20px; border-radius: 10px; width: 30%; text-align: center;">
                        <h3 style="color: #F39C12;">📶 Ping</h3>
                        <p class="metric">{:.0f} ms</p>
                    </div>
                </div>
            """.format(download_speed, upload_speed, results['ping']), unsafe_allow_html=True)

            st.write("### Progresso da Conexão")
            st.progress(min(download_speed / 200, 1.0))
            st.markdown(f"<div style='color: #3498DB; font-weight: bold;'>🔻 Download: {download_speed:.2f} Mbps</div>", unsafe_allow_html=True)

            st.progress(min(upload_speed / 200, 1.0))
            st.markdown(f"<div style='color: #27AE60; font-weight: bold;'>🔺 Upload: {upload_speed:.2f} Mbps</div>", unsafe_allow_html=True)

            st.success("✅ Teste de velocidade concluído com sucesso!")

    st.markdown('<div class="footer">Desenvolvido com ❤️ usando Streamlit</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
