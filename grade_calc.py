from pyscript import document

def compute_grade(event):

    student = document.getElementById("studentName").value

    subjects = {
        "Science": "science",
        "Math": "math",
        "English": "english",
        "Filipino": "filipino",
        "ICT": "ict",
        "PE": "pe"
    }


    subject_order = tuple(subjects.keys())

    grades_list = []
    errors = set() 


    for subject in subject_order:
        field_id = subjects[subject]
        value = document.getElementById(field_id).value
        try:
            score = float(value)
            grades_list.append(score)
        except ValueError:
            errors.add(subject)


    if errors:
        document.getElementById("avg").innerText = ""
        document.getElementById("status").innerText = ""
        document.getElementById("summary").innerHTML = f"Invalid input in: {', '.join(errors)}"
        return

    grade_dict = dict(zip(subject_order, grades_list))

    avg = sum(grades_list) / len(grades_list)
    
    status = "Pass" if avg >= 75 else "Fail"

    document.getElementById("avg").innerText = str(round(avg, 2))
    document.getElementById("status").innerText = status

    summary_html = f"<strong>{student}'s Grade Report:</strong><br>"
    for subject, score in grade_dict.items():
        summary_html += f"{subject}: {score}<br>"

    summary_html += f"<br><strong>Overall Average:</strong> {round(avg,2)}<br>"
    summary_html += f"<strong>Result:</strong> {status}"

    document.getElementById("summary").innerHTML = summary_html
