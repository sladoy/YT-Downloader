from tkinter import Tk, Label, Button, Entry, ttk
from tkinter.filedialog import askdirectory
from pytube import YouTube
from function_and_error_windows import inital_error_window, wrong_output_error_window, download_completed


"""
Button Browse, allows to pick any localization.
Button Add to Queue, add requested link to the tree
Button Download, take every position from the tree and downloads it to user given localization
Button Delete, allows to delete any positions from queue
"""


class DownloadWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title('YT Downloader')

        self.label_link = Label(self.root, text="Input link from YT")
        self.label_link.grid(row=0, column=0, padx=5, sticky='W')

        self.entry_link = Entry(self.root, width=50)
        self.entry_link.grid(row=0, column=1)

        self.label_localization = Label(self.root, text='Where to save a file ?')
        self.label_localization.grid(row=1, column=0, padx=5, sticky='W')

        self.entry_localization = Entry(self.root, width=50)
        self.entry_localization.grid(row=1, column=1)

        self.button_localization = Button(self.root, text='Browse', width=25, command=self.localization)
        self.button_localization.grid(row=1, column=2, sticky='W')

        self.label_output = Label(self.root, text='Choose the Audio or Video')
        self.label_output.grid(row=2, column=0, padx=5)

        self.list_output = ttk.Combobox(self.root, state='readonly', values=('Audio', 'Video'), justify='center')
        self.list_output.grid(row=2, column=1)

        self.button_accept = Button(self.root, text='Add to Queue', width=25, command=self.add_to_queue)
        self.button_accept.grid(row=4, column=1, pady=10)

        self.tree_view = ttk.Treeview(self.root, columns=[0, 1, 2], show='headings')
        self.tree_view.heading(0, text='Name of video')
        self.tree_view.heading(1, text='Link to video')
        self.tree_view.heading(2, text='Output')
        self.tree_view.column(0, width=300)
        self.tree_view.grid(row=5, column=1, pady=25)

        self.button_delete = Button(self.root, text='Delete', width=10,command=self.delete_position)
        self.button_delete.grid(row=5, column=2)

        self.button_download = Button(self.root, text='Download', width=25, height=2, bg='black', fg='white',
                                      command=self.prepare_to_download)
        self.button_download.grid(row=6, column=1)

        self.link = None
        self.more_window = None
        self.link_table = []
        self.name_of_video = None

        self.root.mainloop()

    def take_entry_link(self):
        self.link = self.entry_link.get()

    def find_position(self, link_of_item, output_of_item):
        for x, y in enumerate(self.link_table):
            if link_of_item == y[0] and output_of_item == y[1]:
                return x

    def delete_position(self):
        item = self.tree_view.focus()  # Get id of picked item

        link_of_item = self.tree_view.item(item)['values'][1]  # Get value of picked item (link)
        output_of_item = self.tree_view.item(item)['values'][2]  # Get value of picked item (output)

        item_to_delete = self.find_position(link_of_item, output_of_item)

        self.link_table.remove(self.link_table[item_to_delete])
        self.tree_view.delete(item)

    """This method goes to Add to Queue Button"""
    def add_to_queue(self):
        if self.entry_localization.get() and self.entry_link.get() and self.list_output.get():
            self.take_entry_link()
            yt = YouTube(self.link)
            self.tree_view.insert("", 'end', values=(yt.title, self.link, self.list_output.get()))
            self.entry_link.delete(0, 'end')
            self.link_table.append([self.link, self.list_output.get()])

    """This method goes to Browse Button"""
    def localization(self):
        self.entry_localization.delete(0, 'end')
        path = askdirectory()
        self.entry_localization.insert(0, path)

    """This method goes to Download Button"""
    def prepare_to_download(self):
        """Pick format and download it"""
        if len(self.link_table) != 0:
            while self.link_table:
                first_element = self.link_table[0][0]
                yt = YouTube(first_element)
                if self.link_table[0][1] == "Audio":
                    stream = yt.streams.filter(only_audio=True).first()
                    stream.download(self.entry_localization.get())
                    self.link_table.remove(self.link_table[0])
                    yt = None
                elif self.link_table[0][1] == "Video":
                    stream = yt.streams.first()
                    stream.download(self.entry_localization.get())
                    self.link_table.remove(self.link_table[0])
                    yt = None

            self.tree_view.delete(*self.tree_view.get_children())
            download_completed()
        else:
            inital_error_window()


if __name__ == '__main__':
    DownloadWindow()
