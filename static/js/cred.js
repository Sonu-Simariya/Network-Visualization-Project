function openForm() {
    document.getElementById("myForm").style.display = "block";

}
function closeForm() {
    document.getElementById("myForm").style.display = "none";
}
// Function to display the specified popup and hide others
function showPopup(id) {
    var popups = document.querySelectorAll('.popup');
    popups.forEach(function(popup) {
        if (popup.id === id) {
            popup.style.display = "block";
        } else {
            popup.style.display = "none";
        }
    });
}

// Function to hide the specified popup
function hidePopup(id) {
    var popup = document.getElementById(id);
    popup.style.display = "none";
}
function togleFullscreen() {
    var doc = window.document;
    var docEl = doc.documentElement;

    var requestFullScreen = docEl.requestFullscreen || docEl.mozRequestFullScreen || docEl.webkitRequestFullScreen || docEl.msRequestFullscreen;
    var cancelFullScreen = doc.exitFullscreen || doc.mozCancelFullScreen || doc.webkitExitFullscreen || doc.msExitFullscreen;

    if (!doc.fullscreenElement && !doc.mozFullScreenElement && !doc.webkitFullscreenElement && !doc.msFullscreenElement) {
        requestFullScreen.call(docEl);
        document.body.style.backgroundColor = '#fff';
        document.getElementById("btt").innerHTML="Exit Screen"
        
         // Set background color to white
    } else {
        cancelFullScreen.call(doc);
        document.body.style.backgroundColor = '';
        

    
        document.getElementById("btt").innerHTML="Full Screen"  // Reset background color to default
    }
}
