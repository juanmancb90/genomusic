var Walker = function() {  
    this.x = Math.floor(Math.random() * (window.innerWidth - 100 - window.innerWidth - 100 + 1)) + window.innerWidth - 100;
    this.y = window.innerHeight - 100
    this.radius = 5
    this.frameRate = 1000/30
    this.canvas = document.getElementById('canvas')
    this.context = this.canvas.getContext('2d')
    this.canvas.width = window.innerWidth - 100
    this.canvas.height = window.innerHeight - 100
}

Walker.prototype.setup = function() {
    this.context.clearRect(0, 0, canvas.width, canvas.height);
    this.context.beginPath()
    this.context.arc(this.x, this.y, this.radius, 0, 2 * Math.PI, false)
    this.context.fillStyle = 'white'
    this.context.fill()
}

Walker.prototype.walk = function() {
    r = Math.random()
    this.y--
}

Walker.prototype.animate = function() {
    setInterval(function(){this.walk(); this.setup();}, this.frameRate)
}

var run = function(){
    walker = new Walker()
    walker.animate()
}
