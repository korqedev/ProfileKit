# ProfileKit

A modern, reusable Python user profile system built with CustomTkinter and SQLite.

ProfileKit provides an easy way to create, manage, and display user profiles in desktop applications, featuring profile pictures, bios, status messages, and persistent storage.

Made by @korqedev

---

## Features

* Create user profiles
* Load saved profiles
* Edit profile information
* Delete profiles
* Profile pictures (avatars)
* User bios
* Status messages
* SQLite database storage
* Modern CustomTkinter GUI
* Reusable architecture for other projects

---

## Project Structure

```text
ProfileKit/
├── profilekit/
│   ├── __init__.py
│   ├── database.py
│   ├── profile.py
│   ├── avatar.py
│   └── gui.py
├── examples/
│   └── demo_app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install customtkinter pillow
```

---

## Running the Demo

```bash
python examples/demo_app.py
```

---

## Example Usage

```python
from profilekit import ProfileManager, init_db

init_db()

profiles = ProfileManager()

profiles.create_profile(
    username="korqedev",
    display_name="Korqe Dev",
    bio="Python developer",
    status="Building cool projects",
    avatar_path=""
)

profile = profiles.get_profile("korqedev")

print(profile)
```

---

## Profile Data

Each profile stores:

| Field        | Description               |
| ------------ | ------------------------- |
| Username     | Unique account identifier |
| Display Name | Public profile name       |
| Bio          | User biography            |
| Status       | Current user status       |
| Avatar Path  | Profile picture location  |

---

## Requirements

* Python 3.10+
* CustomTkinter
* Pillow
* SQLite3

---

## Future Plans

* Theme support
* MySQL/PostgreSQL compatibility
* User authentication integration
* Cloud profile syncing
* Profile export/import system
* Plugin support
* Package publishing to PyPI

---

## License

This project is licensed under the MIT License.

---

## Author

**Made by @korqedev**
