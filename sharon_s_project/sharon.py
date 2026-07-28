import os
import tkinter as tk
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import requests

root = tk.Tk()
root.geometry("400x700")
root.title("Modern App")
root.config(bg="#ffffff")

header_frame = tk.Frame(root, bg="#ffffff", height=60, bd=0, highlightthickness=1, highlightbackground="#EEF2F3")
header_frame.pack(fill=tk.X, side=tk.TOP)
header_frame.pack_propagate(False)

bottom_frame = tk.Frame(root, bg="white")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

menu_btn = tk.Button(header_frame, text="☰", font=("Arial", 16), bg="#FFFFFF", fg="#1E293B", bd=0, activebackground="#F1F5F9", cursor="hand2")
menu_btn.pack(side=tk.LEFT, padx=16)

title_label = tk.Label(header_frame, text="Sign Up Page", font=("Arial", 16, "bold"), bg="#FFFFFF",fg="#1E293B")
title_label.pack(side=tk. LEFT, expand=True)
    
settings_btn=tk.Button(header_frame, text="⚙️", font=("Arial", 16), bg="#FFFFFF", fg="#1E293B", bd=0, activebackground="#F1F5F9", cursor="hand2")
settings_btn.pack(side=tk. RIGHT, padx=16)

content_area = tk.Frame(root, bg="#F8FAFC")
content_area.pack(fill=tk. BOTH, expand=True)

username_label = tk.Label(content_area, text= "Username:", font= ("Arial", 12), bg="#F8FAFC", fg="#333333")
username_label.pack(anchor = "w", padx=20, pady=(20,5))

username_entry = tk.Entry(content_area, font=("Arial", 14), bg="#FFFFFF", bd=1, relief="solid")
username_entry.pack(fill=tk. X, padx=20, pady=(0,10))

password_Label = tk.Label(content_area, text= "Password:", font=("Arial", 12), bg="#F8FAFC", fg="#333333")
password_Label.pack(anchor = "w", padx=20, pady=(10,5))

password_entry = tk.Entry(content_area, font=("Arial",14), bg="#FFFFFF", bd=1, relief="solid", show="*")
password_entry.pack(fill=tk. X, padx=20, pady=(0,20))

confirm_password_label = tk.Label(
    content_area,
    text="Confirm Password:",
    font=("Arial", 12),
    bg="#F8FAFC",
    fg="#333333"
)

confirm_password_label.pack(
    anchor="w",
    padx=20,
    pady=(5,5)
)

confirm_password_entry = tk.Entry(
    content_area,
    font=("Arial",14),
    bg="white",
    bd=1,
    relief="solid",
    show="*"
)

confirm_password_entry.pack(
    fill=tk.X,
    padx=20,
    pady=(0,20)
)

student_id_label = tk.Label(content_area,text= "Student ID:", font=("Arial", 12), bg="#F8FAFC", fg="#333333")
student_id_label.pack(anchor= "w", padx= 20, pady=(5, 5))

student_id_entry = tk.Entry(content_area, font=("Arial", 14), bg="#FFFFFF", bd= 1, relief="solid")
student_id_entry.pack(fill=tk. X, padx= 20, pady=(0, 30))

def hide_all_pages():
    """Hide every main content page before showing a new one."""
    content_area.pack_forget()
    forgot_page.pack_forget()
    account_page.pack_forget()
    petition_page.pack_forget()
    diss_threads_page.pack_forget()
    oppor_scholar_page.pack_forget()


def show_account_page():
    """Open only the account page."""
    hide_all_pages()
    account_page.pack(fill="both", expand=True)
    title_label.config(text="Account Page")

    for button in [diss_threads, petition, oppor_scholar, account]:
        button.pack_forget()

    diss_threads.pack(side=tk.LEFT, padx=0)
    petition.pack(side=tk.LEFT, padx=16)
    oppor_scholar.pack(side=tk.LEFT, padx=16)
    account.pack(side=tk.RIGHT, padx=16)

    account.config(bg="grey", fg="white")
    petition.config(bg="white", fg="green")
    diss_threads.config(bg="white", fg="red")
    oppor_scholar.config(bg="white", fg="blue")


def signup_to_account():
    username = username_entry.get().strip()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    student_id = student_id_entry.get().strip()

    # Check required fields
    if (
        username == "" or
        password == "" or
        confirm_password == "" or
        student_id == ""
    ):
        showerror(
            "Missing Information",
            "Please fill in all required fields."
        )
        return

    # Check passwords match
    if password != confirm_password:
        showerror(
            "Password Error",
            "Passwords do not match."
        )
        return

    # Check Student ID
    if not student_id.isdigit():
        showerror(
            "Invalid Student ID",
            "Student ID must only contain numbers."
        )
        return

    # Everything is valid
    username_display.config(text=f"Username: {username}")
    studentid_display.config(text=f"Student ID: {student_id}")
    show_account_page()

signup_button= tk.Button(content_area, text="Sign Up", command=signup_to_account, font=("Arial", 20, "bold"), bg="#091DFB", fg="#FFFFFF")
signup_button.pack(fill=tk. BOTH, padx= 20)

def go_to_forgot_page():
    hide_all_pages()
    forgot_page.pack(fill="both", expand=True)
    forgot_page.config(bg="white")
    title_label.config(text="Verification Code")
        
forgot_page = tk.Frame(root, bg="white")
forgot_page.config(bg="white")

email_label = tk.Label(forgot_page, text="Give Email", font=("Arial", 12), bg="white", fg="#333333")
email_label.pack(anchor="w", padx=40, pady=(10,5))

email_entry = tk.Entry(forgot_page, font=("Arial", 14), bg="#FFFFFF", bd=1, relief="solid")
email_entry.pack(fill="x", padx=40, pady=(0,20))

send_code = tk.Button(forgot_page, text="Send Code", font=("Arial", 14, "bold"), bg="#091DFB", fg="#FFFFFF", bd=0, cursor="hand2")
send_code.pack(fill="x", padx=40, pady=10)

def go_to_content_area():
    hide_all_pages()
    content_area.pack(fill=tk.BOTH, expand=True)
    title_label.config(text="Sign Up Page")

goback = tk.Button(forgot_page, text="←", command=go_to_content_area, font=("Arial", 16), bg="white", fg="black", bd=0, cursor="hand2")
goback.pack(fill="x", padx=40, pady=10)

forgot = tk.Button(content_area, text="Forgot username or password ?", command=go_to_forgot_page, font=("Arial", 15, "bold"), bg="#FFFFFF", fg="red", bd=0)
forgot.pack(fill=tk.BOTH, padx=20, pady=(5, 5))
   
account_page = tk.Frame(root, bg="grey")
account_page.config(bg="grey")

profile_card = tk.Frame(
    account_page,
    bg="white",
    bd=1,
    relief="solid",
    width=320,
    height=220)

profile_card.pack(pady=30)
profile_card.pack_propagate(False)

picture_frame = tk.Frame(
    profile_card,
    bg="lightgrey",
    width=100,
    height=100,
    bd=1,
    relief="solid"
)

picture_frame.pack(pady=15)
picture_frame.pack_propagate(False)
        
def choose_picture():
    global profile_photo

    filename = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if filename:
        image = Image.open(filename)
        image = image.resize((100, 100))

        profile_photo = ImageTk.PhotoImage(image)

        add_picture_btn.config(image=profile_photo, text="")

add_picture_btn = tk.Button(
    picture_frame,
    text="+",
    font=("Arial", 20, "bold"),
    bg="white",
    command=choose_picture
)
add_picture_btn.pack(expand=True)

username_display = tk.Label(
    profile_card,
    text="Username: ",
    font=("Arial", 14),
    bg="white"
)
username_display.pack(pady=5)

studentid_display = tk.Label(
    profile_card,
    text="Student ID: ",
    font=("Arial", 14),
    bg="white"
)
studentid_display.pack()

account = tk.Button(bottom_frame, text="👤", command=show_account_page,  font=("Arial", 25), bg="#FFFFFF", fg="#0B63EF", bd=0, activebackground="#FFFFFF", cursor="hand2")
account.pack(side=tk. RIGHT, padx=16)
account.config(bg="grey", fg="white")

petition_page = tk.Frame(root, bg="lavender")
petition_page.config(bg="lavender")

API_URL = os.getenv(
    "YOUTHLINK_API_URL",
    "https://youthlink.onrender.com",
).rstrip("/")


def current_username():
    username = username_entry.get().strip()
    if not username:
        showerror("Username Required", "Enter or sign up with a username first.")
        return None
    return username


def api_error(title, response=None, exception=None):
    if exception is not None:
        showerror(title, f"Could not connect to the backend.\n\n{exception}")
        return

    try:
        detail = response.json().get("detail", response.text)
    except Exception:
        detail = response.text
    showerror(title, f"{detail}\n\nStatus: {response.status_code}")


def load_petitions():
    for widget in petition_list.winfo_children():
        widget.destroy()

    try:
        response = requests.get(f"{API_URL}/petitions", timeout=5)
    except requests.RequestException as exc:
        api_error("Petition Error", exception=exc)
        return

    if response.status_code != 200:
        api_error("Petition Error", response=response)
        return

    for petition_data in response.json():
        create_petition_box(petition_data)


def create_petition_box(petition_data):
    petition_id = petition_data["id"]
    author = petition_data.get("username", "Unknown")
    title = petition_data.get("title", "Untitled Petition")
    text = petition_data.get("text", "")

    petition_frame = tk.Frame(
        petition_list,
        bg="white",
        bd=1,
        relief="solid"
    )
    petition_frame.pack(fill="x", padx=16, pady=10)

    author_label = tk.Label(
        petition_frame,
        text=f"Started by {author}",
        bg="white",
        fg="#64748B",
        font=("Arial", 9, "italic"),
        anchor="w"
    )
    author_label.pack(fill="x", padx=12, pady=(10, 2))

    petition_title_label = tk.Label(
        petition_frame,
        text=title,
        bg="white",
        fg="#111827",
        justify="left",
        anchor="w",
        wraplength=330,
        font=("Arial", 14, "bold")
    )
    petition_title_label.pack(fill="x", padx=12, pady=(4, 4))

    petition_label = tk.Label(
        petition_frame,
        text=text,
        bg="white",
        fg="#111827",
        justify="left",
        anchor="w",
        wraplength=330,
        font=("Arial", 12)
    )
    petition_label.pack(fill="x", padx=12, pady=(2, 10))

    stats_label = tk.Label(
        petition_frame,
        text="Loading feedback...",
        bg="white",
        fg="#334155",
        font=("Arial", 10, "bold")
    )
    stats_label.pack(anchor="w", padx=12, pady=(0, 6))

    action_frame = tk.Frame(petition_frame, bg="white")
    action_frame.pack(fill="x", padx=10, pady=(0, 8))

    comments_frame = tk.Frame(petition_frame, bg="#F8FAFC")
    comments_visible = False

    def refresh_status():
        username = username_entry.get().strip()
        params = {"username": username} if username else {}

        try:
            response = requests.get(
                f"{API_URL}/petitions/{petition_id}/status",
                params=params,
                timeout=5
            )
        except requests.RequestException:
            stats_label.config(text="Feedback unavailable")
            return

        if response.status_code != 200:
            stats_label.config(text="Feedback unavailable")
            return

        status_data = response.json()
        stats_label.config(
            text=(
                f"👍 {status_data['thumbs_up']}    "
                f"👎 {status_data['thumbs_down']}    "
                f"✍ {status_data['signature_count']} signed"
            )
        )

        user_vote = status_data.get("user_vote")
        up_button.config(relief="sunken" if user_vote == 1 else "raised")
        down_button.config(relief="sunken" if user_vote == -1 else "raised")

        signed = status_data.get("user_signed", False)
        sign_button.config(state="disabled" if signed else "normal")
        withdraw_button.config(state="normal" if signed else "disabled")

    def vote(value):
        username = current_username()
        if not username:
            return

        try:
            response = requests.put(
                f"{API_URL}/petitions/{petition_id}/vote",
                json={"username": username, "value": value},
                timeout=5
            )
        except requests.RequestException as exc:
            api_error("Vote Error", exception=exc)
            return

        if response.status_code == 200:
            refresh_status()
        else:
            api_error("Vote Error", response=response)

    def sign_petition():
        username = current_username()
        if not username:
            return

        try:
            response = requests.post(
                f"{API_URL}/petitions/{petition_id}/signatures",
                json={"username": username},
                timeout=5
            )
        except requests.RequestException as exc:
            api_error("Signature Error", exception=exc)
            return

        if response.status_code in (200, 201):
            refresh_status()
            showinfo("Petition Signed", "Your signature was added.")
        else:
            api_error("Signature Error", response=response)

    def withdraw_signature():
        username = current_username()
        if not username:
            return

        try:
            response = requests.delete(
                f"{API_URL}/petitions/{petition_id}/signatures/{username}",
                timeout=5
            )
        except requests.RequestException as exc:
            api_error("Withdrawal Error", exception=exc)
            return

        if response.status_code == 200:
            refresh_status()
            showinfo("Signature Withdrawn", "Your signature was removed.")
        else:
            api_error("Withdrawal Error", response=response)

    up_button = tk.Button(
        action_frame,
        text="👍",
        command=lambda: vote(1),
        font=("Arial", 13),
        bg="#DCFCE7",
        cursor="hand2"
    )
    up_button.pack(side="left", padx=3)

    down_button = tk.Button(
        action_frame,
        text="👎",
        command=lambda: vote(-1),
        font=("Arial", 13),
        bg="#FEE2E2",
        cursor="hand2"
    )
    down_button.pack(side="left", padx=3)

    sign_button = tk.Button(
        action_frame,
        text="Sign",
        command=sign_petition,
        bg="#22C55E",
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2"
    )
    sign_button.pack(side="left", padx=(12, 3))

    withdraw_button = tk.Button(
        action_frame,
        text="Withdraw",
        command=withdraw_signature,
        bg="#F59E0B",
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2"
    )
    withdraw_button.pack(side="left", padx=3)

    def load_comments():
        for widget in comments_frame.winfo_children():
            widget.destroy()

        try:
            response = requests.get(
                f"{API_URL}/petitions/{petition_id}/comments",
                timeout=5
            )
        except requests.RequestException as exc:
            tk.Label(
                comments_frame,
                text=f"Comments unavailable: {exc}",
                bg="#F8FAFC",
                fg="red",
                wraplength=315
            ).pack(fill="x", padx=8, pady=6)
            return

        if response.status_code != 200:
            tk.Label(
                comments_frame,
                text="Comments could not be loaded.",
                bg="#F8FAFC",
                fg="red"
            ).pack(fill="x", padx=8, pady=6)
            return

        comments = response.json()
        if not comments:
            tk.Label(
                comments_frame,
                text="No comments yet.",
                bg="#F8FAFC",
                fg="#64748B"
            ).pack(fill="x", padx=8, pady=6)

        for comment in comments:
            tk.Label(
                comments_frame,
                text=f"{comment['username']}: {comment['comment']}",
                bg="#F8FAFC",
                anchor="w",
                justify="left",
                wraplength=315
            ).pack(fill="x", padx=8, pady=3)

    comment_row = tk.Frame(petition_frame, bg="white")
    comment_row.pack(fill="x", padx=10, pady=(0, 8))

    comment_entry = tk.Entry(comment_row, font=("Arial", 11))
    comment_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

    def add_comment():
        username = current_username()
        comment = comment_entry.get().strip()
        if not username or not comment:
            return

        try:
            response = requests.post(
                f"{API_URL}/petitions/{petition_id}/comments",
                json={"username": username, "comment": comment},
                timeout=5
            )
        except requests.RequestException as exc:
            api_error("Comment Error", exception=exc)
            return

        if response.status_code in (200, 201):
            comment_entry.delete(0, tk.END)
            if not comments_frame.winfo_ismapped():
                comments_frame.pack(fill="x", padx=10, pady=(0, 8))
            load_comments()
        else:
            api_error("Comment Error", response=response)

    tk.Button(
        comment_row,
        text="Comment",
        command=add_comment,
        bg="#E2E8F0"
    ).pack(side="right")

    def toggle_comments():
        nonlocal comments_visible
        if comments_visible:
            comments_frame.pack_forget()
            comments_button.config(text="Show Comments")
        else:
            comments_frame.pack(fill="x", padx=10, pady=(0, 8))
            load_comments()
            comments_button.config(text="Hide Comments")
        comments_visible = not comments_visible

    footer = tk.Frame(petition_frame, bg="white")
    footer.pack(fill="x", padx=10, pady=(0, 10))

    comments_button = tk.Button(
        footer,
        text="Show Comments",
        command=toggle_comments,
        bg="#E2E8F0"
    )
    comments_button.pack(side="left")

    tk.Button(
        footer,
        text="🗑",
        bg="#DC2626",
        fg="white",
        command=lambda: delete_petition(petition_id, petition_frame)
    ).pack(side="right")

    refresh_status()


def delete_petition(petition_id, petition_frame):
    try:
        response = requests.delete(f"{API_URL}/petitions/{petition_id}", timeout=5)
    except requests.RequestException as exc:
        api_error("Delete Error", exception=exc)
        return

    if response.status_code == 200:
        petition_frame.destroy()
    else:
        api_error("Delete Error", response=response)


def go_to_petition_page():
    hide_all_pages()
    petition_page.pack(fill="both", expand=True)
    petition_page.config(bg="lavender")
    title_label.config(text="Petition Page")
    load_petitions()
    diss_threads.pack(side=tk.LEFT, padx=0)
    diss_threads.config(bg="#FFFFFF", fg="red")
    oppor_scholar.pack(side=tk.LEFT, padx=16)
    account.pack(side=tk.LEFT, padx=16)
    account.config(bg="#FFFFFF", fg="black")
    petition.pack(side=tk.LEFT, padx=16)
    petition.config(bg="grey", fg="white")
    oppor_scholar.config(bg="#FFFFFF", fg="Blue")


def save_petition(event=None):
    title = petition_title_entry.get().strip()
    text = petition_text_area.get("1.0", tk.END).strip()
    username = current_username()

    if not username:
        return

    if not title:
        showwarning("Missing Title", "Enter a title for the petition.")
        petition_title_entry.focus_set()
        return

    if not text:
        showwarning("Missing Description", "Enter a description for the petition.")
        petition_text_area.focus_set()
        return

    try:
        response = requests.post(
            f"{API_URL}/petitions",
            json={
                "username": username,
                "title": title,
                "text": text
            },
            timeout=5
        )
    except requests.RequestException as exc:
        api_error("Petition Error", exception=exc)
        return

    if response.status_code in (200, 201):
        petition_window.destroy()
        load_petitions()
    else:
        api_error("Petition Error", response=response)


def open_blank_document():
    global petition_title_entry, petition_text_area, petition_window

    petition_window = tk.Toplevel(root)
    petition_window.title("Create Petition")
    petition_window.geometry("430x560")
    petition_window.minsize(380, 500)
    petition_window.configure(bg="white")
    petition_window.transient(root)
    petition_window.grab_set()

    tk.Label(
        petition_window,
        text="Create a New Petition",
        bg="white",
        fg="#111827",
        font=("Arial", 16, "bold")
    ).pack(anchor="w", padx=20, pady=(18, 12))

    tk.Label(
        petition_window,
        text="Petition Title",
        bg="white",
        fg="#111827",
        font=("Arial", 11, "bold")
    ).pack(anchor="w", padx=20, pady=(0, 5))

    petition_title_entry = tk.Entry(
        petition_window,
        font=("Arial", 13),
        bd=1,
        relief="solid"
    )
    petition_title_entry.pack(fill="x", padx=20, pady=(0, 15))
    petition_title_entry.focus_set()

    tk.Label(
        petition_window,
        text="Petition Description",
        bg="white",
        fg="#111827",
        font=("Arial", 11, "bold")
    ).pack(anchor="w", padx=20, pady=(0, 5))

    petition_text_area = tk.Text(
        petition_window,
        wrap="word",
        font=("Arial", 12),
        height=14,
        bd=1,
        relief="solid"
    )
    petition_text_area.pack(expand=True, fill="both", padx=20, pady=(0, 15))
    petition_text_area.bind("<Control-Return>", save_petition)

    tk.Button(
        petition_window,
        text="Publish Petition",
        command=save_petition,
        bg="#22C55E",
        fg="white",
        font=("Arial", 12, "bold"),
        bd=0,
        cursor="hand2"
    ).pack(fill="x", padx=20, pady=(0, 20))


# =========================
# PETITION SCROLL AREA
# =========================
petition_container = tk.Frame(petition_page, bg="lavender")
petition_container.pack(fill="both", expand=True)

petition_canvas = tk.Canvas(
    petition_container,
    bg="lavender",
    highlightthickness=0
)
petition_canvas.pack(side=tk.LEFT, fill="both", expand=True)

petition_scrollbar = tk.Scrollbar(
    petition_container,
    orient="vertical",
    command=petition_canvas.yview
)
petition_scrollbar.pack(side=tk.RIGHT, fill="y")
petition_canvas.configure(yscrollcommand=petition_scrollbar.set)

petition_list = tk.Frame(petition_canvas, bg="lavender")
petition_canvas_window = petition_canvas.create_window(
    (0, 0),
    window=petition_list,
    anchor="nw"
)


def update_petition_scroll(event=None):
    petition_canvas.configure(scrollregion=petition_canvas.bbox("all"))


def resize_petition_list(event):
    petition_canvas.itemconfigure(petition_canvas_window, width=event.width)


petition_list.bind("<Configure>", update_petition_scroll)
petition_canvas.bind("<Configure>", resize_petition_list)


def petition_mousewheel(event):
    if petition_page.winfo_ismapped():
        petition_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


petition_canvas.bind_all("<MouseWheel>", petition_mousewheel)

petition_add_button = tk.Button(
    petition_page,
    command=open_blank_document,
    text="✚",
    bg="lightgreen",
    fg="black",
    bd=0,
    font=("Arial", 20),
    cursor="hand2"
)
petition_add_button.pack(pady=10)

petition = tk.Button(bottom_frame, text="📋", command=go_to_petition_page, font=("Arial", 25), bg="#FFFFFF", fg="#0CF089", bd=0, activebackground="#FFFFFF", cursor="hand2")
petition.pack(side=tk. RIGHT, padx=16)

def api_username():
    """Return the signed-in username or a safe fallback."""
    username = username_entry.get().strip()
    return username if username else "Anonymous"


def safe_request(method, url, **kwargs):
    """Send an API request and show a useful error if FastAPI is unavailable."""
    try:
        return requests.request(method, url, timeout=5, **kwargs)
    except requests.RequestException as error:
        showerror(
            "Server Error",
            "Could not connect to the FastAPI server at "
            "https://youthlink.onrender.com.\n\n"
            f"Details: {error}"
        )
        return None


def go_to_diss_threads_page():
    hide_all_pages()
    diss_threads_page.pack(fill="both", expand=True)
    diss_threads_page.config(bg="white")
    title_label.config(text="Discussion Threads")

    oppor_scholar.pack(side=tk.LEFT, padx=0)
    oppor_scholar.config(bg="#FFFFFF", fg="blue")
    petition.pack(side=tk.LEFT, padx=16)
    petition.config(bg="#FFFFFF", fg="green")
    account.pack(side=tk.LEFT, padx=16)
    account.config(bg="#FFFFFF", fg="black")
    diss_threads.pack(side=tk.LEFT, padx=16)
    diss_threads.config(bg="grey", fg="white")

    load_threads()


diss_threads_page = tk.Frame(root, bg="white")

searchframe = tk.Frame(diss_threads_page, bg="white")
searchframe.pack(fill=tk.X, padx=10, pady=10)

searchbox = tk.Entry(
    searchframe,
    font=("Arial", 16),
    bg="white"
)
searchbox.pack(side=tk.LEFT, fill=tk.X, expand=True)


def search_threads():
    load_threads(searchbox.get().strip())


search_button = tk.Button(
    searchframe,
    text="🔍",
    command=search_threads,
    bg="grey",
    fg="white"
)
search_button.pack(side=tk.LEFT, padx=5)
searchbox.bind("<Return>", lambda event: search_threads())

thread_container = tk.Frame(diss_threads_page, bg="white")
thread_container.pack(fill="both", expand=True)

thread_canvas = tk.Canvas(
    thread_container,
    bg="white",
    highlightthickness=0
)
thread_canvas.pack(side=tk.LEFT, fill="both", expand=True)

thread_scrollbar = tk.Scrollbar(
    thread_container,
    orient="vertical",
    command=thread_canvas.yview
)
thread_scrollbar.pack(side=tk.RIGHT, fill="y")
thread_canvas.configure(yscrollcommand=thread_scrollbar.set)

thread_list = tk.Frame(thread_canvas, bg="white")
thread_canvas_window = thread_canvas.create_window(
    (0, 0),
    window=thread_list,
    anchor="nw"
)


def resize_thread_list(event):
    thread_canvas.itemconfigure(thread_canvas_window, width=event.width)


thread_canvas.bind("<Configure>", resize_thread_list)
thread_list.bind(
    "<Configure>",
    lambda event: thread_canvas.configure(
        scrollregion=thread_canvas.bbox("all")
    )
)


def thread_mousewheel(event):
    thread_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


thread_canvas.bind_all("<MouseWheel>", thread_mousewheel)


def load_threads(search_text=""):
    """Load all discussion posts from FastAPI and draw them on the page."""
    for widget in thread_list.winfo_children():
        widget.destroy()

    response = safe_request("GET", f"{API_URL}/threads")
    if response is None:
        return

    if response.status_code != 200:
        showerror(
            "Discussion Error",
            f"Could not load discussion posts: {response.status_code}\n{response.text}"
        )
        return

    try:
        threads = response.json()
    except ValueError:
        showerror("Discussion Error", "The server returned invalid JSON.")
        return

    search_text = search_text.lower()
    visible_threads = []

    for thread in threads:
        title = str(thread.get("title", ""))
        text = str(thread.get("text", ""))
        username = str(thread.get("username", "Anonymous"))

        if search_text and search_text not in f"{title} {text} {username}".lower():
            continue

        visible_threads.append(thread)

    if not visible_threads:
        tk.Label(
            thread_list,
            text="No discussion posts found.",
            bg="white",
            fg="#64748B",
            font=("Arial", 12)
        ).pack(pady=30)
        return

    for thread in visible_threads:
        create_thread_box(
            thread_id=thread["id"],
            title=thread.get("title", "Untitled Discussion"),
            text=thread.get("text", ""),
            username=thread.get("username", "Anonymous")
        )


def create_thread_box(thread_id, title, text, username):
    post_frame = tk.Frame(
        thread_list,
        bg="white",
        bd=1,
        relief="solid"
    )
    post_frame.pack(fill="x", padx=15, pady=10)

    post_header = tk.Frame(post_frame, bg="#E0F2FE")
    post_header.pack(fill="x")

    tk.Label(
        post_header,
        text=title,
        bg="#E0F2FE",
        fg="#0F172A",
        font=("Arial", 13, "bold"),
        anchor="w",
        wraplength=290
    ).pack(side=tk.LEFT, fill="x", expand=True, padx=10, pady=(8, 2))

    tk.Label(
        post_frame,
        text=f"Posted by {username}",
        bg="white",
        fg="#64748B",
        font=("Arial", 9),
        anchor="w"
    ).pack(fill="x", padx=10, pady=(6, 0))

    post_text = tk.Label(
        post_frame,
        text=text,
        bg="white",
        fg="#1E293B",
        font=("Arial", 11),
        justify="left",
        anchor="w",
        wraplength=330,
        cursor="hand2"
    )
    post_text.pack(fill="x", padx=10, pady=10)

    actions_frame = tk.Frame(post_frame, bg="white")
    actions_frame.pack(fill="x", padx=10, pady=(0, 8))

    comments_frame = tk.Frame(post_frame, bg="#F8FAFC")

    comment_entry = tk.Entry(
        comments_frame,
        font=("Arial", 11)
    )

    comments_list = tk.Frame(comments_frame, bg="#F8FAFC")

    def load_thread_comments():
        for widget in comments_list.winfo_children():
            widget.destroy()

        response = safe_request(
            "GET",
            f"{API_URL}/threads/{thread_id}/comments"
        )
        if response is None:
            return

        if response.status_code != 200:
            showerror(
                "Comment Error",
                f"Could not load comments: {response.status_code}"
            )
            return

        comments = response.json()

        if not comments:
            tk.Label(
                comments_list,
                text="No comments yet.",
                bg="#F8FAFC",
                fg="#64748B",
                anchor="w"
            ).pack(fill="x", padx=8, pady=5)

        for comment in comments:
            tk.Label(
                comments_list,
                text=f"{comment.get('username', 'Anonymous')}: "
                     f"{comment.get('comment', '')}",
                bg="#F8FAFC",
                fg="#1E293B",
                justify="left",
                anchor="w",
                wraplength=310
            ).pack(fill="x", padx=8, pady=4)

    def add_thread_comment(event=None):
        comment = comment_entry.get().strip()
        if not comment:
            showwarning("Missing Comment", "Enter a comment first.")
            return

        response = safe_request(
            "POST",
            f"{API_URL}/threads/{thread_id}/comments",
            json={
                "username": api_username(),
                "comment": comment
            }
        )
        if response is None:
            return

        if response.status_code in (200, 201):
            comment_entry.delete(0, tk.END)
            load_thread_comments()
        else:
            showerror(
                "Comment Error",
                f"Could not add comment: {response.status_code}\n{response.text}"
            )

    comment_entry.pack(fill="x", padx=8, pady=(8, 4))
    comment_entry.bind("<Return>", add_thread_comment)

    tk.Button(
        comments_frame,
        text="Post Comment",
        command=add_thread_comment,
        bg="#0284C7",
        fg="white",
        bd=0,
        cursor="hand2"
    ).pack(anchor="e", padx=8, pady=(0, 8))

    comments_list.pack(fill="x", padx=4, pady=(0, 6))

    expanded = False

    def toggle_comments(event=None):
        nonlocal expanded
        if expanded:
            comments_frame.pack_forget()
            comments_button.config(text="Show Comments")
        else:
            comments_frame.pack(fill="x", padx=10, pady=(0, 10))
            load_thread_comments()
            comments_button.config(text="Hide Comments")
        expanded = not expanded

    def delete_thread():
        if not messagebox.askyesno(
            "Delete Discussion",
            "Are you sure you want to delete this discussion post?"
        ):
            return

        response = safe_request(
            "DELETE",
            f"{API_URL}/threads/{thread_id}"
        )
        if response is None:
            return

        if response.status_code in (200, 204):
            post_frame.destroy()
        else:
            showerror(
                "Delete Error",
                f"Could not delete discussion: {response.status_code}\n{response.text}"
            )

    comments_button = tk.Button(
        actions_frame,
        text="Show Comments",
        command=toggle_comments,
        bg="#E2E8F0",
        fg="#0F172A",
        bd=0,
        cursor="hand2"
    )
    comments_button.pack(side=tk.LEFT)

    tk.Button(
        actions_frame,
        text="Delete",
        command=delete_thread,
        bg="#DC2626",
        fg="white",
        bd=0,
        cursor="hand2"
    ).pack(side=tk.RIGHT)

    post_text.bind("<Button-1>", toggle_comments)


def open_new_thread_window():
    """Open a small editor when the blue plus button is pressed."""
    window = tk.Toplevel(root)
    window.title("Create Discussion Post")
    window.geometry("400x500")
    window.configure(bg="white")
    window.transient(root)
    window.grab_set()

    tk.Label(
        window,
        text="Discussion title",
        bg="white",
        font=("Arial", 11, "bold")
    ).pack(anchor="w", padx=20, pady=(20, 5))

    title_entry = tk.Entry(window, font=("Arial", 13))
    title_entry.pack(fill="x", padx=20)
    title_entry.focus_set()

    tk.Label(
        window,
        text="What would you like to discuss?",
        bg="white",
        font=("Arial", 11, "bold")
    ).pack(anchor="w", padx=20, pady=(20, 5))

    post_editor = tk.Text(
        window,
        wrap="word",
        font=("Arial", 12),
        height=14
    )
    post_editor.pack(fill="both", expand=True, padx=20, pady=(0, 15))

    def save_thread(event=None):
        title = title_entry.get().strip()
        text = post_editor.get("1.0", tk.END).strip()

        if not title or not text:
            showwarning(
                "Missing Information",
                "Enter both a title and discussion text."
            )
            return

        response = safe_request(
            "POST",
            f"{API_URL}/threads",
            json={
                "username": api_username(),
                "title": title,
                "text": text
            }
        )
        if response is None:
            return

        if response.status_code in (200, 201):
            window.destroy()
            load_threads()
        else:
            showerror(
                "Discussion Error",
                f"Could not create the post: {response.status_code}\n{response.text}"
            )

    tk.Button(
        window,
        text="Publish Discussion",
        command=save_thread,
        bg="#38BDF8",
        fg="#0F172A",
        font=("Arial", 12, "bold"),
        bd=0,
        cursor="hand2"
    ).pack(fill="x", padx=20, pady=(0, 20))

    window.bind("<Control-Return>", save_thread)


thread_add_button = tk.Button(
    diss_threads_page,
    text="✚",
    command=open_new_thread_window,
    bg="lightblue",
    fg="black",
    font=("Arial", 20),
    bd=0,
    cursor="hand2"
)
thread_add_button.pack(pady=10)


diss_threads = tk.Button(
    bottom_frame,
    text="🗨️",
    command=go_to_diss_threads_page,
    font=("Arial", 25),
    bg="#FFFFFF",
    fg="#044FEF",
    bd=0,
    activebackground="#FFFFFF",
    cursor="hand2"
)
diss_threads.pack(side=tk.LEFT, padx=16)


def go_to_oppor_scholar_page():
    hide_all_pages()
    oppor_scholar_page.pack(fill="both", expand=True)
    title_label.config(text="Opportunities Page")

    diss_threads.pack(side=tk.LEFT, padx=0)
    diss_threads.config(bg="#FFFFFF", fg="red")
    petition.pack(side=tk.LEFT, padx=16)
    petition.config(bg="#FFFFFF", fg="green")
    account.pack(side=tk.LEFT, padx=16)
    account.config(bg="#FFFFFF", fg="black")
    oppor_scholar.pack(side=tk.LEFT, padx=16)
    oppor_scholar.config(bg="grey", fg="white")

    load_opportunities()


oppor_scholar_page = tk.Frame(root, bg="#EFF6FF")

opportunity_search_frame = tk.Frame(oppor_scholar_page, bg="#EFF6FF")
opportunity_search_frame.pack(fill="x", padx=10, pady=10)

opportunity_search_entry = tk.Entry(
    opportunity_search_frame,
    font=("Arial", 14)
)
opportunity_search_entry.pack(side="left", fill="x", expand=True)


def search_opportunities():
    load_opportunities(opportunity_search_entry.get().strip())


tk.Button(
    opportunity_search_frame,
    text="🔍",
    command=search_opportunities,
    bg="#64748B",
    fg="white"
).pack(side="left", padx=(5, 0))

opportunity_search_entry.bind(
    "<Return>",
    lambda event: search_opportunities()
)

opportunity_container = tk.Frame(oppor_scholar_page, bg="#EFF6FF")
opportunity_container.pack(fill="both", expand=True)

opportunity_canvas = tk.Canvas(
    opportunity_container,
    bg="#EFF6FF",
    highlightthickness=0
)
opportunity_canvas.pack(side="left", fill="both", expand=True)

opportunity_scrollbar = tk.Scrollbar(
    opportunity_container,
    orient="vertical",
    command=opportunity_canvas.yview
)
opportunity_scrollbar.pack(side="right", fill="y")
opportunity_canvas.configure(yscrollcommand=opportunity_scrollbar.set)

opportunity_list = tk.Frame(opportunity_canvas, bg="#EFF6FF")
opportunity_canvas_window = opportunity_canvas.create_window(
    (0, 0),
    window=opportunity_list,
    anchor="nw"
)


def resize_opportunity_list(event):
    opportunity_canvas.itemconfigure(
        opportunity_canvas_window,
        width=event.width
    )


opportunity_canvas.bind("<Configure>", resize_opportunity_list)
opportunity_list.bind(
    "<Configure>",
    lambda event: opportunity_canvas.configure(
        scrollregion=opportunity_canvas.bbox("all")
    )
)


def load_opportunities(search_text=""):
    for widget in opportunity_list.winfo_children():
        widget.destroy()

    response = safe_request("GET", f"{API_URL}/opportunities")
    if response is None:
        return

    if response.status_code != 200:
        showerror(
            "Opportunity Error",
            f"Could not load opportunities.\n{response.status_code}\n{response.text}"
        )
        return

    opportunities = response.json()
    search_text = search_text.lower()

    filtered = []
    for opportunity_data in opportunities:
        searchable = " ".join([
            str(opportunity_data.get("title", "")),
            str(opportunity_data.get("organization", "")),
            str(opportunity_data.get("text", "")),
            str(opportunity_data.get("deadline", "")),
        ]).lower()

        if search_text and search_text not in searchable:
            continue
        filtered.append(opportunity_data)

    if not filtered:
        tk.Label(
            opportunity_list,
            text="No opportunities found.",
            bg="#EFF6FF",
            fg="#64748B",
            font=("Arial", 12)
        ).pack(pady=30)
        return

    for opportunity_data in filtered:
        create_opportunity_box(opportunity_data)


def create_opportunity_box(opportunity_data):
    opportunity_id = opportunity_data["id"]

    card = tk.Frame(
        opportunity_list,
        bg="white",
        bd=1,
        relief="solid"
    )
    card.pack(fill="x", padx=15, pady=10)

    tk.Label(
        card,
        text=opportunity_data.get("title", "Untitled Opportunity"),
        bg="#DBEAFE",
        fg="#0F172A",
        font=("Arial", 14, "bold"),
        anchor="w",
        justify="left",
        wraplength=330
    ).pack(fill="x", padx=0, pady=0, ipady=8)

    tk.Label(
        card,
        text=f"Organization: {opportunity_data.get('organization', 'Unknown')}",
        bg="white",
        fg="#334155",
        font=("Arial", 10, "bold"),
        anchor="w"
    ).pack(fill="x", padx=10, pady=(8, 2))

    deadline = opportunity_data.get("deadline")
    if deadline:
        tk.Label(
            card,
            text=f"Deadline: {deadline}",
            bg="white",
            fg="#B45309",
            font=("Arial", 10, "bold"),
            anchor="w"
        ).pack(fill="x", padx=10, pady=2)

    tk.Label(
        card,
        text=opportunity_data.get("text", ""),
        bg="white",
        fg="#1E293B",
        font=("Arial", 11),
        anchor="w",
        justify="left",
        wraplength=330
    ).pack(fill="x", padx=10, pady=(6, 8))

    link = opportunity_data.get("link")
    if link:
        link_label = tk.Label(
            card,
            text=link,
            bg="white",
            fg="#2563EB",
            font=("Arial", 10, "underline"),
            anchor="w",
            cursor="hand2",
            wraplength=330
        )
        link_label.pack(fill="x", padx=10, pady=(0, 8))

        def open_link(event=None, url=link):
            import webbrowser
            webbrowser.open(url)

        link_label.bind("<Button-1>", open_link)

    tk.Label(
        card,
        text=f"Posted by {opportunity_data.get('username', 'Unknown')}",
        bg="white",
        fg="#64748B",
        font=("Arial", 9, "italic"),
        anchor="w"
    ).pack(fill="x", padx=10, pady=(0, 8))

    comment_row = tk.Frame(card, bg="white")
    comment_row.pack(fill="x", padx=10, pady=(0, 8))

    comment_entry = tk.Entry(comment_row, font=("Arial", 11))
    comment_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

    comments_frame = tk.Frame(card, bg="#F8FAFC")
    comments_visible = False

    def load_opportunity_comments():
        for widget in comments_frame.winfo_children():
            widget.destroy()

        response = safe_request(
            "GET",
            f"{API_URL}/opportunities/{opportunity_id}/comments"
        )
        if response is None:
            return

        if response.status_code != 200:
            tk.Label(
                comments_frame,
                text="Comments could not be loaded.",
                bg="#F8FAFC",
                fg="red"
            ).pack(fill="x", padx=8, pady=6)
            return

        comments = response.json()
        if not comments:
            tk.Label(
                comments_frame,
                text="No comments yet.",
                bg="#F8FAFC",
                fg="#64748B"
            ).pack(fill="x", padx=8, pady=6)

        for comment in comments:
            tk.Label(
                comments_frame,
                text=f"{comment.get('username', 'Anonymous')}: "
                     f"{comment.get('comment', '')}",
                bg="#F8FAFC",
                fg="#1E293B",
                anchor="w",
                justify="left",
                wraplength=315
            ).pack(fill="x", padx=8, pady=3)

    def add_opportunity_comment(event=None):
        username = current_username()
        comment = comment_entry.get().strip()

        if not username:
            return
        if not comment:
            showwarning("Missing Comment", "Enter a comment first.")
            return

        response = safe_request(
            "POST",
            f"{API_URL}/opportunities/{opportunity_id}/comments",
            json={
                "username": username,
                "comment": comment
            }
        )
        if response is None:
            return

        if response.status_code in (200, 201):
            comment_entry.delete(0, tk.END)
            if not comments_frame.winfo_ismapped():
                comments_frame.pack(fill="x", padx=10, pady=(0, 8))
            load_opportunity_comments()
        else:
            showerror(
                "Comment Error",
                f"Could not add comment.\n{response.status_code}\n{response.text}"
            )

    tk.Button(
        comment_row,
        text="Comment",
        command=add_opportunity_comment,
        bg="#DBEAFE"
    ).pack(side="right")

    comment_entry.bind("<Return>", add_opportunity_comment)

    footer = tk.Frame(card, bg="white")
    footer.pack(fill="x", padx=10, pady=(0, 10))

    def toggle_opportunity_comments():
        nonlocal comments_visible

        if comments_visible:
            comments_frame.pack_forget()
            comments_button.config(text="Show Comments")
        else:
            comments_frame.pack(fill="x", padx=10, pady=(0, 8))
            load_opportunity_comments()
            comments_button.config(text="Hide Comments")

        comments_visible = not comments_visible

    comments_button = tk.Button(
        footer,
        text="Show Comments",
        command=toggle_opportunity_comments,
        bg="#E2E8F0"
    )
    comments_button.pack(side="left")

    def delete_opportunity():
        if not messagebox.askyesno(
            "Delete Opportunity",
            "Are you sure you want to delete this opportunity?"
        ):
            return

        response = safe_request(
            "DELETE",
            f"{API_URL}/opportunities/{opportunity_id}"
        )
        if response is None:
            return

        if response.status_code in (200, 204):
            card.destroy()
        else:
            showerror(
                "Delete Error",
                f"Could not delete opportunity.\n{response.status_code}\n{response.text}"
            )

    tk.Button(
        footer,
        text="Delete",
        command=delete_opportunity,
        bg="#DC2626",
        fg="white"
    ).pack(side="right")


def open_new_opportunity_window():
    window = tk.Toplevel(root)
    window.title("Create Opportunity")
    window.geometry("440x650")
    window.minsize(400, 580)
    window.configure(bg="white")
    window.transient(root)
    window.grab_set()

    tk.Label(
        window,
        text="Create a New Opportunity",
        bg="white",
        font=("Arial", 16, "bold")
    ).pack(anchor="w", padx=20, pady=(18, 12))

    tk.Label(window, text="Title", bg="white", font=("Arial", 11, "bold")).pack(
        anchor="w", padx=20, pady=(0, 4)
    )
    title_entry = tk.Entry(window, font=("Arial", 12))
    title_entry.pack(fill="x", padx=20, pady=(0, 10))

    tk.Label(
        window,
        text="Organization",
        bg="white",
        font=("Arial", 11, "bold")
    ).pack(anchor="w", padx=20, pady=(0, 4))
    organization_entry = tk.Entry(window, font=("Arial", 12))
    organization_entry.pack(fill="x", padx=20, pady=(0, 10))

    tk.Label(
        window,
        text="Deadline (optional)",
        bg="white",
        font=("Arial", 11, "bold")
    ).pack(anchor="w", padx=20, pady=(0, 4))
    deadline_entry = tk.Entry(window, font=("Arial", 12))
    deadline_entry.pack(fill="x", padx=20, pady=(0, 10))

    tk.Label(
        window,
        text="Application Link (optional)",
        bg="white",
        font=("Arial", 11, "bold")
    ).pack(anchor="w", padx=20, pady=(0, 4))
    link_entry = tk.Entry(window, font=("Arial", 12))
    link_entry.pack(fill="x", padx=20, pady=(0, 10))

    tk.Label(
        window,
        text="Description",
        bg="white",
        font=("Arial", 11, "bold")
    ).pack(anchor="w", padx=20, pady=(0, 4))

    description_editor = tk.Text(
        window,
        wrap="word",
        font=("Arial", 12),
        height=12
    )
    description_editor.pack(fill="both", expand=True, padx=20, pady=(0, 12))

    def publish_opportunity(event=None):
        username = current_username()
        title = title_entry.get().strip()
        organization = organization_entry.get().strip()
        deadline = deadline_entry.get().strip()
        link = link_entry.get().strip()
        description = description_editor.get("1.0", tk.END).strip()

        if not username:
            return

        if not title or not organization or not description:
            showwarning(
                "Missing Information",
                "Title, organization, and description are required."
            )
            return

        if link and not link.startswith(("http://", "https://")):
            showwarning(
                "Invalid Link",
                "The application link must begin with http:// or https://"
            )
            return

        response = safe_request(
            "POST",
            f"{API_URL}/opportunities",
            json={
                "username": username,
                "title": title,
                "organization": organization,
                "deadline": deadline or None,
                "link": link or None,
                "text": description
            }
        )
        if response is None:
            return

        if response.status_code in (200, 201):
            window.destroy()
            load_opportunities()
        else:
            showerror(
                "Opportunity Error",
                f"Could not publish opportunity.\n"
                f"{response.status_code}\n{response.text}"
            )

    tk.Button(
        window,
        text="Publish Opportunity",
        command=publish_opportunity,
        bg="#3B82F6",
        fg="white",
        font=("Arial", 12, "bold"),
        bd=0
    ).pack(fill="x", padx=20, pady=(0, 18))

    window.bind("<Control-Return>", publish_opportunity)
    title_entry.focus_set()


opportunity_add_button = tk.Button(
    oppor_scholar_page,
    text="✚",
    command=open_new_opportunity_window,
    bg="#93C5FD",
    fg="black",
    bd=0,
    font=("Arial", 20),
    cursor="hand2"
)
opportunity_add_button.pack(pady=10)

oppor_scholar = tk.Button(
    bottom_frame,
    text="🌍",
    command=go_to_oppor_scholar_page,
    font=("Arial", 25),
    bg="#FFFFFF",
    fg="#541CEE",
    bd=0,
    activebackground="#FFFFFF",
    cursor="hand2"
)
oppor_scholar.pack(side=tk.RIGHT, padx=16)

for btn in [account, petition, oppor_scholar, diss_threads]:
    btn.pack_forget()

root.mainloop()