import QtQuick 2.0
import QtQuick.Controls 2.15
import QtQuick.Effects

UBaseItem {
    id: root
    property int dialogWidth: 800
    property int dialogHeight: 600
    property alias dialogSource: dialogLoader.source
    property alias bgImageSource: bgImage.source
    property alias bgImageColor: bgImage.placeholderColor
    property bool blurEffect: true
    property int blurEffectRadius: 20
    property bool blurEffectTransparentBorder : true

    UImage
    {
        id: bgImage
        placeholderColor: "white"
        anchors.fill: root
    }

    // FIXME: Blur effect is not working properly, it's just a placeholder for now...  
    // Failed to build graphics pipeline state
    // Failed to link shader program: error: fragment shader input `qt_TexCoord0' with explicit location has no matching output
/*
    ShaderEffect {
        id: blurEffect
        anchors.fill: bgImage
        visible: root.blurEffect

        property var source: bgImage
        //property real radius: root.blurEffectRadius

        fragmentShader: "shaders/blur.qsb"
    }*/
    Loader {
        id: dialogLoader

        anchors.centerIn: root
        width: dialogWidth
        height: dialogHeight
        clip: true
    }
}
