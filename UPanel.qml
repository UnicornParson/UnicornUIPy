import QtQuick 2.0

Item {
    id: root

    property alias background: backgroundItem
    property alias border: borderItem.border

    UBackgroundElement {
        id: backgroundItem
        anchors.fill: root
        color: skin.backgroundColor
    }
    Rectangle {
        id: borderItem

        anchors.fill: parent
        border.color: skin.secondBorderColor
        border.width: skin.defaultBorderSize
        anchors.margins: 0
        radius: 0
    }
}
