// ✅ Parse JWT token
function parseJwt(token) {
    try {
        return JSON.parse(atob(token.split('.')[1]));
    } catch (e) {
        return null;
    }
}

// ✅ Check token expiry
function checkTokenExpiry() {
    const token = localStorage.getItem("access");
    if (!token) {
        alert("⚠️ No token found. Please login.");
        window.location.href = "/student/login/";
        return;
    }

    const decoded = parseJwt(token);
    if (!decoded || Date.now() >= decoded.exp * 1000) {
        alert("⏰ Token expired. Please login again.");
        logout();
    } else {
        document.getElementById("dashboard").style.display = "block";
    }
}

// ✅ Logout function
window.logout = function () {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    alert("👋 Logged out successfully");
    window.location.href = "/student/login/";
};


// ✅ Run on page load
window.addEventListener("DOMContentLoaded", checkTokenExpiry);
