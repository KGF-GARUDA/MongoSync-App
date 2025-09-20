const apiBase = "http://127.0.0.1:8000"; // replace with online URL later

// ------------------ Fetch Teachers ------------------
async function fetchTeachers() {
  try {
    const response = await fetch(`${apiBase}/users`); // fetch from /users endpoint
    const teachers = await response.json();
    localStorage.setItem("teachers", JSON.stringify(teachers)); // cache
    renderTeachers(teachers);
  } catch (error) {
    // Offline mode → load from cache
    const cached = localStorage.getItem("teachers");
    if (cached) renderTeachers(JSON.parse(cached));
    else document.getElementById("teacherList").innerHTML = "<li>No data available offline</li>";
  }
}

function renderTeachers(teachers) {
  const list = document.getElementById("teacherList");
  list.innerHTML = "";
  teachers.forEach(t => {
    const li = document.createElement("li");
    li.textContent = `ID: ${t.id}, Name: ${t.name}, Subject: ${t.subject}`;
    list.appendChild(li);
  });
}

// Fetch teachers on page load
document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("teacherList")) fetchTeachers();

  // ------------------ Admin Login ------------------
  const form = document.getElementById("loginForm");
  if (form) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const username = document.getElementById("username").value.trim();
      const password = document.getElementById("password").value.trim();

      try {
        const res = await fetch(`${apiBase}/admin/login`, {
          method: "POST",
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
          body: new URLSearchParams({ username, password })
        });

        const data = await res.json();

        if (res.ok) {
          localStorage.setItem("token", data.access_token);
          document.getElementById("message").textContent = "✅ Login successful!";

          // 🔹 Check if deleteUserId exists → delete after login
          const userId = localStorage.getItem("deleteUserId");
          if (userId) {
            try {
              const delRes = await fetch(`${apiBase}/duser/${userId}`, {
                method: "DELETE",
                headers: { "Authorization": "Bearer " + data.access_token }
              });
              const delData = await delRes.json();
              alert("✅ " + JSON.stringify(delData));
            } catch (err) {
              alert("❌ Error deleting user");
            }
            localStorage.removeItem("deleteUserId");
          }

          window.location.href = "dashboard.html";
        } else {
          document.getElementById("message").textContent = "❌ " + (data.detail || "Invalid credentials");
        }
      } catch (err) {
        document.getElementById("message").textContent = "⚠️ Login failed: " + err.message;
      }
    });
  }
});
