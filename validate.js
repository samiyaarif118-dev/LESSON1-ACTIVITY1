
    function validate(e) {
        e.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const age = document.getElementById('age').value;
        const msgBox = document.getElementById('messageBox');

        let messages = '';
        if (email === '') {
            messages = 'enter an email.';
            msgBox.style.color = 'red';
        }
        
        if (password === '') {
            messages = 'enter a password.';
            msgBox.style.color = 'red';
        } else if (password === '') {
            messages = 'enter a password.';
            msgBox.style.color = 'red';
        } else if (age === '') {
            messages = 'enter your age.';
            msgBox.style.color = 'red';
        } else {
            message ='login successful!';
            msgBox.style.color = 'green';
        }
msgBox.innerText = message;
    
        }
    