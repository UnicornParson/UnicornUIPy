import QtQuick 2.0

Item {
    id: root

    property int radius: 15
    property color color: "red"

    Rectangle
    {
        width: root.radius * 2
        height: root.radius * 2
        radius: root.radius
        color: root.color

    }
}
