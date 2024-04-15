<script type="module">
  // Import the functions you need from the SDKs you need
    import {initializeApp} from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
    import {getAnalytics} from "https://www.gstatic.com/firebasejs/10.11.0/firebase-analytics.js";
    // TODO: Add SDKs for Firebase products that you want to use
    // https://firebase.google.com/docs/web/setup#available-libraries

    // Your web app's Firebase configuration
    // For Firebase JS SDK v7.20.0 and later, measurementId is optional
    const firebaseConfig = {
        apiKey: "AIzaSyCu4F3cQUoT2o0oIBCKNTh10krTc3wfI_g",
    authDomain: "ev-stations-66c6f.firebaseapp.com",
    projectId: "ev-stations-66c6f",
    storageBucket: "ev-stations-66c6f.appspot.com",
    messagingSenderId: "592696695132",
    appId: "1:592696695132:web:e5cd5424cbf4d8d2584999",
    measurementId: "G-9W1HMHH0NC"
  };

    // Initialize Firebase
    const app = initializeApp(firebaseConfig);
    const analytics = getAnalytics(app);
</script>