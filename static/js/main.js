/**
 * Created by Dima on 24/11/2015.
 */

var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var radius = 10;
canvas.width = window.innerWidth/2;
canvas.height = window.innerHeight/2;

var putPoint = function(e)
{
    context.beginPath();
    context.arc(e.offsetX, e.offsetY, radius, 0, Math.PI*2 );
    context.fill();
}
canvas.addEventListener('mousedown', putPoint);
