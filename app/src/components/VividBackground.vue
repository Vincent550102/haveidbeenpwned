<template>
    <div id="box">
        <canvas ref="canvas"></canvas>
    </div>
</template>

<script>
export default {
    data() {
        return {
            cw: 0,
            ch: 0,
            maxCharCount: 10,
            fallingCharArr: [],
            fontSize: 16,
            maxColums: 0,
            charArr: ['0', '1', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ctx: null
        };
    },
    methods: {
        randomInt(min, max) {
            return Math.floor(Math.random() * (max - min) + min);
        },
        randomFloat(min, max) {
            return Math.random() * (max - min) + min;
        },
        draw(point) {
            point.value = this.charArr[this.randomInt(0, this.charArr.length)].toUpperCase();
            if (point.y < 0) point.speed = this.randomFloat(2, 8);

            this.ctx.fillStyle = "#0F0";
            this.ctx.font = this.fontSize + "px san-serif";
            this.ctx.fillText(point.value, point.x, point.y);

            point.y += point.speed;
            if (point.y > this.ch) {
                point.y = this.randomFloat(-100, 0);
                point.speed = this.randomFloat(2, 8);
            }
        },
        update() {
            this.ctx.fillStyle = "rgba(0,0,0,0.05)";
            this.ctx.fillRect(0, 0, this.cw, this.ch);

            var i = this.fallingCharArr.length;
            while (i--) {
                this.draw(this.fallingCharArr[i]);
            }
            requestAnimationFrame(this.update);
        }
    },
    mounted() {
        this.cw = this.$el.clientWidth;
        this.ch = this.$el.clientHeight;
        this.maxColums = this.cw / this.fontSize;

        var canvas = this.$refs.canvas;
        this.ctx = canvas.getContext('2d');

        canvas.width = this.cw;
        canvas.height = this.ch;

        for (var i = 0; i < this.maxColums; i++) {
            this.fallingCharArr.push({ x: i * this.fontSize, y: this.randomFloat(-500, 0) });
        }

        window.addEventListener('resize', () => {
            this.cw = this.$el.clientWidth;
            this.ch = this.$el.clientHeight;
            this.maxColums = this.cw / (this.fontSize);
            canvas.width = this.cw;
            canvas.height = this.ch;
        });

        this.update();
    }
}
</script>

<style scoped>
#box {
    position: relative;
    width: 100vw;
    height: 100vh;
}

canvas {
    position: absolute;
    width: 100%;
    height: 100%;
}
</style>
