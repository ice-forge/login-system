function logout() {
    if (confirm("Are you sure you want to log out?")) {
        fetch('/auth/logout', {
            method: 'POST'
        }).then(response => {
            if (response.ok) {
                window.location.href = '/auth/login';
            }
        });
    }
}
