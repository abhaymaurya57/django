document.getElementById('staffLoginForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const email = document.getElementById('staffEmail').value;
  const password = document.getElementById('staffPassword').value;

  const response = await fetch('/api/staff-login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });

  const data = await response.json();

  if (response.ok) {
    localStorage.setItem('access_token', data.access);
    localStorage.setItem('refresh_token', data.refresh);
    localStorage.setItem('user_role', 'staff');
    window.location.href = '/staff/dashboard/';
  } else {
    alert(data.detail || "Login failed");
  }
});

