import QtQuick 2.0
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

UBaseItem {
    id: root

    property int pointSize: 12
    property color textColor: skin.consoleTextColor
    property color backgroundColor: skin.consoleBackground
    property int margin: 1
    property color borderColor: skin.consoleBorder
    property int borderThickness: 1
    property bool autoScroll: true
    Flickable {
        anchors.fill: parent
        flickableDirection: Flickable.VerticalFlick

        ScrollBar.vertical: ScrollBar {}
        ScrollBar.horizontal: ScrollBar {}
        clip: true
        

        TextArea.flickable: TextArea {
            id: consoleText
            text: console_controller.text
            font.family: skin.consoleFontName
            font.pixelSize: root.pointSize
            color: root.textColor
            wrapMode: Text.Wrap
            readOnly: true
            selectByMouse: true
            //anchors.fill: parent
            anchors.margins: root.margin

            onTextChanged: { consoleText.cursorPosition = consoleText.length }
            background: Rectangle {
                border.color: root.borderColor
                border.width: root.borderThickness
                anchors.fill: parent
                color: root.backgroundColor
                
            }
        }
    }
}
