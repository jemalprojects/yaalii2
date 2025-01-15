import streamlit as st
st.markdown(
    """
    <script>
      if (/Mobi|Android|iPhone|iPad/i.test(navigator.userAgent)) {
        window.addEventListener('beforeinstallprompt', (e) => {
          e.preventDefault(); // Prevent the default install prompt
          const installPromptEvent = e;

          // Show a custom installation message
          if (confirm("Install the Yaalii2 app for a better experience?")) {
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

st.title("Yaalii2 App with PWA Support")

# Include the manifest and service worker
st.markdown(
    """
    <link rel="manifest" href="manifest.json">
    <script>
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('service-worker.js')
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
