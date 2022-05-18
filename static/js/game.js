
let color = (51, 51, 51, 255);
function setup() {
    createCanvas(400, 400);
  }
  
  function draw() {
    background(color);
    ellipse(mouseX, mouseY, 50, 50);
    
  }


function mouseClicked() {
    console.log("mouseClicked");
}
