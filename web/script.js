
// document.body.addEventListener('touchmove', function(event) {
//     console.log(event.source);
//     //if (event.source == document.body)
//     event.preventDefault();
// }, false);

window.onresize = function() {
    $(document.body).width(window.innerWidth).height(window.innerHeight);
}

$(function() {
    window.onresize();

    document.body.addEventListener('touchstart', function(e){
        alert(e.changedTouches[0].pageX);
    }, false)


});

function start() {
  //document.getElementById('start_button').style.bottom = $(window).height() + 150 + 'px';
  document.getElementById('start_button').style.zIndex = '100';
  document.getElementById('start_button').style.transform = 'scale(20.0)';
  document.getElementById('start_button').style.filter = 'blur(10px)';

  setTimeout(function() {
    document.getElementById('start_button').style.opacity = '0';
    document.getElementById('camera').style.display = 'block';
    document.getElementById('ping_pong_ball').style.display = 'block';
  }, 1000);

  setTimeout(function() {
    document.getElementById('start_button').style.display = 'none';
  }, 1400);
}

function shoot() {
  document.getElementById('ping_pong_ball').style.bottom = $(window).height() + 150 + 'px';
  document.getElementById('ping_pong_ball').style.transform = 'scale(0.5)';
  document.getElementById('ping_pong_ball').style.marginLeft = '-50px';
  document.getElementById('ping_pong_ball').style.opacity = '0';

  setTimeout(function() {
    document.getElementById('ping_pong_ball').style.bottom = 50 + 'px';
    document.getElementById('ping_pong_ball').style.transform = 'scale(1.0)';
    document.getElementById('ping_pong_ball').style.marginLeft = '0px';
  }, 800);

  setTimeout(function() {
    document.getElementById('ping_pong_ball').style.opacity = '1';
  }, 1100);
}
