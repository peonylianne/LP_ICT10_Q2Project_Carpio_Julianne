from pyscript import document


clubs = {
    "Robotics Club": {
        "description": "Design, build, and program robots for competitions.",
        "meeting": ("Every Tuesday", "3:45 - 5:30 PM"), 
        "location": "Computer Lab",
        "advisor": "Ms. Carabot",
        "members": 18,
        "category": "ICT"
    },
    "Music Club": {
        "description": "A club for singing and musical instrument performance.",
        "meeting": ("Monday & Thursday", "4:00 - 5:00 PM"),
        "location": "Music Room",
        "advisor": "Mr. Reyes",
        "members": 25,
        "category": "Arts"
    },
    "Sports Club": {
        "description": "Fitness and sports training for various athletic events.",
        "meeting": ("Friday", "3:00 - 5:00 PM"),
        "location": "Gymnasium",
        "advisor": "Coach Tare",
        "members": 30,
        "category": "Physical Education"
    }
}

select_box = document.getElementById("clubSelect")
select_box.innerHTML = "".join([f"<option>{club}</option>" for club in clubs])

def show_club(event):
    selected = document.getElementById("clubSelect").value
    info = clubs[selected]

    output = (
        f"{selected}\n"
        f"Description: {info['description']}\n"
        f"Meeting Time: {info['meeting'][0]} {info['meeting'][1]}\n"
        f"Location: {info['location']}\n"
        f"Advisor: {info['advisor']}\n"
        f"Number of Members: {info['members']}\n"
        f"Category: {info['category']}"
    )

    document.getElementById("output").innerText = output
