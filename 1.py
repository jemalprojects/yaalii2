import streamlit as st

st.title("Yaalii2 App with PWA Support")

# Include the manifest and service worker
st.markdown(
    """
    <link rel="manifest" href="/manifest.json">
    <script>
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/service-worker.js')
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
