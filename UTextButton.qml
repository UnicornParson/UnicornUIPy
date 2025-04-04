import QtQuick 2.12
import TemplatesTypes 1.0
UBaseItem {
    id: root

    property alias text: label.text
    property alias textFormat: label.textFormat
    property alias textColor: label.color
    property alias font: label.font

    property alias borderColor: border.color
    property alias backgroundColor: background.color
    

    property int borderSize : skin.defaultBorderSize
    property int borderRadius : skin.defaultBorderRadius
    property int margin: skin.defaultMargin

    property int state: ButtonState.Normal
    property bool isPressed: false

    property color backgroundHoveredColor: skin.buttonHoveredBackgroundColor
    property color backgroundHoveredBorderColor: skin.buttonHoveredBorderColor
    itemName: "UTextButton"

    signal clicked()
    signal pressed()
    signal released()
    signal hoverOn()
    signal hoverOf()

    Rectangle {
        id: border

        anchors.fill: parent
        color: skin.buttonBorderColor
        anchors.margins: margin
        radius: borderRadius
    }

    Rectangle {

        id: background
        anchors.fill: parent
        color: skin.buttonBackgroundColor
        anchors.margins: borderSize + margin
        radius: borderRadius
    }


    Text {
        id: label
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        width: background.width - (2 * margin)
        text: "no text"
        color: skin.buttonFontColor
        minimumPointSize: 10
        font.pointSize: 60
        fontSizeMode: Text.Fit
    }

    MouseArea {
        id: mouceArea
        anchors.fill: parent
        hoverEnabled: true
        enabled: root.state !== ButtonState.Disabled
        preventStealing: true
        onContainsMouseChanged:
        {
            if(root.state !== ButtonState.Disabled)
            {
                root.state = containsMouse ? ButtonState.Hovered : ButtonState.Normal
            }
        }

        onPressed: {
            console.log("onPressed")
            root.isPressed = true
            root.pressed()
        }

        onReleased:
        {
            root.released()
            if(root.isPressed)
            {
                root.clicked()
            }
            root.isPressed = false

        }
    }


    states: [
        State {
            name: "hovered"
            when: root.state === ButtonState.Hovered
            PropertyChanges {
                target: background
                color: root.backgroundHoveredColor
            }
            PropertyChanges {
                target: border
                color: root.backgroundHoveredBorderColor
            }
        }
    ]
}
