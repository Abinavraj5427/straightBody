
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
// window.onload = function fetch() {
//     docRef.get().then(function (doc) {
//         if (doc && doc.exists) {
//             // console.log("test");
//             const myData = doc.data();
//             //document.getElementById("titleName").innerHTML = myData.FirstName;
//             userID = myData.UserNumber;
//         }
//         else {
//             console.log("error");
//         }
//     })

// }

window.onload = function load() {
    var keys = [];
    var values = [];

    const events = firebase.firestore().collection('Postures')
    events.onSnapshot((querySnapshot) => {
        const tempDoc = []
        querySnapshot.forEach((doc) => {
            keys.push(doc.data().time);
            values.push(doc.data().area);
            tempDoc.push({ id: doc.id, ...doc.data() })
        })
        console.log(tempDoc)
        update();
    })

    function update() {
        var ctx = document.getElementById('myChart').getContext('2d');
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

    const events2 = firebase.firestore().collection('EyeMovement')
    events2.onSnapshot((querySnapshot) => {
        const tempDoc = []
        querySnapshot.forEach((doc) => {
            keys.push(doc.data().time);
            if (doc.data().onScreen == false){
                values.push(0);
            }
            else{
                values.push(1);
            }
            tempDoc.push({ id: doc.id, ...doc.data() })
        })
        console.log(tempDoc)
        update2();
    })

    function update2() {
        var ctx = document.getElementById('otherChart').getContext('2d');
        var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'line',
            // The data for our dataset
            data: {
                labels: keys,
                datasets: [{
                    label: 'Eye Movement',
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


