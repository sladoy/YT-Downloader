# from tkinter import Tk, Label, Button, ttk
#
#
#
#   Someday i will make this
#
#
#
# class ChooseWindow:
#     def __init__(self):
#         self.root = None
#         self.x = None
#         self.label = None
#         self.choose_tree_view = None
#         self.ok_button = None
#         self.cancel_button = None
#         self.values = None
#         self.tree_values = None
#         self.itag_table = []
#
#     def create_window(self, all_qualities):
#         self.root = Tk()
#         self.root.title('Choosing Window')
#         self.label = Label(self.root, text='Choose format:\t')
#         self.label.pack()
#
#         self.choose_tree_view = ttk.Treeview(self.root, columns=[0, 1, 2, 3, 4, 5], show='headings')
#         self.choose_tree_view.heading(0, text='Tag')
#         self.choose_tree_view.heading(1, text='Format')
#         self.choose_tree_view.heading(2, text='FPS')
#         self.choose_tree_view.heading(3, text='ABR')
#         self.choose_tree_view.heading(4, text='Video Codec')
#         self.choose_tree_view.heading(5, text='Audio Codec')
#
#         self.choose_tree_view.column(0, width=30)
#         self.choose_tree_view.column(1, width=100)
#         self.choose_tree_view.column(2, width=30)
#         self.choose_tree_view.column(3, width=50)
#
#         self.choose_tree_view.pack()
#
#         self.ok_button = Button(self.root, text='OK', command=lambda :[self.pass_value(), self.get_value()])
#         self.ok_button.pack()
#         self.cancel_button = Button(self.root, text='Cancel')
#         self.cancel_button.pack()
#
#         for x in all_qualities.all():
#             self.choose_tree_view.insert("", "end", values=[x.itag, x.mime_type, x.fps,
#                                                             x.abr, x.audio_codec, x.video_codec])
#
#         self.root.mainloop()
#
#     def pass_value(self):
#         self.values = self.choose_tree_view.focus()
#         return self.choose_tree_view.item(self.values)['values'][0]
#
#     def get_value(self):
#         self.values = self.choose_tree_view.focus()
#         self.tree_values = self.choose_tree_view.item(self.values)
#
#
