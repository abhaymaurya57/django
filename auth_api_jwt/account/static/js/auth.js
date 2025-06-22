function parseJwt(token) {
  if (!token || token.split('.').length !== 3) return null;
  try {
    return JSON.parse(atob(token.split('.')[1]));
  } catch (e) {
    return null;
  }
}

function checkTokenExpiry() {
  const token = localStorage.getItem('access');
  const decoded = parseJwt(token);

  if (!token || !decoded) {
    alert("❌ No valid token found. Please login.");
    localStorage.clear();
    window.location.href = "/api/user/login-form/";
    return;
  }

  const now = Date.now();
  const expiry = decoded.exp * 1000;

  if (expiry < now) {
    alert("⏰ Your session has expired. Please login again.");
    localStorage.clear();
    window.location.href = "/api/user/login-form/";
  } else {
    const minutesLeft = Math.round((expiry - now) / 60000);
    console.log(`🔐 Token is valid. Expires in ${minutesLeft} minute(s).`);
  }
}

checkTokenExpiry();
setInterval(checkTokenExpiry, 60000); // ⏳ Check every minute
