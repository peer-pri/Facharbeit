import customtkinter
import os
from PIL import Image
import tkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Lunaris - Gui Builder")
        self.geometry("1490x700")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        def accepted_terms():
            print("Accepted Terms!")
            self.frame_2_button.configure(state="normal")
            self.frame_3_button.configure(state="normal")

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image.png")), size=(450, 120))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Lunaris", image=self.logo_image,
                                                             compound="left", corner_radius=100, font=customtkinter.CTkFont(size=16, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Terms of Service",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Drag & Drop Builder",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Default Code - Beta",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_2_button.configure(state="disabled")
        self.frame_3_button.configure(state="disabled")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame,hover_color="darkgreen",command=accepted_terms,font=("Arial", 18), text="Accept Terms of Service")
        self.home_frame_button_1.grid(row=4, column=0, padx=20, pady=10)

        self.home_frame_lable_1 = customtkinter.CTkLabel(self.home_frame, fg_color="#6aa0a2", anchor="center",font=("Arial", 16), corner_radius=10, text=f"""                                                     
                                            Use of Service                                                 
You must comply with these Terms and any applicable laws. You are responsible for maintaining the confidentiality of your account. 
You may not engage in any activity that disrupts the service or infringes upon others' rights.

                                                         
Intellectual Property
Our GUI Builder and its content are protected by intellectual property laws. You may not copy, modify, distribute, or sell any part of our GUI Builder without our written consent.

                                                         
User Content
You own the content you create using our GUI Builder. By using our service, you grant us a license to use, reproduce, and distribute your content.

                                                         
Limitation of Liability
We are not liable for any damages arising from the use of our GUI Builder. This includes loss of profits, data, or other intangible losses.

                                                         
Modifications and Termination
We may modify or terminate our GUI Builder without notice. We may update these Terms, and your continued use constitutes acceptance of the changes.

                                                         
Privacy
We handle your personal information in accordance with applicable privacy laws. Refer to our Privacy Policy for details.
""")
        self.home_frame_lable_1.grid(row=1, column=0, padx=20, pady=10)

        




        def make_draggable(button):
            def on_drag_start(event):
                button.startX = event.x
                button.startY = event.y

            def on_drag_motion(event):
                x, y = event.x, event.y
                deltaX = x - button.startX
                deltaY = y - button.startY
                newX = button.winfo_x() + deltaX
                newY = button.winfo_y() + deltaY
                button.place(x=newX, y=newY)

            def on_drag_release(event):
                if button.winfo_x() > 300:
                    button.configure(state="normal")
                else:
                    button.destroy()

            button.bind("<Button-1>", on_drag_start)
            button.bind("<B1-Motion>", on_drag_motion)
            button.bind("<ButtonRelease-1>", on_drag_release)




        from tkinter import Tk, Text, Button, StringVar

        start_input = StringVar()
        label_input = StringVar()
        button_input = StringVar()
        lever_input = StringVar()
        slider_input = StringVar()
        end_input = StringVar()

        def create_input_window(title, input_variable):
            def save_text():
                input_variable.set(text.get("1.0", "end-1c"))  # Save the input text to the input_variable
                root.destroy()  # Close the window

            root = Tk()
            root.title(title)
            text = Text(root)
            text.pack()
            text.insert("end", input_variable.get())  # Insert the previously saved input text
            save_button = Button(root, text="Save", command=save_text)
            save_button.pack()
            root.mainloop()

        def start_clicked():
            create_input_window("Start Input", start_input)
            print("Start button clicked")
            print("Input:", start_input.get())  # Use the input variable in your code

        def label_clicked():
            create_input_window("Label Input", label_input)
            print("Label button clicked")
            print("Input:", label_input.get())  # Use the input variable in your code

        def button_clicked():
            create_input_window("Button Input", button_input)
            print("Button button clicked")
            print("Input:", button_input.get())  # Use the input variable in your code

        def lever_clicked():
            create_input_window("Lever Input", lever_input)
            print("Lever button clicked")
            print("Input:", lever_input.get())  # Use the input variable in your code

        def slider_clicked():
            create_input_window("Slider Input", slider_input)
            print("Slider button clicked")
            print("Input:", slider_input.get())  # Use the input variable in your code

        def end_clicked():
            create_input_window("End Input", end_input)
            print("End button clicked")
            print("Input:", end_input.get())  # Use the input variable in your code


        def add_element():
            choice = self.optionmenu.get()
            print("Add element:", choice)
            if choice != "Choose your Element":
                new_button = customtkinter.CTkButton(self.second_frame, hover_color="darkgreen", font=("Arial", 18), text=choice)
                new_button.grid(row=len(self.buttons) + 2, column=0, padx=20, pady=10)
                self.buttons.append(new_button)
                new_button.configure(state="disabled")
                make_draggable(new_button)  # Make the new button movable

                if choice == "Start":
                    new_button.configure(command=start_clicked)
                elif choice == "Label":
                    new_button.configure(command=label_clicked)
                elif choice == "Button":
                    new_button.configure(command=button_clicked)
                elif choice == "Lever":
                    new_button.configure(command=lever_clicked)
                elif choice == "Slider":
                    new_button.configure(command=slider_clicked)
                elif choice == "End":
                    new_button.configure(command=end_clicked)
                

        # Create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.second_frame_label_1 = customtkinter.CTkLabel(self.second_frame, fg_color="#6aa0a2", anchor="nw", font=("Arial", 16), corner_radius=10, text="Move the elements to the right to use them in the GUI.\nElements that are too near to the left get deleted.")
        self.second_frame_label_1.grid(row=0, column=0, padx=20, pady=10, columnspan=2)

        def optionmenu_callback(choice):
            print("Selected element:", choice)

        # Create option menu in the second frame
        self.optionmenu = customtkinter.CTkOptionMenu(self.second_frame, 
                                                    values=["Choose your Element", "Start","Label", "Button", "Lever", "Slider", "End"],
                                                    command=optionmenu_callback)
        self.optionmenu.grid(row=1, column=0, padx=20, pady=10, sticky="nw")

        self.buttons = []

        self.second_frame_frame_button_1 = customtkinter.CTkButton(self.second_frame, hover_color="darkgreen", command=add_element, font=("Arial", 18), text="Add Element")
        self.second_frame_frame_button_1.grid(row=1, column=1, padx=20, pady=10)

        def save_output(output, filename_filetype):
            with open(filename_filetype, "w") as file:
                file.write(output)
            print("Output saved as " + filename_filetype)

        def output_element():
            try:
                print(start_input.get())
                output1 = start_input.get()
            except:
                pass
            try:
                print(label_input.get())
                output2 = label_input.get()
            except:
                pass
            try:
                print(button_input.get())
                output3 = button_input.get()
            except:
                pass
            try:
                print(lever_input.get())
                output4 = lever_input.get()
            except:
                pass
            try:
                print(slider_input.get())
                output5 = slider_input.get()
            except:
                pass
            try:
                print(end_input.get())
                output6 = end_input.get()
            except:
                pass

            global output
            output = output1 + "\n" + output2 + "\n" + output3 + "\n" + output4 + "\n" + output5 + "\n" + output6

            choice_output = input("Do you want to save the output? [Yes / No]: ")
            if choice_output == "Yes":
                filename_filetype = input("Input the filename with the file format ending: ")
                save_output(output, filename_filetype)  # Pass the output and filename_filetype arguments to the save_output function
                                    

        self.second_frame_frame_button_2 = customtkinter.CTkButton(self.second_frame, hover_color="darkgreen", command=output_element, font=("Arial", 18), text="Output")
        self.second_frame_frame_button_2.grid(row=1, column=2, padx=20, pady=10)       

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.customcode_lable1 = customtkinter.CTkLabel(self.third_frame, width=980, height=460, fg_color="#6aa0a2", anchor="center", font=("Arial", 9), corner_radius=10, text="""
Default Lua Code:
                                                        
local Fluent = loadstring(game:HttpGet("https://github.com/dawid-scripts/Fluent/releases/latest/download/main.lua"))()
local SaveManager = loadstring(game:HttpGet("https://raw.githubusercontent.com/dawid-scripts/Fluent/master/Addons/SaveManager.lua"))()
local InterfaceManager = loadstring(game:HttpGet("https://raw.githubusercontent.com/dawid-scripts/Fluent/master/Addons/InterfaceManager.lua"))()
local Window = Fluent:CreateWindow({
    Title = "Fluent " .. Fluent.Version,
    TabWidth = 160,
    Size = UDim2.fromOffset(580, 460),
    Acrylic = true, -- The blur may be detectable, setting this to false disables blur entirely
})
local Tabs = {
    Main = Window:AddTab({ Title = "Main", Icon = "" }),
    Settings = Window:AddTab({ Title = "Settings", Icon = "settings" })
}
local Options = Fluent.Options
do
    Tabs.Main:AddButton({
        Title = "Button",
        Description = "Very important button",
        Callback = function()
            Window:Dialog({
                Title = "Title",
                Content = "This is a dialog",
                Buttons = {
                    {
                        Title = "Confirm",
                        Callback = function()
                            print("Confirmed the dialog.")
                        end
                    },
                }
            })
        end
    })
    local Toggle = Tabs.Main:AddToggle("MyToggle", {Title = "Toggle", Default = false })
    Toggle:OnChanged(function()
        print("Toggle changed:", Options.MyToggle.Value)
    end)
    Options.MyToggle:SetValue(false)
    local Slider = Tabs.Main:AddSlider("Slider", {
        Title = "Slider",
        Description = "This is a slider",
        Default = 2,
        Min = 0,
        Callback = function(Value)
            print("Slider was changed:", Value)
        end
    })
    Slider:OnChanged(function(Value)
        print("Slider changed:", Value)
    end)
    Slider:SetValue(3)
    local Input = Tabs.Main:AddInput("Input", {
        Title = "Input",
        Callback = function(Value)
            print("Input changed:", Value)
        end
    })
end                                                                                                           
                                                        """)
        self.customcode_lable1.grid(row=0, column=2, padx=20, pady=10, columnspan=5)


        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()


    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
