import random
from flask import Flask, render_template

students_per_group = 3

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    student_list = [
        "강지민", "강현정", "김기훈", "김민규", "김민주", "김재진", "김준호",
        "박성우", "박정현", "방재현", "배창윤", "송호창", "양민석", "이건우",
        "이성현", "이시영", "이아진", "이현직", "정대기", "조우석", "최건희", 
        "최재흥", "한아름누리", "황준호"
    ]

    # 강제로 팀 배정할 학생들 예시
    fixed_groups = {
        1: ["양민석", "황준호", "이건우"],  # 1조에 반드시 이 3명
    }

    def create_group_html(group_num, students):
        return f"""<div class="group">
            <div class="group-title">{group_num}조 ({len(students)}명)</div>
            <div class="members">{', '.join(students)}</div>
        </div>"""

    @app.route("/")
    def index():
        # 이미 배정된 학생 제외하고 섞기
        assigned_students = sum(fixed_groups.values(), [])  # 2차원 리스트를 1차원으로
        remaining_students = [s for s in student_list if s not in assigned_students]
        random.shuffle(remaining_students)

        groups = []
        total_groups = (len(student_list) + students_per_group - 1) // students_per_group

        # 고정 그룹 먼저 넣기
        for group_num in range(1, total_groups + 1):
            if group_num in fixed_groups:
                groups.append(fixed_groups[group_num])
            else:
                group = remaining_students[:students_per_group]
                remaining_students = remaining_students[students_per_group:]
                groups.append(group)

        # 남은 학생을 1조나 마지막 조에 합치기
        if remaining_students:
            groups[-1] += remaining_students

        # 그룹 HTML 생성
        groups_html = ""
        for idx, group in enumerate(groups):
            groups_html += create_group_html(idx + 1, group)

        return render_template('index.html', group_html=groups_html, total_students=len(student_list))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, use_reloader=True, extra_files=['templates/index.html', 'static/styles.css'])
