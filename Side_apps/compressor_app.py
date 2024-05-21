import FreeSimpleGUI as fsg
import zipfile
import pathlib


def make_archive(filepaths: list[pathlib.Path], folderpath: pathlib.Path):
    save_path  = pathlib.Path(folderpath, "compressed.zip")
    with zipfile.ZipFile(save_path, "w") as zipf:
        for file in filepaths:
            file = pathlib.Path(file)
            zipf.write(file, arcname=file.name)



src_label = fsg.Text("Select a file to compress:")
disp_files = fsg.Input(key="display_files")
select_files_button = fsg.FilesBrowse("Choose", key="files")

dst_label = fsg.Text("Select a destination folder:")
disp_folder = fsg.Input(key="display_folder")
select_folder_button = fsg.FolderBrowse("Choose", key="folder")

compress_button = fsg.Button("Compress")
output_label = fsg.Text(key="output_label")

window = fsg.Window("Compressor App",
                    layout=[[src_label,disp_files,select_files_button],
                            [dst_label,disp_folder,select_folder_button],
                            [compress_button, output_label]],
                    font=("Helvetica", 20),)

while True:
    event, values = window.read()
    print(event, values)
    filespath = values["files"].split(";")
    folder = values["folder"]
    make_archive(filespath, folder)
    window["output_label"].update("Files compressed successfully!!")
    if event == fsg.WIN_CLOSED:
        break
window.close()