localStorage.setItem("accessToken", data.access);

const response = await apiRequest('/api/login/', loginData);
if (response.ok) {
    localStorage.setItem("accessToken", response.data.access);
}


async function apiRequest(endpoint, data={}, method='POST', useToken=false) {
    const headers = { 'Content-Type': 'application/json' };
    if (useToken) {
        const token = localStorage.getItem("accessToken");
        if (!token) throw "No access token";
        headers['Authorization'] = `Bearer ${token}`;
    }
    const res = await fetch(endpoint, { method, headers,
        ...(method==='GET'?{}:{ body: JSON.stringify(data) }) });
    const json = await res.json();
    return { ok: res.ok, status: res.status, data: json };
}
