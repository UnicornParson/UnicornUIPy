// solution from https://stackoverflow.com/questions/35553792/show-fps-in-qml

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.15
import QtQuick.Effects
//import Qt5Compat.GraphicalEffects
Item {
    id: root

    property alias bgColor: background.color
    property alias textColor: fpsText.color
    property alias spinerSource: spinnerImage.source
    property alias spinerColor:spinnerImage.color
    //property alias spinerCachedColor: spinnerImage.cachedEffect
    property alias spinerVisible: spinnerImage.visible
    property bool coloredImage: true
    property int spinnerHeight: 16
    property int delimiterSize: 2
    property int frameCounter: 0
    property int frameCounterAvg: 0
    property int counter: 0
    property int fps: 0
    property int fpsAvg: 0

    function frameSwappedHandler(){
        root.frameCounter++
    }

    width:  ((spinnerImage.visible) ? spinnerImage.width : 0) + fpsText.width + (delimiterSize * 2);
    height: spinnerHeight
    visible: globals ? globals.fpsIndicatorEnabled : false
    Rectangle {
        id: background
        color: "black"
        height: root.height
        width: root.width
    }

    Image {
        id: spinnerImage
        property alias color: cOverlay.colorizationColor
        //property alias cachedEffect: cOverlay.cached

        anchors.left: parent.left
        anchors.top: parent.top

        width: root.spinnerHeight
        height: root.spinnerHeight
        sourceSize: Qt.size(spinnerHeight, spinnerHeight)
        source: "img/circleWhite.png"
/*
        ColorOverlay {
            id: cOverlay

            visible: root.coloredImage
            cached: true
            anchors.fill: spinnerImage
            source: spinnerImage
            color: "#ccffff"
        }*/
        MultiEffect {
            id: cOverlay
            //cached: False
            source: spinnerImage
            anchors.fill: spinnerImage
            colorization: 1
            colorizationColor: "#ccffff"
        }
        NumberAnimation on rotation {
            from:0
            to: 360
            duration: 800
            loops: Animation.Infinite
        }
    }

    Text {
        id: fpsText

        anchors.left: spinnerImage.visible ? spinnerImage.right : root.left
        anchors.leftMargin: root.delimiterSize
        anchors.verticalCenter: spinnerImage.verticalCenter
        color: "#c0c0c0"
        font.pixelSize: (root.height > 2) ? (root.height - 2) : 2
        text: ((!spinnerImage.visible) ? "FPS: " : "") + root.fps
    }

    Timer {
        id: updateTimer

        interval: 1000
        repeat: true
        running: false
        onTriggered: {
            root.fps = root.frameCounter;
            root.frameCounter = 0;
        }
    }

    Component.onCompleted: {
        updateTimer.start()
    }
}
