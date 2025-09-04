import random
from flask import Flask, render_template

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    student_list = [
        "강지민", "강현정", "김기훈", "김민규", "김민주", "김재진", "김준호",
        "박성우", "박정현", "방재현", "배창윤", "송호창", "양민석", "이건우",
        "이성현", "이시영", "이아진", "이현직", "정대기", "조우석", "최건희", 
        "최재흥", "한아름누리", "황준호"
    ]

    def create_group_html(group_num, students):
        return f"""<div class="group">
            <div class="group-title">{group_num}조 ({len(students)}명)</div>
            <div class="members">{', '.join(students)}</div>
        </div>"""

    @app.route("/")
    def index():
        shuffled = student_list[:]
        random.shuffle(shuffled)

        students_per_group = 8
        total_students = len(shuffled)
        groups_html = ""

        # 전체 3조를 만들되, 남은 인원 1명을 1조에 합치기
        groups = []
        start_idx = 0
        for i in range(3):
            end_idx = start_idx + students_per_group
            group = shuffled[start_idx:end_idx]
            groups.append(group)
            start_idx = end_idx

        # 남은 학생을 1조에 합치기
        remaining_students = shuffled[start_idx:]
        if remaining_students:
            groups[0] += remaining_students

        # 그룹 HTML 생성
        for idx, group in enumerate(groups):
            groups_html += create_group_html(idx + 1, group)

        return render_template('index.html', group_html=groups_html, total_students=total_students)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, use_reloader=True, extra_files=['templates/index.html', 'static/styles.css'])
