#version 300 es

// Объявляем входные и выходные переменные
in vec2 qt_TexCoord0;
out vec4 fragColor;

// Объявляем uniform-переменные
uniform sampler2D source;
uniform float radius;

void main() {
    vec2 uv = qt_TexCoord0;
    vec4 color = vec4(0.0);
    float total = 0.0;

    // Цикл для размытия
    for (int x = -int(radius); x <= int(radius); x++) {
        for (int y = -int(radius); y <= int(radius); y++) {
            vec2 offset = vec2(float(x), float(y)) / textureSize(source, 0);
            color += texture(source, uv + offset);
            total += 1.0;
        }
    }
    fragColor = color / total;
}
