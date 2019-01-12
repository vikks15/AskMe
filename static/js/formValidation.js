function validateForm() {
    let error = document.getElementsByClassName('form-error');
    let title = document.forms['ask-form']['title'];
    let text = document.forms['ask-form']['text'];
    let tags = document.forms['ask-form']['tags'];

    if (title.value.length == 0 || text.value.length == 0 || tags.value.length == 0) {
        error[0].textContent = 'Empty fields!';
        return false;
    }

    if (title.value.length > 64) {
        error[0].textContent = 'Sorry, maximum size of question title is 64 symbols!';
        return false;
    }
}