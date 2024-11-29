import tkinter as tk
import pygame

# Initialize pygame mixer for background music
pygame.mixer.init()

# Global variable to track if music is muted
is_muted = False

# Function to play background music
def play_music():
    global is_muted
    if not is_muted:
        try:
            pygame.mixer.music.load("retro_music.mp3")  # Ensure you have an MP3 file named retro_music.mp3
            pygame.mixer.music.play(-1, 0.0)  # Loop the music indefinitely
        except pygame.error as e:
            print("Error playing music:", e)

# Function to mute or unmute the background music
def toggle_mute():
    global is_muted
    is_muted = not is_muted
    if is_muted:
        pygame.mixer.music.stop()
        mute_button.config(text="Unmute Music", bg="#FF0000", fg="#FFFFFF")
    else:
        play_music()
        mute_button.config(text="Mute Music", bg="#00FF00", fg="#FFFFFF")

# Define distros by category
distros_by_category = {
    "Gaming": [
        {"name": "Pop!_OS", "description": "Optimized for gaming with hybrid graphics.", "release_date": "2017"},
        {"name": "SteamOS", "description": "Tailored for Steam gaming and Linux support.", "release_date": "2013"},
        {"name": "Ubuntu GamePack", "description": "Gaming-focused Ubuntu with preinstalled software.", "release_date": "2018"},
        {"name": "Solus", "description": "A rolling release focused on gaming and usability.", "release_date": "2015"},
        {"name": "Lakka", "description": "A lightweight distro for retro gaming.", "release_date": "2014"},
        {"name": "RetroPie", "description": "Focused on retro gaming and emulation.", "release_date": "2014"},
        {"name": "Game Drift Linux", "description": "Optimized for gaming and streaming.", "release_date": "2018"},
        {"name": "SteamOS 3", "description": "Latest version for Steam Deck and gaming.", "release_date": "2021"},
        {"name": "Manjaro Gaming Edition", "description": "Manjaro optimized for gaming.", "release_date": "2015"},
        {"name": "Garuda Linux Gaming", "description": "Garuda Linux with a gaming focus.", "release_date": "2020"},
    ],
    "Security": [
        {"name": "Kali Linux", "description": "A distribution for penetration testing.", "release_date": "2013"},
        {"name": "Parrot Security OS", "description": "Security and forensics focused OS.", "release_date": "2013"},
        {"name": "BlackArch", "description": "Arch-based distribution for security researchers.", "release_date": "2013"},
        {"name": "Tails", "description": "Focused on privacy and anonymity.", "release_date": "2009"},
        {"name": "Qubes OS", "description": "Security-focused OS that isolates apps in virtual machines.", "release_date": "2012"},
        {"name": "Pentoo", "description": "Security-focused Gentoo-based distro.", "release_date": "2006"},
        {"name": "Whonix", "description": "Focuses on anonymity using Tor.", "release_date": "2012"},
        {"name": "Subgraph OS", "description": "A privacy-focused operating system.", "release_date": "2015"},
        {"name": "Blackbuntu", "description": "A security-focused Ubuntu derivative.", "release_date": "2009"},
    ],
    "General Use": [
        {"name": "Ubuntu", "description": "User-friendly with wide community support.", "release_date": "2004"},
        {"name": "Fedora", "description": "Cutting-edge open-source software and features.", "release_date": "2003"},
        {"name": "Debian", "description": "Stable and reliable, used as a base for many distributions.", "release_date": "1993"},
        {"name": "Arch Linux", "description": "Rolling release for advanced users.", "release_date": "2002"},
        {"name": "Manjaro", "description": "User-friendly distribution based on Arch.", "release_date": "2011"},
        {"name": "Zorin OS", "description": "Designed to make Linux easy for beginners.", "release_date": "2009"},
        {"name": "MX Linux", "description": "A fast and efficient distribution for general use.", "release_date": "2014"},
        {"name": "Linux Mint", "description": "A beginner-friendly distribution based on Ubuntu.", "release_date": "2006"},
        {"name": "Solus", "description": "A rolling release distribution focused on desktop usability.", "release_date": "2015"},
        {"name": "EndeavourOS", "description": "An Arch-based distribution with a user-friendly approach.", "release_date": "2019"},
        {"name": "Pop!_OS", "description": "Ubuntu-based with a focus on developer and gamer tools.", "release_date": "2017"},
    ],
    "Privacy and Security": [
        {"name": "Tails", "description": "Focused on privacy and anonymity.", "release_date": "2009"},
        {"name": "Whonix", "description": "Focuses on anonymity using Tor.", "release_date": "2012"},
        {"name": "Subgraph OS", "description": "A privacy-focused operating system.", "release_date": "2015"},
        {"name": "Qubes OS", "description": "Security-focused OS that isolates apps in virtual machines.", "release_date": "2012"},
        {"name": "Tinfoil OS", "description": "A lightweight privacy-focused OS.", "release_date": "2020"},
    ],
    "Multimedia": [
        {"name": "Ubuntu Studio", "description": "Linux for creative professionals, focused on audio and video editing.", "release_date": "2007"},
        {"name": "Kdenlive", "description": "A video editing software with support for professional workflows.", "release_date": "2003"},
        {"name": "AV Linux", "description": "Multimedia and video editing focused Linux.", "release_date": "2007"},
        {"name": "Lightworks", "description": "Professional video editing software.", "release_date": "2011"},
        {"name": "Puppy Linux Multimedia", "description": "Lightweight Linux for multimedia tasks.", "release_date": "2003"},
    ],
    "Education": [
        {"name": "Edubuntu", "description": "An Ubuntu derivative aimed at education.", "release_date": "2005"},
        {"name": "DoudouLinux", "description": "Aimed at children and educational environments.", "release_date": "2011"},
        {"name": "Sugar on a Stick", "description": "A lightweight OS designed for children’s learning.", "release_date": "2007"},
        {"name": "Kali Linux", "description": "A distribution for security and forensics, also used for education.", "release_date": "2013"},
        {"name": "School Linux", "description": "An education-focused operating system.", "release_date": "2004"},
    ],
    # Adding more categories and distros would go here...
}

# Function to display distros in a selected category
def show_distros(category):
    for widget in main_frame.winfo_children():
        widget.destroy()
    home_button = tk.Button(main_frame, text="Home", font=("Press Start 2P", 16), command=show_home, fg="#FF00FF", bg="#000000", relief="flat")
    home_button.pack(pady=10)

    distros = distros_by_category.get(category, [])
    for distro in distros:
        label = tk.Label(main_frame, text=f"{distro['name']} - {distro['description']}", font=("Press Start 2P", 12), fg="#00FF00", bg="#000000", justify="left")
        label.pack(pady=10)

    # Create retro background and pixel effect
    create_pixel_gradient()

# Function to show the home menu
def show_home():
    for widget in main_frame.winfo_children():
        widget.destroy()

    title_label = tk.Label(main_frame, text="Linux Distro Encyclopedia", font=("Press Start 2P", 24, "bold"), fg="#FF00FF", bg="#000000")
    title_label.pack(pady=20)

    categories = list(distros_by_category.keys())
    for category in categories:
        button = tk.Button(main_frame, text=category, font=("Press Start 2P", 14), command=lambda c=category: show_distros(c), fg="#00FF00", bg="#000000", relief="flat")
        button.pack(pady=10, fill="x")

    # Create retro background and pixel effect
    create_pixel_gradient()

# Function to create a pixelated gradient effect
def create_pixel_gradient():
    for widget in main_frame.winfo_children():
        widget.configure(bg="#000000")  # Set background color to black for pixel effect

# Setup main window
root = tk.Tk()
root.title("Linux Distro Encyclopedia")
root.geometry("600x600")
root.config(bg="#000000")

# Create a frame for the content
main_frame = tk.Frame(root, bg="#000000")
main_frame.pack(fill="both", expand=True)

# Play background music
play_music()

# Mute button
mute_button = tk.Button(root, text="Mute Music", font=("Press Start 2P", 16), command=toggle_mute, bg="#00FF00", fg="#FFFFFF", relief="flat")
mute_button.pack(pady=20)



import webbrowser

# Function to open URLs in the web browser
def open_url(url):
    webbrowser.open(url)

# Function to show the credits
def show_credits():
    for widget in main_frame.winfo_children():
        widget.destroy()

    credits_label = tk.Label(main_frame, text="Credits", font=("Press Start 2P", 24, "bold"), fg="#FF00FF", bg="#000000")
    credits_label.pack(pady=20)

    # Create a Text widget to show credits with clickable links
    credits_text = tk.Text(main_frame, font=("Press Start 2P", 12), fg="#00FF00", bg="#000000", wrap="word", height=10, width=50)
    credits_text.pack(pady=10)

    credits_content = """
    Developed by: MetroTM (https://github.com/MetroTopia)
    Music by: [Artist Name]

    Copy and paste the links into your web browser!
    """

    credits_text.insert(tk.END, credits_content)

    # Make the link clickable
    credits_text.tag_configure("hyperlink", foreground="blue", underline=True)
    credits_text.tag_add("hyperlink", "21.0", "42.0")  # For the GitHub link
    credits_text.tag_bind("hyperlink", "<Button-1>", lambda e: open_url("https://github.com/MetroTopia"))

    credits_text.config(state=tk.DISABLED)  # Make text widget read-only

    back_button = tk.Button(main_frame, text="Back", font=("Press Start 2P", 16), command=show_home, fg="#FF00FF", bg="#000000", relief="flat")
    back_button.pack(pady=10)

    # Create retro background and pixel effect
    create_pixel_gradient()


    # Create retro background and pixel effect
    create_pixel_gradient()

# Update the home screen to include a Credits button
def show_home():
    for widget in main_frame.winfo_children():
        widget.destroy()

    title_label = tk.Label(main_frame, text="Linux Distro Encyclopedia", font=("Press Start 2P", 24, "bold"), fg="#FF00FF", bg="#000000")
    title_label.pack(pady=20)

    categories = list(distros_by_category.keys())
    for category in categories:
        button = tk.Button(main_frame, text=category, font=("Press Start 2P", 14), command=lambda c=category: show_distros(c), fg="#00FF00", bg="#000000", relief="flat")
        button.pack(pady=10, fill="x")

    # Add Credits button
    credits_button = tk.Button(main_frame, text="Credits", font=("Press Start 2P", 14), command=show_credits, fg="#00FF00", bg="#000000", relief="flat")
    credits_button.pack(pady=10, fill="x")

    # Create retro background and pixel effect
    create_pixel_gradient()




# Show the home screen
show_home()

# Run the application
root.mainloop()
