fetch(`/api/courses/${COURSE_ID}/`)
.then(res => res.json())
.then(data => {
    title.innerText = data.course.title
    desc.innerText = data.course.long_description

    if (!data.logged_in) {
        enrollBtn.innerText = "Login to enroll"
        enrollBtn.disabled = true
    } else if (data.enrolled) {
        enrollBtn.innerText = "You are enrolled"
        enrollBtn.disabled = true
    } else {
        enrollBtn.innerText = "Enroll"
        enrollBtn.onclick = () => {
            fetch(`/api/courses/${COURSE_ID}/enroll/`, {method:'POST'})
            .then(() => location.reload())
        }
    }

    lessons.innerHTML = data.lessons
        .map(l => `<li><a href="/lessons/${l.id}/">${l.title}</a></li>`)
        .join('')
})
