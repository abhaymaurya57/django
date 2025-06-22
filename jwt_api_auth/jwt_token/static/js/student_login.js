document.getElementById("loginForm")?.addEventListener("submit", async function (e) {
  e.preventDefault();

  const userid = document.getElementById("userid").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch("/api/login/student/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ userid, password }),
    });

    const data = await res.json();

    if (res.ok && data.access) {
      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);
      alert("✅ Login successful!");
      window.location.href = "/student/dashboard/";
    } else {
      alert("❌ Login failed: " + (data.detail || "Invalid credentials"));
    }
  } catch (err) {
    alert("⚠️ Error logging in. Please try again.");
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