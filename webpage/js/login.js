// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
var firebaseConfig = {
    apiKey: "AIzaSyBzkhAV5Of1Nc2MYaBe9PIYL_MmuSq5URw",
    authDomain: "straightbody-4dec9.firebaseapp.com",
    databaseURL: "https://straightbody-4dec9.firebaseio.com",
    projectId: "straightbody-4dec9",
    storageBucket: "straightbody-4dec9.appspot.com",
    messagingSenderId: "922824382292",
    appId: "1:922824382292:web:69586bb5eac68bf0c51ac1",
    measurementId: "G-C7RY3SJSX3"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const auth = firebase.auth();

function signUp(){
    var email = document.getElementById("username");
    var password = document.getElementById("password");

    const promise = auth.createUserWithEmailAndPassword(email.value, password.value);
    if (promise.catch(e=> alert(e.message)));
    else{
        alert("Signed Up");
    }

    
}
var email
function signIn(){
    email = document.getElementById("username");
    var password = document.getElementById("password");

    const promise = auth.signInWithEmailAndPassword(email.value, password.value);
    if(promise.catch(e=> alert(e.message)));
    else{
        alert("Signed In" + email.value);
    }

    
}

function signOut(){
    auth.signOut();
    alert("Signed out");
}

auth.onAuthStateChanged(function(user){
    if(user){
        window.open("webpage\dash.html");
        // export {email as email}
    }
    else{
        //not logged in
    }
});