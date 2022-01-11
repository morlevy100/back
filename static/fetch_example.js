function getusers(){
    console.log('clicked');
    fetch('https://reqres.in/api/users?page=2').then(
        response => response.json()
    ).then(
        response_obj => put_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_inside_html(response_obj_data) {

    const curr_main = document.querySelector("main");
        const section = document.createElement('section');
        section.innerHTML = `
        <img src="${response_obj_data[1].avatar}" alt="Profile Picture"/>
        <div>
            <span>${response_obj_data[1].first_name} ${response_obj_data[1].last_name}</span>
            <br>
            <a href="mailto:${response_obj_data[1].email}">Send Email</a>
        </div>
        `;
        curr_main.appendChild(section);
}
