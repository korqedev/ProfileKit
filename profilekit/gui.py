import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image

from .database import init_db
from .profile import ProfileManager
from .avatar import save_avatar


class ProfileKitApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        init_db()
        self.manager = ProfileManager()
        self.current_avatar = ""

        self.title("ProfileKit")
        self.geometry("620x720")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.main_frame = ctk.CTkFrame(self, corner_radius=20)
        self.main_frame.pack(padx=25, pady=25, fill="both", expand=True)

        self.build_ui()

    def build_ui(self):
        ctk.CTkLabel(
            self.main_frame,
            text="ProfileKit",
            font=("Arial", 34, "bold")
        ).pack(pady=(25, 5))

        ctk.CTkLabel(
            self.main_frame,
            text="Reusable Python User Profile System",
            font=("Arial", 15),
            text_color="gray"
        ).pack(pady=(0, 20))

        self.avatar_label = ctk.CTkLabel(
            self.main_frame,
            text="No Avatar",
            width=160,
            height=160,
            corner_radius=80,
            fg_color="#222222"
        )
        self.avatar_label.pack(pady=10)

        ctk.CTkButton(
            self.main_frame,
            text="Choose Avatar",
            command=self.choose_avatar,
            width=220
        ).pack(pady=10)

        self.username_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Username",
            width=380,
            height=42
        )
        self.username_entry.pack(pady=8)

        self.display_name_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Display Name",
            width=380,
            height=42
        )
        self.display_name_entry.pack(pady=8)

        self.status_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Status Message",
            width=380,
            height=42
        )
        self.status_entry.pack(pady=8)

        self.bio_box = ctk.CTkTextbox(
            self.main_frame,
            width=380,
            height=120
        )
        self.bio_box.pack(pady=8)
        self.bio_box.insert("1.0", "Bio...")

        ctk.CTkButton(
            self.main_frame,
            text="Create Profile",
            command=self.create_profile,
            width=380,
            height=42
        ).pack(pady=(18, 8))

        ctk.CTkButton(
            self.main_frame,
            text="Load Profile",
            command=self.load_profile,
            width=380,
            height=42
        ).pack(pady=8)

        ctk.CTkButton(
            self.main_frame,
            text="Update Profile",
            command=self.update_profile,
            width=380,
            height=42
        ).pack(pady=8)

        ctk.CTkButton(
            self.main_frame,
            text="Delete Profile",
            command=self.delete_profile,
            fg_color="#8b0000",
            hover_color="#650000",
            width=380,
            height=42
        ).pack(pady=8)

        ctk.CTkLabel(
            self.main_frame,
            text="Made by @korqedev",
            font=("Arial", 13),
            text_color="gray"
        ).pack(side="bottom", pady=15)

    def choose_avatar(self):
        path = filedialog.askopenfilename(
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.webp")
            ]
        )

        if not path:
            return

        self.current_avatar = save_avatar(path)
        self.display_avatar(self.current_avatar)

    def display_avatar(self, path):
        try:
            image = Image.open(path)
            ctk_image = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=(160, 160)
            )

            self.avatar_label.configure(
                image=ctk_image,
                text=""
            )

            self.avatar_label.image = ctk_image

        except Exception:
            self.avatar_label.configure(
                image=None,
                text="No Avatar"
            )

    def create_profile(self):
        username = self.username_entry.get().strip()
        display_name = self.display_name_entry.get().strip()
        status = self.status_entry.get().strip()
        bio = self.bio_box.get("1.0", "end").strip()

        if not username:
            messagebox.showerror("Error", "Username is required.")
            return

        success = self.manager.create_profile(
            username=username,
            display_name=display_name,
            bio=bio,
            status=status,
            avatar_path=self.current_avatar
        )

        if success:
            messagebox.showinfo("Success", "Profile created successfully.")
        else:
            messagebox.showerror("Error", "Username already exists.")

    def load_profile(self):
        username = self.username_entry.get().strip()

        if not username:
            messagebox.showerror("Error", "Enter a username to load.")
            return

        profile = self.manager.get_profile(username)

        if not profile:
            messagebox.showerror("Error", "Profile not found.")
            return

        self.display_name_entry.delete(0, "end")
        self.display_name_entry.insert(0, profile["display_name"] or "")

        self.status_entry.delete(0, "end")
        self.status_entry.insert(0, profile["status"] or "")

        self.bio_box.delete("1.0", "end")
        self.bio_box.insert("1.0", profile["bio"] or "")

        self.current_avatar = profile["avatar_path"] or ""

        if self.current_avatar:
            self.display_avatar(self.current_avatar)

        messagebox.showinfo("Loaded", "Profile loaded successfully.")

    def update_profile(self):
        username = self.username_entry.get().strip()

        if not username:
            messagebox.showerror("Error", "Enter a username to update.")
            return

        self.manager.update_profile(
            username=username,
            display_name=self.display_name_entry.get().strip(),
            bio=self.bio_box.get("1.0", "end").strip(),
            status=self.status_entry.get().strip(),
            avatar_path=self.current_avatar
        )

        messagebox.showinfo("Updated", "Profile updated successfully.")

    def delete_profile(self):
        username = self.username_entry.get().strip()

        if not username:
            messagebox.showerror("Error", "Enter a username to delete.")
            return

        self.manager.delete_profile(username)
        messagebox.showinfo("Deleted", "Profile deleted successfully.")
        self.clear_fields()

    def clear_fields(self):
        self.username_entry.delete(0, "end")
        self.display_name_entry.delete(0, "end")
        self.status_entry.delete(0, "end")
        self.bio_box.delete("1.0", "end")
        self.current_avatar = ""
        self.avatar_label.configure(image=None, text="No Avatar")
