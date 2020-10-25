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
var firestore = firebase.firestore();

var user = "Shreyas";
var docRef = firestore.collection("Users").doc(user);
var userID;
window.onload = function fetch() {
    docRef.get().then(function (doc) {
        if (doc && doc.exists) {
            const myData = doc.data();
            document.getElementById("titleName").innerHTML = myData.FirstName;
            userID = myData.UserNumber;
        }
        else {
            console.log("error");
        }
    })
}

var data2;
function load() {
    docRef = firestore.collection("EyeMovement").doc(String(userID));
    docRef.onSnapshot(function (doc) {
        const myData = doc.data();
        data2 = myData.FocusedTime;
        console.log(data2)
        update();
    })

    function update(){
    var ctx = document.getElementById('myChart').getContext('2d');
    var keys = [];
    var values = [];
    for (i = 0; i < data2.length; i++) {
        keys.push(i);
        values.push(data2[i]);

    }
    var arr = [0, 1, 2]
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',
        // The data for our dataset
        data: {
            labels: keys,
            datasets: [{
                label: 'Posture',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: values,
            }]
        },
        // Configuration options go here
        options: {}
    });
}
}


