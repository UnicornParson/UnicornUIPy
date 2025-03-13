import QtQuick 2.0

Item {
    id: root

    property alias background: backgroundItem

    UBackgroundElement {
        id: backgroundItem
        anchors.fill: root
        color: skin.backgroundColor
    }
}
