from django.shortcuts import render, redirect
from .firebase import db


# Add sample students
def add_students(request):
    students = [
        {"name": "Ana", "score": 85, "subject": "Math", "exam_date": "2026-02-01"},
        {"name": "Ben", "score": 90, "subject": "Science", "exam_date": "2026-02-02"},
        {"name": "Cara", "score": 78, "subject": "English", "exam_date": "2026-02-03"},
    ]

    for student in students:
        db.collection("students").add(student)

    return render(request, "success.html")


# Fetch data
def student_data(request):
    docs = db.collection("students").stream()

    names = []
    scores = []
    subjects = []
    dates = []

    for doc in docs:
        data = doc.to_dict()
        names.append(data["name"])
        scores.append(data["score"])
        subjects.append(data["subject"])
        dates.append(data["exam_date"])

    context = {
        "names": names,
        "scores": scores,
        "subjects": subjects,
        "dates": dates,
    }

    return render(request, "dashboard.html", context)


# Dynamic Form
def add_student_form(request):
    if request.method == "POST":
        student = {
            "name": request.POST.get("name"),
            "score": int(request.POST.get("score")),
            "subject": request.POST.get("subject"),
            "exam_date": request.POST.get("exam_date"),
        }

        db.collection("students").add(student)
        return redirect("/dashboard/")

    return render(request, "add_form.html")