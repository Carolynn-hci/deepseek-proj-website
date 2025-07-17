function new_chat(event) {
    if (confirm('Your current chat will not be saved!') == true) {
        window.location.href = '';
    }
};

function logout_nav(event) {
    if (confirm('Do you want to log out?') == true){
        window.location.href = '../logout';
    }
};

function return_home(event) {
    window.location.href = '../'
}