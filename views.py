from django.shortcuts import render, redirect
from .models import Course, Enrollment, Question, Choice, Submission

# Submit exam
def submit(request, course_id):
    course = Course.objects.get(id=course_id)
    enrollment = Enrollment.objects.first()  # simple demo

    selected_choices = []

    if request.method == "POST":
        for key, value in request.POST.items():
            if key.startswith('question_'):
                choice = Choice.objects.get(id=value)
                selected_choices.append(choice)

        submission = Submission.objects.create(enrollment=enrollment)
        submission.choices.set(selected_choices)

        return redirect('result', course_id=course.id)


# Show result
def show_exam_result(request, course_id):
    course = Course.objects.get(id=course_id)
    submission = Submission.objects.last()

    questions = Question.objects.filter(course=course)

    selected_ids = []
    total_score = 0
    possible_score = 0

    for question in questions:
        possible_score += question.grade

        correct_choices = question.choice_set.filter(is_correct=True)
        selected = submission.choices.filter(question=question)

        selected_ids += [choice.id for choice in selected]

        if set(correct_choices) == set(selected):
            total_score += question.grade

    context = {
        'course': course,
        'questions': questions,   # 👈 IMPORTANT
        'selected_ids': selected_ids,
        'grade': total_score,
        'possible': possible_score
    }

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
