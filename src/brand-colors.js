for (var i = 0; i < colores.length; i++) {
  var div = document.createElement("canvas");
  document.getElementById("colores").appendChild(div);

  var id = "canvas-" + [i + 1];
  div.setAttribute("id", id);

  var canvas = document.getElementById(id);
  var ctx = canvas.getContext("2d");

  ctx.fillStyle = colores[i];
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  console.log("Canvas: " + (i + 1) + " -  color: " + colores[i]);
}
