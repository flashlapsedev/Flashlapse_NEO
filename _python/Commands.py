import Settings
from time import sleep

def light_confirm(self):
    #current_CMD = "1~"+str(self.Start_spinBox.value())+"~"+str(self.End_spinBox.value())+"~"+ str(self.R_spinBox.value()) + "~" + str(self.G_spinBox.value()) + "~" + str(self.B_spinBox.value()+ "~" + str(self.BRT_spinBox.value())
    Settings.commands_list.append(current_CMD)
    #Settings.sendCMD()

'''def full_color_change(self):
    temp = self.Full_Color_Select.currentIndex()

    self.Left_Select.setCurrentIndex(0)
    self.Right_Select.setCurrentIndex(0)
    self.Top_Color_Select.setCurrentIndex(0)
    self.LL_Color_Select.setCurrentIndex(0)
    self.LR_Color_Select.setCurrentIndex(0)

    if temp == 1:
        Settings.ASD.write(bytes("1~0~58~255~0~0~1", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~0~58~0~255~0~1", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~0~58~0~0~255~1", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~0~58~85~85~85~1", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~0~58~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~1", 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~0~58~0~0~0~1", 'UTF-8'))

def half_color_change_left(self):

    temp = self.Left_Select.currentIndex()

    self.Full_Color_Select.setCurrentIndex(0)    
    self.Top_Color_Select.setCurrentIndex(0)
    self.LL_Color_Select.setCurrentIndex(0)
    self.LR_Color_Select.setCurrentIndex(0)

    if temp == 1:
        Settings.ASD.write(bytes("1~0~29~255~0~0~2", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~0~29~0~255~0~2", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~0~29~0~0~255~2", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~0~29~85~85~85~2", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~0~29~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~2", 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~0~29~0~0~0~2", 'UTF-8'))

def half_color_change_right(self):

    self.Full_Color_Select.setCurrentIndex(0)
    self.Top_Color_Select.setCurrentIndex(0)
    self.LL_Color_Select.setCurrentIndex(0)
    self.LR_Color_Select.setCurrentIndex(0)
    
    temp = self.Right_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes("1~29~58~255~0~0~2", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~29~58~0~255~0~2", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~29~58~0~0~255~2", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~29~58~85~85~85~2", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~29~58~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~2", 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~29~58~0~0~0~2", 'UTF-8'))

def third_color_change_top(self):

    self.Full_Color_Select.setCurrentIndex(0)
    self.Left_Select.setCurrentIndex(0)
    self.Right_Select.setCurrentIndex(0)
    
    temp = self.Top_Color_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes("1~19~38~255~0~0~3", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~19~38~0~255~0~3", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~19~38~0~0~255~3", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~19~38~85~85~85~3", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~19~38~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~3", 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~19~38~0~0~0~3", 'UTF-8'))

def third_color_change_lower_left(self):

    self.Full_Color_Select.setCurrentIndex(0)
    self.Left_Select.setCurrentIndex(0)
    self.Right_Select.setCurrentIndex(0)
    
    temp = self.LL_Color_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes("1~0~19~255~0~0~3", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~0~19~0~255~0~3", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~0~19~0~0~255~3", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~0~19~85~85~85~3", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~0~19~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~3", 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~0~19~255~0~0~3", 'UTF-8'))

def third_color_change_lower_right(self):

    self.Full_Color_Select.setCurrentIndex(0)
    self.Left_Select.setCurrentIndex(0)
    self.Right_Select.setCurrentIndex(0)
    
    temp = self.LR_Color_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes("1~38~58~255~0~0~3", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~38~58~0~255~0~3", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~38~58~0~0~255~3", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~38~58~85~85~85~3", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~38~58~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~3", 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~38~58~0~0~0~3", 'UTF-8'))

def inject_code(self):
    Settings.ASD.write(bytes(self.IC_0.text()+"~"+self.IC_1.text()+"~"+self.IC_2.text()+"~"+self.IC_3.text()+"~"+self.IC_4.text()+"~"+self.IC_5.text()+"~"+self.IC_6.text(), 'UTF-8'))'''