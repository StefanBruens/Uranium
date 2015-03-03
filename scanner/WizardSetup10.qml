import QtQuick 2.1
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.1
import QtQuick.Controls.Styles 1.1

import UM 1.0 as UM
WizardPane
{
    contents: ColumnLayout
    {
        anchors.fill: parent
        Text
        {
            id:introText
            text: "<b>Object Shade</b><br>Choose the shade of the object that you're about to scan."
            wrapMode: Text.Wrap
            Layout.maximumWidth:paneWidth
        }
        
        Image
        {
            Layout.maximumWidth:parent.width
            source:"placeholder.png";
        }
        
        ExclusiveGroup { id: objectShadeType }
        ColumnLayout
        {
            id: objectTypeSelection
            RadioButton 
            {
                text: "Light"
                checked: true
                exclusiveGroup: objectShadeType
            }
            RadioButton 
            {
                text: "Medium"
                exclusiveGroup: objectShadeType
            }
            RadioButton 
            {
                text: "Dark"
                exclusiveGroup: objectShadeType
            }
        }
    }    
    buttons:NextButton
    {
        onClicked:
        {
            UM.ToolbarData.setState(11);
        }
    }
}
