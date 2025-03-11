#version 440

// Explicit precision specification (optional)
//precision highp float;
layout(location = 0) in vec2 qt_TexCoord0;
layout(location = 0) out vec4 fragColor;

layout(set = 0, binding = 0) uniform sampler2D source;
//Ыlayout(set = 0, binding = 1) uniform float radius;



void main() {
    vec2 uv = qt_TexCoord0;
    vec4 color = vec4(0.0);
    float total = 0.0;
    float radius = 20.0;
    // Optimization: calculate texture size once
    ivec2 texSize = textureSize(source, 0);
    
    for (int x = -int(radius); x <= int(radius); x++) {
        for (int y = -int(radius); y <= int(radius); y++) {
            // Normalize offset relative to texture size
            vec2 offset = vec2(x, y) / vec2(texSize);
            color += texture(source, uv + offset);
            total += 1.0;
        }
    }

    fragColor = color / total;
}