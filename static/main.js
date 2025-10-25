function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

async function getAllTodos(url) {
  try {
    const response = await fetch(url, {
      headers: { "X-Requested-With": "XMLHttpRequest" }
    });
    const data = await response.json();
    console.log("Respuesta del backend:", data); //

    const todoList = document.getElementById("todoList");
    todoList.innerHTML = "";

    if (data.context && data.context.length > 0) {
      data.context.forEach(todo => {
        const todoHTMLElement = `
          <li>
            <p><strong>Task:</strong> ${todo.task}</p>
            <p><strong>Completed?:</strong> ${todo.completed}</p>
          </li>`;
        todoList.innerHTML += todoHTMLElement;
      });
    } else {
      todoList.innerHTML = "<li>No hay tareas registradas.</li>";
    }
  } catch (error) {
    console.error("Error cargando todos:", error);
  }
}

async function addTodo(url, payload) {
  try {
    const response = await fetch(url, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ payload: payload })
    });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    console.log("Todo agregado:", data);
  } catch (err) {
    console.error("Error addTodo:", err);
  }
}

async function updateTodo(url, payload) {
  try {
    const response = await fetch(url, {
      method: "PUT",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ payload: payload })
    });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    console.log("Todo actualizado:", data);
  } catch (err) {
    console.error("Error updateTodo:", err);
  }
}

async function deleteTodo(url) {
  try {
    const response = await fetch(url, {
      method: "DELETE",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": getCookie("csrftoken")
      }
    });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    console.log("Todo eliminado:", data);
  } catch (err) {
    console.error("Error deleteTodo:", err);
  }
}
