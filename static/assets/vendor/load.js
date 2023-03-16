document.addEventListener('DOMContentLoaded', (event) => {
    console.log("hello worldddd")

    // make fethc API request for all posts
    fetch('/date/')
        .then(response => response.json())
        .then(date => {

            console.log(typeof date)

            // clean all exsiting posts
            my_date_element = document.getElementById('sidebar-stats__value');
            my_date_element.innerHTML = date



        });

    event.preventDefault();
});