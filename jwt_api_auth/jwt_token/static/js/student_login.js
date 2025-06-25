document.addEventListener('DOMContentLoaded', function () {
  const loginForm = document.getElementById('loginForm');

  if (loginForm) {
    loginForm.addEventListener('submit', async function (e) {
      e.preventDefault();

      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      try {
        const response = await fetch('/api/student-login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
          // Store tokens
          localStorage.setItem('access_token', data.access);
          localStorage.setItem('refresh_token', data.refresh);
          localStorage.setItem('user_role', 'student');

          // Redirect to dashboard
          window.location.href = '/student/dashboard/';
        } else {
          alert(data.detail || 'Invalid email or password');
        }
      } catch (error) {
        console.error('Login error:', error);
        alert('Something went wrong. Please try again.');
      }
    });
  }
});




    // <script>
    // document.getElementById("loginForm").addEventListener("submit", loginStudent);

    // function loginStudent(event) {
    //     event.preventDefault();

    //     const userid = document.getElementById("userid").value;
    //     const password = document.getElementById("password").value;

    //     fetch("/api/login/student/", {
    //         method: "POST",
    //         headers: { "Content-Type": "application/json" },
    //         body: JSON.stringify({ userid, password })
    //     })
    //     .then(response => response.json().then(data => ({ ok: response.ok, data })))
    //     .then(({ ok, data }) => {
    //         if (ok && data.access) {
    //             localStorage.setItem("access", data.access);
    //             localStorage.setItem("refresh", data.refresh);
    //             alert("✅ Logged in successfully");
    //             window.location.href = "/student/dashboard/";
    //         } else {
    //             alert("❌ Login failed: " + (data.detail || "Invalid credentials"));
    //         }
    //     })
    //     .catch(error => {
    //         console.error("Fetch error:", error);
    //         alert("⚠️ An error occurred. Please try again.");
    //     });
    // }
    // </script>