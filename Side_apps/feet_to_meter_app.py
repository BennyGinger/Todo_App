import FreeSimpleGUI as fsg

def convert_feet_to_meters(feet: float, inches: float) -> float:
    """Converts feet and inches to meters."""
    # 1 foot = 0.3048 meters
    # 1 inch = 0.0254 meters
    return feet * 0.3048 + inches * 0.0254

feet_label = fsg.Text("Enter Feet:")
feet_box = fsg.Input(key="feet")
inch_label = fsg.Text("Enter Inches:")
inch_box = fsg.Input(key="inches")

convert_button = fsg.Button("Convert")
exit_button = fsg.Button("Exit")
output_label = fsg.Text(key="output_label")

window = fsg.Window("Feet to Meters App",
                    layout=[[feet_label, feet_box],
                            [inch_label, inch_box],
                            [convert_button, exit_button, output_label]],
                    font=("Helvetica", 20),)

while True:
    event, values = window.read()
    if event == "Convert":
        feet = float(values["feet"])
        inches = float(values["inches"])
        meters = convert_feet_to_meters(feet, inches)
        window["output_label"].update(f"{meters} meters.")
    if event == "Exit" or event == fsg.WIN_CLOSED:
        break
