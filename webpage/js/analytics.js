
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

window.onload = function load() {
    var keys = [];
    var values = [];

    var count = 0;
    var events = firebase.firestore().collection('Postures')
    events = events.orderBy('time', 'desc').limit(10);
    events.get().then((querySnapshot) => {
        const tempDoc = []
        querySnapshot.forEach((doc) => {
            keys.push(++count);
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

    keys2 = []
    values2 = []

    var count2=0;
    var events2 = firebase.firestore().collection('EyeMovement')
    events2 = events2.orderBy('time', 'desc').limit(10);
    events2.get().then((querySnapshot) => {
        const tempDoc = []
        querySnapshot.forEach((doc) => {
            keys2.push(++count2);
            if (doc.data().onScreen == false) {
                values2.push(0);
            }
            else {
                values2.push(1);
            }
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
                labels: keys2,
                datasets: [{
                    label: 'Eye Movement',
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: values2,
                }]
            },
            // Configuration options go here
            options: {
                xAxes: [{
                    ticks: {
                        autoSkip: true,
                        maxTicksLimit: 5
                    }
                }]
            }
        });
    }

    contactCounter = []
    contact = []
    const events3 = firebase.firestore().collection('EyeMovement')
    events3.get().then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
            contactCounter.push(doc.data().contactCounter);
            contact.push(doc.data().counter);
        })
        update3();
    })

    function update3() {
        var thi = document.getElementById('concpi').getContext('2d');
        var concpi = new Chart(thi, {
            // The type of chart we want to create
            type: 'doughnut',

            // The data for our dataset
            data: {
                labels: ["Total Concentration"],
                datasets: [{
                    data: [20, 10],
                    backgroundColor: ['rgb(131,142,211)', 'rgb(9, 8, 61)'],
                    borderColor: ['rgb(131, 142, 211)', 'rgb(9, 8, 61)']
                }]
            },

            // Configuration options go here
            options: {}
        });
    }

}


