document.getElementById('adminLoginForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const email = document.getElementById('adminEmail').value;
  const password = document.getElementById('adminPassword').value;

  const response = await fetch('/api/admin-login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });

  const data = await response.json();

  if (response.ok) {
    localStorage.setItem('access_token', data.access);
    localStorage.setItem('refresh_token', data.refresh);
    localStorage.setItem('user_role', 'admin');
    window.location.href = '/adminn/dashboard/';
  } else {
    alert(data.detail || "Login failed");
  }
});

