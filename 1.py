import streamlit as st

st.title("Streamlit App with PWA Support")

# Add manifest and register service worker
st.markdown(
    """
    <link rel="manifest" href="https://your-hosting-url/manifest.json">
    <script>
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('https://your-hosting-url/service-worker.js')
        .then(function(registration) {
          console.log('Service Worker registered with scope:', registration.scope);
        })
        .catch(function(error) {
          console.log('Service Worker registration failed:', error);
        });
      }
    </script>
    """,
    unsafe_allow_html=True,
)
