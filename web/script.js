
document.body.addEventListener('touchmove', function(event) {
    console.log(event.source);
    //if (event.source == document.body)
    event.preventDefault();
}, false);

window.onresize = function() {
    $(document.body).width(window.innerWidth).height(window.innerHeight);
}

$(function() {
    window.onresize();
});


// $(function() {
//     var obj = document.getElementById('appView');
//     obj.addEventListener('touchmove', function(event) {
//     // If there's exactly one finger inside this element
//     if (event.targetTouches.length == 1) {
//         var touch = event.targetTouches[0];
//         // Place element where the finger is
//         obj.style.left = touch.pageX + 'px';
//         obj.style.top = touch.pageY + 'px';
//     }
//     }, false);
// });
