import streamlit as st
import pandas as pd
import altair as alt

# Load data
df = pd.read_csv("SwizzleSip.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Influencer'] = df['Influencer_Brand'].str.extract(r'(@[\w\.]+)')

# Sidebar
st.sidebar.title("🔑 AI Assistant Setup")
st.sidebar.text_input("Google AI API Key:", type="password")
st.sidebar.markdown("[📎 Dapatkan API Key di sini](https://example.com)")

st.sidebar.markdown("### 🎛️ Filter Data")

# Filter platform
platforms = df['Platform'].unique()
selected_platforms = st.sidebar.multiselect("Platform:", platforms, default=list(platforms))

# Filter influencer
influencers = df['Influencer'].dropna().unique()
selected_influencers = st.sidebar.multiselect("Influencer:", influencers, default=list(influencers))

# Filter tanggal
min_date = df['Date'].min()
max_date = df['Date'].max()
selected_date = st.sidebar.date_input("Rentang Tanggal:", [min_date, max_date])

# Apply filter
filtered_df = df[
    (df['Platform'].isin(selected_platforms)) &
    (df['Influencer'].isin(selected_influencers)) &
    (df['Date'] >= pd.to_datetime(selected_date[0])) &
    (df['Date'] <= pd.to_datetime(selected_date[1]))
]

# Header
st.title("📊 SwizzleSip AI-Powered Media Intelligence")
st.markdown("Dashboard ini menganalisis performa media sosial brand **SwizzleSip**. Gunakan filter di sidebar untuk menjelajahi data.")

# KPIs
st.markdown("## Ringkasan Performa (KPIs)")
col1, col2, col3 = st.columns(3)
col1.metric("Total Posts", filtered_df.shape[0])
col2.metric("Total Engagements", f"{filtered_df['Engagements'].sum():,}")
col3.metric("Avg. Engagement / Post", f"{filtered_df['Engagements'].mean():,.0f}")

st.markdown("---")

# Total Engagement per Platform
st.markdown("### Visualisasi Data Interaktif")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Total Engagement per Platform")
    platform_data = filtered_df.groupby('Platform')['Engagements'].sum().reset_index()
    bar = alt.Chart(platform_data).mark_bar(color="#80b1d3").encode(
        x=alt.X('Engagements:Q', title='Total Engagements'),
        y=alt.Y('Platform:N', sort='-x'),
        tooltip=['Platform', 'Engagements']
    )
    st.altair_chart(bar, use_container_width=True)

with col2:
    st.markdown("#### Distribusi Sentimen Postingan")
    sentiment_data = filtered_df['Sentiment'].value_counts().reset_index()
    sentiment_data.columns = ['Sentiment', 'Count']
    pie = alt.Chart(sentiment_data).mark_arc(innerRadius=50).encode(
        theta=alt.Theta("Count:Q"),
        color=alt.Color("Sentiment:N", scale=alt.Scale(scheme="tableau20")),
        tooltip=["Sentiment", "Count"]
    )
    st.altair_chart(pie, use_container_width=True)

# Top 10 Influencer
st.markdown("#### Top 10 Influencer by Engagement")
top_inf = filtered_df.groupby('Influencer')['Engagements'].sum().nlargest(10).reset_index()
inf_chart = alt.Chart(top_inf).mark_bar(color="#b3de69").encode(
    x=alt.X("Engagements:Q", title="Total Engagements"),
    y=alt.Y("Influencer:N", sort='-x'),
    tooltip=["Influencer", "Engagements"]
)
st.altair_chart(inf_chart, use_container_width=True)

st.markdown("---")

# AI Assistant (Dummy)
st.markdown("### 🤖 AI Analyst Assistant")
st.caption("Dapatkan ringkasan analisis otomatis dari data yang telah Anda filter di atas.")
if st.button("Generate Insight"):
    st.info("📌 Fitur analisis AI akan aktif saat API Key dimasukkan. Coming soon!")
