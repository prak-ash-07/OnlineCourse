fetch('/api/courses/')
.then(res => res.json())
.then(data => {
    let html = ''
    data.forEach(c => {
        html += `
        <div class="card">
            <h3>${c.title}</h3>
            <p>${c.short_description}</p>
            <a href="/courses/${c.id}/">View</a>
        </div>`
    })
    courses.innerHTML = html
})



