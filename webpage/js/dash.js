
// var varaible = document.getElementById("dude");
// varaible.innerHTML = "10";


eel.get_video()();

eel.expose(updateImageSrc);
function updateImageSrc(val) {
    let elem = document.getElementById('bg');
    elem.src = "data:image/jpeg;base64," + val
}

