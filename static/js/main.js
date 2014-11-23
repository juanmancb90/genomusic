var Walker = function() {  
    this.x = window.innerWidth / 2
    this.y = window.innerHeight / 2
    this.radius = 1
    this.frameRate = 1000/30
    this.canvas = document.getElementById('canvas')
    this.context = this.canvas.getContext('2d')
    this.canvas.width = window.innerWidth
    this.canvas.height = window.innerHeight
}

Walker.prototype.setup = function() {
    this.context.beginPath()
    this.context.arc(this.x, this.y, this.radius, 0, 2 * Math.PI, false)
    this.context.fillStyle = 'black'
    this.context.fill()
}

Walker.prototype.walk = function() {
    r = Math.random()
    if (r < 0.1) {
        this.x++
    } else if (r < 0.2) {
        this.x--
    } else if (r < 0.4) {
        this.y++
    } else {
        this.y--
    }
}

Walker.prototype.animate = function() {
    this.walk()
    this.setup()
}

var run = function(){
    w = new Walker()
    setInterval(function(){w.animate()}, w.frameRate)
}
run()