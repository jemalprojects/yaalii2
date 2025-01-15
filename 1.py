import streamlit as st

st.title("Streamlit App with PWA Support")

# Add manifest and register service worker
st.markdown(
    """
    <link rel="manifest" href="https://yaalii2.streamlit.app/manifest.json">
    <script>
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('https://yaalii2.streamlit.app/service-worker.js')
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
st.markdown(
    """
    <script>
      if (/Mobi|Android|iPhone|iPad/i.test(navigator.userAgent)) {
        // Listen for the install prompt
        window.addEventListener('beforeinstallprompt', (e) => {
          e.preventDefault(); // Prevent the default browser prompt
          const installPromptEvent = e;

          // Show a custom message
          if (confirm("Do you want to install this app for a better experience?")) {
            installPromptEvent.prompt(); // Show the install prompt
            installPromptEvent.userChoice.then((choiceResult) => {
              if (choiceResult.outcome === 'accepted') {
                console.log('User accepted the install prompt');
              } else {
                console.log('User dismissed the install prompt');
              }
            });
          }
        });
      }
    </script>
    """,
    unsafe_allow_html=True,
)
